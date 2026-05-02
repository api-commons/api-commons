---
api_specs:
- filename: amazon-lookout-for-metrics-openapi-original.yaml
  format: yaml
  label: Amazon Lookout for Metrics API
  slug: amazon-lookout-for-metrics-api
  spec_type: OpenAPI
  url: https://raw.githubusercontent.com/api-evangelist/amazon-lookout-for-metrics/refs/heads/main/openapi/amazon-lookout-for-metrics-openapi-original.yaml
categories:
- examples
- http
- info
- 'no'
- openapi
- operation
- parameter
- paths
- response
- schema
- security
- servers
description: Spectral linting rules defining API design standards and conventions for Amazon Lookout for Metrics.
layout: rules
name: Amazon Lookout for Metrics API Rules
provider_name: Amazon Lookout for Metrics
provider_slug: amazon-lookout-for-metrics
rule_count: 24
rules:
- description: Info title must be present and start with "Amazon Lookout for Metrics"
  given: $.info
  name: info-title-required
  severity: error
- description: Info description must be present
  given: $.info
  name: info-description-required
  severity: warn
- description: API version must be defined
  given: $.info
  name: info-version-required
  severity: error
- description: Must use OpenAPI 3.0.x
  given: $
  name: openapi-version
  severity: error
- description: Servers must be defined
  given: $
  name: servers-required
  severity: error
- description: Server URLs should use HTTPS
  given: $.servers[*]
  name: servers-https
  severity: warn
- description: Every operation must have an operationId
  given: $.paths[*][get,post,put,patch,delete]
  name: operation-operationId-required
  severity: error
- description: Every operation must have a summary
  given: $.paths[*][get,post,put,patch,delete]
  name: operation-summary-required
  severity: warn
- description: Operation summaries should start with "Amazon Lookout for Metrics"
  given: $.paths[*][get,post,put,patch,delete].summary
  name: operation-summary-prefix
  severity: info
- description: Every operation should have a description
  given: $.paths[*][get,post,put,patch,delete]
  name: operation-description-required
  severity: warn
- description: Every operation must have at least one tag
  given: $.paths[*][get,post,put,patch,delete]
  name: operation-tags-required
  severity: warn
- description: Path segments should use PascalCase (AWS convention for action-based paths)
  given: $.paths
  name: paths-kebab-case
  severity: info
- description: All parameters must have descriptions
  given: $.paths[*][get,post,put,patch,delete].parameters[*]
  name: parameter-description-required
  severity: warn
- description: Operations must have at least one 2xx response
  given: $.paths[*][post]
  name: response-success-required
  severity: error
- description: All responses must have a description
  given: $.paths[*][get,post,put,patch,delete].responses[*]
  name: response-description-required
  severity: warn
- description: Operations should document 401 Unauthorized responses
  given: $.paths[*][post]
  name: response-error-401
  severity: info
- description: Top-level schemas in components should have descriptions
  given: $.components.schemas[*]
  name: schema-description
  severity: info
- description: Schema properties should define a type
  given: $.components.schemas[*].properties[*]
  name: schema-property-type
  severity: warn
- description: Security schemes must be defined
  given: $.components
  name: security-schemes-required
  severity: error
- description: AWS Signature Version 4 security should be documented
  given: $.components.securitySchemes
  name: security-aws-sigv4
  severity: warn
- description: GET operations should not have request bodies
  given: $.paths[*].get
  name: http-get-no-body
  severity: error
- description: DELETE operations should not have request bodies
  given: $.paths[*].delete
  name: http-delete-no-body
  severity: warn
- description: Descriptions should not be empty strings
  given: $..description
  name: no-empty-descriptions
  severity: warn
- description: Schema properties should include examples
  given: $.components.schemas[*].properties[*]
  name: examples-encouraged
  severity: info
rules_file: rules/amazon-lookout-for-metrics-spectral-rules.yml
rules_url: https://raw.githubusercontent.com/api-evangelist/amazon-lookout-for-metrics/refs/heads/main/rules/amazon-lookout-for-metrics-spectral-rules.yml
severity_counts:
  error: 8
  hint: 0
  info: 5
  warn: 11
slug: amazon-lookout-for-metrics-spectral-rules
source_filename: amazon-lookout-for-metrics-spectral-rules.yml
source_heading: Spectral Ruleset
source_yaml: "rules:\n\n  # INFO / METADATA\n  info-title-required:\n    description: Info title must be present and start with \"Amazon Lookout for Metrics\"\n    severity: error\n    given: \"$.info\"\n    then:\n      field: title\n      function: truthy\n\n  info-description-required:\n    description: Info description must be present\n    severity: warn\n    given: \"$.info\"\n    then:\n      field: description\n      function: truthy\n\n  info-version-required:\n    description: API version must be defined\n    severity: error\n    given: \"$.info\"\n    then:\n      field: version\n      function: truthy\n\n  # OPENAPI VERSION\n  openapi-version:\n    description: Must use OpenAPI 3.0.x\n    severity: error\n    given: \"$\"\n    then:\n      field: openapi\n      function: pattern\n      functionOptions:\n        match: \"^3\\\\.0\\\\.\"\n\n  # SERVERS\n  servers-required:\n    description: Servers must be defined\n    severity: error\n    given: \"$\"\n    then:\n      field: servers\n\
  \      function: truthy\n\n  servers-https:\n    description: Server URLs should use HTTPS\n    severity: warn\n    given: \"$.servers[*]\"\n    then:\n      field: url\n      function: pattern\n      functionOptions:\n        match: \"^https://\"\n\n  # OPERATIONS\n  operation-operationId-required:\n    description: Every operation must have an operationId\n    severity: error\n    given: \"$.paths[*][get,post,put,patch,delete]\"\n    then:\n      field: operationId\n      function: truthy\n\n  operation-summary-required:\n    description: Every operation must have a summary\n    severity: warn\n    given: \"$.paths[*][get,post,put,patch,delete]\"\n    then:\n      field: summary\n      function: truthy\n\n  operation-summary-prefix:\n    description: Operation summaries should start with \"Amazon Lookout for Metrics\"\n    severity: info\n    given: \"$.paths[*][get,post,put,patch,delete].summary\"\n    then:\n      function: pattern\n      functionOptions:\n        match: \"^Amazon\
  \ Lookout for Metrics\"\n\n  operation-description-required:\n    description: Every operation should have a description\n    severity: warn\n    given: \"$.paths[*][get,post,put,patch,delete]\"\n    then:\n      field: description\n      function: truthy\n\n  operation-tags-required:\n    description: Every operation must have at least one tag\n    severity: warn\n    given: \"$.paths[*][get,post,put,patch,delete]\"\n    then:\n      field: tags\n      function: truthy\n\n  # PATHS\n  paths-kebab-case:\n    description: Path segments should use PascalCase (AWS convention for action-based paths)\n    severity: info\n    given: \"$.paths\"\n    then:\n      field: \"@key\"\n      function: pattern\n      functionOptions:\n        match: \"^/[A-Za-z][A-Za-z0-9]*$\"\n\n  # PARAMETERS\n  parameter-description-required:\n    description: All parameters must have descriptions\n    severity: warn\n    given: \"$.paths[*][get,post,put,patch,delete].parameters[*]\"\n    then:\n      field: description\n\
  \      function: truthy\n\n  # RESPONSES\n  response-success-required:\n    description: Operations must have at least one 2xx response\n    severity: error\n    given: \"$.paths[*][post]\"\n    then:\n      field: responses\n      function: schema\n      functionOptions:\n        schema:\n          type: object\n          minProperties: 1\n\n  response-description-required:\n    description: All responses must have a description\n    severity: warn\n    given: \"$.paths[*][get,post,put,patch,delete].responses[*]\"\n    then:\n      field: description\n      function: truthy\n\n  response-error-401:\n    description: Operations should document 401 Unauthorized responses\n    severity: info\n    given: \"$.paths[*][post]\"\n    then:\n      field: responses\n      function: schema\n      functionOptions:\n        schema:\n          type: object\n\n  # SCHEMAS\n  schema-description:\n    description: Top-level schemas in components should have descriptions\n    severity: info\n    given:\
  \ \"$.components.schemas[*]\"\n    then:\n      field: description\n      function: truthy\n\n  schema-property-type:\n    description: Schema properties should define a type\n    severity: warn\n    given: \"$.components.schemas[*].properties[*]\"\n    then:\n      field: type\n      function: truthy\n\n  # SECURITY\n  security-schemes-required:\n    description: Security schemes must be defined\n    severity: error\n    given: \"$.components\"\n    then:\n      field: securitySchemes\n      function: truthy\n\n  security-aws-sigv4:\n    description: AWS Signature Version 4 security should be documented\n    severity: warn\n    given: \"$.components.securitySchemes\"\n    then:\n      function: truthy\n\n  # HTTP METHOD CONVENTIONS\n  http-get-no-body:\n    description: GET operations should not have request bodies\n    severity: error\n    given: \"$.paths[*].get\"\n    then:\n      field: requestBody\n      function: falsy\n\n  http-delete-no-body:\n    description: DELETE operations\
  \ should not have request bodies\n    severity: warn\n    given: \"$.paths[*].delete\"\n    then:\n      field: requestBody\n      function: falsy\n\n  # GENERAL QUALITY\n  no-empty-descriptions:\n    description: Descriptions should not be empty strings\n    severity: warn\n    given: \"$..description\"\n    then:\n      function: pattern\n      functionOptions:\n        match: \".+\"\n\n  examples-encouraged:\n    description: Schema properties should include examples\n    severity: info\n    given: \"$.components.schemas[*].properties[*]\"\n    then:\n      field: example\n      function: truthy\n"
source_yaml_url: https://raw.githubusercontent.com/api-evangelist/amazon-lookout-for-metrics/refs/heads/main/rules/amazon-lookout-for-metrics-spectral-rules.yml
tags:
- Anomaly Detection
- Business Intelligence
- Machine Learning
- Metrics
- Monitoring
- Spectral
- Linting
- API Governance
---
