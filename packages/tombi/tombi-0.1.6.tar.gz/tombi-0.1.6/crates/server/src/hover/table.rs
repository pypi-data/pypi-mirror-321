use config::TomlVersion;
use schema_store::{Accessor, Accessors, SchemaDefinitions, ValueSchema, ValueType};

use super::{
    get_all_of_hover_content, get_any_of_hover_content, get_one_of_hover_content, GetHoverContent,
    HoverContent,
};

impl GetHoverContent for document_tree::Table {
    fn get_hover_content(
        &self,
        accessors: &Vec<Accessor>,
        value_schema: Option<&ValueSchema>,
        toml_version: TomlVersion,
        position: text::Position,
        keys: &[document_tree::Key],
        definitions: &SchemaDefinitions,
    ) -> Option<HoverContent> {
        if let Some(key) = keys.first() {
            if let Some(value) = self.get(key) {
                let key_str = key.to_raw_text(toml_version);
                let accessor = Accessor::Key(key_str.clone());

                match value_schema {
                    Some(ValueSchema::Table(table_schema)) => {
                        if let Some(mut property) = table_schema.properties.get_mut(&accessor) {
                            let required = table_schema
                                .required
                                .as_ref()
                                .map(|r| r.contains(&key_str))
                                .unwrap_or(false);

                            return value
                                .get_hover_content(
                                    &accessors
                                        .clone()
                                        .into_iter()
                                        .chain(std::iter::once(accessor))
                                        .collect(),
                                    property.resolve(definitions).ok(),
                                    toml_version,
                                    position,
                                    &keys[1..],
                                    definitions,
                                )
                                .map(|hover_content| {
                                    if keys.len() == 1
                                        && !required
                                        && matches!(
                                            hover_content.keys.last(),
                                            Some(Accessor::Key(_))
                                        )
                                    {
                                        hover_content.into_nullable()
                                    } else {
                                        hover_content
                                    }
                                });
                        } else if let Some(additiona_property_schema) =
                            &table_schema.additional_property_schema
                        {
                            if let Ok(mut additiona_property_schema) =
                                additiona_property_schema.write()
                            {
                                return value
                                    .get_hover_content(
                                        &accessors
                                            .clone()
                                            .into_iter()
                                            .chain(std::iter::once(accessor))
                                            .collect(),
                                        additiona_property_schema.resolve(definitions).ok(),
                                        toml_version,
                                        position,
                                        &keys[1..],
                                        definitions,
                                    )
                                    .map(|hover_content| {
                                        if keys.len() == 1
                                            && matches!(
                                                hover_content.keys.last(),
                                                Some(Accessor::Key(_))
                                            )
                                        {
                                            hover_content.into_nullable()
                                        } else {
                                            hover_content
                                        }
                                    });
                            }
                        }
                    }
                    Some(ValueSchema::OneOf(one_of_schema)) => {
                        if let Some(hover_content) = get_one_of_hover_content(
                            self,
                            accessors,
                            one_of_schema,
                            toml_version,
                            position,
                            keys,
                            definitions,
                        ) {
                            return Some(hover_content);
                        }
                    }
                    Some(ValueSchema::AnyOf(any_of_schema)) => {
                        if let Some(hover_content) = get_any_of_hover_content(
                            self,
                            accessors,
                            any_of_schema,
                            toml_version,
                            position,
                            keys,
                            definitions,
                        ) {
                            return Some(hover_content);
                        }
                    }
                    Some(ValueSchema::AllOf(all_of_schema)) => {
                        if let Some(hover_content) = get_all_of_hover_content(
                            self,
                            accessors,
                            all_of_schema,
                            toml_version,
                            position,
                            keys,
                            definitions,
                        ) {
                            return Some(hover_content);
                        }
                    }
                    Some(_) => return None,
                    None => {}
                }

                return value.get_hover_content(
                    &accessors
                        .clone()
                        .into_iter()
                        .chain(std::iter::once(accessor))
                        .collect(),
                    None,
                    toml_version,
                    position,
                    &keys[1..],
                    definitions,
                );
            } else {
                return None;
            }
        } else {
            match value_schema {
                Some(ValueSchema::Table(table_schema)) => {
                    return Some(HoverContent {
                        title: table_schema.title.clone(),
                        description: table_schema.description.clone(),
                        keys: Accessors::new(accessors.clone()),
                        value_type: ValueType::Table,
                        enumerated_values: vec![],
                        schema_url: None,
                        range: Some(self.range()),
                    });
                }
                Some(ValueSchema::OneOf(one_of_schema)) => {
                    if let Some(hover_content) = get_one_of_hover_content(
                        self,
                        accessors,
                        one_of_schema,
                        toml_version,
                        position,
                        keys,
                        definitions,
                    ) {
                        return Some(hover_content);
                    }
                }
                Some(ValueSchema::AnyOf(any_of_schema)) => {
                    if let Some(hover_content) = get_any_of_hover_content(
                        self,
                        accessors,
                        any_of_schema,
                        toml_version,
                        position,
                        keys,
                        definitions,
                    ) {
                        return Some(hover_content);
                    }
                }
                Some(ValueSchema::AllOf(all_of_schema)) => {
                    if let Some(hover_content) = get_all_of_hover_content(
                        self,
                        accessors,
                        all_of_schema,
                        toml_version,
                        position,
                        keys,
                        definitions,
                    ) {
                        return Some(hover_content);
                    }
                }
                Some(_) => return None,
                None => {}
            }
        }

        Some(HoverContent {
            title: None,
            description: None,
            keys: Accessors::new(accessors.clone()),
            value_type: ValueType::Table,
            enumerated_values: vec![],
            schema_url: None,
            range: Some(self.range()),
        })
    }
}
