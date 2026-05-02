---
api_specs:
- filename: gitlab-api-v4-groups-openapi-original.yml
  format: yaml
  label: GitLab Groups API
  slug: apiv4groups
  spec_type: OpenAPI
  url: https://raw.githubusercontent.com/api-evangelist/gitlab/refs/heads/main/openapi/gitlab-api-v4-groups-openapi-original.yml
- filename: gitlab-api-v4-projects-openapi-original.yml
  format: yaml
  label: GitLab Projects API
  slug: apiv4projects
  spec_type: OpenAPI
  url: https://raw.githubusercontent.com/api-evangelist/gitlab/refs/heads/main/openapi/gitlab-api-v4-projects-openapi-original.yml
- filename: gitlab-api-v4-admin-openapi-original.yml
  format: yaml
  label: GitLab Admin API
  slug: apiv4admin
  spec_type: OpenAPI
  url: https://raw.githubusercontent.com/api-evangelist/gitlab/refs/heads/main/openapi/gitlab-api-v4-admin-openapi-original.yml
- filename: gitlab-api-v4-applications-openapi-original.yml
  format: yaml
  label: GitLab Applications API
  slug: apiv4applications
  spec_type: OpenAPI
  url: https://raw.githubusercontent.com/api-evangelist/gitlab/refs/heads/main/openapi/gitlab-api-v4-applications-openapi-original.yml
- filename: gitlab-api-v4-avatar-openapi-original.yml
  format: yaml
  label: GitLab Avatar API
  slug: apiv4avatar
  spec_type: OpenAPI
  url: https://raw.githubusercontent.com/api-evangelist/gitlab/refs/heads/main/openapi/gitlab-api-v4-avatar-openapi-original.yml
- filename: gitlab-api-v4-broadcast-messages-openapi-original.yml
  format: yaml
  label: GitLab Broadcast Messages API
  slug: apiv4broadcast-messages
  spec_type: OpenAPI
  url: https://raw.githubusercontent.com/api-evangelist/gitlab/refs/heads/main/openapi/gitlab-api-v4-broadcast-messages-openapi-original.yml
- filename: gitlab-api-v4-bulk-imports-openapi-original.yml
  format: yaml
  label: GitLab Bulk Imports API
  slug: apiv4bulk-imports
  spec_type: OpenAPI
  url: https://raw.githubusercontent.com/api-evangelist/gitlab/refs/heads/main/openapi/gitlab-api-v4-bulk-imports-openapi-original.yml
- filename: gitlab-api-v4-application-openapi-original.yml
  format: yaml
  label: GitLab Application Settings API
  slug: apiv4application
  spec_type: OpenAPI
  url: https://raw.githubusercontent.com/api-evangelist/gitlab/refs/heads/main/openapi/gitlab-api-v4-application-openapi-original.yml
- filename: gitlab-api-v4-metadata-openapi-original.yml
  format: yaml
  label: GitLab Metadata API
  slug: apiv4metadata
  spec_type: OpenAPI
  url: https://raw.githubusercontent.com/api-evangelist/gitlab/refs/heads/main/openapi/gitlab-api-v4-metadata-openapi-original.yml
- filename: gitlab-api-v4-version-openapi-original.yml
  format: yaml
  label: GitLab Version API
  slug: apiv4version
  spec_type: OpenAPI
  url: https://raw.githubusercontent.com/api-evangelist/gitlab/refs/heads/main/openapi/gitlab-api-v4-version-openapi-original.yml
- filename: gitlab-openapi-original.yml
  format: yaml
  label: GitLab REST API
  slug: gitlab-rest-api
  spec_type: OpenAPI
  url: https://raw.githubusercontent.com/api-evangelist/gitlab/refs/heads/main/openapi/gitlab-openapi-original.yml
- filename: gitlab-oauth2-openapi.yml
  format: yaml
  label: GitLab OAuth 2.0 API
  slug: gitlab-oauth2-api
  spec_type: OpenAPI
  url: https://raw.githubusercontent.com/api-evangelist/gitlab/refs/heads/main/openapi/gitlab-oauth2-openapi.yml
- filename: gitlab-webhooks-openapi.yml
  format: yaml
  label: GitLab Webhooks
  slug: gitlab-webhooks
  spec_type: OpenAPI
  url: https://raw.githubusercontent.com/api-evangelist/gitlab/refs/heads/main/openapi/gitlab-webhooks-openapi.yml
categories:
- get
- info
- 'no'
- openapi
- operation
- parameter
- paths
- request
- response
- schema
- security
- servers
- tags
description: Spectral linting rules defining API design standards and conventions for GitLab.
layout: rules
name: GitLab API Rules
provider_name: GitLab
provider_slug: gitlab
rule_count: 24
rules:
- description: API title must be present.
  given: $.info
  name: info-title-required
  severity: error
- description: Title should start with "GitLab".
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
- description: Paths must not have trailing slashes.
  given: $.paths
  name: paths-no-trailing-slash
  severity: error
- description: Path segments should use snake_case (GitLab convention).
  given: $.paths
  name: paths-snake-case
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
- description: Parameter names should use snake_case (GitLab convention).
  given: $.paths[*][get,post,put,patch,delete].parameters[*]
  name: parameter-snake-case
  severity: warn
- description: Request bodies should use application/json.
  given: $.paths[*][post,put,patch].requestBody.content
  name: request-body-json
  severity: warn
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
- description: Schema properties should use snake_case (GitLab convention).
  given: $.components.schemas[*].properties
  name: schema-properties-snake-case
  severity: info
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
rules_file: rules/gitlab-spectral-rules.yml
rules_url: https://raw.githubusercontent.com/api-evangelist/gitlab/refs/heads/main/rules/gitlab-spectral-rules.yml
severity_counts:
  error: 15
  hint: 0
  info: 3
  warn: 6
slug: gitlab-spectral-rules
source_filename: gitlab-spectral-rules.yml
source_heading: Spectral Ruleset
source_yaml: "rules:\n  info-title-required:\n    description: API title must be present.\n    severity: error\n    given: $.info\n    then:\n      field: title\n      function: truthy\n  info-title-format:\n    description: Title should start with \"GitLab\".\n    severity: warn\n    given: $.info.title\n    then:\n      function: pattern\n      functionOptions:\n        match: \"^GitLab \"\n  info-description-required:\n    description: API description must be present.\n    severity: error\n    given: $.info\n    then:\n      field: description\n      function: truthy\n  info-version-required:\n    description: API version must be specified.\n    severity: error\n    given: $.info\n    then:\n      field: version\n      function: truthy\n  openapi-version-3:\n    description: OpenAPI version must be 3.0.x.\n    severity: error\n    given: $\n    then:\n      field: openapi\n      function: pattern\n      functionOptions:\n        match: \"^3\\\\.0\\\\.\"\n  servers-defined:\n    description:\
  \ At least one server must be defined.\n    severity: error\n    given: $\n    then:\n      field: servers\n      function: truthy\n  servers-https-only:\n    description: Server URLs must use HTTPS.\n    severity: error\n    given: $.servers[*].url\n    then:\n      function: pattern\n      functionOptions:\n        match: \"^https://\"\n  paths-no-trailing-slash:\n    description: Paths must not have trailing slashes.\n    severity: error\n    given: $.paths\n    then:\n      field: \"@key\"\n      function: pattern\n      functionOptions:\n        notMatch: \"\\\\/$\"\n  paths-snake-case:\n    description: Path segments should use snake_case (GitLab convention).\n    severity: info\n    given: $.paths\n    then:\n      field: \"@key\"\n      function: pattern\n      functionOptions:\n        notMatch: \"\\\\/[a-z]+[A-Z]\"\n  operation-description-required:\n    description: Every operation must have a description.\n    severity: error\n    given: $.paths[*][get,post,put,patch,delete]\n\
  \    then:\n      field: description\n      function: truthy\n  operation-operationid-required:\n    description: Every operation must have an operationId.\n    severity: error\n    given: $.paths[*][get,post,put,patch,delete]\n    then:\n      field: operationId\n      function: truthy\n  operation-operationid-unique:\n    description: Operation IDs must be unique.\n    severity: error\n    given: $\n    then:\n      function: oasOpId\n  operation-tags-required:\n    description: Every operation must have at least one tag.\n    severity: warn\n    given: $.paths[*][get,post,put,patch,delete]\n    then:\n      field: tags\n      function: truthy\n  tags-title-case:\n    description: Tag names should use Title Case.\n    severity: info\n    given: $.tags[*].name\n    then:\n      function: pattern\n      functionOptions:\n        match: \"^[A-Z][a-zA-Z0-9]*(\\\\s[A-Za-z0-9]+)*$\"\n  parameter-description-required:\n    description: All parameters must have a description.\n    severity:\
  \ error\n    given: $.paths[*][get,post,put,patch,delete].parameters[*]\n    then:\n      field: description\n      function: truthy\n  parameter-snake-case:\n    description: Parameter names should use snake_case (GitLab convention).\n    severity: warn\n    given: $.paths[*][get,post,put,patch,delete].parameters[*]\n    then:\n      field: name\n      function: pattern\n      functionOptions:\n        match: \"^[a-z][a-z0-9_]*$\"\n  request-body-json:\n    description: Request bodies should use application/json.\n    severity: warn\n    given: $.paths[*][post,put,patch].requestBody.content\n    then:\n      field: application/json\n      function: truthy\n  response-success-required:\n    description: Every operation must define a success response.\n    severity: error\n    given: $.paths[*][get,post,put,patch,delete].responses\n    then:\n      function: schema\n      functionOptions:\n        schema:\n          anyOf:\n            - required: [\"200\"]\n            - required: [\"\
  201\"]\n            - required: [\"204\"]\n  response-description-required:\n    description: All responses must have a description.\n    severity: error\n    given: $.paths[*][get,post,put,patch,delete].responses[*]\n    then:\n      field: description\n      function: truthy\n  schema-names-pascalcase:\n    description: Schema names should use PascalCase.\n    severity: warn\n    given: $.components.schemas\n    then:\n      field: \"@key\"\n      function: pattern\n      functionOptions:\n        match: \"^[A-Z][a-zA-Z0-9]*$\"\n  schema-properties-snake-case:\n    description: Schema properties should use snake_case (GitLab convention).\n    severity: info\n    given: $.components.schemas[*].properties\n    then:\n      field: \"@key\"\n      function: pattern\n      functionOptions:\n        match: \"^[a-z][a-z0-9]*(_[a-z0-9]+)*$\"\n  security-schemes-defined:\n    description: Security schemes should be defined.\n    severity: warn\n    given: $.components\n    then:\n      field:\
  \ securitySchemes\n      function: truthy\n  get-no-request-body:\n    description: GET operations must not have a request body.\n    severity: error\n    given: $.paths[*].get\n    then:\n      field: requestBody\n      function: falsy\n  no-empty-descriptions:\n    description: Descriptions must not be empty.\n    severity: error\n    given: \"$..description\"\n    then:\n      function: truthy\n"
source_yaml_url: https://raw.githubusercontent.com/api-evangelist/gitlab/refs/heads/main/rules/gitlab-spectral-rules.yml
tags:
- Code
- Platform
- Software Development
- Source Control
- Spectral
- Linting
- API Governance
---
