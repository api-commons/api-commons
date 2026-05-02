---
api_specs:
- filename: bjs-wholesale-club-openapi.yaml
  format: yaml
  label: BJ's Wholesale Club API
  slug: bjs-wholesale-club
  spec_type: OpenAPI
  url: https://raw.githubusercontent.com/api-evangelist/bjs-wholesale-club/refs/heads/main/openapi/bjs-wholesale-club-openapi.yaml
categories:
- bjs
description: Spectral linting rules defining API design standards and conventions for BJ's Wholesale Club.
layout: rules
name: BJ's Wholesale Club API Rules
provider_name: BJ's Wholesale Club
provider_slug: bjs-wholesale-club
rule_count: 5
rules:
- description: Orders and membership verifications must include a membershipNumber
  given: $.paths['/membership/verify'].post.requestBody.content['application/json'].schema
  name: bjs-membership-number-required
  severity: warn
- description: Order status must be one of the defined enum values
  given: $.components.schemas.Order.properties.status
  name: bjs-order-status-enum
  severity: warn
- description: Product price must be defined as a number type
  given: $.components.schemas.Product.properties.price
  name: bjs-product-price-positive
  severity: warn
- description: All endpoints must use ApiKeyAuth security scheme
  given: $.paths[*][*]
  name: bjs-api-key-security
  severity: warn
- description: All operations should have at least one tag
  given: $.paths[*][*]
  name: bjs-operations-have-tags
  severity: warn
rules_file: rules/bjs-spectral-rules.yml
rules_url: https://raw.githubusercontent.com/api-evangelist/bjs-wholesale-club/refs/heads/main/rules/bjs-spectral-rules.yml
severity_counts:
  error: 0
  hint: 0
  info: 0
  warn: 5
slug: bjs-spectral-rules
source_filename: bjs-spectral-rules.yml
source_heading: Spectral Ruleset
source_yaml: "rules:\n  bjs-membership-number-required:\n    description: Orders and membership verifications must include a membershipNumber\n    message: \"{{description}}\"\n    given: \"$.paths['/membership/verify'].post.requestBody.content['application/json'].schema\"\n    then:\n      field: required\n      function: schema\n      functionOptions:\n        schema:\n          type: array\n          contains:\n            const: membershipNumber\n\n  bjs-order-status-enum:\n    description: Order status must be one of the defined enum values\n    message: \"Order status field must use defined enum values\"\n    given: \"$.components.schemas.Order.properties.status\"\n    then:\n      field: enum\n      function: truthy\n\n  bjs-product-price-positive:\n    description: Product price must be defined as a number type\n    message: \"Product price must be a numeric type\"\n    given: \"$.components.schemas.Product.properties.price\"\n    then:\n      field: type\n      function: pattern\n\
  \      functionOptions:\n        match: \"^number$\"\n\n  bjs-api-key-security:\n    description: All endpoints must use ApiKeyAuth security scheme\n    message: \"Endpoint must specify ApiKeyAuth security\"\n    given: \"$.paths[*][*]\"\n    then:\n      field: security\n      function: truthy\n\n  bjs-operations-have-tags:\n    description: All operations should have at least one tag\n    message: \"Operation must include at least one tag\"\n    given: \"$.paths[*][*]\"\n    then:\n      field: tags\n      function: truthy\n"
source_yaml_url: https://raw.githubusercontent.com/api-evangelist/bjs-wholesale-club/refs/heads/main/rules/bjs-spectral-rules.yml
tags:
- Ecommerce
- Membership
- Retail
- Wholesale
- Spectral
- Linting
- API Governance
---
