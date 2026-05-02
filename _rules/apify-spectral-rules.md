---
api_specs:
- filename: apify-api.yaml
  format: yaml
  label: Apify API
  slug: apify-api
  spec_type: OpenAPI
  url: https://raw.githubusercontent.com/api-evangelist/apify/refs/heads/main/openapi/apify-api.yaml
categories:
- info
- operation
- pagination
- parameter
- paths
- response
- servers
description: Spectral linting rules defining API design standards and conventions for Apify.
layout: rules
name: Apify API Rules
provider_name: Apify
provider_slug: apify
rule_count: 11
rules:
- description: API title must start with 'Apify'.
  given: $.info
  name: info-title-prefix
  severity: warn
- description: API must have a description.
  given: $.info
  name: info-description-required
  severity: error
- description: All server URLs must use HTTPS.
  given: $.servers[*]
  name: servers-https
  severity: error
- description: Operation summaries must start with 'Apify'.
  given: $.paths[*][get,post,put,patch,delete]
  name: operation-summary-prefix
  severity: warn
- description: Every operation must have an operationId.
  given: $.paths[*][get,post,put,patch,delete]
  name: operation-id-required
  severity: error
- description: OperationId must use camelCase.
  given: $.paths[*][get,post,put,patch,delete]
  name: operation-id-camelcase
  severity: warn
- description: Every operation must have at least one tag.
  given: $.paths[*][get,post,put,patch,delete]
  name: operation-tags-required
  severity: warn
- description: Paths must include API version /v2/ prefix.
  given: $.paths
  name: paths-v2-version
  severity: info
- description: Every operation must have a 2xx response.
  given: $.paths[*][get,post,put,patch,delete].responses
  name: response-success-required
  severity: error
- description: All parameters must have a description.
  given: $.paths[*][get,post,put,patch,delete].parameters[*]
  name: parameter-description-required
  severity: warn
- description: Collection endpoints should use limit/offset pagination.
  given: $.paths[*].get.parameters[*]
  name: pagination-limit-offset
  severity: info
rules_file: rules/apify-spectral-rules.yml
rules_url: https://raw.githubusercontent.com/api-evangelist/apify/refs/heads/main/rules/apify-spectral-rules.yml
severity_counts:
  error: 4
  hint: 0
  info: 2
  warn: 5
slug: apify-spectral-rules
source_filename: apify-spectral-rules.yml
source_heading: Spectral Ruleset
source_yaml: "extends: spectral:oas\nrules:\n  info-title-prefix:\n    description: API title must start with 'Apify'.\n    severity: warn\n    given: '$.info'\n    then:\n      field: title\n      function: pattern\n      functionOptions:\n        match: '^Apify'\n\n  info-description-required:\n    description: API must have a description.\n    severity: error\n    given: '$.info'\n    then:\n      field: description\n      function: truthy\n\n  servers-https:\n    description: All server URLs must use HTTPS.\n    severity: error\n    given: '$.servers[*]'\n    then:\n      field: url\n      function: pattern\n      functionOptions:\n        match: '^https://'\n\n  operation-summary-prefix:\n    description: Operation summaries must start with 'Apify'.\n    severity: warn\n    given: '$.paths[*][get,post,put,patch,delete]'\n    then:\n      field: summary\n      function: pattern\n      functionOptions:\n        match: '^Apify'\n\n  operation-id-required:\n    description: Every operation\
  \ must have an operationId.\n    severity: error\n    given: '$.paths[*][get,post,put,patch,delete]'\n    then:\n      field: operationId\n      function: truthy\n\n  operation-id-camelcase:\n    description: OperationId must use camelCase.\n    severity: warn\n    given: '$.paths[*][get,post,put,patch,delete]'\n    then:\n      field: operationId\n      function: pattern\n      functionOptions:\n        match: '^[a-z][a-zA-Z0-9]*$'\n\n  operation-tags-required:\n    description: Every operation must have at least one tag.\n    severity: warn\n    given: '$.paths[*][get,post,put,patch,delete]'\n    then:\n      field: tags\n      function: truthy\n\n  paths-v2-version:\n    description: Paths must include API version /v2/ prefix.\n    severity: info\n    given: '$.paths'\n    then:\n      field: '@key'\n      function: pattern\n      functionOptions:\n        notMatch: '^/v[0-9]+'\n\n  response-success-required:\n    description: Every operation must have a 2xx response.\n    severity:\
  \ error\n    given: '$.paths[*][get,post,put,patch,delete].responses'\n    then:\n      function: schema\n      functionOptions:\n        schema:\n          anyOf:\n            - required: ['200']\n            - required: ['201']\n            - required: ['204']\n\n  parameter-description-required:\n    description: All parameters must have a description.\n    severity: warn\n    given: '$.paths[*][get,post,put,patch,delete].parameters[*]'\n    then:\n      field: description\n      function: truthy\n\n  pagination-limit-offset:\n    description: Collection endpoints should use limit/offset pagination.\n    severity: info\n    given: '$.paths[*].get.parameters[*]'\n    then:\n      field: name\n      function: enumeration\n      functionOptions:\n        values: [limit, offset, exclusiveStartKey]\n"
source_yaml_url: https://raw.githubusercontent.com/api-evangelist/apify/refs/heads/main/rules/apify-spectral-rules.yml
tags:
- Actors
- Browser Automation
- Crawling
- Data Aggregation
- Data Extraction
- Web Automation
- Web Scraping
- Spectral
- Linting
- API Governance
---
