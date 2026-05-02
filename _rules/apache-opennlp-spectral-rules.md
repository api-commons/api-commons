---
api_specs:
- filename: apache-opennlp-tools.yaml
  format: yaml
  label: Apache OpenNLP
  slug: apache-opennlp
  spec_type: OpenAPI
  url: https://raw.githubusercontent.com/api-evangelist/apache-opennlp/refs/heads/main/openapi/apache-opennlp-tools.yaml
categories:
- info
- operation
- paths
- request
- response
- schema
description: Spectral linting rules defining API design standards and conventions for Apache OpenNLP.
layout: rules
name: Apache OpenNLP API Rules
provider_name: Apache OpenNLP
provider_slug: apache-opennlp
rule_count: 10
rules:
- description: API must have a title
  given: $.info
  name: info-title-required
  severity: error
- description: API must have a description
  given: $.info
  name: info-description-required
  severity: warn
- description: Operations must have summaries
  given: $.paths[*][*]
  name: operation-summary-required
  severity: error
- description: Operations must have operationIds
  given: $.paths[*][*]
  name: operation-operationId-required
  severity: error
- description: Operations must have tags
  given: $.paths[*][*]
  name: operation-tags-required
  severity: warn
- description: Summaries should start with Apache OpenNLP
  given: $.paths[*][get,post,put,delete,patch].summary
  name: operation-summary-apache-prefix
  severity: info
- description: Path segments should use kebab-case
  given: $.paths[*]~
  name: paths-kebab-case
  severity: warn
- description: Request bodies should use application/json
  given: $.paths[*][post,put,patch].requestBody.content
  name: request-body-content-type
  severity: warn
- description: Operations must have a 200 success response
  given: $.paths[*][*].responses
  name: response-success-required
  severity: error
- description: Schema properties should have types defined
  given: $.components.schemas[*].properties[*]
  name: schema-type-defined
  severity: warn
rules_file: rules/apache-opennlp-spectral-rules.yml
rules_url: https://raw.githubusercontent.com/api-evangelist/apache-opennlp/refs/heads/main/rules/apache-opennlp-spectral-rules.yml
severity_counts:
  error: 4
  hint: 0
  info: 1
  warn: 5
slug: apache-opennlp-spectral-rules
source_filename: apache-opennlp-spectral-rules.yml
source_heading: Spectral Ruleset
source_yaml: "extends: \"spectral:oas\"\nrules:\n  info-title-required:\n    description: \"API must have a title\"\n    severity: error\n    given: \"$.info\"\n    then:\n      field: title\n      function: truthy\n  info-description-required:\n    description: \"API must have a description\"\n    severity: warn\n    given: \"$.info\"\n    then:\n      field: description\n      function: truthy\n  operation-summary-required:\n    description: \"Operations must have summaries\"\n    severity: error\n    given: \"$.paths[*][*]\"\n    then:\n      field: summary\n      function: truthy\n  operation-operationId-required:\n    description: \"Operations must have operationIds\"\n    severity: error\n    given: \"$.paths[*][*]\"\n    then:\n      field: operationId\n      function: truthy\n  operation-tags-required:\n    description: \"Operations must have tags\"\n    severity: warn\n    given: \"$.paths[*][*]\"\n    then:\n      field: tags\n      function: truthy\n  operation-summary-apache-prefix:\n\
  \    description: \"Summaries should start with Apache OpenNLP\"\n    severity: info\n    given: \"$.paths[*][get,post,put,delete,patch].summary\"\n    then:\n      function: pattern\n      functionOptions:\n        match: \"^Apache OpenNLP\"\n  paths-kebab-case:\n    description: \"Path segments should use kebab-case\"\n    severity: warn\n    given: \"$.paths[*]~\"\n    then:\n      function: pattern\n      functionOptions:\n        match: \"^(/[a-z0-9{}-]+)+$\"\n  request-body-content-type:\n    description: \"Request bodies should use application/json\"\n    severity: warn\n    given: \"$.paths[*][post,put,patch].requestBody.content\"\n    then:\n      function: schema\n      functionOptions:\n        schema:\n          required: [\"application/json\"]\n  response-success-required:\n    description: \"Operations must have a 200 success response\"\n    severity: error\n    given: \"$.paths[*][*].responses\"\n    then:\n      function: schema\n      functionOptions:\n        schema:\n\
  \          required: [\"200\"]\n  schema-type-defined:\n    description: \"Schema properties should have types defined\"\n    severity: warn\n    given: \"$.components.schemas[*].properties[*]\"\n    then:\n      function: schema\n      functionOptions:\n        schema:\n          anyOf:\n            - required: [\"type\"]\n            - required: [\"$ref\"]\n"
source_yaml_url: https://raw.githubusercontent.com/api-evangelist/apache-opennlp/refs/heads/main/rules/apache-opennlp-spectral-rules.yml
tags:
- Machine Learning
- Natural Language Processing
- NLP
- Text Processing
- Apache
- Open Source
- Java
- Spectral
- Linting
- API Governance
---
