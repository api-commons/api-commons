---
categories:
- async
- get
- global
- info
- list
- oauth2
- openapi
- operation
- parameter
- paths
- response
- security
- servers
- tags
description: Spectral linting rules defining API design standards and conventions for Allianz Technology Standards.
layout: rules
name: Allianz Technology Standards API Rules
provider_name: Allianz Technology Standards
provider_slug: allianz-technology-standards
rule_count: 22
rules:
- description: API title must start with "Allianz"
  given: $.info.title
  name: info-title-allianz-prefix
  severity: warn
- description: API info must have a description
  given: $.info
  name: info-description-required
  severity: error
- description: API info must define a version
  given: $.info
  name: info-version-required
  severity: error
- description: Specs must use OpenAPI 3.x (API-first standard)
  given: $.openapi
  name: openapi-version-3
  severity: error
- description: At least one server must be defined
  given: $
  name: servers-defined
  severity: error
- description: Server URLs must use HTTPS (Allianz security standard)
  given: $.servers[*].url
  name: servers-https
  severity: error
- description: Paths must not have trailing slashes
  given: $.paths
  name: paths-no-trailing-slash
  severity: error
- description: Every operation must have a summary
  given: $.paths[*][get,post,put,patch,delete]
  name: operation-summary-required
  severity: error
- description: Every operation must have a description
  given: $.paths[*][get,post,put,patch,delete]
  name: operation-description-required
  severity: error
- description: Every operation must have an operationId
  given: $.paths[*][get,post,put,patch,delete]
  name: operation-id-required
  severity: error
- description: Every operation must have at least one tag
  given: $.paths[*][get,post,put,patch,delete]
  name: operation-tags-required
  severity: error
- description: List operations should support pageSize query parameter (Allianz pagination standard)
  given: $.paths[*].get.parameters[*].name
  name: list-operations-page-size
  severity: warn
- description: List operations should support page query parameter (Allianz pagination standard)
  given: $.paths[*].get.parameters[*].name
  name: list-operations-page-param
  severity: warn
- description: Async POST operations should return 202 Accepted (Allianz async pattern)
  given: $.paths[*].post.responses
  name: async-post-returns-202
  severity: info
- description: Security schemes must be defined (OAuth2 standard)
  given: $.components
  name: security-schemes-defined
  severity: error
- description: OAuth2 security scheme should be defined (Allianz OAuth2 standard)
  given: $.components.securitySchemes
  name: oauth2-scheme-required
  severity: warn
- description: Global security should be defined
  given: $
  name: global-security-defined
  severity: warn
- description: GET operations must not have request bodies
  given: $.paths[*].get
  name: get-no-request-body
  severity: error
- description: All responses must have descriptions
  given: $.paths[*][get,post,put,patch,delete].responses[*]
  name: response-description-required
  severity: error
- description: Operations should define a 401 response
  given: $.paths[*][get,post,put,patch,delete].responses
  name: response-401-required
  severity: warn
- description: Global tags array should be defined
  given: $
  name: tags-defined
  severity: warn
- description: All parameters must have descriptions
  given: $.paths[*][get,post,put,patch,delete].parameters[*]
  name: parameter-description-required
  severity: error
rules_file: rules/allianz-technology-standards-spectral-rules.yml
rules_url: https://raw.githubusercontent.com/api-evangelist/allianz-technology-standards/refs/heads/main/rules/allianz-technology-standards-spectral-rules.yml
severity_counts:
  error: 14
  hint: 0
  info: 1
  warn: 7
slug: allianz-technology-standards-spectral-rules
source_filename: allianz-technology-standards-spectral-rules.yml
source_heading: Spectral Ruleset
source_yaml: "# Allianz Technology Standards Spectral Rules\n# Enforces Allianz API design conventions based on the technology standards documentation\n\nrules:\n\n  info-title-allianz-prefix:\n    description: API title must start with \"Allianz\"\n    severity: warn\n    given: \"$.info.title\"\n    then:\n      function: pattern\n      functionOptions:\n        match: \"^Allianz\"\n\n  info-description-required:\n    description: API info must have a description\n    severity: error\n    given: \"$.info\"\n    then:\n      field: description\n      function: truthy\n\n  info-version-required:\n    description: API info must define a version\n    severity: error\n    given: \"$.info\"\n    then:\n      field: version\n      function: truthy\n\n  openapi-version-3:\n    description: Specs must use OpenAPI 3.x (API-first standard)\n    severity: error\n    given: \"$.openapi\"\n    then:\n      function: pattern\n      functionOptions:\n        match: \"^3\\\\.\"\n\n  servers-defined:\n\
  \    description: At least one server must be defined\n    severity: error\n    given: \"$\"\n    then:\n      field: servers\n      function: truthy\n\n  servers-https:\n    description: Server URLs must use HTTPS (Allianz security standard)\n    severity: error\n    given: \"$.servers[*].url\"\n    then:\n      function: pattern\n      functionOptions:\n        match: \"^https://\"\n\n  paths-no-trailing-slash:\n    description: Paths must not have trailing slashes\n    severity: error\n    given: \"$.paths\"\n    then:\n      function: pattern\n      functionOptions:\n        notMatch: \"\\\\/$\"\n\n  operation-summary-required:\n    description: Every operation must have a summary\n    severity: error\n    given: \"$.paths[*][get,post,put,patch,delete]\"\n    then:\n      field: summary\n      function: truthy\n\n  operation-description-required:\n    description: Every operation must have a description\n    severity: error\n    given: \"$.paths[*][get,post,put,patch,delete]\"\n  \
  \  then:\n      field: description\n      function: truthy\n\n  operation-id-required:\n    description: Every operation must have an operationId\n    severity: error\n    given: \"$.paths[*][get,post,put,patch,delete]\"\n    then:\n      field: operationId\n      function: truthy\n\n  operation-tags-required:\n    description: Every operation must have at least one tag\n    severity: error\n    given: \"$.paths[*][get,post,put,patch,delete]\"\n    then:\n      field: tags\n      function: truthy\n\n  # ALLIANZ PAGINATION STANDARD\n  list-operations-page-size:\n    description: List operations should support pageSize query parameter (Allianz pagination standard)\n    severity: warn\n    given: \"$.paths[*].get.parameters[*].name\"\n    then:\n      function: pattern\n      functionOptions:\n        match: \"^(pageSize|page_size|limit)$\"\n\n  list-operations-page-param:\n    description: List operations should support page query parameter (Allianz pagination standard)\n    severity: warn\n\
  \    given: \"$.paths[*].get.parameters[*].name\"\n    then:\n      function: pattern\n      functionOptions:\n        match: \"^(page|offset)$\"\n\n  # ALLIANZ ASYNC PATTERN\n  async-post-returns-202:\n    description: Async POST operations should return 202 Accepted (Allianz async pattern)\n    severity: info\n    given: \"$.paths[*].post.responses\"\n    then:\n      function: schema\n      functionOptions:\n        schema:\n          type: object\n\n  # SECURITY\n  security-schemes-defined:\n    description: Security schemes must be defined (OAuth2 standard)\n    severity: error\n    given: \"$.components\"\n    then:\n      field: securitySchemes\n      function: truthy\n\n  oauth2-scheme-required:\n    description: OAuth2 security scheme should be defined (Allianz OAuth2 standard)\n    severity: warn\n    given: \"$.components.securitySchemes\"\n    then:\n      function: schema\n      functionOptions:\n        schema:\n          type: object\n          required:\n            - OAuth2\n\
  \n  global-security-defined:\n    description: Global security should be defined\n    severity: warn\n    given: \"$\"\n    then:\n      field: security\n      function: truthy\n\n  # HTTP METHOD CONVENTIONS\n  get-no-request-body:\n    description: GET operations must not have request bodies\n    severity: error\n    given: \"$.paths[*].get\"\n    then:\n      field: requestBody\n      function: falsy\n\n  # RESPONSE STANDARDS\n  response-description-required:\n    description: All responses must have descriptions\n    severity: error\n    given: \"$.paths[*][get,post,put,patch,delete].responses[*]\"\n    then:\n      field: description\n      function: truthy\n\n  response-401-required:\n    description: Operations should define a 401 response\n    severity: warn\n    given: \"$.paths[*][get,post,put,patch,delete].responses\"\n    then:\n      function: schema\n      functionOptions:\n        schema:\n          type: object\n          required:\n            - \"401\"\n\n  # TAGS\n  tags-defined:\n\
  \    description: Global tags array should be defined\n    severity: warn\n    given: \"$\"\n    then:\n      field: tags\n      function: truthy\n\n  # PARAMETER STANDARDS\n  parameter-description-required:\n    description: All parameters must have descriptions\n    severity: error\n    given: \"$.paths[*][get,post,put,patch,delete].parameters[*]\"\n    then:\n      field: description\n      function: truthy\n"
source_yaml_url: https://raw.githubusercontent.com/api-evangelist/allianz-technology-standards/refs/heads/main/rules/allianz-technology-standards-spectral-rules.yml
tags:
- Best Practices
- Enterprise Architecture
- Guidelines
- Software Development
- Technology Standards
- API Design
- OpenAPI
- Spectral
- Linting
- API Governance
---
