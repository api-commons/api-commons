---
categories:
- banuba
description: Spectral linting rules defining API design standards and conventions for Banuba.
layout: rules
name: Banuba API Rules
provider_name: Banuba
provider_slug: banuba
rule_count: 7
rules:
- description: Banuba Face AR SDK APIs must have documentation.
  given: $.apis[*]
  name: banuba-face-ar-sdk-has-documentation
  severity: error
- description: All Banuba API entries must have a description.
  given: $.apis[*]
  name: banuba-api-has-description
  severity: error
- description: All Banuba API entries must have a name.
  given: $.apis[*]
  name: banuba-api-has-name
  severity: error
- description: All Banuba API entries must have a humanURL.
  given: $.apis[*]
  name: banuba-api-has-human-url
  severity: error
- description: All Banuba API entries must have tags.
  given: $.apis[*]
  name: banuba-api-has-tags
  severity: warn
- description: Banuba APIs.json must have a name.
  given: $
  name: banuba-apis-json-has-name
  severity: error
- description: Banuba APIs.json must have a description.
  given: $
  name: banuba-apis-json-has-description
  severity: error
rules_file: rules/banuba-spectral-rules.yml
rules_url: https://raw.githubusercontent.com/api-evangelist/banuba/refs/heads/main/rules/banuba-spectral-rules.yml
severity_counts:
  error: 6
  hint: 0
  info: 0
  warn: 1
slug: banuba-spectral-rules
source_filename: banuba-spectral-rules.yml
source_heading: Spectral Ruleset
source_yaml: "rules:\n  banuba-face-ar-sdk-has-documentation:\n    description: Banuba Face AR SDK APIs must have documentation.\n    message: \"{{description}}\"\n    severity: error\n    given: \"$.apis[*]\"\n    then:\n      field: properties\n      function: schema\n      functionOptions:\n        schema:\n          type: array\n          contains:\n            type: object\n            properties:\n              type:\n                const: Documentation\n            required:\n              - type\n\n  banuba-api-has-description:\n    description: All Banuba API entries must have a description.\n    message: \"{{description}}\"\n    severity: error\n    given: \"$.apis[*]\"\n    then:\n      field: description\n      function: truthy\n\n  banuba-api-has-name:\n    description: All Banuba API entries must have a name.\n    message: \"{{description}}\"\n    severity: error\n    given: \"$.apis[*]\"\n    then:\n      field: name\n      function: truthy\n\n  banuba-api-has-human-url:\n\
  \    description: All Banuba API entries must have a humanURL.\n    message: \"{{description}}\"\n    severity: error\n    given: \"$.apis[*]\"\n    then:\n      field: humanURL\n      function: truthy\n\n  banuba-api-has-tags:\n    description: All Banuba API entries must have tags.\n    message: \"{{description}}\"\n    severity: warn\n    given: \"$.apis[*]\"\n    then:\n      field: tags\n      function: truthy\n\n  banuba-apis-json-has-name:\n    description: Banuba APIs.json must have a name.\n    message: \"{{description}}\"\n    severity: error\n    given: \"$\"\n    then:\n      field: name\n      function: truthy\n\n  banuba-apis-json-has-description:\n    description: Banuba APIs.json must have a description.\n    message: \"{{description}}\"\n    severity: error\n    given: \"$\"\n    then:\n      field: description\n      function: truthy\n"
source_yaml_url: https://raw.githubusercontent.com/api-evangelist/banuba/refs/heads/main/rules/banuba-spectral-rules.yml
tags:
- AR
- Augmented Reality
- Beauty
- Face Recognition
- Facial
- SDK
- Video
- Spectral
- Linting
- API Governance
---
