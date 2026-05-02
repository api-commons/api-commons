---
api_specs:
- filename: csg-forte-rest-openapi.yml
  format: yaml
  label: CSG Forte REST API
  slug: csg-forte-rest-api
  spec_type: OpenAPI
  url: https://raw.githubusercontent.com/api-evangelist/csg/refs/heads/main/openapi/csg-forte-rest-openapi.yml
categories:
- csg
description: Spectral linting rules defining API design standards and conventions for CSG Systems.
layout: rules
name: CSG Systems API Rules
provider_name: CSG Systems
provider_slug: csg
rule_count: 7
rules:
- description: CSG Forte servers must use HTTPS.
  given: $.servers[*].url
  name: csg-forte-server-https
  severity: error
- description: CSG Forte server URLs must include /v{n} version segment.
  given: $.servers[*].url
  name: csg-forte-versioned-path
  severity: error
- description: Resource paths must be scoped under /organizations/{organizationId}/locations/{locationId}.
  given: $.paths
  name: csg-forte-org-location-path
  severity: warn
- description: organizationId path parameter must match org_ prefix pattern.
  given: $.paths[*][get,post,put,delete].parameters[?(@.name=='organizationId')]
  name: csg-forte-org-id-pattern
  severity: warn
- description: Payment-method endpoints must declare an authentication requirement.
  given: $.paths[?(@property.match(/paymentmethods/))][post,put]
  name: csg-forte-pci-required
  severity: error
- description: Operations must declare a tag.
  given: $.paths[*][get,post,put,delete]
  name: csg-forte-tag-required
  severity: warn
- description: Operation IDs should be camelCase.
  given: $.paths[*][get,post,put,delete].operationId
  name: csg-forte-operation-id-camel
  severity: warn
rules_file: rules/csg-forte-rules.yml
rules_url: https://raw.githubusercontent.com/api-evangelist/csg/refs/heads/main/rules/csg-forte-rules.yml
severity_counts:
  error: 3
  hint: 0
  info: 0
  warn: 4
slug: csg-forte-rules
source_filename: csg-forte-rules.yml
source_heading: Spectral Ruleset
source_yaml: "extends: [[spectral:oas, all]]\nrules:\n  csg-forte-server-https:\n    description: CSG Forte servers must use HTTPS.\n    given: $.servers[*].url\n    severity: error\n    then:\n      function: pattern\n      functionOptions:\n        match: '^https://'\n  csg-forte-versioned-path:\n    description: CSG Forte server URLs must include /v{n} version segment.\n    given: $.servers[*].url\n    severity: error\n    then:\n      function: pattern\n      functionOptions:\n        match: '/v[0-9]+'\n  csg-forte-org-location-path:\n    description: Resource paths must be scoped under /organizations/{organizationId}/locations/{locationId}.\n    given: $.paths\n    severity: warn\n    then:\n      function: schema\n      functionOptions:\n        schema:\n          type: object\n          patternProperties:\n            \"^/organizations/\\\\{organizationId\\\\}/locations/\\\\{locationId\\\\}\":\n              type: object\n          additionalProperties: false\n  csg-forte-org-id-pattern:\n\
  \    description: organizationId path parameter must match org_ prefix pattern.\n    given: $.paths[*][get,post,put,delete].parameters[?(@.name=='organizationId')]\n    severity: warn\n    then:\n      field: schema.pattern\n      function: truthy\n  csg-forte-pci-required:\n    description: Payment-method endpoints must declare an authentication requirement.\n    given: $.paths[?(@property.match(/paymentmethods/))][post,put]\n    severity: error\n    then:\n      field: security\n      function: truthy\n  csg-forte-tag-required:\n    description: Operations must declare a tag.\n    given: $.paths[*][get,post,put,delete]\n    severity: warn\n    then:\n      field: tags\n      function: truthy\n  csg-forte-operation-id-camel:\n    description: Operation IDs should be camelCase.\n    given: $.paths[*][get,post,put,delete].operationId\n    severity: warn\n    then:\n      function: pattern\n      functionOptions:\n        match: '^[a-z][a-zA-Z0-9]+$'\n"
source_yaml_url: https://raw.githubusercontent.com/api-evangelist/csg/refs/heads/main/rules/csg-forte-rules.yml
tags:
- Billing
- Customer Engagement
- Payments
- Revenue Management
- Telecom
- Spectral
- Linting
- API Governance
---
