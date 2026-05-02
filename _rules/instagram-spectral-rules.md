---
api_specs:
- filename: instagram-graph-api.yaml
  format: yaml
  label: Instagram API with Instagram Login
  slug: instagram-api-with-instagram-login
  spec_type: OpenAPI
  url: https://raw.githubusercontent.com/api-evangelist/instagram/refs/heads/main/openapi/instagram-graph-api.yaml
- filename: instagram-graph-api.yaml
  format: yaml
  label: Instagram API with Facebook Login
  slug: instagram-api-with-facebook-login
  spec_type: OpenAPI
  url: https://raw.githubusercontent.com/api-evangelist/instagram/refs/heads/main/openapi/instagram-graph-api.yaml
categories:
- get
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
- tags
description: Spectral linting rules defining API design standards and conventions for Instagram.
layout: rules
name: Instagram API Rules
provider_name: Instagram
provider_slug: instagram
rule_count: 20
rules:
- description: API title must be present.
  given: $.info
  name: info-title-required
  severity: error
- description: Title should start with "Instagram".
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
- description: OpenAPI version must be 3.0.x.
  given: $
  name: openapi-version-3
  severity: error
- description: At least one server must be defined.
  given: $
  name: servers-defined
  severity: error
- description: Server URLs must use HTTPS.
  given: $.servers[*].url
  name: servers-https-only
  severity: error
- description: Server URLs should use graph.facebook.com or graph.instagram.com.
  given: $.servers[*].url
  name: servers-graph-domain
  severity: info
- description: Paths must not have trailing slashes.
  given: $.paths
  name: paths-no-trailing-slash
  severity: error
- description: Every operation must have a description.
  given: $.paths[*][get,post,put,patch,delete]
  name: operation-description-required
  severity: error
- description: Every operation must have an operationId.
  given: $.paths[*][get,post,put,patch,delete]
  name: operation-operationid-required
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
- description: Schema names should use PascalCase.
  given: $.components.schemas
  name: schema-names-pascalcase
  severity: warn
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
rules_file: rules/instagram-spectral-rules.yml
rules_url: https://raw.githubusercontent.com/api-evangelist/instagram/refs/heads/main/rules/instagram-spectral-rules.yml
severity_counts:
  error: 14
  hint: 0
  info: 2
  warn: 4
slug: instagram-spectral-rules
source_filename: instagram-spectral-rules.yml
source_heading: Spectral Ruleset
source_yaml: "rules:\n  info-title-required:\n    description: API title must be present.\n    severity: error\n    given: $.info\n    then:\n      field: title\n      function: truthy\n  info-title-format:\n    description: Title should start with \"Instagram\".\n    severity: warn\n    given: $.info.title\n    then:\n      function: pattern\n      functionOptions:\n        match: \"^Instagram \"\n  info-description-required:\n    description: API description must be present.\n    severity: error\n    given: $.info\n    then:\n      field: description\n      function: truthy\n  info-version-required:\n    description: API version must be specified.\n    severity: error\n    given: $.info\n    then:\n      field: version\n      function: truthy\n  openapi-version-3:\n    description: OpenAPI version must be 3.0.x.\n    severity: error\n    given: $\n    then:\n      field: openapi\n      function: pattern\n      functionOptions:\n        match: \"^3\\\\.0\\\\.\"\n  servers-defined:\n   \
  \ description: At least one server must be defined.\n    severity: error\n    given: $\n    then:\n      field: servers\n      function: truthy\n  servers-https-only:\n    description: Server URLs must use HTTPS.\n    severity: error\n    given: $.servers[*].url\n    then:\n      function: pattern\n      functionOptions:\n        match: \"^https://\"\n  servers-graph-domain:\n    description: Server URLs should use graph.facebook.com or graph.instagram.com.\n    severity: info\n    given: $.servers[*].url\n    then:\n      function: pattern\n      functionOptions:\n        match: \"(graph\\\\.facebook\\\\.com|graph\\\\.instagram\\\\.com)\"\n  paths-no-trailing-slash:\n    description: Paths must not have trailing slashes.\n    severity: error\n    given: $.paths\n    then:\n      field: \"@key\"\n      function: pattern\n      functionOptions:\n        notMatch: \"\\\\/$\"\n  operation-description-required:\n    description: Every operation must have a description.\n    severity: error\n\
  \    given: $.paths[*][get,post,put,patch,delete]\n    then:\n      field: description\n      function: truthy\n  operation-operationid-required:\n    description: Every operation must have an operationId.\n    severity: error\n    given: $.paths[*][get,post,put,patch,delete]\n    then:\n      field: operationId\n      function: truthy\n  operation-tags-required:\n    description: Every operation must have at least one tag.\n    severity: warn\n    given: $.paths[*][get,post,put,patch,delete]\n    then:\n      field: tags\n      function: truthy\n  tags-title-case:\n    description: Tag names should use Title Case.\n    severity: info\n    given: $.tags[*].name\n    then:\n      function: pattern\n      functionOptions:\n        match: \"^[A-Z][a-zA-Z0-9]*(\\\\s[A-Za-z0-9]+)*$\"\n  parameter-description-required:\n    description: All parameters must have a description.\n    severity: error\n    given: $.paths[*][get,post,put,patch,delete].parameters[*]\n    then:\n      field: description\n\
  \      function: truthy\n  response-success-required:\n    description: Every operation must define a success response.\n    severity: error\n    given: $.paths[*][get,post,put,patch,delete].responses\n    then:\n      function: schema\n      functionOptions:\n        schema:\n          anyOf:\n            - required: [\"200\"]\n            - required: [\"201\"]\n            - required: [\"204\"]\n  response-description-required:\n    description: All responses must have a description.\n    severity: error\n    given: $.paths[*][get,post,put,patch,delete].responses[*]\n    then:\n      field: description\n      function: truthy\n  schema-names-pascalcase:\n    description: Schema names should use PascalCase.\n    severity: warn\n    given: $.components.schemas\n    then:\n      field: \"@key\"\n      function: pattern\n      functionOptions:\n        match: \"^[A-Z][a-zA-Z0-9]*$\"\n  security-schemes-defined:\n    description: Security schemes should be defined.\n    severity: warn\n \
  \   given: $.components\n    then:\n      field: securitySchemes\n      function: truthy\n  get-no-request-body:\n    description: GET operations must not have a request body.\n    severity: error\n    given: $.paths[*].get\n    then:\n      field: requestBody\n      function: falsy\n  no-empty-descriptions:\n    description: Descriptions must not be empty.\n    severity: error\n    given: \"$..description\"\n    then:\n      function: truthy\n"
source_yaml_url: https://raw.githubusercontent.com/api-evangelist/instagram/refs/heads/main/rules/instagram-spectral-rules.yml
tags:
- Instagram
- Meta
- Photos
- Social Media
- Videos
- Content Publishing
- Spectral
- Linting
- API Governance
---
