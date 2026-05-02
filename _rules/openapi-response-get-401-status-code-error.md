---
name: OpenAPI Response Get 401 Status Code Error
description: >-
  GET responses should have a 401 unauthorized HTTP status code, communicating
  that consumers do not have access
message: GET Responses Has 401 Status Code
given: $.paths.*.get.responses
severity: error
tags:
  - OpenAPI
  - Responses
  - GET
  - 4xx
view_sort: J
guidance: Errors
guidanceUrl: https://guidance.apievangelist.com/errors
rule:
  openapi-response-get-401-status-code-error:
    description: >-
      GET responses should have a 401 unauthorized HTTP status code,
      communicating that consumers do not have access
    message: GET Responses Has 401 Status Code
    severity: error
    given: $.paths.*.get.responses
    then:
      field: '401'
      function: truthy
slug: openapi-response-get-401-status-code-error
---