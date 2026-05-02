---
api_specs:
- filename: adobe-campaign-standard-openapi-original.yml
  format: yaml
  label: Adobe Campaign Standard API
  slug: standard-api
  spec_type: OpenAPI
  url: https://raw.githubusercontent.com/api-evangelist/adobe-campaign/refs/heads/main/openapi/adobe-campaign-standard-openapi-original.yml
- filename: adobe-campaign-classic-openapi-original.yml
  format: yaml
  label: Adobe Campaign Classic API
  slug: classic-api
  spec_type: OpenAPI
  url: https://raw.githubusercontent.com/api-evangelist/adobe-campaign/refs/heads/main/openapi/adobe-campaign-classic-openapi-original.yml
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
description: Spectral linting rules defining API design standards and conventions for Adobe Campaign.
layout: rules
name: Adobe Campaign API Rules
provider_name: Adobe Campaign
provider_slug: adobe-campaign
rule_count: 17
rules:
- description: API title must be present.
  given: $.info
  name: info-title-required
  severity: error
- description: Title should start with "Adobe Campaign".
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
rules_file: rules/adobe-campaign-spectral-rules.yml
rules_url: https://raw.githubusercontent.com/api-evangelist/adobe-campaign/refs/heads/main/rules/adobe-campaign-spectral-rules.yml
severity_counts:
  error: 14
  hint: 0
  info: 1
  warn: 2
slug: adobe-campaign-spectral-rules
source_filename: adobe-campaign-spectral-rules.yml
source_heading: Spectral Ruleset
source_yaml: "rules:\n  info-title-required:\n    description: API title must be present.\n    severity: error\n    given: $.info\n    then: {field: title, function: truthy}\n  info-title-format:\n    description: Title should start with \"Adobe Campaign\".\n    severity: warn\n    given: $.info.title\n    then: {function: pattern, functionOptions: {match: \"^Adobe Campaign\"}}\n  info-description-required:\n    severity: error\n    given: $.info\n    then: {field: description, function: truthy}\n  info-version-required:\n    severity: error\n    given: $.info\n    then: {field: version, function: truthy}\n  servers-defined:\n    severity: error\n    given: $\n    then: {field: servers, function: truthy}\n  servers-https-only:\n    severity: error\n    given: $.servers[*].url\n    then: {function: pattern, functionOptions: {match: \"^https://\"}}\n  paths-no-trailing-slash:\n    severity: error\n    given: $.paths\n    then: {field: \"@key\", function: pattern, functionOptions: {notMatch:\
  \ \"\\\\/$\"}}\n  operation-description-required:\n    severity: error\n    given: $.paths[*][get,post,put,patch,delete]\n    then: {field: description, function: truthy}\n  operation-operationid-required:\n    severity: error\n    given: $.paths[*][get,post,put,patch,delete]\n    then: {field: operationId, function: truthy}\n  operation-operationid-unique:\n    severity: error\n    given: $\n    then: {function: oasOpId}\n  tags-title-case:\n    severity: info\n    given: $.tags[*].name\n    then: {function: pattern, functionOptions: {match: \"^[A-Z][a-zA-Z0-9]*(\\\\s[A-Za-z0-9]+)*$\"}}\n  parameter-description-required:\n    severity: error\n    given: $.paths[*][get,post,put,patch,delete].parameters[*]\n    then: {field: description, function: truthy}\n  response-success-required:\n    severity: error\n    given: $.paths[*][get,post,put,patch,delete].responses\n    then: {function: schema, functionOptions: {schema: {anyOf: [{required: [\"200\"]}, {required: [\"201\"]}, {required: [\"\
  204\"]}]}}}\n  response-description-required:\n    severity: error\n    given: $.paths[*][get,post,put,patch,delete].responses[*]\n    then: {field: description, function: truthy}\n  security-schemes-defined:\n    severity: warn\n    given: $.components\n    then: {field: securitySchemes, function: truthy}\n  get-no-request-body:\n    severity: error\n    given: $.paths[*].get\n    then: {field: requestBody, function: falsy}\n  no-empty-descriptions:\n    severity: error\n    given: \"$..description\"\n    then: {function: truthy}\n"
source_yaml_url: https://raw.githubusercontent.com/api-evangelist/adobe-campaign/refs/heads/main/rules/adobe-campaign-spectral-rules.yml
tags:
- Campaign Management
- Customer Experience
- Email Marketing
- Marketing Automation
- Multi-Channel Marketing
- Spectral
- Linting
- API Governance
---
