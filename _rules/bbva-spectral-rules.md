---
categories:
- bbva
description: Spectral linting rules defining API design standards and conventions for BBVA.
layout: rules
name: BBVA API Rules
provider_name: BBVA
provider_slug: bbva
rule_count: 6
rules:
- description: BBVA API operations must use OAuth 2.0 Bearer token authentication.
  given: $.paths[?(!@property.match('(token|oauth)'))].*.security
  name: bbva-bearer-auth-required
  severity: error
- description: All BBVA API operations must have an operationId.
  given: $.paths.*.*
  name: bbva-operation-id-required
  severity: error
- description: All GET operations should define a 200 success response.
  given: $.paths.*.get.responses
  name: bbva-response-200-required
  severity: warn
- description: Operations should define a 400 error response for bad requests.
  given: $.paths.*.*.responses
  name: bbva-error-response-400
  severity: warn
- description: BBVA multi-country APIs should document country selection mechanism.
  given: $.info
  name: bbva-country-header-documented
  severity: info
- description: IBAN fields should use string format with pattern constraint.
  given: $.components.schemas..[?(@property === 'iban')]
  name: bbva-iban-format
  severity: warn
rules_file: rules/bbva-spectral-rules.yml
rules_url: https://raw.githubusercontent.com/api-evangelist/bbva/refs/heads/main/rules/bbva-spectral-rules.yml
severity_counts:
  error: 2
  hint: 0
  info: 1
  warn: 3
slug: bbva-spectral-rules
source_filename: bbva-spectral-rules.yml
source_heading: Spectral Ruleset
source_yaml: "rules:\n  bbva-bearer-auth-required:\n    description: BBVA API operations must use OAuth 2.0 Bearer token authentication.\n    message: Operation must include BearerAuth or OAuth2 security requirement.\n    severity: error\n    given: $.paths[?(!@property.match('(token|oauth)'))].*.security\n    then:\n      function: schema\n      functionOptions:\n        schema:\n          type: array\n          minItems: 1\n\n  bbva-operation-id-required:\n    description: All BBVA API operations must have an operationId.\n    message: Operation is missing operationId.\n    severity: error\n    given: $.paths.*.*\n    then:\n      field: operationId\n      function: truthy\n\n  bbva-response-200-required:\n    description: All GET operations should define a 200 success response.\n    message: GET operation is missing a 200 response.\n    severity: warn\n    given: $.paths.*.get.responses\n    then:\n      field: '200'\n      function: truthy\n\n  bbva-error-response-400:\n    description:\
  \ Operations should define a 400 error response for bad requests.\n    message: Operation is missing a 400 Bad Request response definition.\n    severity: warn\n    given: $.paths.*.*.responses\n    then:\n      field: '400'\n      function: truthy\n\n  bbva-country-header-documented:\n    description: BBVA multi-country APIs should document country selection mechanism.\n    message: Consider documenting the country or region selection header/parameter.\n    severity: info\n    given: $.info\n    then:\n      field: description\n      function: truthy\n\n  bbva-iban-format:\n    description: IBAN fields should use string format with pattern constraint.\n    message: IBAN property should specify format or pattern.\n    severity: warn\n    given: $.components.schemas..[?(@property === 'iban')]\n    then:\n      field: type\n      function: truthy\n"
source_yaml_url: https://raw.githubusercontent.com/api-evangelist/bbva/refs/heads/main/rules/bbva-spectral-rules.yml
tags:
- Banking
- Financial Services
- Open Banking
- PSD2
- Spain
- Mexico
- Spectral
- Linting
- API Governance
---
