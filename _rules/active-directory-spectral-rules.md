---
api_specs:
- filename: active-directory-users-openapi.yaml
  format: yaml
  label: Microsoft Graph Users API
  slug: ''
  spec_type: OpenAPI
  url: https://raw.githubusercontent.com/api-evangelist/active-directory/refs/heads/main/openapi/active-directory-users-openapi.yaml
- filename: active-directory-groups-openapi.yaml
  format: yaml
  label: Microsoft Graph Groups API
  slug: ''
  spec_type: OpenAPI
  url: https://raw.githubusercontent.com/api-evangelist/active-directory/refs/heads/main/openapi/active-directory-groups-openapi.yaml
- filename: active-directory-applications-openapi.yaml
  format: yaml
  label: Microsoft Graph Applications and Service Principals API
  slug: ''
  spec_type: OpenAPI
  url: https://raw.githubusercontent.com/api-evangelist/active-directory/refs/heads/main/openapi/active-directory-applications-openapi.yaml
categories:
- ad
description: Spectral linting rules defining API design standards and conventions for Microsoft Active Directory.
layout: rules
name: Microsoft Active Directory API Rules
provider_name: Microsoft Active Directory
provider_slug: active-directory
rule_count: 33
rules:
- description: Microsoft Graph APIs must use graph.microsoft.com as the server URL
  given: $.servers[*].url
  name: ad-graph-server-url
  severity: error
- description: All Microsoft Graph servers must use HTTPS
  given: $.servers[*].url
  name: ad-https-only
  severity: error
- description: Every operation must have a non-empty summary
  given: $.paths[*][get,post,patch,put,delete]
  name: ad-operation-summary-required
  severity: error
- description: Operation summaries must use Title Case (each word capitalized)
  given: $.paths[*][get,post,patch,put,delete].summary
  name: ad-operation-summary-title-case
  severity: warn
- description: Operation summaries must be prefixed with 'Active Directory'
  given: $.paths[*][get,post,patch,put,delete].summary
  name: ad-operation-summary-prefix
  severity: warn
- description: Every operation should have a detailed description
  given: $.paths[*][get,post,patch,put,delete]
  name: ad-operation-description-required
  severity: warn
- description: Every operation must have an operationId
  given: $.paths[*][get,post,patch,put,delete]
  name: ad-operation-id-required
  severity: error
- description: Operation IDs must use kebab-case
  given: $.paths[*][get,post,patch,put,delete].operationId
  name: ad-operation-id-kebab-case
  severity: warn
- description: Every operation must have at least one tag
  given: $.paths[*][get,post,patch,put,delete]
  name: ad-operation-tags-required
  severity: warn
- description: All tags used in operations must be declared in the global tags list
  given: $.paths[*][get,post,patch,put,delete].tags[*]
  name: ad-tags-defined
  severity: warn
- description: APIs must declare an OAuth2 security scheme
  given: $.components.securitySchemes
  name: ad-oauth2-security-scheme
  severity: error
- description: Every operation must declare security requirements
  given: $.paths[*][get,post,patch,put,delete]
  name: ad-security-required
  severity: error
- description: GET operations must return a 200 response
  given: $.paths[*].get
  name: ad-get-200-response
  severity: error
- description: POST operations creating resources should return 201
  given: $.paths[*].post
  name: ad-post-201-response
  severity: warn
- description: DELETE operations must return 204 No Content
  given: $.paths[*].delete
  name: ad-delete-204-response
  severity: error
- description: PATCH operations must return 204 No Content
  given: $.paths[*].patch
  name: ad-patch-204-response
  severity: warn
- description: All operations must define a 401 Unauthorized response
  given: $.paths[*][get,post,patch,put,delete]
  name: ad-401-response
  severity: warn
- description: List operations should support $filter OData parameter
  given: $.paths[?(!@property.match(/{[^}]+}$/))].get
  name: ad-list-filter-param
  severity: warn
- description: List operations should support $top pagination parameter
  given: $.paths[*].get.parameters[*]
  name: ad-list-top-param
  severity: info
- description: POST operations must define a request body
  given: $.paths[*].post
  name: ad-post-request-body
  severity: error
- description: PATCH operations must define a request body
  given: $.paths[*].patch
  name: ad-patch-request-body
  severity: error
- description: Request bodies must use application/json content type
  given: $.paths[*][post,patch,put].requestBody.content
  name: ad-request-body-json
  severity: error
- description: ID properties should be documented as UUID format
  given: $.components.schemas[*].properties.id
  name: ad-schema-id-uuid
  severity: warn
- description: All schemas must have descriptions
  given: $.components.schemas[*]
  name: ad-schemas-have-descriptions
  severity: warn
- description: Schema properties should have descriptions
  given: $.components.schemas[*].properties[*]
  name: ad-properties-have-descriptions
  severity: info
- description: API paths must use lowercase letters
  given: $.paths[*]~
  name: ad-path-lowercase
  severity: error
- description: API paths must not end with a trailing slash
  given: $.paths[*]~
  name: ad-path-no-trailing-slash
  severity: error
- description: Path parameters for resource IDs should use descriptive names ending in 'Id'
  given: $.paths[*][get,patch,delete].parameters[?(@.in=='path')].name
  name: ad-path-id-parameter
  severity: warn
- description: API info must include a contact object
  given: $.info
  name: ad-info-contact
  severity: warn
- description: API info must include license information
  given: $.info
  name: ad-info-license
  severity: warn
- description: API info should include terms of service URL
  given: $.info
  name: ad-info-terms-of-service
  severity: info
- description: Successful responses must include application/json content type
  given: $.paths[*][get,post].responses[200,201].content
  name: ad-response-json-content
  severity: error
- description: Operations should include x-microcks-operation for mock generation
  given: $.paths[*][get,post,patch,put,delete]
  name: ad-microcks-operation
  severity: info
rules_file: rules/active-directory-spectral-rules.yml
rules_url: https://raw.githubusercontent.com/api-evangelist/active-directory/refs/heads/main/rules/active-directory-spectral-rules.yml
severity_counts:
  error: 14
  hint: 0
  info: 4
  warn: 15
slug: active-directory-spectral-rules
source_filename: active-directory-spectral-rules.yml
source_heading: Spectral Ruleset
source_yaml: "extends: spectral:oas\n\nrules:\n\n  # ── Microsoft Graph Server Validation ────────────────────────────────────────\n\n  ad-graph-server-url:\n    description: Microsoft Graph APIs must use graph.microsoft.com as the server URL\n    message: \"Server URL must be graph.microsoft.com/v1.0 or graph.microsoft.com/beta\"\n    severity: error\n    given: \"$.servers[*].url\"\n    then:\n      function: pattern\n      functionOptions:\n        match: \"^https://graph\\\\.microsoft\\\\.com/(v1\\\\.0|beta)$\"\n\n  ad-https-only:\n    description: All Microsoft Graph servers must use HTTPS\n    message: \"Server URL must use HTTPS\"\n    severity: error\n    given: \"$.servers[*].url\"\n    then:\n      function: pattern\n      functionOptions:\n        match: \"^https://\"\n\n  # ── Operation Summary and Description ────────────────────────────────────────\n\n  ad-operation-summary-required:\n    description: Every operation must have a non-empty summary\n    message: \"Operation '{{path}}'\
  \ must have a summary\"\n    severity: error\n    given: \"$.paths[*][get,post,patch,put,delete]\"\n    then:\n      field: summary\n      function: truthy\n\n  ad-operation-summary-title-case:\n    description: Operation summaries must use Title Case (each word capitalized)\n    message: \"Operation summary '{{value}}' must use Title Case\"\n    severity: warn\n    given: \"$.paths[*][get,post,patch,put,delete].summary\"\n    then:\n      function: pattern\n      functionOptions:\n        match: \"^[A-Z][a-zA-Z0-9]*([ ][A-Z][a-zA-Z0-9]*)*$\"\n\n  ad-operation-summary-prefix:\n    description: Operation summaries must be prefixed with 'Active Directory'\n    message: \"Operation summary must start with 'Active Directory'\"\n    severity: warn\n    given: \"$.paths[*][get,post,patch,put,delete].summary\"\n    then:\n      function: pattern\n      functionOptions:\n        match: \"^Active Directory \"\n\n  ad-operation-description-required:\n    description: Every operation should have\
  \ a detailed description\n    message: \"Operation '{{path}}' should have a description\"\n    severity: warn\n    given: \"$.paths[*][get,post,patch,put,delete]\"\n    then:\n      field: description\n      function: truthy\n\n  ad-operation-id-required:\n    description: Every operation must have an operationId\n    message: \"Operation '{{path}}' must have an operationId\"\n    severity: error\n    given: \"$.paths[*][get,post,patch,put,delete]\"\n    then:\n      field: operationId\n      function: truthy\n\n  ad-operation-id-kebab-case:\n    description: Operation IDs must use kebab-case\n    message: \"operationId '{{value}}' must use kebab-case\"\n    severity: warn\n    given: \"$.paths[*][get,post,patch,put,delete].operationId\"\n    then:\n      function: pattern\n      functionOptions:\n        match: \"^[a-z][a-z0-9]*(-[a-z0-9]+)*$\"\n\n  # ── Tags ─────────────────────────────────────────────────────────────────────\n\n  ad-operation-tags-required:\n    description: Every\
  \ operation must have at least one tag\n    message: \"Operation '{{path}}' must define at least one tag\"\n    severity: warn\n    given: \"$.paths[*][get,post,patch,put,delete]\"\n    then:\n      field: tags\n      function: truthy\n\n  ad-tags-defined:\n    description: All tags used in operations must be declared in the global tags list\n    message: \"Tag '{{value}}' must be declared in the global tags array\"\n    severity: warn\n    given: \"$.paths[*][get,post,patch,put,delete].tags[*]\"\n    then:\n      function: enumeration\n      functionOptions:\n        values:\n          - Users\n          - Groups\n          - Members\n          - Owners\n          - Applications\n          - Service Principals\n          - App Role Assignments\n          - Devices\n          - Directory Roles\n          - Conditional Access\n          - Identity Governance\n          - Identity Protection\n          - Authentication Methods\n          - Reports\n\n  # ── Authentication ────────────────────────────────────────────────────────────\n\
  \n  ad-oauth2-security-scheme:\n    description: APIs must declare an OAuth2 security scheme\n    message: \"Security schemes must include an OAuth2 definition\"\n    severity: error\n    given: \"$.components.securitySchemes\"\n    then:\n      function: schema\n      functionOptions:\n        schema:\n          type: object\n          required: [oauth2]\n\n  ad-security-required:\n    description: Every operation must declare security requirements\n    message: \"Operation '{{path}}' must declare OAuth2 security requirements\"\n    severity: error\n    given: \"$.paths[*][get,post,patch,put,delete]\"\n    then:\n      field: security\n      function: truthy\n\n  # ── Responses ────────────────────────────────────────────────────────────────\n\n  ad-get-200-response:\n    description: GET operations must return a 200 response\n    message: \"GET operation '{{path}}' must define a 200 response\"\n    severity: error\n    given: \"$.paths[*].get\"\n    then:\n      field: responses.200\n\
  \      function: truthy\n\n  ad-post-201-response:\n    description: POST operations creating resources should return 201\n    message: \"POST operation '{{path}}' should define a 201 response\"\n    severity: warn\n    given: \"$.paths[*].post\"\n    then:\n      field: responses.201\n      function: truthy\n\n  ad-delete-204-response:\n    description: DELETE operations must return 204 No Content\n    message: \"DELETE operation '{{path}}' must return 204\"\n    severity: error\n    given: \"$.paths[*].delete\"\n    then:\n      field: responses.204\n      function: truthy\n\n  ad-patch-204-response:\n    description: PATCH operations must return 204 No Content\n    message: \"PATCH operation '{{path}}' must return 204\"\n    severity: warn\n    given: \"$.paths[*].patch\"\n    then:\n      field: responses.204\n      function: truthy\n\n  ad-401-response:\n    description: All operations must define a 401 Unauthorized response\n    message: \"Operation '{{path}}' must define a 401 response\"\
  \n    severity: warn\n    given: \"$.paths[*][get,post,patch,put,delete]\"\n    then:\n      field: responses.401\n      function: truthy\n\n  # ── OData Parameters ─────────────────────────────────────────────────────────\n\n  ad-list-filter-param:\n    description: List operations should support $filter OData parameter\n    message: \"GET collection operation '{{path}}' should have a $filter query parameter\"\n    severity: warn\n    given: \"$.paths[?(!@property.match(/{[^}]+}$/))].get\"\n    then:\n      function: schema\n      functionOptions:\n        schema:\n          type: object\n          required: [parameters]\n\n  ad-list-top-param:\n    description: List operations should support $top pagination parameter\n    message: \"GET collection operation should support $top pagination\"\n    severity: info\n    given: \"$.paths[*].get.parameters[*]\"\n    then:\n      field: name\n      function: pattern\n      functionOptions:\n        match: \"^\\\\$top$|^\\\\$filter$|^\\\\$select$|^userId$|^groupId$|^applicationId$|^servicePrincipalId$|^memberId$\"\
  \n\n  # ── Request Body ─────────────────────────────────────────────────────────────\n\n  ad-post-request-body:\n    description: POST operations must define a request body\n    message: \"POST operation '{{path}}' must define a request body\"\n    severity: error\n    given: \"$.paths[*].post\"\n    then:\n      field: requestBody\n      function: truthy\n\n  ad-patch-request-body:\n    description: PATCH operations must define a request body\n    message: \"PATCH operation '{{path}}' must define a request body\"\n    severity: error\n    given: \"$.paths[*].patch\"\n    then:\n      field: requestBody\n      function: truthy\n\n  ad-request-body-json:\n    description: Request bodies must use application/json content type\n    message: \"Request body must use application/json media type\"\n    severity: error\n    given: \"$.paths[*][post,patch,put].requestBody.content\"\n    then:\n      field: \"application/json\"\n      function: truthy\n\n  # ── Schema Design ─────────────────────────────────────────────────────────────\n\
  \n  ad-schema-id-uuid:\n    description: ID properties should be documented as UUID format\n    message: \"Property 'id' should have format: uuid\"\n    severity: warn\n    given: \"$.components.schemas[*].properties.id\"\n    then:\n      field: format\n      function: truthy\n\n  ad-schemas-have-descriptions:\n    description: All schemas must have descriptions\n    message: \"Schema '{{path}}' must have a description\"\n    severity: warn\n    given: \"$.components.schemas[*]\"\n    then:\n      field: description\n      function: truthy\n\n  ad-properties-have-descriptions:\n    description: Schema properties should have descriptions\n    message: \"Property '{{path}}' should have a description\"\n    severity: info\n    given: \"$.components.schemas[*].properties[*]\"\n    then:\n      field: description\n      function: truthy\n\n  # ── Path Conventions ──────────────────────────────────────────────────────────\n\n  ad-path-lowercase:\n    description: API paths must use lowercase\
  \ letters\n    message: \"Path '{{path}}' must use lowercase letters\"\n    severity: error\n    given: \"$.paths[*]~\"\n    then:\n      function: pattern\n      functionOptions:\n        match: \"^(/[a-z][a-zA-Z0-9${}/_-]*)+$\"\n\n  ad-path-no-trailing-slash:\n    description: API paths must not end with a trailing slash\n    message: \"Path '{{path}}' must not end with a trailing slash\"\n    severity: error\n    given: \"$.paths[*]~\"\n    then:\n      function: pattern\n      functionOptions:\n        notMatch: \"/$\"\n\n  ad-path-id-parameter:\n    description: Path parameters for resource IDs should use descriptive names ending in 'Id'\n    message: \"Path parameter '{{value}}' should end in 'Id' (e.g. userId, groupId)\"\n    severity: warn\n    given: \"$.paths[*][get,patch,delete].parameters[?(@.in=='path')].name\"\n    then:\n      function: pattern\n      functionOptions:\n        match: \"(Id|id)$\"\n\n  # ── Info ──────────────────────────────────────────────────────────────────────\n\
  \n  ad-info-contact:\n    description: API info must include a contact object\n    message: \"API info must include a contact object\"\n    severity: warn\n    given: \"$.info\"\n    then:\n      field: contact\n      function: truthy\n\n  ad-info-license:\n    description: API info must include license information\n    message: \"API info must include a license object\"\n    severity: warn\n    given: \"$.info\"\n    then:\n      field: license\n      function: truthy\n\n  ad-info-terms-of-service:\n    description: API info should include terms of service URL\n    message: \"API info should include a termsOfService URL\"\n    severity: info\n    given: \"$.info\"\n    then:\n      field: termsOfService\n      function: truthy\n\n  # ── Content Type ──────────────────────────────────────────────────────────────\n\n  ad-response-json-content:\n    description: Successful responses must include application/json content type\n    message: \"Response '{{path}}' must include application/json\
  \ content\"\n    severity: error\n    given: \"$.paths[*][get,post].responses[200,201].content\"\n    then:\n      field: \"application/json\"\n      function: truthy\n\n  # ── Microcks Examples ─────────────────────────────────────────────────────────\n\n  ad-microcks-operation:\n    description: Operations should include x-microcks-operation for mock generation\n    message: \"Operation '{{path}}' should include x-microcks-operation extension\"\n    severity: info\n    given: \"$.paths[*][get,post,patch,put,delete]\"\n    then:\n      field: x-microcks-operation\n      function: truthy\n"
source_yaml_url: https://raw.githubusercontent.com/api-evangelist/active-directory/refs/heads/main/rules/active-directory-spectral-rules.yml
tags:
- Active Directory
- Authentication
- Authorization
- Directory Services
- Identity Management
- Microsoft Entra
- Zero Trust
- Spectral
- Linting
- API Governance
---
