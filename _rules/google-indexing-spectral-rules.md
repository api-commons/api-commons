---
api_specs:
- filename: openapi.yml
  format: yaml
  label: Google Indexing API
  slug: ''
  spec_type: OpenAPI
  url: https://raw.githubusercontent.com/api-evangelist/google-indexing/refs/heads/main/openapi/openapi.yml
categories:
- deprecated
- info
- 'no'
- operation
- paths
- response
- servers
- tags
description: Spectral linting rules defining API design standards and conventions for Google Indexing.
layout: rules
name: Google Indexing API Rules
provider_name: Google Indexing
provider_slug: google-indexing
rule_count: 13
rules:
- description: ''
  given: $.info
  name: info-title-required
  severity: error
- description: ''
  given: $.info
  name: info-description-required
  severity: error
- description: ''
  given: $.info
  name: info-version-required
  severity: error
- description: ''
  given: $
  name: servers-defined
  severity: error
- description: ''
  given: $.servers[*].url
  name: servers-https-only
  severity: error
- description: ''
  given: $.paths
  name: paths-no-trailing-slash
  severity: error
- description: ''
  given: $.paths[*][get,post,put,patch,delete]
  name: operation-description-required
  severity: error
- description: ''
  given: $.paths[*][get,post,put,patch,delete]
  name: operation-operationid-required
  severity: error
- description: ''
  given: $
  name: operation-operationid-unique
  severity: error
- description: ''
  given: $.tags[*].name
  name: tags-title-case
  severity: info
- description: ''
  given: $.paths[*][get,post,put,patch,delete].responses
  name: response-success-required
  severity: error
- description: Deprecated operations should explain the deprecation.
  given: $.paths[*][get,post,put,patch,delete][?(@.deprecated==true)]
  name: deprecated-description
  severity: warn
- description: ''
  given: $..description
  name: no-empty-descriptions
  severity: error
rules_file: rules/google-indexing-spectral-rules.yml
rules_url: https://raw.githubusercontent.com/api-evangelist/google-indexing/refs/heads/main/rules/google-indexing-spectral-rules.yml
severity_counts:
  error: 11
  hint: 0
  info: 1
  warn: 1
slug: google-indexing-spectral-rules
source_filename: google-indexing-spectral-rules.yml
source_heading: Spectral Ruleset
source_yaml: "rules:\n  info-title-required:\n    severity: error\n    given: $.info\n    then: {field: title, function: truthy}\n  info-description-required:\n    severity: error\n    given: $.info\n    then: {field: description, function: truthy}\n  info-version-required:\n    severity: error\n    given: $.info\n    then: {field: version, function: truthy}\n  servers-defined:\n    severity: error\n    given: $\n    then: {field: servers, function: truthy}\n  servers-https-only:\n    severity: error\n    given: $.servers[*].url\n    then: {function: pattern, functionOptions: {match: \"^https://\"}}\n  paths-no-trailing-slash:\n    severity: error\n    given: $.paths\n    then: {field: \"@key\", function: pattern, functionOptions: {notMatch: \"\\\\/$\"}}\n  operation-description-required:\n    severity: error\n    given: $.paths[*][get,post,put,patch,delete]\n    then: {field: description, function: truthy}\n  operation-operationid-required:\n    severity: error\n    given: $.paths[*][get,post,put,patch,delete]\n\
  \    then: {field: operationId, function: truthy}\n  operation-operationid-unique:\n    severity: error\n    given: $\n    then: {function: oasOpId}\n  tags-title-case:\n    severity: info\n    given: $.tags[*].name\n    then: {function: pattern, functionOptions: {match: \"^[A-Z][a-zA-Z0-9]*(\\\\s[A-Za-z0-9]+)*$\"}}\n  response-success-required:\n    severity: error\n    given: $.paths[*][get,post,put,patch,delete].responses\n    then: {function: schema, functionOptions: {schema: {anyOf: [{required: [\"200\"]}, {required: [\"201\"]}, {required: [\"204\"]}]}}}\n  deprecated-description:\n    severity: warn\n    description: Deprecated operations should explain the deprecation.\n    given: $.paths[*][get,post,put,patch,delete][?(@.deprecated==true)]\n    then: {field: description, function: pattern, functionOptions: {match: \"[Dd]eprecated|[Ss]unset\"}}\n  no-empty-descriptions:\n    severity: error\n    given: \"$..description\"\n    then: {function: truthy}\n"
source_yaml_url: https://raw.githubusercontent.com/api-evangelist/google-indexing/refs/heads/main/rules/google-indexing-spectral-rules.yml
tags:
- Crawling
- Google
- Indexing
- Search
- SEO
- URLs
- Spectral
- Linting
- API Governance
---
