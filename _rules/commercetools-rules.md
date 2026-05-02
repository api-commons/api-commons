---
api_specs:
- filename: commercetools-http-api-openapi.yml
  format: yaml
  label: Commercetools HTTP API
  slug: http-api
  spec_type: OpenAPI
  url: https://raw.githubusercontent.com/api-evangelist/commercetools/refs/heads/main/openapi/commercetools-http-api-openapi.yml
- filename: commercetools-import-api-openapi.yml
  format: yaml
  label: Commercetools Import API
  slug: import-api
  spec_type: OpenAPI
  url: https://raw.githubusercontent.com/api-evangelist/commercetools/refs/heads/main/openapi/commercetools-import-api-openapi.yml
- filename: commercetools-change-history-api-openapi.yml
  format: yaml
  label: Commercetools Change History API
  slug: change-history-api
  spec_type: OpenAPI
  url: https://raw.githubusercontent.com/api-evangelist/commercetools/refs/heads/main/openapi/commercetools-change-history-api-openapi.yml
categories:
- commercetools
description: Spectral linting rules defining API design standards and conventions for commercetools.
layout: rules
name: commercetools API Rules
provider_name: commercetools
provider_slug: commercetools
rule_count: 9
rules:
- description: API info must include a contact block.
  given: $.info
  name: commercetools-info-contact
  severity: error
- description: Server URLs must use HTTPS.
  given: $.servers[*].url
  name: commercetools-server-https
  severity: error
- description: Public server URL should point to *.commercetools.com.
  given: $.servers[*].url
  name: commercetools-server-host
  severity: warn
- description: Production server URLs should be regional (use {region}).
  given: $.servers[*].url
  name: commercetools-regional-server
  severity: info
- description: APIs must declare OAuth 2.0 security.
  given: $.components.securitySchemes[*]
  name: commercetools-oauth-security
  severity: error
- description: Every operation must declare a unique operationId.
  given: $.paths[*][get,post,put,patch,delete]
  name: commercetools-operation-id
  severity: error
- description: Operations must declare at least one tag.
  given: $.paths[*][get,post,put,patch,delete]
  name: commercetools-operation-tags
  severity: warn
- description: Project-scoped paths must include a {projectKey} parameter.
  given: $.paths[?(@property.indexOf('{projectKey}') > -1)]
  name: commercetools-project-key-path
  severity: warn
- description: Mutating operations should declare 400 and 409 error responses.
  given: $.paths[*][post,put,patch,delete].responses
  name: commercetools-error-responses
  severity: warn
rules_file: rules/commercetools-rules.yml
rules_url: https://raw.githubusercontent.com/api-evangelist/commercetools/refs/heads/main/rules/commercetools-rules.yml
severity_counts:
  error: 4
  hint: 0
  info: 1
  warn: 4
slug: commercetools-rules
source_filename: commercetools-rules.yml
source_heading: Spectral Ruleset
source_yaml: "extends:\n  - spectral:oas\n\n# Spectral linting rules for commercetools Composable Commerce APIs.\n# Tuned to commercetools.com conventions: regional api.{region}.commercetools.com\n# servers, OAuth 2.0 client-credentials authentication, project-key path\n# scoping, and strongly typed JSON resources.\nrules:\n  commercetools-info-contact:\n    description: API info must include a contact block.\n    severity: error\n    given: \"$.info\"\n    then:\n      field: contact\n      function: truthy\n\n  commercetools-server-https:\n    description: Server URLs must use HTTPS.\n    severity: error\n    given: \"$.servers[*].url\"\n    then:\n      function: pattern\n      functionOptions:\n        match: \"^https://\"\n\n  commercetools-server-host:\n    description: Public server URL should point to *.commercetools.com.\n    severity: warn\n    given: \"$.servers[*].url\"\n    then:\n      function: pattern\n      functionOptions:\n        match: \"commercetools.com\"\n\n  commercetools-regional-server:\n\
  \    description: Production server URLs should be regional (use {region}).\n    severity: info\n    given: \"$.servers[*].url\"\n    then:\n      function: pattern\n      functionOptions:\n        match: \"{region}\"\n\n  commercetools-oauth-security:\n    description: APIs must declare OAuth 2.0 security.\n    severity: error\n    given: \"$.components.securitySchemes[*]\"\n    then:\n      function: schema\n      functionOptions:\n        schema:\n          type: object\n          properties:\n            type:\n              enum: [\"oauth2\", \"http\"]\n\n  commercetools-operation-id:\n    description: Every operation must declare a unique operationId.\n    severity: error\n    given: \"$.paths[*][get,post,put,patch,delete]\"\n    then:\n      field: operationId\n      function: truthy\n\n  commercetools-operation-tags:\n    description: Operations must declare at least one tag.\n    severity: warn\n    given: \"$.paths[*][get,post,put,patch,delete]\"\n    then:\n      field: tags\n\
  \      function: schema\n      functionOptions:\n        schema:\n          type: array\n          minItems: 1\n\n  commercetools-project-key-path:\n    description: Project-scoped paths must include a {projectKey} parameter.\n    severity: warn\n    given: \"$.paths[?(@property.indexOf('{projectKey}') > -1)]\"\n    then:\n      function: truthy\n\n  commercetools-error-responses:\n    description: Mutating operations should declare 400 and 409 error responses.\n    severity: warn\n    given: \"$.paths[*][post,put,patch,delete].responses\"\n    then:\n      function: schema\n      functionOptions:\n        schema:\n          type: object\n          anyOf:\n            - required: [\"400\"]\n            - required: [\"401\"]\n            - required: [\"404\"]\n            - required: [\"409\"]\n"
source_yaml_url: https://raw.githubusercontent.com/api-evangelist/commercetools/refs/heads/main/rules/commercetools-rules.yml
tags:
- Commerce
- Composable Commerce
- E-Commerce
- GraphQL
- REST
- SDK
- Spectral
- Linting
- API Governance
---
