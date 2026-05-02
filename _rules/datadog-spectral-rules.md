---
api_specs:
- filename: datadog-api-openapi.yml
  format: yaml
  label: Datadog API
  slug: datadog-api
  spec_type: OpenAPI
  url: https://raw.githubusercontent.com/api-evangelist/datadog/refs/heads/main/openapi/datadog-api-openapi.yml
- filename: datadog-metrics-openapi.yml
  format: yaml
  label: Datadog Metrics API
  slug: datadog-metrics-api
  spec_type: OpenAPI
  url: https://raw.githubusercontent.com/api-evangelist/datadog/refs/heads/main/openapi/datadog-metrics-openapi.yml
- filename: datadog-logs-openapi.yml
  format: yaml
  label: Datadog Logs API
  slug: datadog-logs-api
  spec_type: OpenAPI
  url: https://raw.githubusercontent.com/api-evangelist/datadog/refs/heads/main/openapi/datadog-logs-openapi.yml
- filename: datadog-events-openapi.yml
  format: yaml
  label: Datadog Events API
  slug: datadog-events-api
  spec_type: OpenAPI
  url: https://raw.githubusercontent.com/api-evangelist/datadog/refs/heads/main/openapi/datadog-events-openapi.yml
- filename: datadog-monitors-openapi.yml
  format: yaml
  label: Datadog Monitors API
  slug: datadog-monitors-api
  spec_type: OpenAPI
  url: https://raw.githubusercontent.com/api-evangelist/datadog/refs/heads/main/openapi/datadog-monitors-openapi.yml
- filename: datadog-incidents-openapi.yml
  format: yaml
  label: Datadog Incidents API
  slug: datadog-incidents-api
  spec_type: OpenAPI
  url: https://raw.githubusercontent.com/api-evangelist/datadog/refs/heads/main/openapi/datadog-incidents-openapi.yml
categories:
- get
- info
- 'no'
- operation
- parameter
- paths
- response
- security
- servers
- tags
description: Spectral linting rules defining API design standards and conventions for Datadog.
layout: rules
name: Datadog API Rules
provider_name: Datadog
provider_slug: datadog
rule_count: 19
rules:
- description: ''
  given: $.info
  name: info-title-required
  severity: error
- description: ''
  given: $.info.title
  name: info-title-format
  severity: warn
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
  given: $.paths
  name: paths-version-prefix
  severity: info
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
  given: $.paths[*][get,post,put,patch,delete]
  name: operation-tags-required
  severity: warn
- description: ''
  given: $.tags[*].name
  name: tags-title-case
  severity: info
- description: ''
  given: $.paths[*][get,post,put,patch,delete].parameters[*]
  name: parameter-description-required
  severity: error
- description: ''
  given: $.paths[*][get,post,put,patch,delete].responses
  name: response-success-required
  severity: error
- description: ''
  given: $.paths[*][get,post,put,patch,delete].responses[*]
  name: response-description-required
  severity: error
- description: ''
  given: $.components
  name: security-schemes-defined
  severity: warn
- description: ''
  given: $.paths[*].get
  name: get-no-request-body
  severity: error
- description: ''
  given: $..description
  name: no-empty-descriptions
  severity: error
rules_file: rules/datadog-spectral-rules.yml
rules_url: https://raw.githubusercontent.com/api-evangelist/datadog/refs/heads/main/rules/datadog-spectral-rules.yml
severity_counts:
  error: 14
  hint: 0
  info: 2
  warn: 3
slug: datadog-spectral-rules
source_filename: datadog-spectral-rules.yml
source_heading: Spectral Ruleset
source_yaml: "rules:\n  info-title-required:\n    severity: error\n    given: $.info\n    then: {field: title, function: truthy}\n  info-title-format:\n    severity: warn\n    given: $.info.title\n    then: {function: pattern, functionOptions: {match: \"^Datadog \"}}\n  info-description-required:\n    severity: error\n    given: $.info\n    then: {field: description, function: truthy}\n  info-version-required:\n    severity: error\n    given: $.info\n    then: {field: version, function: truthy}\n  servers-defined:\n    severity: error\n    given: $\n    then: {field: servers, function: truthy}\n  servers-https-only:\n    severity: error\n    given: $.servers[*].url\n    then: {function: pattern, functionOptions: {match: \"^https://\"}}\n  paths-no-trailing-slash:\n    severity: error\n    given: $.paths\n    then: {field: \"@key\", function: pattern, functionOptions: {notMatch: \"\\\\/$\"}}\n  paths-version-prefix:\n    severity: info\n    given: $.paths\n    then: {field: \"@key\", function:\
  \ pattern, functionOptions: {match: \"^\\\\/api\\\\/v[0-9]|^\\\\/v[0-9]\"}}\n  operation-description-required:\n    severity: error\n    given: $.paths[*][get,post,put,patch,delete]\n    then: {field: description, function: truthy}\n  operation-operationid-required:\n    severity: error\n    given: $.paths[*][get,post,put,patch,delete]\n    then: {field: operationId, function: truthy}\n  operation-operationid-unique:\n    severity: error\n    given: $\n    then: {function: oasOpId}\n  operation-tags-required:\n    severity: warn\n    given: $.paths[*][get,post,put,patch,delete]\n    then: {field: tags, function: truthy}\n  tags-title-case:\n    severity: info\n    given: $.tags[*].name\n    then: {function: pattern, functionOptions: {match: \"^[A-Z][a-zA-Z0-9]*(\\\\s[A-Za-z0-9]+)*$\"}}\n  parameter-description-required:\n    severity: error\n    given: $.paths[*][get,post,put,patch,delete].parameters[*]\n    then: {field: description, function: truthy}\n  response-success-required:\n \
  \   severity: error\n    given: $.paths[*][get,post,put,patch,delete].responses\n    then: {function: schema, functionOptions: {schema: {anyOf: [{required: [\"200\"]}, {required: [\"201\"]}, {required: [\"204\"]}]}}}\n  response-description-required:\n    severity: error\n    given: $.paths[*][get,post,put,patch,delete].responses[*]\n    then: {field: description, function: truthy}\n  security-schemes-defined:\n    severity: warn\n    given: $.components\n    then: {field: securitySchemes, function: truthy}\n  get-no-request-body:\n    severity: error\n    given: $.paths[*].get\n    then: {field: requestBody, function: falsy}\n  no-empty-descriptions:\n    severity: error\n    given: \"$..description\"\n    then: {function: truthy}\n"
source_yaml_url: https://raw.githubusercontent.com/api-evangelist/datadog/refs/heads/main/rules/datadog-spectral-rules.yml
tags:
- Analytics
- Dashboards
- Monitoring
- Platform
- T1
- Visualizations
- Spectral
- Linting
- API Governance
---
