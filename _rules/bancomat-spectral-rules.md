---
categories:
- bancomat
description: Spectral linting rules defining API design standards and conventions for Bancomat.
layout: rules
name: Bancomat API Rules
provider_name: Bancomat
provider_slug: bancomat
rule_count: 10
rules:
- description: API title must be present.
  given: $.info
  name: bancomat-info-title-required
  severity: error
- description: API description must be present.
  given: $.info
  name: bancomat-info-description-required
  severity: warn
- description: API version must be present.
  given: $.info
  name: bancomat-info-version-required
  severity: error
- description: All operations must have an operationId.
  given: $.paths[*][get,post,put,patch,delete]
  name: bancomat-operation-id-required
  severity: error
- description: All operations must have a summary.
  given: $.paths[*][get,post,put,patch,delete]
  name: bancomat-operation-summary-required
  severity: warn
- description: Payment endpoints must return a status field.
  given: $.components.schemas.Payment.properties
  name: bancomat-payment-status-response
  severity: warn
- description: All BANCOMAT APIs must define security schemes.
  given: $
  name: bancomat-security-required
  severity: error
- description: GET operations must define a 200 response.
  given: $.paths[*].get.responses
  name: bancomat-response-200-required
  severity: error
- description: Error responses must include a schema.
  given: $.paths[*][*].responses[4XX].content[*]
  name: bancomat-error-response-schema
  severity: warn
- description: All named schemas must have a description.
  given: $.components.schemas[*]
  name: bancomat-schema-description-required
  severity: warn
rules_file: rules/bancomat-spectral-rules.yml
rules_url: https://raw.githubusercontent.com/api-evangelist/bancomat/refs/heads/main/rules/bancomat-spectral-rules.yml
severity_counts:
  error: 5
  hint: 0
  info: 0
  warn: 5
slug: bancomat-spectral-rules
source_filename: bancomat-spectral-rules.yml
source_heading: Spectral Ruleset
source_yaml: "rules:\n  bancomat-info-title-required:\n    description: API title must be present.\n    message: \"API info must include a title.\"\n    severity: error\n    given: \"$.info\"\n    then:\n      field: title\n      function: truthy\n\n  bancomat-info-description-required:\n    description: API description must be present.\n    message: \"API info must include a description.\"\n    severity: warn\n    given: \"$.info\"\n    then:\n      field: description\n      function: truthy\n\n  bancomat-info-version-required:\n    description: API version must be present.\n    message: \"API info must include a version.\"\n    severity: error\n    given: \"$.info\"\n    then:\n      field: version\n      function: truthy\n\n  bancomat-operation-id-required:\n    description: All operations must have an operationId.\n    message: \"Operation must have an operationId.\"\n    severity: error\n    given: \"$.paths[*][get,post,put,patch,delete]\"\n    then:\n      field: operationId\n    \
  \  function: truthy\n\n  bancomat-operation-summary-required:\n    description: All operations must have a summary.\n    message: \"Operation must have a summary.\"\n    severity: warn\n    given: \"$.paths[*][get,post,put,patch,delete]\"\n    then:\n      field: summary\n      function: truthy\n\n  bancomat-payment-status-response:\n    description: Payment endpoints must return a status field.\n    message: \"Payment response schemas should include a status field.\"\n    severity: warn\n    given: \"$.components.schemas.Payment.properties\"\n    then:\n      field: status\n      function: truthy\n\n  bancomat-security-required:\n    description: All BANCOMAT APIs must define security schemes.\n    message: \"API must define security requirements.\"\n    severity: error\n    given: \"$\"\n    then:\n      field: security\n      function: truthy\n\n  bancomat-response-200-required:\n    description: GET operations must define a 200 response.\n    message: \"GET operations must define a\
  \ 200 success response.\"\n    severity: error\n    given: \"$.paths[*].get.responses\"\n    then:\n      field: \"200\"\n      function: truthy\n\n  bancomat-error-response-schema:\n    description: Error responses must include a schema.\n    message: \"4xx responses should include an error schema.\"\n    severity: warn\n    given: \"$.paths[*][*].responses[4XX].content[*]\"\n    then:\n      field: schema\n      function: truthy\n\n  bancomat-schema-description-required:\n    description: All named schemas must have a description.\n    message: \"Schema components must have a description.\"\n    severity: warn\n    given: \"$.components.schemas[*]\"\n    then:\n      field: description\n      function: truthy\n"
source_yaml_url: https://raw.githubusercontent.com/api-evangelist/bancomat/refs/heads/main/rules/bancomat-spectral-rules.yml
tags:
- ATM
- Banking
- Financial Services
- Italy
- Mobile Payments
- Payments
- Debit Cards
- Spectral
- Linting
- API Governance
---
