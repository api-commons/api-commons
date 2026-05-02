---
slug: owasp-api8-2023-define-error-responses-500-warn
icon: alert-triangle
name: OWASP API8 2023 Define Error Responses 500
description: >-
  OWASP API Security recommends defining schemas for all responses, even errors.
  The 500 describes what happens when a request fails with an internal server
  error, so it is important to define this for documentation and contract testing.
message: Operation is missing a 500 error response.
given: $.paths..responses
severity: warn
view_sort: B
tags:
  - OWASP
  - Security
  - Responses
  - Errors
  - OpenAPI
guidance: Errors
guidanceUrl: https://guidance.apievangelist.com/errors
rule:
  owasp-api8-2023-define-error-responses-500-warn:
    description: >-
      OWASP API Security recommends defining schemas for all responses, even errors.
      The 500 describes what happens when a request fails with an internal server
      error, so it is important to define this for documentation and contract testing.
    message: Operation is missing a 500 error response.
    given: $.paths..responses
    severity: warn
    then:
      field: "500"
      function: truthy
---
