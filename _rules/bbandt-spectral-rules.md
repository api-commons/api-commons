---
categories:
- truist
description: Spectral linting rules defining API design standards and conventions for BB&T Corp (Truist).
layout: rules
name: BB&T Corp (Truist) API Rules
provider_name: BB&T Corp (Truist)
provider_slug: bbandt-corp
rule_count: 5
rules:
- description: All Truist API operations must use OAuth 2.0 Bearer authentication.
  given: $.paths.*.*.security
  name: truist-bearer-auth-required
  severity: error
- description: All Truist API operations must have an operationId.
  given: $.paths.*.*
  name: truist-operation-id-required
  severity: error
- description: All GET operations should define a 200 success response.
  given: $.paths.*.get.responses
  name: truist-response-200-required
  severity: warn
- description: Operations should define standard error responses.
  given: $.paths.*.*.responses
  name: truist-error-responses-defined
  severity: info
- description: List operations should support pagination parameters.
  given: $.paths[?(@property.match('accounts|transactions'))].get.parameters
  name: truist-pagination-parameters
  severity: info
rules_file: rules/bbandt-spectral-rules.yml
rules_url: https://raw.githubusercontent.com/api-evangelist/bbandt-corp/refs/heads/main/rules/bbandt-spectral-rules.yml
severity_counts:
  error: 2
  hint: 0
  info: 2
  warn: 1
slug: bbandt-spectral-rules
source_filename: bbandt-spectral-rules.yml
source_heading: Spectral Ruleset
source_yaml: "rules:\n  truist-bearer-auth-required:\n    description: All Truist API operations must use OAuth 2.0 Bearer authentication.\n    message: Operation must include OAuth2 or BearerAuth security requirement.\n    severity: error\n    given: $.paths.*.*.security\n    then:\n      function: schema\n      functionOptions:\n        schema:\n          type: array\n          minItems: 1\n\n  truist-operation-id-required:\n    description: All Truist API operations must have an operationId.\n    message: Operation is missing operationId.\n    severity: error\n    given: $.paths.*.*\n    then:\n      field: operationId\n      function: truthy\n\n  truist-response-200-required:\n    description: All GET operations should define a 200 success response.\n    message: GET operation is missing a 200 response.\n    severity: warn\n    given: $.paths.*.get.responses\n    then:\n      field: '200'\n      function: truthy\n\n  truist-error-responses-defined:\n    description: Operations should\
  \ define standard error responses.\n    message: Consider defining 400, 401, and 403 error responses.\n    severity: info\n    given: $.paths.*.*.responses\n    then:\n      field: '401'\n      function: truthy\n\n  truist-pagination-parameters:\n    description: List operations should support pagination parameters.\n    message: Consider adding page/limit or cursor pagination to list operations.\n    severity: info\n    given: $.paths[?(@property.match('accounts|transactions'))].get.parameters\n    then:\n      function: schema\n      functionOptions:\n        schema:\n          type: array\n          minItems: 1\n"
source_yaml_url: https://raw.githubusercontent.com/api-evangelist/bbandt-corp/refs/heads/main/rules/bbandt-spectral-rules.yml
tags:
- Banking
- Financial Services
- Open Banking
- Truist
- BB&T
- Spectral
- Linting
- API Governance
---
