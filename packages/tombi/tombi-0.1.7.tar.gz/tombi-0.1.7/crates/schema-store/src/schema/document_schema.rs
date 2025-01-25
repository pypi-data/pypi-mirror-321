use std::sync::{Arc, RwLock};

use super::{referable_schema::Referable, SchemaDefinitions, SchemaProperties, ValueSchema};
use super::{Schema, SchemaItem, TableSchema};
use crate::Accessor;
use config::TomlVersion;
use dashmap::DashMap;

#[derive(Debug, Clone)]
pub struct DocumentSchema {
    pub document_url: url::Url,
    pub schema_id: Option<url::Url>,
    pub(crate) toml_version: Option<TomlVersion>,
    pub title: Option<String>,
    pub description: Option<String>,
    pub properties: SchemaProperties,
    pub additional_properties: bool,
    pub additional_property_schema: Option<SchemaItem>,
    pub required: Option<Vec<String>>,
    pub min_properties: Option<usize>,
    pub max_properties: Option<usize>,
    pub definitions: SchemaDefinitions,
}

impl DocumentSchema {
    pub fn new(value: serde_json::Value, document_url: url::Url) -> Self {
        let toml_version = value.get("x-tombi-toml-version").and_then(|obj| match obj {
            serde_json::Value::String(version) => {
                serde_json::from_str(&format!("\"{version}\"")).ok()
            }
            _ => None,
        });
        let title = value
            .get("title")
            .and_then(|v| v.as_str().map(|s| s.to_string()));

        let description = value
            .get("description")
            .and_then(|v| v.as_str().map(|s| s.to_string()));

        let schema_url = value
            .get("$id")
            .and_then(|v| v.as_str())
            .and_then(|s| url::Url::parse(s).ok());

        let properties = DashMap::default();
        if value.get("properties").is_some() {
            if let Some(serde_json::Value::Object(object)) = value.get("properties") {
                for (key, value) in object.into_iter() {
                    let Some(object) = value.as_object() else {
                        continue;
                    };
                    if let Some(value_schema) = Referable::<ValueSchema>::new(&object) {
                        properties.insert(Accessor::Key(key.into()), value_schema);
                    }
                }
            }
        }

        let (additional_properties, additional_property_schema) =
            match value.get("additionalProperties") {
                Some(serde_json::Value::Bool(allow)) => (*allow, None),
                Some(serde_json::Value::Object(object)) => {
                    let value_schema = Referable::<ValueSchema>::new(object);
                    (
                        true,
                        value_schema.map(|schema| Arc::new(RwLock::new(schema))),
                    )
                }
                _ => (true, None),
            };

        let definitions = DashMap::default();
        if value.get("definitions").is_some() {
            if let Some(serde_json::Value::Object(object)) = value.get("definitions") {
                for (key, value) in object.into_iter() {
                    let Some(object) = value.as_object() else {
                        continue;
                    };
                    if let Some(value_schema) = Referable::<ValueSchema>::new(&object) {
                        definitions.insert(format!("#/definitions/{key}"), value_schema);
                    }
                }
            }
        }
        if value.get("$defs").is_some() {
            if let Some(serde_json::Value::Object(object)) = value.get("$defs") {
                for (key, value) in object.into_iter() {
                    let Some(object) = value.as_object() else {
                        continue;
                    };
                    if let Some(value_schema) = Referable::<ValueSchema>::new(&object) {
                        definitions.insert(format!("#/$defs/{key}"), value_schema);
                    }
                }
            }
        }

        Self {
            document_url,
            schema_id: schema_url,
            toml_version,
            title,
            description,
            properties,
            additional_properties,
            additional_property_schema,
            required: value.get("required").and_then(|v| {
                v.as_array().map(|arr| {
                    arr.iter()
                        .filter_map(|v| v.as_str().map(|s| s.to_string()))
                        .collect()
                })
            }),
            min_properties: value
                .get("minProperties")
                .and_then(|v| v.as_u64().map(|u| u as usize)),
            max_properties: value
                .get("maxProperties")
                .and_then(|v| v.as_u64().map(|u| u as usize)),
            definitions,
        }
    }

    pub fn toml_version(&self) -> Option<TomlVersion> {
        self.toml_version.inspect(|version| {
            tracing::debug!("use schema TOML version: {version}");
        })
    }

    pub fn value_type(&self) -> crate::ValueType {
        crate::ValueType::Table
    }
}

impl From<DocumentSchema> for (ValueSchema, SchemaDefinitions) {
    fn from(document_schema: DocumentSchema) -> Self {
        (
            ValueSchema::Table(TableSchema {
                title: document_schema.title,
                description: document_schema.description,
                properties: document_schema.properties,
                additional_properties: document_schema.additional_properties,
                additional_property_schema: document_schema.additional_property_schema,
                required: document_schema.required,
                min_properties: document_schema.min_properties,
                max_properties: document_schema.max_properties,
                default: None,
            }),
            document_schema.definitions,
        )
    }
}

impl Schema for DocumentSchema {
    fn find_schema_candidates(
        &self,
        accessors: &[Accessor],
        definitions: &SchemaDefinitions,
    ) -> (Vec<ValueSchema>, Vec<crate::Error>) {
        let mut candidates = Vec::new();
        let mut errors = Vec::new();

        if accessors.is_empty() {
            for mut value in self.properties.iter_mut() {
                if let Ok(schema) = value.resolve(definitions) {
                    let (schema_candidates, schema_errors) =
                        schema.find_schema_candidates(accessors, definitions);
                    candidates.extend(schema_candidates);
                    errors.extend(schema_errors);
                }
            }

            return (candidates, errors);
        }

        if let Some(mut value) = self.properties.get_mut(&accessors[0]) {
            if let Ok(schema) = value.resolve(&definitions) {
                return schema.find_schema_candidates(&accessors[1..], &definitions);
            }
        }

        (candidates, errors)
    }
}
