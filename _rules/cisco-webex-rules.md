---
api_specs:
- filename: cisco-webex-meetings-openapi.yml
  format: yaml
  label: Webex Meetings API
  slug: webex-meetings-api
  spec_type: OpenAPI
  url: https://raw.githubusercontent.com/api-evangelist/cisco-webex/refs/heads/main/openapi/cisco-webex-meetings-openapi.yml
- filename: cisco-webex-messaging-openapi.yml
  format: yaml
  label: Webex Messaging API
  slug: webex-messaging-api
  spec_type: OpenAPI
  url: https://raw.githubusercontent.com/api-evangelist/cisco-webex/refs/heads/main/openapi/cisco-webex-messaging-openapi.yml
- filename: cisco-webex-people-openapi.yml
  format: yaml
  label: Webex People API
  slug: webex-people-api
  spec_type: OpenAPI
  url: https://raw.githubusercontent.com/api-evangelist/cisco-webex/refs/heads/main/openapi/cisco-webex-people-openapi.yml
- filename: cisco-webex-teams-openapi.yml
  format: yaml
  label: Webex Teams API
  slug: webex-teams-api
  spec_type: OpenAPI
  url: https://raw.githubusercontent.com/api-evangelist/cisco-webex/refs/heads/main/openapi/cisco-webex-teams-openapi.yml
- filename: cisco-webex-rooms-openapi.yml
  format: yaml
  label: Webex Rooms API
  slug: webex-rooms-api
  spec_type: OpenAPI
  url: https://raw.githubusercontent.com/api-evangelist/cisco-webex/refs/heads/main/openapi/cisco-webex-rooms-openapi.yml
- filename: cisco-webex-webhooks-openapi.yml
  format: yaml
  label: Webex Webhooks API
  slug: webex-webhooks-api
  spec_type: OpenAPI
  url: https://raw.githubusercontent.com/api-evangelist/cisco-webex/refs/heads/main/openapi/cisco-webex-webhooks-openapi.yml
- filename: cisco-webex-devices-openapi.yml
  format: yaml
  label: Webex Devices API
  slug: webex-devices-api
  spec_type: OpenAPI
  url: https://raw.githubusercontent.com/api-evangelist/cisco-webex/refs/heads/main/openapi/cisco-webex-devices-openapi.yml
- filename: cisco-webex-memberships-openapi.yml
  format: yaml
  label: Webex Memberships API
  slug: webex-memberships-api
  spec_type: OpenAPI
  url: https://raw.githubusercontent.com/api-evangelist/cisco-webex/refs/heads/main/openapi/cisco-webex-memberships-openapi.yml
- filename: cisco-webex-team-memberships-openapi.yml
  format: yaml
  label: Webex Team Memberships API
  slug: webex-team-memberships-api
  spec_type: OpenAPI
  url: https://raw.githubusercontent.com/api-evangelist/cisco-webex/refs/heads/main/openapi/cisco-webex-team-memberships-openapi.yml
- filename: cisco-webex-events-openapi.yml
  format: yaml
  label: Webex Events API
  slug: webex-events-api
  spec_type: OpenAPI
  url: https://raw.githubusercontent.com/api-evangelist/cisco-webex/refs/heads/main/openapi/cisco-webex-events-openapi.yml
- filename: cisco-webex-recordings-openapi.yml
  format: yaml
  label: Webex Recordings API
  slug: webex-recordings-api
  spec_type: OpenAPI
  url: https://raw.githubusercontent.com/api-evangelist/cisco-webex/refs/heads/main/openapi/cisco-webex-recordings-openapi.yml
- filename: cisco-webex-call-controls-openapi.yml
  format: yaml
  label: Webex Call Controls API
  slug: webex-call-controls-api
  spec_type: OpenAPI
  url: https://raw.githubusercontent.com/api-evangelist/cisco-webex/refs/heads/main/openapi/cisco-webex-call-controls-openapi.yml
- filename: cisco-webex-attachment-actions-openapi.yml
  format: yaml
  label: Webex Attachment Actions API
  slug: webex-attachment-actions-api
  spec_type: OpenAPI
  url: https://raw.githubusercontent.com/api-evangelist/cisco-webex/refs/heads/main/openapi/cisco-webex-attachment-actions-openapi.yml
- filename: cisco-webex-organizations-openapi.yml
  format: yaml
  label: Webex Organizations API
  slug: webex-organizations-api
  spec_type: OpenAPI
  url: https://raw.githubusercontent.com/api-evangelist/cisco-webex/refs/heads/main/openapi/cisco-webex-organizations-openapi.yml
- filename: cisco-webex-licenses-openapi.yml
  format: yaml
  label: Webex Licenses API
  slug: webex-licenses-api
  spec_type: OpenAPI
  url: https://raw.githubusercontent.com/api-evangelist/cisco-webex/refs/heads/main/openapi/cisco-webex-licenses-openapi.yml
- filename: cisco-webex-roles-openapi.yml
  format: yaml
  label: Webex Roles API
  slug: webex-roles-api
  spec_type: OpenAPI
  url: https://raw.githubusercontent.com/api-evangelist/cisco-webex/refs/heads/main/openapi/cisco-webex-roles-openapi.yml
- filename: cisco-webex-workspaces-openapi.yml
  format: yaml
  label: Webex Workspaces API
  slug: webex-workspaces-api
  spec_type: OpenAPI
  url: https://raw.githubusercontent.com/api-evangelist/cisco-webex/refs/heads/main/openapi/cisco-webex-workspaces-openapi.yml
- filename: cisco-webex-admin-audit-events-openapi.yml
  format: yaml
  label: Webex Admin Audit Events API
  slug: webex-admin-audit-events-api
  spec_type: OpenAPI
  url: https://raw.githubusercontent.com/api-evangelist/cisco-webex/refs/heads/main/openapi/cisco-webex-admin-audit-events-openapi.yml
- filename: cisco-webex-converged-recordings-openapi.yml
  format: yaml
  label: Webex Converged Recordings API
  slug: webex-converged-recordings-api
  spec_type: OpenAPI
  url: https://raw.githubusercontent.com/api-evangelist/cisco-webex/refs/heads/main/openapi/cisco-webex-converged-recordings-openapi.yml
categories:
- webex
description: Spectral linting rules defining API design standards and conventions for Cisco Webex.
layout: rules
name: Cisco Webex API Rules
provider_name: Cisco Webex
provider_slug: cisco-webex
rule_count: 6
rules:
- description: All Webex API servers MUST use HTTPS.
  given: $.servers[*].url
  name: webex-server-https
  severity: error
- description: Webex server URL SHOULD be webexapis.com/v1.
  given: $.servers[*].url
  name: webex-base-url
  severity: warn
- description: Operations MUST have an operationId.
  given: $.paths[*][get,post,put,delete,patch]
  name: webex-operation-id
  severity: error
- description: Operations MUST have a summary.
  given: $.paths[*][get,post,put,delete,patch]
  name: webex-summary-required
  severity: warn
- description: Operations MUST be tagged for Webex domain grouping.
  given: $.paths[*][get,post,put,delete,patch].tags
  name: webex-tag-required
  severity: warn
- description: API SHOULD declare OAuth 2.0 security scheme.
  given: $.components.securitySchemes
  name: webex-oauth-security
  severity: warn
rules_file: rules/cisco-webex-rules.yml
rules_url: https://raw.githubusercontent.com/api-evangelist/cisco-webex/refs/heads/main/rules/cisco-webex-rules.yml
severity_counts:
  error: 2
  hint: 0
  info: 0
  warn: 4
slug: cisco-webex-rules
source_filename: cisco-webex-rules.yml
source_heading: Spectral Ruleset
source_yaml: "extends:\n  - spectral:oas\nrules:\n  webex-server-https:\n    description: All Webex API servers MUST use HTTPS.\n    severity: error\n    given: $.servers[*].url\n    then:\n      function: pattern\n      functionOptions:\n        match: '^https://'\n  webex-base-url:\n    description: Webex server URL SHOULD be webexapis.com/v1.\n    severity: warn\n    given: $.servers[*].url\n    then:\n      function: pattern\n      functionOptions:\n        match: '^https://webexapis\\.com/v1'\n  webex-operation-id:\n    description: Operations MUST have an operationId.\n    severity: error\n    given: $.paths[*][get,post,put,delete,patch]\n    then:\n      field: operationId\n      function: truthy\n  webex-summary-required:\n    description: Operations MUST have a summary.\n    severity: warn\n    given: $.paths[*][get,post,put,delete,patch]\n    then:\n      field: summary\n      function: truthy\n  webex-tag-required:\n    description: Operations MUST be tagged for Webex domain grouping.\n\
  \    severity: warn\n    given: $.paths[*][get,post,put,delete,patch].tags\n    then:\n      function: truthy\n  webex-oauth-security:\n    description: API SHOULD declare OAuth 2.0 security scheme.\n    severity: warn\n    given: $.components.securitySchemes\n    then:\n      function: truthy\n"
source_yaml_url: https://raw.githubusercontent.com/api-evangelist/cisco-webex/refs/heads/main/rules/cisco-webex-rules.yml
tags:
- Collaboration
- Communications
- Meetings
- Messaging
- Teams
- Video Conferencing
- Spectral
- Linting
- API Governance
---
