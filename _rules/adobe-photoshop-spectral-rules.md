---
api_specs:
- filename: adobe-photoshop-api-openapi-original.yml
  format: yaml
  label: Adobe Photoshop API
  slug: photoshop-api
  spec_type: OpenAPI
  url: https://raw.githubusercontent.com/api-evangelist/adobe-photoshop/refs/heads/main/openapi/adobe-photoshop-api-openapi-original.yml
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
description: Spectral linting rules defining API design standards and conventions for Adobe Photoshop.
layout: rules
name: Adobe Photoshop API Rules
provider_name: Adobe Photoshop
provider_slug: adobe-photoshop
rule_count: 19
rules:
- description: API title must be present.
  given: $.info
  name: info-title-required
  severity: error
- description: Title should start with "Adobe" or "Photoshop".
  given: $.info.title
  name: info-title-format
  severity: warn
- description: API description must be present.
  given: $.info
  name: info-description-required
  severity: error
- description: API version must be specified.
  given: $.info
  name: info-version-required
  severity: error
- description: At least one server must be defined.
  given: $
  name: servers-defined
  severity: error
- description: Server URLs must use HTTPS.
  given: $.servers[*].url
  name: servers-https-only
  severity: error
- description: Paths must not have trailing slashes.
  given: $.paths
  name: paths-no-trailing-slash
  severity: error
- description: Path segments should use camelCase.
  given: $.paths
  name: paths-camelcase
  severity: info
- description: Every operation must have a description.
  given: $.paths[*][get,post,put,patch,delete]
  name: operation-description-required
  severity: error
- description: Every operation must have an operationId.
  given: $.paths[*][get,post,put,patch,delete]
  name: operation-operationid-required
  severity: error
- description: Operation IDs must be unique.
  given: $
  name: operation-operationid-unique
  severity: error
- description: Every operation must have at least one tag.
  given: $.paths[*][get,post,put,patch,delete]
  name: operation-tags-required
  severity: warn
- description: Tag names should use Title Case.
  given: $.tags[*].name
  name: tags-title-case
  severity: info
- description: All parameters must have a description.
  given: $.paths[*][get,post,put,patch,delete].parameters[*]
  name: parameter-description-required
  severity: error
- description: Every operation must define a success response.
  given: $.paths[*][get,post,put,patch,delete].responses
  name: response-success-required
  severity: error
- description: All responses must have a description.
  given: $.paths[*][get,post,put,patch,delete].responses[*]
  name: response-description-required
  severity: error
- description: Security schemes should be defined.
  given: $.components
  name: security-schemes-defined
  severity: warn
- description: GET operations must not have a request body.
  given: $.paths[*].get
  name: get-no-request-body
  severity: error
- description: Descriptions must not be empty.
  given: $..description
  name: no-empty-descriptions
  severity: error
rules_file: rules/adobe-photoshop-spectral-rules.yml
rules_url: https://raw.githubusercontent.com/api-evangelist/adobe-photoshop/refs/heads/main/rules/adobe-photoshop-spectral-rules.yml
severity_counts:
  error: 14
  hint: 0
  info: 2
  warn: 3
slug: adobe-photoshop-spectral-rules
source_filename: adobe-photoshop-spectral-rules.yml
source_heading: Spectral Ruleset
source_yaml: "rules:\n  info-title-required:\n    description: API title must be present.\n    severity: error\n    given: $.info\n    then: {field: title, function: truthy}\n  info-title-format:\n    description: Title should start with \"Adobe\" or \"Photoshop\".\n    severity: warn\n    given: $.info.title\n    then: {function: pattern, functionOptions: {match: \"^(Adobe|Photoshop) \"}}\n  info-description-required:\n    description: API description must be present.\n    severity: error\n    given: $.info\n    then: {field: description, function: truthy}\n  info-version-required:\n    description: API version must be specified.\n    severity: error\n    given: $.info\n    then: {field: version, function: truthy}\n  servers-defined:\n    description: At least one server must be defined.\n    severity: error\n    given: $\n    then: {field: servers, function: truthy}\n  servers-https-only:\n    description: Server URLs must use HTTPS.\n    severity: error\n    given: $.servers[*].url\n\
  \    then: {function: pattern, functionOptions: {match: \"^https://\"}}\n  paths-no-trailing-slash:\n    description: Paths must not have trailing slashes.\n    severity: error\n    given: $.paths\n    then: {field: \"@key\", function: pattern, functionOptions: {notMatch: \"\\\\/$\"}}\n  paths-camelcase:\n    description: Path segments should use camelCase.\n    severity: info\n    given: $.paths\n    then: {field: \"@key\", function: pattern, functionOptions: {notMatch: \"\\\\/[a-z]+_[a-z]\"}}\n  operation-description-required:\n    description: Every operation must have a description.\n    severity: error\n    given: $.paths[*][get,post,put,patch,delete]\n    then: {field: description, function: truthy}\n  operation-operationid-required:\n    description: Every operation must have an operationId.\n    severity: error\n    given: $.paths[*][get,post,put,patch,delete]\n    then: {field: operationId, function: truthy}\n  operation-operationid-unique:\n    description: Operation IDs must\
  \ be unique.\n    severity: error\n    given: $\n    then: {function: oasOpId}\n  operation-tags-required:\n    description: Every operation must have at least one tag.\n    severity: warn\n    given: $.paths[*][get,post,put,patch,delete]\n    then: {field: tags, function: truthy}\n  tags-title-case:\n    description: Tag names should use Title Case.\n    severity: info\n    given: $.tags[*].name\n    then: {function: pattern, functionOptions: {match: \"^[A-Z][a-zA-Z0-9]*(\\\\s[A-Za-z0-9]+)*$\"}}\n  parameter-description-required:\n    description: All parameters must have a description.\n    severity: error\n    given: $.paths[*][get,post,put,patch,delete].parameters[*]\n    then: {field: description, function: truthy}\n  response-success-required:\n    description: Every operation must define a success response.\n    severity: error\n    given: $.paths[*][get,post,put,patch,delete].responses\n    then: {function: schema, functionOptions: {schema: {anyOf: [{required: [\"200\"]}, {required:\
  \ [\"201\"]}, {required: [\"202\"]}, {required: [\"204\"]}]}}}\n  response-description-required:\n    description: All responses must have a description.\n    severity: error\n    given: $.paths[*][get,post,put,patch,delete].responses[*]\n    then: {field: description, function: truthy}\n  security-schemes-defined:\n    description: Security schemes should be defined.\n    severity: warn\n    given: $.components\n    then: {field: securitySchemes, function: truthy}\n  get-no-request-body:\n    description: GET operations must not have a request body.\n    severity: error\n    given: $.paths[*].get\n    then: {field: requestBody, function: falsy}\n  no-empty-descriptions:\n    description: Descriptions must not be empty.\n    severity: error\n    given: \"$..description\"\n    then: {function: truthy}\n"
source_yaml_url: https://raw.githubusercontent.com/api-evangelist/adobe-photoshop/refs/heads/main/rules/adobe-photoshop-spectral-rules.yml
tags:
- AI/ML
- Creative Cloud
- Image Editing
- Photoshop
- Plugins
- REST API
- Scripting
- Spectral
- Linting
- API Governance
---
