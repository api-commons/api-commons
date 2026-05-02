---
slug: owasp-api8-2023-define-error-responses-401-warn
icon: alert-triangle
name: OWASP API8 2023 Define Error Responses 401
description: >-
  OWASP API Security recommends defining schemas for all responses, even errors.
  The 401 describes what happens when a request is unauthorized, so it is
  important to define this for documentation and contract testing.
message: Operation is missing a 401 error response.
given: $.paths..responses
severity: warn
view_sort: B
tags:
  - OWASP
  - Security
  - Responses
  - Authentication
  - OpenAPI
guidance: Security
guidanceUrl: https://guidance.apievangelist.com/security
rule:
  owasp-api8-2023-define-error-responses-401-warn:
    description: >-
      OWASP API Security recommends defining schemas for all responses, even errors.
      The 401 describes what happens when a request is unauthorized, so it is
      important to define this for documentation and contract testing.
    message: Operation is missing a 401 error response.
    given: $.paths..responses
    severity: warn
    then:
      field: "401"
      function: truthy
---
