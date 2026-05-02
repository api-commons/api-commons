---
api_specs:
- filename: amazon-marketplace-openapi-original.yaml
  format: yaml
  label: AWS Marketplace Catalog API
  slug: aws-marketplace-catalog-api
  spec_type: OpenAPI
  url: https://raw.githubusercontent.com/api-evangelist/amazon-marketplace/refs/heads/main/openapi/amazon-marketplace-openapi-original.yaml
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
description: Spectral linting rules defining API design standards and conventions for Amazon Marketplace.
layout: rules
name: Amazon Marketplace API Rules
provider_name: Amazon Marketplace
provider_slug: amazon-marketplace
rule_count: 18
rules:
- description: Info title must be present
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
- description: Operation summaries should start with "Amazon Marketplace"
  given: $.paths[*][get,post,put,patch,delete].summary
  name: operation-summary-prefix
  severity: info
- description: Every operation must have at least one tag
  given: $.paths[*][get,post,put,patch,delete]
  name: operation-tags-required
  severity: warn
- description: All parameters must have descriptions
  given: $.paths[*][get,post,put,patch,delete].parameters[*]
  name: parameter-description-required
  severity: warn
- description: All responses must have a description
  given: $.paths[*][get,post,put,patch,delete].responses[*]
  name: response-description-required
  severity: warn
- description: Top-level schemas should have descriptions
  given: $.components.schemas[*]
  name: schema-description
  severity: info
- description: Security schemes must be defined
  given: $.components
  name: security-schemes-required
  severity: error
- description: GET operations should not have request bodies
  given: $.paths[*].get
  name: http-get-no-body
  severity: error
- description: Descriptions should not be empty strings
  given: $..description
  name: no-empty-descriptions
  severity: warn
- description: Path segments should use kebab-case
  given: $.paths
  name: paths-kebab-case
  severity: info
- description: Schema properties should include examples
  given: $.components.schemas[*].properties[*]
  name: examples-encouraged
  severity: info
rules_file: rules/amazon-marketplace-spectral-rules.yml
rules_url: https://raw.githubusercontent.com/api-evangelist/amazon-marketplace/refs/heads/main/rules/amazon-marketplace-spectral-rules.yml
severity_counts:
  error: 7
  hint: 0
  info: 4
  warn: 7
slug: amazon-marketplace-spectral-rules
source_filename: amazon-marketplace-spectral-rules.yml
source_heading: Spectral Ruleset
source_yaml: "rules:\n  info-title-required:\n    description: Info title must be present\n    severity: error\n    given: \"$.info\"\n    then:\n      field: title\n      function: truthy\n  info-description-required:\n    description: Info description must be present\n    severity: warn\n    given: \"$.info\"\n    then:\n      field: description\n      function: truthy\n  info-version-required:\n    description: API version must be defined\n    severity: error\n    given: \"$.info\"\n    then:\n      field: version\n      function: truthy\n  openapi-version:\n    description: Must use OpenAPI 3.0.x\n    severity: error\n    given: \"$\"\n    then:\n      field: openapi\n      function: pattern\n      functionOptions:\n        match: \"^3\\\\.0\\\\.\"\n  servers-required:\n    description: Servers must be defined\n    severity: error\n    given: \"$\"\n    then:\n      field: servers\n      function: truthy\n  servers-https:\n    description: Server URLs should use HTTPS\n    severity:\
  \ warn\n    given: \"$.servers[*]\"\n    then:\n      field: url\n      function: pattern\n      functionOptions:\n        match: \"^https://\"\n  operation-operationId-required:\n    description: Every operation must have an operationId\n    severity: error\n    given: \"$.paths[*][get,post,put,patch,delete]\"\n    then:\n      field: operationId\n      function: truthy\n  operation-summary-required:\n    description: Every operation must have a summary\n    severity: warn\n    given: \"$.paths[*][get,post,put,patch,delete]\"\n    then:\n      field: summary\n      function: truthy\n  operation-summary-prefix:\n    description: Operation summaries should start with \"Amazon Marketplace\"\n    severity: info\n    given: \"$.paths[*][get,post,put,patch,delete].summary\"\n    then:\n      function: pattern\n      functionOptions:\n        match: \"^Amazon Marketplace\"\n  operation-tags-required:\n    description: Every operation must have at least one tag\n    severity: warn\n    given:\
  \ \"$.paths[*][get,post,put,patch,delete]\"\n    then:\n      field: tags\n      function: truthy\n  parameter-description-required:\n    description: All parameters must have descriptions\n    severity: warn\n    given: \"$.paths[*][get,post,put,patch,delete].parameters[*]\"\n    then:\n      field: description\n      function: truthy\n  response-description-required:\n    description: All responses must have a description\n    severity: warn\n    given: \"$.paths[*][get,post,put,patch,delete].responses[*]\"\n    then:\n      field: description\n      function: truthy\n  schema-description:\n    description: Top-level schemas should have descriptions\n    severity: info\n    given: \"$.components.schemas[*]\"\n    then:\n      field: description\n      function: truthy\n  security-schemes-required:\n    description: Security schemes must be defined\n    severity: error\n    given: \"$.components\"\n    then:\n      field: securitySchemes\n      function: truthy\n  http-get-no-body:\n\
  \    description: GET operations should not have request bodies\n    severity: error\n    given: \"$.paths[*].get\"\n    then:\n      field: requestBody\n      function: falsy\n  no-empty-descriptions:\n    description: Descriptions should not be empty strings\n    severity: warn\n    given: \"$..description\"\n    then:\n      function: pattern\n      functionOptions:\n        match: \".+\"\n  paths-kebab-case:\n    description: Path segments should use kebab-case\n    severity: info\n    given: \"$.paths\"\n    then:\n      field: \"@key\"\n      function: pattern\n      functionOptions:\n        match: \"^(/[a-z0-9{}_.\\\\-]+)+$\"\n  examples-encouraged:\n    description: Schema properties should include examples\n    severity: info\n    given: \"$.components.schemas[*].properties[*]\"\n    then:\n      field: example\n      function: truthy\n"
source_yaml_url: https://raw.githubusercontent.com/api-evangelist/amazon-marketplace/refs/heads/main/rules/amazon-marketplace-spectral-rules.yml
tags:
- Commerce
- ISV
- Marketplace
- Software Catalog
- Spectral
- Linting
- API Governance
---
