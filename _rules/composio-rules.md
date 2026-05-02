---
api_specs:
- filename: composio-openapi-original.yml
  format: yaml
  label: Composio Tool Router API
  slug: tool-router-api
  spec_type: OpenAPI
  url: https://raw.githubusercontent.com/api-evangelist/composio/refs/heads/main/openapi/composio-openapi-original.yml
- filename: composio-openapi-original.yml
  format: yaml
  label: Composio Tools API
  slug: tools-api
  spec_type: OpenAPI
  url: https://raw.githubusercontent.com/api-evangelist/composio/refs/heads/main/openapi/composio-openapi-original.yml
- filename: composio-openapi-original.yml
  format: yaml
  label: Composio Connected Accounts API
  slug: connected-accounts-api
  spec_type: OpenAPI
  url: https://raw.githubusercontent.com/api-evangelist/composio/refs/heads/main/openapi/composio-openapi-original.yml
- filename: composio-openapi-original.yml
  format: yaml
  label: Composio Auth Configs API
  slug: auth-configs-api
  spec_type: OpenAPI
  url: https://raw.githubusercontent.com/api-evangelist/composio/refs/heads/main/openapi/composio-openapi-original.yml
- filename: composio-openapi-original.yml
  format: yaml
  label: Composio Triggers API
  slug: triggers-api
  spec_type: OpenAPI
  url: https://raw.githubusercontent.com/api-evangelist/composio/refs/heads/main/openapi/composio-openapi-original.yml
- filename: composio-openapi-original.yml
  format: yaml
  label: Composio Toolkits API
  slug: toolkits-api
  spec_type: OpenAPI
  url: https://raw.githubusercontent.com/api-evangelist/composio/refs/heads/main/openapi/composio-openapi-original.yml
categories:
- composio
description: Spectral linting rules defining API design standards and conventions for Composio.
layout: rules
name: Composio API Rules
provider_name: Composio
provider_slug: composio
rule_count: 10
rules:
- description: API contact information must be present.
  given: $.info
  name: composio-info-contact
  severity: error
- description: API terms of service must be declared.
  given: $.info
  name: composio-info-terms
  severity: warn
- description: All server URLs must use HTTPS.
  given: $.servers[*].url
  name: composio-server-https
  severity: error
- description: Server URLs must include the /api/v3 segment.
  given: $.servers[*].url
  name: composio-server-versioned
  severity: warn
- description: An x-api-key header security scheme must be defined.
  given: $.components.securitySchemes
  name: composio-apikey-security
  severity: error
- description: Every operation must declare at least one tag.
  given: $.paths[*][get,post,put,patch,delete]
  name: composio-operation-tags
  severity: warn
- description: Every operation must include a short summary.
  given: $.paths[*][get,post,put,patch,delete]
  name: composio-operation-summary
  severity: warn
- description: Every operation must declare a unique operationId.
  given: $.paths[*][get,post,put,patch,delete]
  name: composio-operation-id
  severity: error
- description: Mutating operations should declare 4xx error responses.
  given: $.paths[*][post,put,patch,delete].responses
  name: composio-error-responses
  severity: warn
- description: Resource path segments should use camelCase, matching the v3 surface.
  given: $.paths
  name: composio-resource-naming
  severity: info
rules_file: rules/composio-rules.yml
rules_url: https://raw.githubusercontent.com/api-evangelist/composio/refs/heads/main/rules/composio-rules.yml
severity_counts:
  error: 4
  hint: 0
  info: 1
  warn: 5
slug: composio-rules
source_filename: composio-rules.yml
source_heading: Spectral Ruleset
source_yaml: "extends:\n  - spectral:oas\n\n# Spectral linting rules tuned for the Composio v3 API.\n# Validates that OpenAPI specs follow the conventions described at\n# https://docs.composio.dev/reference — API key authentication via\n# x-api-key (project) or x-org-api-key (organization) headers, JSON\n# request and response bodies, and resource-oriented v3 paths under\n# https://backend.composio.dev/api/v3.\nrules:\n  composio-info-contact:\n    description: API contact information must be present.\n    severity: error\n    given: \"$.info\"\n    then:\n      field: contact\n      function: truthy\n\n  composio-info-terms:\n    description: API terms of service must be declared.\n    severity: warn\n    given: \"$.info\"\n    then:\n      field: termsOfService\n      function: truthy\n\n  composio-server-https:\n    description: All server URLs must use HTTPS.\n    severity: error\n    given: \"$.servers[*].url\"\n    then:\n      function: pattern\n      functionOptions:\n        match:\
  \ \"^https://\"\n\n  composio-server-versioned:\n    description: Server URLs must include the /api/v3 segment.\n    severity: warn\n    given: \"$.servers[*].url\"\n    then:\n      function: pattern\n      functionOptions:\n        match: \"/api/v3$\"\n\n  composio-apikey-security:\n    description: An x-api-key header security scheme must be defined.\n    severity: error\n    given: \"$.components.securitySchemes\"\n    then:\n      function: truthy\n\n  composio-operation-tags:\n    description: Every operation must declare at least one tag.\n    severity: warn\n    given: \"$.paths[*][get,post,put,patch,delete]\"\n    then:\n      field: tags\n      function: schema\n      functionOptions:\n        schema:\n          type: array\n          minItems: 1\n\n  composio-operation-summary:\n    description: Every operation must include a short summary.\n    severity: warn\n    given: \"$.paths[*][get,post,put,patch,delete]\"\n    then:\n      field: summary\n      function: truthy\n\n \
  \ composio-operation-id:\n    description: Every operation must declare a unique operationId.\n    severity: error\n    given: \"$.paths[*][get,post,put,patch,delete]\"\n    then:\n      field: operationId\n      function: truthy\n\n  composio-error-responses:\n    description: Mutating operations should declare 4xx error responses.\n    severity: warn\n    given: \"$.paths[*][post,put,patch,delete].responses\"\n    then:\n      function: schema\n      functionOptions:\n        schema:\n          type: object\n          anyOf:\n            - required: [\"400\"]\n            - required: [\"401\"]\n            - required: [\"403\"]\n            - required: [\"404\"]\n            - required: [\"422\"]\n\n  composio-resource-naming:\n    description: Resource path segments should use camelCase, matching the v3 surface.\n    severity: info\n    given: \"$.paths\"\n    then:\n      function: truthy\n"
source_yaml_url: https://raw.githubusercontent.com/api-evangelist/composio/refs/heads/main/rules/composio-rules.yml
tags:
- AI Agents
- Authentication
- Integrations
- OAuth
- Tools
- Unified_API
- Spectral
- Linting
- API Governance
---
