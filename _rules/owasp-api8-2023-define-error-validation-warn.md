---
slug: owasp-api8-2023-define-error-validation-warn
icon: alert-triangle
name: OWASP API8 2023 Define Error Validation
description: >-
  Carefully define schemas for all the API responses, including either 400, 422
  or 4XX responses which describe errors caused by invalid requests.
message: Missing error validation response of either 400, 422, or 4XX.
given: $.paths..responses
severity: warn
view_sort: B
tags:
  - OWASP
  - Security
  - Responses
  - Validation
  - OpenAPI
guidance: Security
guidanceUrl: https://guidance.apievangelist.com/security
rule:
  owasp-api8-2023-define-error-validation-warn:
    description: >-
      Carefully define schemas for all the API responses, including either 400, 422
      or 4XX responses which describe errors caused by invalid requests.
    message: Missing error validation response of either 400, 422, or 4XX.
    given: $.paths..responses
    severity: warn
    then:
      function: schema
      functionOptions:
        schema:
          anyOf:
            - required: ["400"]
            - required: ["422"]
            - required: ["4XX"]
---
