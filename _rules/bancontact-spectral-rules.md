---
categories:
- bancontact
description: Spectral linting rules defining API design standards and conventions for Bancontact.
layout: rules
name: Bancontact API Rules
provider_name: Bancontact
provider_slug: bancontact
rule_count: 12
rules:
- description: API title must be present.
  given: $.info
  name: bancontact-info-title-required
  severity: error
- description: API description must be present.
  given: $.info
  name: bancontact-info-description-required
  severity: warn
- description: API version must be present.
  given: $.info
  name: bancontact-info-version-required
  severity: error
- description: All operations must have an operationId.
  given: $.paths[*][get,post,put,patch,delete]
  name: bancontact-operation-id-required
  severity: error
- description: All operations must have a summary.
  given: $.paths[*][get,post,put,patch,delete]
  name: bancontact-operation-summary-required
  severity: warn
- description: Payment response schemas must include a status field.
  given: $.components.schemas.Payment.properties
  name: bancontact-payment-status-field
  severity: warn
- description: Payment request schemas must include amount.
  given: $.components.schemas.PaymentRequest.properties
  name: bancontact-payment-amount-required
  severity: error
- description: All Bancontact APIs must define security schemes.
  given: $
  name: bancontact-security-required
  severity: error
- description: Payment operations should document webhook callbacks.
  given: $.paths[*].post
  name: bancontact-webhook-callback
  severity: info
- description: POST operations should return 201 on resource creation.
  given: $.paths[*].post.responses
  name: bancontact-response-201-for-post
  severity: warn
- description: Error responses must include a schema.
  given: $.paths[*][*].responses[4XX].content[*]
  name: bancontact-error-response-schema
  severity: warn
- description: All named schemas must have a description.
  given: $.components.schemas[*]
  name: bancontact-schema-description-required
  severity: warn
rules_file: rules/bancontact-spectral-rules.yml
rules_url: https://raw.githubusercontent.com/api-evangelist/bancontact/refs/heads/main/rules/bancontact-spectral-rules.yml
severity_counts:
  error: 5
  hint: 0
  info: 1
  warn: 6
slug: bancontact-spectral-rules
source_filename: bancontact-spectral-rules.yml
source_heading: Spectral Ruleset
source_yaml: "rules:\n  bancontact-info-title-required:\n    description: API title must be present.\n    message: \"API info must include a title.\"\n    severity: error\n    given: \"$.info\"\n    then:\n      field: title\n      function: truthy\n\n  bancontact-info-description-required:\n    description: API description must be present.\n    message: \"API info must include a description.\"\n    severity: warn\n    given: \"$.info\"\n    then:\n      field: description\n      function: truthy\n\n  bancontact-info-version-required:\n    description: API version must be present.\n    message: \"API info must include a version.\"\n    severity: error\n    given: \"$.info\"\n    then:\n      field: version\n      function: truthy\n\n  bancontact-operation-id-required:\n    description: All operations must have an operationId.\n    message: \"Operation must have an operationId.\"\n    severity: error\n    given: \"$.paths[*][get,post,put,patch,delete]\"\n    then:\n      field: operationId\n\
  \      function: truthy\n\n  bancontact-operation-summary-required:\n    description: All operations must have a summary.\n    message: \"Operation must have a summary.\"\n    severity: warn\n    given: \"$.paths[*][get,post,put,patch,delete]\"\n    then:\n      field: summary\n      function: truthy\n\n  bancontact-payment-status-field:\n    description: Payment response schemas must include a status field.\n    message: \"Payment schemas should include a status field.\"\n    severity: warn\n    given: \"$.components.schemas.Payment.properties\"\n    then:\n      field: status\n      function: truthy\n\n  bancontact-payment-amount-required:\n    description: Payment request schemas must include amount.\n    message: \"Payment request schemas should include an amount field.\"\n    severity: error\n    given: \"$.components.schemas.PaymentRequest.properties\"\n    then:\n      field: amount\n      function: truthy\n\n  bancontact-security-required:\n    description: All Bancontact APIs\
  \ must define security schemes.\n    message: \"API must define security requirements.\"\n    severity: error\n    given: \"$\"\n    then:\n      field: security\n      function: truthy\n\n  bancontact-webhook-callback:\n    description: Payment operations should document webhook callbacks.\n    message: \"POST payment operations should document callback webhooks.\"\n    severity: info\n    given: \"$.paths[*].post\"\n    then:\n      field: callbacks\n      function: truthy\n\n  bancontact-response-201-for-post:\n    description: POST operations should return 201 on resource creation.\n    message: \"POST operations creating resources should return 201.\"\n    severity: warn\n    given: \"$.paths[*].post.responses\"\n    then:\n      field: \"201\"\n      function: truthy\n\n  bancontact-error-response-schema:\n    description: Error responses must include a schema.\n    message: \"4xx responses should include an error schema.\"\n    severity: warn\n    given: \"$.paths[*][*].responses[4XX].content[*]\"\
  \n    then:\n      field: schema\n      function: truthy\n\n  bancontact-schema-description-required:\n    description: All named schemas must have a description.\n    message: \"Schema components must have a description.\"\n    severity: warn\n    given: \"$.components.schemas[*]\"\n    then:\n      field: description\n      function: truthy\n"
source_yaml_url: https://raw.githubusercontent.com/api-evangelist/bancontact/refs/heads/main/rules/bancontact-spectral-rules.yml
tags:
- Banking
- Belgium
- Debit Cards
- E-Commerce
- Fintech
- Payments
- Spectral
- Linting
- API Governance
---
