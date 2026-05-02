---
api_specs:
- filename: chs-patient-access-api-openapi.yml
  format: yaml
  label: Community Health Systems Patient Access API
  slug: patient-access-api
  spec_type: OpenAPI
  url: https://raw.githubusercontent.com/api-evangelist/community-health-systems/refs/heads/main/openapi/chs-patient-access-api-openapi.yml
categories:
- chs
description: Spectral linting rules defining API design standards and conventions for Community Health Systems.
layout: rules
name: Community Health Systems API Rules
provider_name: Community Health Systems
provider_slug: community-health-systems
rule_count: 9
rules:
- description: API info must include a contact block.
  given: $.info
  name: chs-info-contact
  severity: error
- description: Server URLs must use HTTPS.
  given: $.servers[*].url
  name: chs-server-https
  severity: error
- description: Server URLs should point to api.chs.net.
  given: $.servers[*].url
  name: chs-server-host
  severity: warn
- description: Server URL should include the /fhir/r4 base path.
  given: $.servers[*].url
  name: chs-fhir-r4-base
  severity: warn
- description: Every operation must declare a unique operationId.
  given: $.paths[*][get,post,put,patch,delete]
  name: chs-operation-id
  severity: error
- description: Operations must declare at least one tag.
  given: $.paths[*][get,post,put,patch,delete]
  name: chs-operation-tags
  severity: warn
- description: FHIR responses should use application/fhir+json content type.
  given: $.paths[*][get,post,put,patch].responses.200.content
  name: chs-fhir-mediatype
  severity: warn
- description: API must declare OAuth2 with SMART-on-FHIR scopes.
  given: $.components.securitySchemes
  name: chs-oauth2-smart
  severity: error
- description: Paths should be capitalized FHIR resource type names.
  given: $.paths
  name: chs-fhir-resource-paths
  severity: info
rules_file: rules/community-health-systems-rules.yml
rules_url: https://raw.githubusercontent.com/api-evangelist/community-health-systems/refs/heads/main/rules/community-health-systems-rules.yml
severity_counts:
  error: 4
  hint: 0
  info: 1
  warn: 4
slug: community-health-systems-rules
source_filename: community-health-systems-rules.yml
source_heading: Spectral Ruleset
source_yaml: "extends:\n  - spectral:oas\n\n# Spectral linting rules for the Community Health Systems FHIR APIs.\n# Tuned to CMS Interoperability Final Rule (CMS-9115-F) requirements:\n# FHIR R4 servers, SMART-on-FHIR OAuth2 with patient/launch scopes,\n# and FHIR Bundle response shapes.\nrules:\n  chs-info-contact:\n    description: API info must include a contact block.\n    severity: error\n    given: \"$.info\"\n    then:\n      field: contact\n      function: truthy\n\n  chs-server-https:\n    description: Server URLs must use HTTPS.\n    severity: error\n    given: \"$.servers[*].url\"\n    then:\n      function: pattern\n      functionOptions:\n        match: \"^https://\"\n\n  chs-server-host:\n    description: Server URLs should point to api.chs.net.\n    severity: warn\n    given: \"$.servers[*].url\"\n    then:\n      function: pattern\n      functionOptions:\n        match: \"api\\\\.chs\\\\.net\"\n\n  chs-fhir-r4-base:\n    description: Server URL should include the /fhir/r4\
  \ base path.\n    severity: warn\n    given: \"$.servers[*].url\"\n    then:\n      function: pattern\n      functionOptions:\n        match: \"/fhir/r4\"\n\n  chs-operation-id:\n    description: Every operation must declare a unique operationId.\n    severity: error\n    given: \"$.paths[*][get,post,put,patch,delete]\"\n    then:\n      field: operationId\n      function: truthy\n\n  chs-operation-tags:\n    description: Operations must declare at least one tag.\n    severity: warn\n    given: \"$.paths[*][get,post,put,patch,delete]\"\n    then:\n      field: tags\n      function: schema\n      functionOptions:\n        schema:\n          type: array\n          minItems: 1\n\n  chs-fhir-mediatype:\n    description: FHIR responses should use application/fhir+json content type.\n    severity: warn\n    given: \"$.paths[*][get,post,put,patch].responses.200.content\"\n    then:\n      function: schema\n      functionOptions:\n        schema:\n          type: object\n          anyOf:\n   \
  \         - required: ['application/fhir+json']\n            - required: ['application/json']\n\n  chs-oauth2-smart:\n    description: API must declare OAuth2 with SMART-on-FHIR scopes.\n    severity: error\n    given: \"$.components.securitySchemes\"\n    then:\n      function: schema\n      functionOptions:\n        schema:\n          type: object\n          properties:\n            oauth2:\n              type: object\n              properties:\n                type:\n                  const: oauth2\n\n  chs-fhir-resource-paths:\n    description: Paths should be capitalized FHIR resource type names.\n    severity: info\n    given: \"$.paths\"\n    then:\n      function: schema\n      functionOptions:\n        schema:\n          type: object\n"
source_yaml_url: https://raw.githubusercontent.com/api-evangelist/community-health-systems/refs/heads/main/rules/community-health-systems-rules.yml
tags:
- CMS-9115-F
- FHIR
- Healthcare
- Hospitals
- Interoperability
- Patient Access
- Provider Directory
- SMART-on-FHIR
- Spectral
- Linting
- API Governance
---
