---
api_specs:
- filename: apache-orc-tools-api.yaml
  format: yaml
  label: Apache ORC
  slug: apache-orc
  spec_type: OpenAPI
  url: https://raw.githubusercontent.com/api-evangelist/apache-orc/refs/heads/main/openapi/apache-orc-tools-api.yaml
categories:
- info
- operation
- paths
- response
- schema
description: Spectral linting rules defining API design standards and conventions for Apache ORC.
layout: rules
name: Apache ORC API Rules
provider_name: Apache ORC
provider_slug: apache-orc
rule_count: 8
rules:
- description: API must have a title
  given: $.info
  name: info-title-required
  severity: error
- description: Operations must have summaries
  given: $.paths[*][*]
  name: operation-summary-required
  severity: error
- description: ''
  given: $.paths[*][*]
  name: operation-operationId-required
  severity: error
- description: ''
  given: $.paths[*][*]
  name: operation-tags-required
  severity: warn
- description: Summaries should start with Apache ORC
  given: $.paths[*][get,post,put,delete,patch].summary
  name: operation-summary-apache-prefix
  severity: info
- description: ''
  given: $.paths[*]~
  name: paths-kebab-case
  severity: warn
- description: ''
  given: $.paths[*][*].responses
  name: response-success-required
  severity: error
- description: ''
  given: $.components.schemas[*].properties[*]
  name: schema-type-defined
  severity: warn
rules_file: rules/apache-orc-spectral-rules.yml
rules_url: https://raw.githubusercontent.com/api-evangelist/apache-orc/refs/heads/main/rules/apache-orc-spectral-rules.yml
severity_counts:
  error: 4
  hint: 0
  info: 1
  warn: 3
slug: apache-orc-spectral-rules
source_filename: apache-orc-spectral-rules.yml
source_heading: Spectral Ruleset
source_yaml: "extends: \"spectral:oas\"\nrules:\n  info-title-required:\n    description: \"API must have a title\"\n    severity: error\n    given: \"$.info\"\n    then:\n      field: title\n      function: truthy\n  operation-summary-required:\n    description: \"Operations must have summaries\"\n    severity: error\n    given: \"$.paths[*][*]\"\n    then:\n      field: summary\n      function: truthy\n  operation-operationId-required:\n    severity: error\n    given: \"$.paths[*][*]\"\n    then:\n      field: operationId\n      function: truthy\n  operation-tags-required:\n    severity: warn\n    given: \"$.paths[*][*]\"\n    then:\n      field: tags\n      function: truthy\n  operation-summary-apache-prefix:\n    description: \"Summaries should start with Apache ORC\"\n    severity: info\n    given: \"$.paths[*][get,post,put,delete,patch].summary\"\n    then:\n      function: pattern\n      functionOptions:\n        match: \"^Apache ORC\"\n  paths-kebab-case:\n    severity: warn\n  \
  \  given: \"$.paths[*]~\"\n    then:\n      function: pattern\n      functionOptions:\n        match: \"^(/[a-z0-9{}-]+)+$\"\n  response-success-required:\n    severity: error\n    given: \"$.paths[*][*].responses\"\n    then:\n      function: schema\n      functionOptions:\n        schema:\n          required: [\"200\"]\n  schema-type-defined:\n    severity: warn\n    given: \"$.components.schemas[*].properties[*]\"\n    then:\n      function: schema\n      functionOptions:\n        schema:\n          anyOf:\n            - required: [\"type\"]\n            - required: [\"$ref\"]\n"
source_yaml_url: https://raw.githubusercontent.com/api-evangelist/apache-orc/refs/heads/main/rules/apache-orc-spectral-rules.yml
tags:
- Big Data
- Columnar Storage
- Compression
- File Format
- Hadoop
- Apache
- Open Source
- Spectral
- Linting
- API Governance
---
