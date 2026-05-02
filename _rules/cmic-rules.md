---
api_specs:
- filename: cmic-construction-erp-openapi.yml
  format: yaml
  label: CMiC Construction ERP API
  slug: cmic-api
  spec_type: OpenAPI
  url: https://raw.githubusercontent.com/api-evangelist/cmic/refs/heads/main/openapi/cmic-construction-erp-openapi.yml
categories:
- cmic
description: Spectral linting rules defining API design standards and conventions for CMiC.
layout: rules
name: CMiC API Rules
provider_name: CMiC
provider_slug: cmic
rule_count: 9
rules:
- description: API contact information must be present.
  given: $.info
  name: cmic-info-contact
  severity: error
- description: All server URLs must use HTTPS.
  given: $.servers[*].url
  name: cmic-server-https
  severity: error
- description: Production server should target api.cmic.ca.
  given: $.servers[*].url
  name: cmic-server-host
  severity: warn
- description: An OAuth 2.0 security scheme must be defined.
  given: $.components.securitySchemes[*]
  name: cmic-oauth-security
  severity: error
- description: Every operation must declare a unique operationId.
  given: $.paths[*][get,post,put,patch,delete]
  name: cmic-operation-id
  severity: error
- description: Operations must declare at least one tag.
  given: $.paths[*][get,post,put,patch,delete]
  name: cmic-operation-tags
  severity: warn
- description: List GET operations should accept limit and offset parameters.
  given: $.paths[*].get[?(@.operationId && @.operationId.match(/^list/))]
  name: cmic-list-pagination
  severity: warn
- description: Operations must declare 401 and 403 responses.
  given: $.paths[*][get,post,put,patch,delete].responses
  name: cmic-error-responses
  severity: warn
- description: Server URLs should include the /rest base path.
  given: $.servers[?(@.url && @.url.indexOf('api.cmic.ca') > -1)].url
  name: cmic-rest-base-path
  severity: warn
rules_file: rules/cmic-rules.yml
rules_url: https://raw.githubusercontent.com/api-evangelist/cmic/refs/heads/main/rules/cmic-rules.yml
severity_counts:
  error: 4
  hint: 0
  info: 0
  warn: 5
slug: cmic-rules
source_filename: cmic-rules.yml
source_heading: Spectral Ruleset
source_yaml: "extends:\n  - spectral:oas\n\n# Spectral linting rules for CMiC Construction ERP API.\n# Tuned to api.cmic.ca conventions: HTTPS-only, OAuth 2.0 client credentials,\n# /pm-rest-api/v1 base path, paginated list operations, and tag-grouped\n# resources for projects, jobs, vendors, equipment, and documents.\nrules:\n  cmic-info-contact:\n    description: API contact information must be present.\n    severity: error\n    given: \"$.info\"\n    then:\n      field: contact\n      function: truthy\n\n  cmic-server-https:\n    description: All server URLs must use HTTPS.\n    severity: error\n    given: \"$.servers[*].url\"\n    then:\n      function: pattern\n      functionOptions:\n        match: \"^https://\"\n\n  cmic-server-host:\n    description: Production server should target api.cmic.ca.\n    severity: warn\n    given: \"$.servers[*].url\"\n    then:\n      function: pattern\n      functionOptions:\n        match: \"api\\\\.cmic\\\\.ca\"\n\n  cmic-oauth-security:\n    description:\
  \ An OAuth 2.0 security scheme must be defined.\n    severity: error\n    given: \"$.components.securitySchemes[*]\"\n    then:\n      function: schema\n      functionOptions:\n        schema:\n          type: object\n          properties:\n            type:\n              enum: [\"oauth2\", \"openIdConnect\"]\n\n  cmic-operation-id:\n    description: Every operation must declare a unique operationId.\n    severity: error\n    given: \"$.paths[*][get,post,put,patch,delete]\"\n    then:\n      field: operationId\n      function: truthy\n\n  cmic-operation-tags:\n    description: Operations must declare at least one tag.\n    severity: warn\n    given: \"$.paths[*][get,post,put,patch,delete]\"\n    then:\n      field: tags\n      function: schema\n      functionOptions:\n        schema:\n          type: array\n          minItems: 1\n\n  cmic-list-pagination:\n    description: List GET operations should accept limit and offset parameters.\n    severity: warn\n    given: \"$.paths[*].get[?(@.operationId\
  \ && @.operationId.match(/^list/))]\"\n    then:\n      field: parameters\n      function: schema\n      functionOptions:\n        schema:\n          type: array\n          minItems: 1\n\n  cmic-error-responses:\n    description: Operations must declare 401 and 403 responses.\n    severity: warn\n    given: \"$.paths[*][get,post,put,patch,delete].responses\"\n    then:\n      function: schema\n      functionOptions:\n        schema:\n          type: object\n          required: [\"401\"]\n\n  cmic-rest-base-path:\n    description: Server URLs should include the /rest base path.\n    severity: warn\n    given: \"$.servers[?(@.url && @.url.indexOf('api.cmic.ca') > -1)].url\"\n    then:\n      function: pattern\n      functionOptions:\n        match: \"/rest\"\n"
source_yaml_url: https://raw.githubusercontent.com/api-evangelist/cmic/refs/heads/main/rules/cmic-rules.yml
tags:
- Construction
- ERP
- Finance
- Project Management
- Spectral
- Linting
- API Governance
---
