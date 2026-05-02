---
categories:
- classif
description: Spectral linting rules defining API design standards and conventions for Classif.io.
layout: rules
name: Classif.io API Rules
provider_name: Classif.io
provider_slug: classif-io
rule_count: 6
rules:
- description: API info MUST contain a contact email or URL.
  given: $.info
  name: classif-info-contact
  severity: warn
- description: All Classif.io API servers MUST use HTTPS.
  given: $.servers[*].url
  name: classif-https-only
  severity: error
- description: Operations MUST have an operationId.
  given: $.paths[*][get,post,put,delete,patch]
  name: classif-operation-id
  severity: error
- description: Operations MUST be tagged for classification domain grouping.
  given: $.paths[*][get,post,put,delete,patch].tags
  name: classif-tag-required
  severity: warn
- description: API MUST define API key security schemes.
  given: $.components.securitySchemes
  name: classif-security-required
  severity: error
- description: Classification operations SHOULD accept image inputs (multipart or URL).
  given: $.paths
  name: classif-image-input
  severity: warn
rules_file: rules/classif-io-rules.yml
rules_url: https://raw.githubusercontent.com/api-evangelist/classif-io/refs/heads/main/rules/classif-io-rules.yml
severity_counts:
  error: 3
  hint: 0
  info: 0
  warn: 3
slug: classif-io-rules
source_filename: classif-io-rules.yml
source_heading: Spectral Ruleset
source_yaml: "extends:\n  - spectral:oas\nrules:\n  classif-info-contact:\n    description: API info MUST contain a contact email or URL.\n    severity: warn\n    given: $.info\n    then:\n      field: contact\n      function: truthy\n  classif-https-only:\n    description: All Classif.io API servers MUST use HTTPS.\n    severity: error\n    given: $.servers[*].url\n    then:\n      function: pattern\n      functionOptions:\n        match: '^https://'\n  classif-operation-id:\n    description: Operations MUST have an operationId.\n    severity: error\n    given: $.paths[*][get,post,put,delete,patch]\n    then:\n      field: operationId\n      function: truthy\n  classif-tag-required:\n    description: Operations MUST be tagged for classification domain grouping.\n    severity: warn\n    given: $.paths[*][get,post,put,delete,patch].tags\n    then:\n      function: truthy\n  classif-security-required:\n    description: API MUST define API key security schemes.\n    severity: error\n    given:\
  \ $.components.securitySchemes\n    then:\n      function: truthy\n  classif-image-input:\n    description: Classification operations SHOULD accept image inputs (multipart or URL).\n    severity: warn\n    given: $.paths\n    then:\n      function: truthy\n"
source_yaml_url: https://raw.githubusercontent.com/api-evangelist/classif-io/refs/heads/main/rules/classif-io-rules.yml
tags:
- Apparel
- Classification
- Computer Vision
- Fashion
- Image Recognition
- Machine Learning
- Recommendation
- Spectral
- Linting
- API Governance
---
