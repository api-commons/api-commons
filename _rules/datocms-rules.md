---
api_specs:
- filename: datocms-content-management-api.yml
  format: yaml
  label: DatoCMS Content Management API
  slug: datocms
  spec_type: OpenAPI
  url: https://raw.githubusercontent.com/api-evangelist/datocms/refs/heads/main/openapi/datocms-content-management-api.yml
categories:
- datocms
description: Spectral linting rules defining API design standards and conventions for DatoCMS.
layout: rules
name: DatoCMS API Rules
provider_name: DatoCMS
provider_slug: datocms
rule_count: 5
rules:
- description: CMA server URL must be https://site-api.datocms.com.
  given: $.servers[*].url
  name: datocms-server-base
  severity: error
- description: Operations must use API token bearer auth.
  given: $.components.securitySchemes.apiTokenAuth
  name: datocms-bearer-auth
  severity: error
- description: Request and response bodies should use application/vnd.api+json.
  given: $.paths.*.*.requestBody.content
  name: datocms-jsonapi-content-type
  severity: warn
- description: Every operation must declare a tag.
  given: $.paths[*][*]
  name: datocms-operation-tags
  severity: error
- description: List endpoints should accept page[offset] and page[limit] params.
  given: $.paths.*.get
  name: datocms-page-pagination
  severity: warn
rules_file: rules/datocms-rules.yml
rules_url: https://raw.githubusercontent.com/api-evangelist/datocms/refs/heads/main/rules/datocms-rules.yml
severity_counts:
  error: 3
  hint: 0
  info: 0
  warn: 2
slug: datocms-rules
source_filename: datocms-rules.yml
source_heading: Spectral Ruleset
source_yaml: "extends:\n  - spectral:oas\nrules:\n  datocms-server-base:\n    description: CMA server URL must be https://site-api.datocms.com.\n    given: $.servers[*].url\n    severity: error\n    then:\n      function: pattern\n      functionOptions:\n        match: \"^https://site-api\\\\.datocms\\\\.com$\"\n  datocms-bearer-auth:\n    description: Operations must use API token bearer auth.\n    given: $.components.securitySchemes.apiTokenAuth\n    severity: error\n    then:\n      field: scheme\n      function: pattern\n      functionOptions:\n        match: \"^bearer$\"\n  datocms-jsonapi-content-type:\n    description: Request and response bodies should use application/vnd.api+json.\n    given: $.paths.*.*.requestBody.content\n    severity: warn\n    then:\n      field: application/vnd.api+json\n      function: truthy\n  datocms-operation-tags:\n    description: Every operation must declare a tag.\n    given: $.paths[*][*]\n    severity: error\n    then:\n      field: tags\n     \
  \ function: truthy\n  datocms-page-pagination:\n    description: List endpoints should accept page[offset] and page[limit] params.\n    given: $.paths.*.get\n    severity: warn\n    then:\n      function: truthy\n"
source_yaml_url: https://raw.githubusercontent.com/api-evangelist/datocms/refs/heads/main/rules/datocms-rules.yml
tags:
- CMS
- Content Delivery
- Content Management
- GraphQL
- Headless CMS
- Spectral
- Linting
- API Governance
---
