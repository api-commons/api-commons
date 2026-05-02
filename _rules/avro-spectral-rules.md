---
categories:
- avro
description: Spectral linting rules defining API design standards and conventions for Apache Avro.
layout: rules
name: Apache Avro API Rules
provider_name: Apache Avro
provider_slug: avro
rule_count: 15
rules:
- description: Avro schemas must specify a type.
  given: $
  name: avro-schema-type-required
  severity: error
- description: Avro record types must have a name.
  given: $..[?(@.type == 'record')]
  name: avro-record-name-required
  severity: error
- description: Avro record types must have a fields array.
  given: $..[?(@.type == 'record')]
  name: avro-record-fields-required
  severity: error
- description: Each Avro record field must have a name.
  given: $..fields[*]
  name: avro-field-name-required
  severity: error
- description: Each Avro record field must have a type.
  given: $..fields[*]
  name: avro-field-type-required
  severity: error
- description: Avro enum types must have a name.
  given: $..[?(@.type == 'enum')]
  name: avro-enum-name-required
  severity: error
- description: Avro enum types must define symbols.
  given: $..[?(@.type == 'enum')]
  name: avro-enum-symbols-required
  severity: error
- description: Avro fixed types must have a name.
  given: $..[?(@.type == 'fixed')]
  name: avro-fixed-name-required
  severity: error
- description: Avro fixed types must specify a size.
  given: $..[?(@.type == 'fixed')]
  name: avro-fixed-size-required
  severity: error
- description: Avro named types should include a namespace.
  given: $..[?(@.type == 'record' || @.type == 'enum' || @.type == 'fixed')]
  name: avro-namespace-recommended
  severity: warn
- description: Avro schemas should include documentation.
  given: $
  name: avro-doc-recommended
  severity: warn
- description: Avro record fields should include documentation.
  given: $..fields[*]
  name: avro-field-doc-recommended
  severity: info
- description: Nullable Avro fields should specify a default value.
  given: $..fields[?(@.type[0] == 'null')]
  name: avro-field-default-for-nullable
  severity: warn
- description: Avro schema names should use camelCase or PascalCase.
  given: $..name
  name: avro-name-camel-case
  severity: info
- description: Avro namespaces should use dot-separated package notation.
  given: $..namespace
  name: avro-namespace-dot-separated
  severity: warn
rules_file: rules/avro-spectral-rules.yml
rules_url: https://raw.githubusercontent.com/api-evangelist/avro/refs/heads/main/rules/avro-spectral-rules.yml
severity_counts:
  error: 9
  hint: 0
  info: 2
  warn: 4
slug: avro-spectral-rules
source_filename: avro-spectral-rules.yml
source_heading: Spectral Ruleset
source_yaml: "rules:\n  avro-schema-type-required:\n    description: \"Avro schemas must specify a type.\"\n    message: \"Avro schema must have a type field.\"\n    severity: error\n    given: \"$\"\n    then:\n      field: type\n      function: truthy\n\n  avro-record-name-required:\n    description: \"Avro record types must have a name.\"\n    message: \"Record type must have a name field.\"\n    severity: error\n    given: \"$..[?(@.type == 'record')]\"\n    then:\n      field: name\n      function: truthy\n\n  avro-record-fields-required:\n    description: \"Avro record types must have a fields array.\"\n    message: \"Record type must define fields.\"\n    severity: error\n    given: \"$..[?(@.type == 'record')]\"\n    then:\n      field: fields\n      function: truthy\n\n  avro-field-name-required:\n    description: \"Each Avro record field must have a name.\"\n    message: \"Record field must have a name.\"\n    severity: error\n    given: \"$..fields[*]\"\n    then:\n      field:\
  \ name\n      function: truthy\n\n  avro-field-type-required:\n    description: \"Each Avro record field must have a type.\"\n    message: \"Record field must have a type.\"\n    severity: error\n    given: \"$..fields[*]\"\n    then:\n      field: type\n      function: truthy\n\n  avro-enum-name-required:\n    description: \"Avro enum types must have a name.\"\n    message: \"Enum type must have a name.\"\n    severity: error\n    given: \"$..[?(@.type == 'enum')]\"\n    then:\n      field: name\n      function: truthy\n\n  avro-enum-symbols-required:\n    description: \"Avro enum types must define symbols.\"\n    message: \"Enum type must have a symbols array.\"\n    severity: error\n    given: \"$..[?(@.type == 'enum')]\"\n    then:\n      field: symbols\n      function: truthy\n\n  avro-fixed-name-required:\n    description: \"Avro fixed types must have a name.\"\n    message: \"Fixed type must have a name.\"\n    severity: error\n    given: \"$..[?(@.type == 'fixed')]\"\n    then:\n\
  \      field: name\n      function: truthy\n\n  avro-fixed-size-required:\n    description: \"Avro fixed types must specify a size.\"\n    message: \"Fixed type must have a size in bytes.\"\n    severity: error\n    given: \"$..[?(@.type == 'fixed')]\"\n    then:\n      field: size\n      function: truthy\n\n  avro-namespace-recommended:\n    description: \"Avro named types should include a namespace.\"\n    message: \"Named type should have a namespace for disambiguation.\"\n    severity: warn\n    given: \"$..[?(@.type == 'record' || @.type == 'enum' || @.type == 'fixed')]\"\n    then:\n      field: namespace\n      function: truthy\n\n  avro-doc-recommended:\n    description: \"Avro schemas should include documentation.\"\n    message: \"Schema or named type should have a doc string.\"\n    severity: warn\n    given: \"$\"\n    then:\n      field: doc\n      function: truthy\n\n  avro-field-doc-recommended:\n    description: \"Avro record fields should include documentation.\"\n   \
  \ message: \"Field should have a doc string describing its purpose.\"\n    severity: info\n    given: \"$..fields[*]\"\n    then:\n      field: doc\n      function: truthy\n\n  avro-field-default-for-nullable:\n    description: \"Nullable Avro fields should specify a default value.\"\n    message: \"Nullable union field should provide a default value.\"\n    severity: warn\n    given: \"$..fields[?(@.type[0] == 'null')]\"\n    then:\n      field: default\n      function: defined\n\n  avro-name-camel-case:\n    description: \"Avro schema names should use camelCase or PascalCase.\"\n    message: \"Schema name should use camelCase or PascalCase convention.\"\n    severity: info\n    given: \"$..name\"\n    then:\n      function: pattern\n      functionOptions:\n        match: \"^[a-zA-Z][a-zA-Z0-9]*$\"\n\n  avro-namespace-dot-separated:\n    description: \"Avro namespaces should use dot-separated package notation.\"\n    message: \"Namespace should use dot-separated notation (e.g., com.example.avro).\"\
  \n    severity: warn\n    given: \"$..namespace\"\n    then:\n      function: pattern\n      functionOptions:\n        match: \"^[a-z][a-z0-9]*(\\\\.[a-z][a-z0-9]*)*$\"\n"
source_yaml_url: https://raw.githubusercontent.com/api-evangelist/avro/refs/heads/main/rules/avro-spectral-rules.yml
tags:
- Apache
- Big Data
- Binary Format
- Data Serialization
- Schema Evolution
- Spectral
- Linting
- API Governance
---
