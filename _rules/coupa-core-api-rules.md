---
api_specs:
- filename: api_docs
  format: yaml
  label: Coupa Core API
  slug: ''
  spec_type: OpenAPI
  url: https://compass.coupa.com/en-us/api_docs
categories:
- coupa
description: Spectral linting rules defining API design standards and conventions for Coupa.
layout: rules
name: Coupa API Rules
provider_name: Coupa
provider_slug: coupa
rule_count: 13
rules:
- description: API info object should include contact information.
  given: $.info
  name: coupa-info-contact
  severity: error
- description: API info object should include license information.
  given: $.info
  name: coupa-info-license
  severity: warn
- description: All servers must use HTTPS.
  given: $.servers[*].url
  name: coupa-server-https
  severity: error
- description: Servers should reference the Coupa instance host.
  given: $.servers[*].url
  name: coupa-base-url
  severity: warn
- description: Operations should be protected by OAuth 2.0 or API key.
  given: $.security
  name: coupa-required-auth
  severity: error
- description: Every operation must have at least one tag.
  given: $.paths.*[get,post,put,delete,patch]
  name: coupa-operation-tags
  severity: error
- description: Every operation must have a summary.
  given: $.paths.*[get,post,put,delete,patch]
  name: coupa-operation-summary
  severity: error
- description: Operations should include a description.
  given: $.paths.*[get,post,put,delete,patch]
  name: coupa-operation-description
  severity: warn
- description: Every operation summary should be prefixed with "Coupa".
  given: $.paths.*[get,post,put,delete,patch].summary
  name: coupa-summary-prefix
  severity: warn
- description: Every operation must have an operationId.
  given: $.paths.*[get,post,put,delete,patch]
  name: coupa-operation-id
  severity: error
- description: Path segments should use snake_case to match Coupa resource naming.
  given: $.paths
  name: coupa-resource-naming
  severity: warn
- description: Operations should declare 401 and 404 error responses.
  given: $.paths.*[get,put,delete,patch]
  name: coupa-error-responses
  severity: warn
- description: List operations should support offset and limit query parameters.
  given: $.paths[?(@property.match(/.*s$/))][get].parameters
  name: coupa-pagination-params
  severity: info
rules_file: rules/coupa-core-api-rules.yml
rules_url: https://raw.githubusercontent.com/api-evangelist/coupa/refs/heads/main/rules/coupa-core-api-rules.yml
severity_counts:
  error: 6
  hint: 0
  info: 1
  warn: 6
slug: coupa-core-api-rules
source_filename: coupa-core-api-rules.yml
source_heading: Spectral Ruleset
source_yaml: "extends: [\"spectral:oas\"]\ndocumentationUrl: https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation\nrules:\n  coupa-info-contact:\n    description: API info object should include contact information.\n    message: \"{{description}}: info.contact is required.\"\n    given: \"$.info\"\n    severity: error\n    then:\n      field: contact\n      function: truthy\n  coupa-info-license:\n    description: API info object should include license information.\n    given: \"$.info\"\n    severity: warn\n    then:\n      field: license\n      function: truthy\n  coupa-server-https:\n    description: All servers must use HTTPS.\n    given: \"$.servers[*].url\"\n    severity: error\n    then:\n      function: pattern\n      functionOptions:\n        match: \"^https://\"\n  coupa-base-url:\n    description: Servers should reference the Coupa instance host.\n    given: \"$.servers[*].url\"\n    severity: warn\n    then:\n      function: pattern\n\
  \      functionOptions:\n        match: \"coupahost.com\"\n  coupa-required-auth:\n    description: Operations should be protected by OAuth 2.0 or API key.\n    given: \"$.security\"\n    severity: error\n    then:\n      function: truthy\n  coupa-operation-tags:\n    description: Every operation must have at least one tag.\n    given: \"$.paths.*[get,post,put,delete,patch]\"\n    severity: error\n    then:\n      field: tags\n      function: truthy\n  coupa-operation-summary:\n    description: Every operation must have a summary.\n    given: \"$.paths.*[get,post,put,delete,patch]\"\n    severity: error\n    then:\n      field: summary\n      function: truthy\n  coupa-operation-description:\n    description: Operations should include a description.\n    given: \"$.paths.*[get,post,put,delete,patch]\"\n    severity: warn\n    then:\n      field: description\n      function: truthy\n  coupa-summary-prefix:\n    description: Every operation summary should be prefixed with \"Coupa\".\n   \
  \ message: '{{description}}: summary should start with \"Coupa\".'\n    given: \"$.paths.*[get,post,put,delete,patch].summary\"\n    severity: warn\n    then:\n      function: pattern\n      functionOptions:\n        match: \"^Coupa\"\n  coupa-operation-id:\n    description: Every operation must have an operationId.\n    given: \"$.paths.*[get,post,put,delete,patch]\"\n    severity: error\n    then:\n      field: operationId\n      function: truthy\n  coupa-resource-naming:\n    description: Path segments should use snake_case to match Coupa resource naming.\n    given: \"$.paths\"\n    severity: warn\n    then:\n      field: \"@key\"\n      function: pattern\n      functionOptions:\n        match: \"^/[a-z0-9_/{}]+$\"\n  coupa-error-responses:\n    description: Operations should declare 401 and 404 error responses.\n    given: \"$.paths.*[get,put,delete,patch]\"\n    severity: warn\n    then:\n      field: responses.401\n      function: truthy\n  coupa-pagination-params:\n    description:\
  \ List operations should support offset and limit query parameters.\n    given: \"$.paths[?(@property.match(/.*s$/))][get].parameters\"\n    severity: info\n    then:\n      function: schema\n      functionOptions:\n        schema:\n          type: array\n"
source_yaml_url: https://raw.githubusercontent.com/api-evangelist/coupa/refs/heads/main/rules/coupa-core-api-rules.yml
tags:
- BSM
- Business Spend Management
- Cloud Platform
- Enterprise
- Financial Management
- Invoicing
- Procurement
- Supply Chain
- Spectral
- Linting
- API Governance
---
