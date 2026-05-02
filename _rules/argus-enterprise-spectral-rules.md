---
api_specs:
- filename: argus-enterprise-core-openapi.yml
  format: yaml
  label: ARGUS Enterprise Core API
  slug: argus-enterprise-core
  spec_type: OpenAPI
  url: https://raw.githubusercontent.com/api-evangelist/argus-enterprise/refs/heads/main/openapi/argus-enterprise-core-openapi.yml
- filename: argus-enterprise-webhooks-openapi.yml
  format: yaml
  label: ARGUS Enterprise Webhook API
  slug: argus-enterprise-webhooks
  spec_type: OpenAPI
  url: https://raw.githubusercontent.com/api-evangelist/argus-enterprise/refs/heads/main/openapi/argus-enterprise-webhooks-openapi.yml
categories:
- info
- 'no'
- operation
- parameter
- paths
- response
- schema
- security
description: Spectral linting rules defining API design standards and conventions for ARGUS Enterprise.
layout: rules
name: ARGUS Enterprise API Rules
provider_name: ARGUS Enterprise
provider_slug: argus-enterprise
rule_count: 14
rules:
- description: API title should start with "Argus Enterprise"
  given: $.info.title
  name: info-title-prefix
  severity: warn
- description: API must have a description
  given: $.info
  name: info-description-required
  severity: error
- description: Every operation must have a summary
  given: $.paths[*][get,post,put,delete,patch]
  name: operation-summary-required
  severity: error
- description: Summaries should start with "Argus Enterprise"
  given: $.paths[*][get,post,put,delete,patch].summary
  name: operation-summary-prefix
  severity: warn
- description: Every operation must have an operationId
  given: $.paths[*][get,post,put,delete,patch]
  name: operation-operationid-required
  severity: error
- description: Operations must be tagged
  given: $.paths[*][get,post,put,delete,patch]
  name: operation-tags-required
  severity: warn
- description: Paths should be versioned
  given: $.paths[*]~
  name: paths-versioned
  severity: info
- description: Path segments should use kebab-case
  given: $.paths[*]~
  name: paths-kebab-case
  severity: warn
- description: Every operation must define responses
  given: $.paths[*][get,post,put,delete,patch].responses
  name: response-success-required
  severity: error
- description: All responses must have descriptions
  given: $.paths[*][get,post,put,delete,patch].responses[*]
  name: response-description-required
  severity: warn
- description: API must define security schemes
  given: $
  name: security-definitions-required
  severity: warn
- description: Schema properties should have descriptions
  given: $.components.schemas[*].properties[*]
  name: schema-properties-description
  severity: info
- description: Summaries must not be empty
  given: $.paths[*][get,post,put,delete,patch].summary
  name: no-empty-summaries
  severity: error
- description: Parameters should have descriptions
  given: $.paths[*][get,post,put,delete,patch].parameters[*]
  name: parameter-description-required
  severity: warn
rules_file: rules/argus-enterprise-spectral-rules.yml
rules_url: https://raw.githubusercontent.com/api-evangelist/argus-enterprise/refs/heads/main/rules/argus-enterprise-spectral-rules.yml
severity_counts:
  error: 5
  hint: 0
  info: 2
  warn: 7
slug: argus-enterprise-spectral-rules
source_filename: argus-enterprise-spectral-rules.yml
source_heading: Spectral Ruleset
source_yaml: "# ARGUS Enterprise API Spectral Ruleset\n\nrules:\n\n  info-title-prefix:\n    description: API title should start with \"Argus Enterprise\"\n    severity: warn\n    given: \"$.info.title\"\n    then:\n      function: pattern\n      functionOptions:\n        match: \"^Argus Enterprise\"\n\n  info-description-required:\n    description: API must have a description\n    severity: error\n    given: \"$.info\"\n    then:\n      field: description\n      function: truthy\n\n  operation-summary-required:\n    description: Every operation must have a summary\n    severity: error\n    given: \"$.paths[*][get,post,put,delete,patch]\"\n    then:\n      field: summary\n      function: truthy\n\n  operation-summary-prefix:\n    description: Summaries should start with \"Argus Enterprise\"\n    severity: warn\n    given: \"$.paths[*][get,post,put,delete,patch].summary\"\n    then:\n      function: pattern\n      functionOptions:\n        match: \"^Argus Enterprise\"\n\n  operation-operationid-required:\n\
  \    description: Every operation must have an operationId\n    severity: error\n    given: \"$.paths[*][get,post,put,delete,patch]\"\n    then:\n      field: operationId\n      function: truthy\n\n  operation-tags-required:\n    description: Operations must be tagged\n    severity: warn\n    given: \"$.paths[*][get,post,put,delete,patch]\"\n    then:\n      field: tags\n      function: truthy\n\n  paths-versioned:\n    description: Paths should be versioned\n    severity: info\n    given: \"$.paths[*]~\"\n    then:\n      function: pattern\n      functionOptions:\n        match: \"^/v[0-9]\"\n\n  paths-kebab-case:\n    description: Path segments should use kebab-case\n    severity: warn\n    given: \"$.paths[*]~\"\n    then:\n      function: pattern\n      functionOptions:\n        match: \"^(/v[0-9]+)?(/[a-z0-9{}-]+)*$\"\n\n  response-success-required:\n    description: Every operation must define responses\n    severity: error\n    given: \"$.paths[*][get,post,put,delete,patch].responses\"\
  \n    then:\n      function: schema\n      functionOptions:\n        schema:\n          type: object\n          minProperties: 1\n\n  response-description-required:\n    description: All responses must have descriptions\n    severity: warn\n    given: \"$.paths[*][get,post,put,delete,patch].responses[*]\"\n    then:\n      field: description\n      function: truthy\n\n  security-definitions-required:\n    description: API must define security schemes\n    severity: warn\n    given: \"$\"\n    then:\n      field: components\n      function: truthy\n\n  schema-properties-description:\n    description: Schema properties should have descriptions\n    severity: info\n    given: \"$.components.schemas[*].properties[*]\"\n    then:\n      field: description\n      function: truthy\n\n  no-empty-summaries:\n    description: Summaries must not be empty\n    severity: error\n    given: \"$.paths[*][get,post,put,delete,patch].summary\"\n    then:\n      function: pattern\n      functionOptions:\n\
  \        match: \".+\"\n\n  parameter-description-required:\n    description: Parameters should have descriptions\n    severity: warn\n    given: \"$.paths[*][get,post,put,delete,patch].parameters[*]\"\n    then:\n      field: description\n      function: truthy\n"
source_yaml_url: https://raw.githubusercontent.com/api-evangelist/argus-enterprise/refs/heads/main/rules/argus-enterprise-spectral-rules.yml
tags:
- Altus Group
- Asset Management
- Cash Flow Modeling
- Commercial Real Estate
- Portfolio Management
- Valuation
- Spectral
- Linting
- API Governance
---
