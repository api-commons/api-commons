---
api_specs:
- filename: bitbucket-cloud-rest-api-openapi.json
  format: json
  label: Bitbucket Cloud REST API
  slug: bitbucket-cloud-rest-api
  spec_type: OpenAPI
  url: https://raw.githubusercontent.com/api-evangelist/bitbucket/refs/heads/main/openapi/bitbucket-cloud-rest-api-openapi.json
categories:
- delete
- get
- info
- operation
- pagination
- parameter
- paths
- response
- schema
- security
- tag
description: Spectral linting rules defining API design standards and conventions for Bitbucket.
layout: rules
name: Bitbucket API Rules
provider_name: Bitbucket
provider_slug: bitbucket
rule_count: 19
rules:
- description: Info object must have a title
  given: $.info
  name: info-title-required
  severity: error
- description: Info object must have a description
  given: $.info
  name: info-description-required
  severity: error
- description: Info object must have a version
  given: $.info
  name: info-version-required
  severity: error
- description: Path segments should use kebab-case
  given: $.paths
  name: paths-kebab-case
  severity: warn
- description: Paths must not have trailing slashes
  given: $.paths
  name: paths-no-trailing-slash
  severity: error
- description: Operations must have a summary
  given: $.paths[*][get,post,put,patch,delete]
  name: operation-summary-required
  severity: error
- description: Operations must have a description
  given: $.paths[*][get,post,put,patch,delete]
  name: operation-description-required
  severity: warn
- description: Operations must have an operationId
  given: $.paths[*][get,post,put,patch,delete]
  name: operation-operationid-required
  severity: error
- description: Operations must have at least one tag
  given: $.paths[*][get,post,put,patch,delete]
  name: operation-tags-required
  severity: warn
- description: Operation summaries should start with Bitbucket
  given: $.paths[*][get,post,put,patch,delete].summary
  name: operation-summary-prefix
  severity: info
- description: Parameters must have descriptions
  given: $.paths[*][get,post,put,patch,delete].parameters[*]
  name: parameter-description-required
  severity: warn
- description: Operations must define a success response
  given: $.paths[*][get,post,put,patch,delete].responses
  name: response-success-required
  severity: error
- description: Schemas should have a type defined
  given: $.definitions[*]
  name: schema-type-required
  severity: warn
- description: Schema properties should use snake_case
  given: $.definitions[*].properties
  name: schema-property-snake-case
  severity: warn
- description: Global security should be defined
  given: $
  name: security-global-defined
  severity: warn
- description: GET operations must not have a request body
  given: $.paths[*].get
  name: get-no-request-body
  severity: error
- description: DELETE operations should not have a request body
  given: $.paths[*].delete
  name: delete-no-request-body
  severity: warn
- description: Paginated endpoints should use page-based pagination
  given: $.paths[*].get.parameters[?(@.name=='page')]
  name: pagination-use-page
  severity: info
- description: Tag names should use Title Case
  given: $.tags[*].name
  name: tag-title-case
  severity: warn
rules_file: rules/bitbucket-spectral-rules.yml
rules_url: https://raw.githubusercontent.com/api-evangelist/bitbucket/refs/heads/main/rules/bitbucket-spectral-rules.yml
severity_counts:
  error: 8
  hint: 0
  info: 2
  warn: 9
slug: bitbucket-spectral-rules
source_filename: bitbucket-spectral-rules.yml
source_heading: Spectral Ruleset
source_yaml: "rules:\n  # INFO / METADATA\n  info-title-required:\n    description: Info object must have a title\n    given: $.info\n    severity: error\n    then:\n      field: title\n      function: truthy\n\n  info-description-required:\n    description: Info object must have a description\n    given: $.info\n    severity: error\n    then:\n      field: description\n      function: truthy\n\n  info-version-required:\n    description: Info object must have a version\n    given: $.info\n    severity: error\n    then:\n      field: version\n      function: truthy\n\n  # PATHS\n  paths-kebab-case:\n    description: Path segments should use kebab-case\n    given: $.paths\n    severity: warn\n    then:\n      field: \"@key\"\n      function: pattern\n      functionOptions:\n        match: \"^(/[a-z0-9_-]+(/{[a-zA-Z_]+})?)*$\"\n\n  paths-no-trailing-slash:\n    description: Paths must not have trailing slashes\n    given: $.paths\n    severity: error\n    then:\n      field: \"@key\"\n    \
  \  function: pattern\n      functionOptions:\n        notMatch: \"/$\"\n\n  # OPERATIONS\n  operation-summary-required:\n    description: Operations must have a summary\n    given: $.paths[*][get,post,put,patch,delete]\n    severity: error\n    then:\n      field: summary\n      function: truthy\n\n  operation-description-required:\n    description: Operations must have a description\n    given: $.paths[*][get,post,put,patch,delete]\n    severity: warn\n    then:\n      field: description\n      function: truthy\n\n  operation-operationid-required:\n    description: Operations must have an operationId\n    given: $.paths[*][get,post,put,patch,delete]\n    severity: error\n    then:\n      field: operationId\n      function: truthy\n\n  operation-tags-required:\n    description: Operations must have at least one tag\n    given: $.paths[*][get,post,put,patch,delete]\n    severity: warn\n    then:\n      field: tags\n      function: truthy\n\n  operation-summary-prefix:\n    description:\
  \ Operation summaries should start with Bitbucket\n    given: $.paths[*][get,post,put,patch,delete].summary\n    severity: info\n    then:\n      function: pattern\n      functionOptions:\n        match: \"^Bitbucket \"\n\n  # PARAMETERS\n  parameter-description-required:\n    description: Parameters must have descriptions\n    given: $.paths[*][get,post,put,patch,delete].parameters[*]\n    severity: warn\n    then:\n      field: description\n      function: truthy\n\n  # RESPONSES\n  response-success-required:\n    description: Operations must define a success response\n    given: $.paths[*][get,post,put,patch,delete].responses\n    severity: error\n    then:\n      function: schema\n      functionOptions:\n        schema:\n          anyOf:\n            - required: [\"200\"]\n            - required: [\"201\"]\n            - required: [\"204\"]\n\n  # SCHEMAS\n  schema-type-required:\n    description: Schemas should have a type defined\n    given: $.definitions[*]\n    severity: warn\n\
  \    then:\n      field: type\n      function: truthy\n\n  # PROPERTY NAMING\n  schema-property-snake-case:\n    description: Schema properties should use snake_case\n    given: $.definitions[*].properties\n    severity: warn\n    then:\n      field: \"@key\"\n      function: pattern\n      functionOptions:\n        match: \"^[a-z][a-z0-9_]*$\"\n\n  # SECURITY\n  security-global-defined:\n    description: Global security should be defined\n    given: $\n    severity: warn\n    then:\n      field: security\n      function: truthy\n\n  # HTTP METHOD CONVENTIONS\n  get-no-request-body:\n    description: GET operations must not have a request body\n    given: $.paths[*].get\n    severity: error\n    then:\n      field: requestBody\n      function: falsy\n\n  delete-no-request-body:\n    description: DELETE operations should not have a request body\n    given: $.paths[*].delete\n    severity: warn\n    then:\n      field: requestBody\n      function: falsy\n\n  # PAGINATION\n  pagination-use-page:\n\
  \    description: Paginated endpoints should use page-based pagination\n    given: $.paths[*].get.parameters[?(@.name=='page')]\n    severity: info\n    then:\n      field: name\n      function: truthy\n\n  # TAGS\n  tag-title-case:\n    description: Tag names should use Title Case\n    given: $.tags[*].name\n    severity: warn\n    then:\n      function: pattern\n      functionOptions:\n        match: \"^[A-Z]\"\n"
source_yaml_url: https://raw.githubusercontent.com/api-evangelist/bitbucket/refs/heads/main/rules/bitbucket-spectral-rules.yml
tags:
- Atlassian
- CI/CD
- Code Collaboration
- Code Review
- DevOps
- Git
- Pull Requests
- Repository Hosting
- Version Control
- Spectral
- Linting
- API Governance
---
