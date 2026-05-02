---
api_specs:
- filename: ruckus-one-api-openapi.yml
  format: yaml
  label: RUCKUS One API
  slug: ruckus-one-api
  spec_type: OpenAPI
  url: https://raw.githubusercontent.com/api-evangelist/commscope-holding/refs/heads/main/openapi/ruckus-one-api-openapi.yml
categories:
- ruckus
description: Spectral linting rules defining API design standards and conventions for CommScope Holding.
layout: rules
name: CommScope Holding API Rules
provider_name: CommScope Holding
provider_slug: commscope-holding
rule_count: 9
rules:
- description: API info must include a contact block.
  given: $.info
  name: ruckus-info-contact
  severity: error
- description: Server URLs must use HTTPS.
  given: $.servers[*].url
  name: ruckus-server-https
  severity: error
- description: Servers should be on the api.*.ruckus.cloud domain.
  given: $.servers[*].url
  name: ruckus-server-host
  severity: warn
- description: API definition should declare multiple regional servers.
  given: $.servers
  name: ruckus-multi-region
  severity: info
- description: Every operation must declare a unique operationId.
  given: $.paths[*][get,post,put,patch,delete]
  name: ruckus-operation-id
  severity: error
- description: Operations must declare at least one tag.
  given: $.paths[*][get,post,put,patch,delete]
  name: ruckus-operation-tags
  severity: warn
- description: API should declare a JWT bearer security scheme.
  given: $.components.securitySchemes
  name: ruckus-bearer-auth
  severity: error
- description: Tenant-scoped resources should use the {tenantId} path parameter.
  given: $.paths[?(@property.indexOf('tenant') > -1)]
  name: ruckus-tenant-path
  severity: info
- description: Write operations should document a 202 Accepted async response.
  given: $.paths[*][post,put,patch].responses
  name: ruckus-async-202
  severity: info
rules_file: rules/commscope-holding-rules.yml
rules_url: https://raw.githubusercontent.com/api-evangelist/commscope-holding/refs/heads/main/rules/commscope-holding-rules.yml
severity_counts:
  error: 4
  hint: 0
  info: 3
  warn: 2
slug: commscope-holding-rules
source_filename: commscope-holding-rules.yml
source_heading: Spectral Ruleset
source_yaml: "extends:\n  - spectral:oas\n\n# Spectral linting rules for the RUCKUS One API (CommScope).\n# Tuned to api.ruckus.cloud conventions: regional servers, JWT bearer\n# auth via /oauth2/token, tenant-scoped paths, and asynchronous writes.\nrules:\n  ruckus-info-contact:\n    description: API info must include a contact block.\n    severity: error\n    given: \"$.info\"\n    then:\n      field: contact\n      function: truthy\n\n  ruckus-server-https:\n    description: Server URLs must use HTTPS.\n    severity: error\n    given: \"$.servers[*].url\"\n    then:\n      function: pattern\n      functionOptions:\n        match: \"^https://\"\n\n  ruckus-server-host:\n    description: Servers should be on the api.*.ruckus.cloud domain.\n    severity: warn\n    given: \"$.servers[*].url\"\n    then:\n      function: pattern\n      functionOptions:\n        match: \"ruckus\\\\.cloud\"\n\n  ruckus-multi-region:\n    description: API definition should declare multiple regional servers.\n\
  \    severity: info\n    given: \"$.servers\"\n    then:\n      function: schema\n      functionOptions:\n        schema:\n          type: array\n          minItems: 2\n\n  ruckus-operation-id:\n    description: Every operation must declare a unique operationId.\n    severity: error\n    given: \"$.paths[*][get,post,put,patch,delete]\"\n    then:\n      field: operationId\n      function: truthy\n\n  ruckus-operation-tags:\n    description: Operations must declare at least one tag.\n    severity: warn\n    given: \"$.paths[*][get,post,put,patch,delete]\"\n    then:\n      field: tags\n      function: schema\n      functionOptions:\n        schema:\n          type: array\n          minItems: 1\n\n  ruckus-bearer-auth:\n    description: API should declare a JWT bearer security scheme.\n    severity: error\n    given: \"$.components.securitySchemes\"\n    then:\n      function: schema\n      functionOptions:\n        schema:\n          type: object\n          properties:\n            BearerAuth:\n\
  \              type: object\n              properties:\n                type:\n                  const: http\n                scheme:\n                  const: bearer\n                bearerFormat:\n                  const: JWT\n\n  ruckus-tenant-path:\n    description: Tenant-scoped resources should use the {tenantId} path parameter.\n    severity: info\n    given: \"$.paths[?(@property.indexOf('tenant') > -1)]\"\n    then:\n      function: pattern\n      functionOptions:\n        match: \"{tenantId}\"\n\n  ruckus-async-202:\n    description: Write operations should document a 202 Accepted async response.\n    severity: info\n    given: \"$.paths[*][post,put,patch].responses\"\n    then:\n      function: schema\n      functionOptions:\n        schema:\n          type: object\n          anyOf:\n            - required: ['200']\n            - required: ['201']\n            - required: ['202']\n            - required: ['204']\n"
source_yaml_url: https://raw.githubusercontent.com/api-evangelist/commscope-holding/refs/heads/main/rules/commscope-holding-rules.yml
tags:
- Access Points
- Cabling
- Connectivity
- ICX Switches
- Infrastructure
- Networking
- RUCKUS
- Wi-Fi
- Spectral
- Linting
- API Governance
---
