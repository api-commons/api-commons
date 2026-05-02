---
api_specs:
- filename: schema-registry.yml
  format: yaml
  label: Confluent Schema Registry REST API
  slug: schema-registry-rest-api
  spec_type: OpenAPI
  url: https://raw.githubusercontent.com/api-evangelist/confluent-schema-registry/refs/heads/main/openapi/schema-registry.yml
categories:
- schema
description: Spectral linting rules defining API design standards and conventions for Confluent Schema Registry.
layout: rules
name: Confluent Schema Registry API Rules
provider_name: Confluent Schema Registry
provider_slug: confluent-schema-registry
rule_count: 10
rules:
- description: API contact information must be present.
  given: $.info
  name: schema-registry-info-contact
  severity: error
- description: API license must be declared.
  given: $.info
  name: schema-registry-info-license
  severity: error
- description: At least one server URL must be defined.
  given: $.servers
  name: schema-registry-server-defined
  severity: error
- description: All paths must live under /subjects, /schemas, /config, /mode, /compatibility, /contexts, or /exporters.
  given: $.paths
  name: schema-registry-paths-prefix
  severity: warn
- description: Every operation must define an operationId.
  given: $.paths[*][get,post,put,patch,delete]
  name: schema-registry-operation-id
  severity: error
- description: Every operation must declare at least one tag.
  given: $.paths[*][get,post,put,patch,delete]
  name: schema-registry-operation-tags
  severity: warn
- description: Tags must come from the Schema Registry vocabulary (Subjects, Schemas, Config, Mode, Compatibility, Contexts, Exporters).
  given: $.paths[*][get,post,put,patch,delete].tags[*]
  name: schema-registry-tag-vocabulary
  severity: warn
- description: Non-2xx responses should reference the ErrorMessage schema.
  given: $.paths[*][get,post,put,patch,delete].responses[?(@property.match(/^[45][0-9][0-9]$/))].content.application/json.schema
  name: schema-registry-error-shape
  severity: warn
- description: 2xx responses should serve application/json (or application/vnd.schemaregistry.v1+json).
  given: $.paths[*][get,post,put,patch,delete].responses[?(@property == '200' || @property == '201')].content
  name: schema-registry-content-type
  severity: warn
- description: Compatibility levels should use canonical values.
  given: $.components.schemas.Config.properties.compatibility
  name: schema-registry-compatibility-enum
  severity: warn
rules_file: rules/confluent-schema-registry-rules.yml
rules_url: https://raw.githubusercontent.com/api-evangelist/confluent-schema-registry/refs/heads/main/rules/confluent-schema-registry-rules.yml
severity_counts:
  error: 4
  hint: 0
  info: 0
  warn: 6
slug: confluent-schema-registry-rules
source_filename: confluent-schema-registry-rules.yml
source_heading: Spectral Ruleset
source_yaml: "extends:\n  - spectral:oas\n\n# Spectral linting rules tuned for Confluent Schema Registry.\n# Validates that the OpenAPI spec follows Schema Registry conventions:\n# resource paths under /subjects, /schemas, /config, /mode, /compatibility,\n# JSON content types, and consistent use of the Subjects/Schemas/Config tags.\nrules:\n  schema-registry-info-contact:\n    description: API contact information must be present.\n    severity: error\n    given: \"$.info\"\n    then:\n      field: contact\n      function: truthy\n\n  schema-registry-info-license:\n    description: API license must be declared.\n    severity: error\n    given: \"$.info\"\n    then:\n      field: license\n      function: truthy\n\n  schema-registry-server-defined:\n    description: At least one server URL must be defined.\n    severity: error\n    given: \"$.servers\"\n    then:\n      function: schema\n      functionOptions:\n        schema:\n          type: array\n          minItems: 1\n\n  schema-registry-paths-prefix:\n\
  \    description: All paths must live under /subjects, /schemas, /config, /mode, /compatibility, /contexts, or /exporters.\n    severity: warn\n    given: \"$.paths\"\n    then:\n      field: \"@key\"\n      function: pattern\n      functionOptions:\n        match: \"^/(subjects|schemas|config|mode|compatibility|contexts|exporters)(/.*)?$\"\n\n  schema-registry-operation-id:\n    description: Every operation must define an operationId.\n    severity: error\n    given: \"$.paths[*][get,post,put,patch,delete]\"\n    then:\n      field: operationId\n      function: truthy\n\n  schema-registry-operation-tags:\n    description: Every operation must declare at least one tag.\n    severity: warn\n    given: \"$.paths[*][get,post,put,patch,delete]\"\n    then:\n      field: tags\n      function: schema\n      functionOptions:\n        schema:\n          type: array\n          minItems: 1\n\n  schema-registry-tag-vocabulary:\n    description: Tags must come from the Schema Registry vocabulary (Subjects,\
  \ Schemas, Config, Mode, Compatibility, Contexts, Exporters).\n    severity: warn\n    given: \"$.paths[*][get,post,put,patch,delete].tags[*]\"\n    then:\n      function: enumeration\n      functionOptions:\n        values:\n          - Subjects\n          - Schemas\n          - Config\n          - Mode\n          - Compatibility\n          - Contexts\n          - Exporters\n\n  schema-registry-error-shape:\n    description: Non-2xx responses should reference the ErrorMessage schema.\n    severity: warn\n    given: \"$.paths[*][get,post,put,patch,delete].responses[?(@property.match(/^[45][0-9][0-9]$/))].content.application/json.schema\"\n    then:\n      field: $ref\n      function: pattern\n      functionOptions:\n        match: \"ErrorMessage\"\n\n  schema-registry-content-type:\n    description: 2xx responses should serve application/json (or application/vnd.schemaregistry.v1+json).\n    severity: warn\n    given: \"$.paths[*][get,post,put,patch,delete].responses[?(@property == '200'\
  \ || @property == '201')].content\"\n    then:\n      field: \"@key\"\n      function: pattern\n      functionOptions:\n        match: \"^application/(vnd\\\\.schemaregistry\\\\.v1\\\\+json|json)$\"\n\n  schema-registry-compatibility-enum:\n    description: Compatibility levels should use canonical values.\n    severity: warn\n    given: \"$.components.schemas.Config.properties.compatibility\"\n    then:\n      field: enum\n      function: schema\n      functionOptions:\n        schema:\n          type: array\n          contains:\n            enum:\n              - NONE\n              - BACKWARD\n              - BACKWARD_TRANSITIVE\n              - FORWARD\n              - FORWARD_TRANSITIVE\n              - FULL\n              - FULL_TRANSITIVE\n"
source_yaml_url: https://raw.githubusercontent.com/api-evangelist/confluent-schema-registry/refs/heads/main/rules/confluent-schema-registry-rules.yml
tags:
- Apache Kafka
- Avro
- Compatibility
- Confluent
- Data Governance
- Data Streaming
- JSON Schema
- Open Source
- Protobuf
- REST
- Schema Evolution
- Schema Registry
- Spectral
- Linting
- API Governance
---
