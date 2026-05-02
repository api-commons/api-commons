---
api_specs:
- filename: cpsc-recalls-openapi.yml
  format: yaml
  label: CPSC Recalls API
  slug: recalls
  spec_type: OpenAPI
  url: https://raw.githubusercontent.com/api-evangelist/consumer-product-safety-commission/refs/heads/main/openapi/cpsc-recalls-openapi.yml
categories:
- cpsc
description: Spectral linting rules defining API design standards and conventions for Consumer Product Safety Commission.
layout: rules
name: Consumer Product Safety Commission API Rules
provider_name: Consumer Product Safety Commission
provider_slug: consumer-product-safety-commission
rule_count: 7
rules:
- description: API contact information must be present.
  given: $.info
  name: cpsc-info-contact
  severity: error
- description: All server URLs must use HTTPS.
  given: $.servers[*].url
  name: cpsc-server-https
  severity: error
- description: Server URLs must point to a *.cpsc.gov or saferproducts.gov host.
  given: $.servers[*].url
  name: cpsc-server-host
  severity: warn
- description: Every operation must declare a unique operationId.
  given: $.paths[*][get,post,put,patch,delete]
  name: cpsc-operation-id
  severity: error
- description: Operations must declare at least one tag.
  given: $.paths[*][get,post,put,patch,delete]
  name: cpsc-operation-tags
  severity: warn
- description: GET endpoints should accept a `format` parameter for JSON or XML.
  given: $.paths[*].get
  name: cpsc-format-parameter
  severity: info
- description: Responses should declare application/json and application/xml.
  given: $.paths[*].get.responses['200'].content
  name: cpsc-content-types
  severity: info
rules_file: rules/consumer-product-safety-commission-rules.yml
rules_url: https://raw.githubusercontent.com/api-evangelist/consumer-product-safety-commission/refs/heads/main/rules/consumer-product-safety-commission-rules.yml
severity_counts:
  error: 3
  hint: 0
  info: 2
  warn: 2
slug: consumer-product-safety-commission-rules
source_filename: consumer-product-safety-commission-rules.yml
source_heading: Spectral Ruleset
source_yaml: "extends:\n  - spectral:oas\n\n# Spectral linting rules for the CPSC Recalls API.\n# Tuned to saferproducts.gov / cpsc.gov public-data conventions: HTTPS,\n# unauthenticated public access, JSON or XML output, and PascalCase\n# query parameter names.\nrules:\n  cpsc-info-contact:\n    description: API contact information must be present.\n    severity: error\n    given: \"$.info\"\n    then:\n      field: contact\n      function: truthy\n\n  cpsc-server-https:\n    description: All server URLs must use HTTPS.\n    severity: error\n    given: \"$.servers[*].url\"\n    then:\n      function: pattern\n      functionOptions:\n        match: \"^https://\"\n\n  cpsc-server-host:\n    description: Server URLs must point to a *.cpsc.gov or saferproducts.gov host.\n    severity: warn\n    given: \"$.servers[*].url\"\n    then:\n      function: pattern\n      functionOptions:\n        match: \"(cpsc\\\\.gov|saferproducts\\\\.gov)\"\n\n  cpsc-operation-id:\n    description: Every operation\
  \ must declare a unique operationId.\n    severity: error\n    given: \"$.paths[*][get,post,put,patch,delete]\"\n    then:\n      field: operationId\n      function: truthy\n\n  cpsc-operation-tags:\n    description: Operations must declare at least one tag.\n    severity: warn\n    given: \"$.paths[*][get,post,put,patch,delete]\"\n    then:\n      field: tags\n      function: schema\n      functionOptions:\n        schema:\n          type: array\n          minItems: 1\n\n  cpsc-format-parameter:\n    description: GET endpoints should accept a `format` parameter for JSON or XML.\n    severity: info\n    given: \"$.paths[*].get\"\n    then:\n      field: parameters\n      function: schema\n      functionOptions:\n        schema:\n          type: array\n          contains:\n            type: object\n            properties:\n              name:\n                enum: [\"format\"]\n\n  cpsc-content-types:\n    description: Responses should declare application/json and application/xml.\n  \
  \  severity: info\n    given: \"$.paths[*].get.responses['200'].content\"\n    then:\n      function: schema\n      functionOptions:\n        schema:\n          type: object\n          anyOf:\n            - required: [\"application/json\"]\n            - required: [\"application/xml\"]\n"
source_yaml_url: https://raw.githubusercontent.com/api-evangelist/consumer-product-safety-commission/refs/heads/main/rules/consumer-product-safety-commission-rules.yml
tags:
- Consumer Protection
- Federal Government
- Hazards
- Open Data
- Product Safety
- Recalls
- Spectral
- Linting
- API Governance
---
