---
name: OpenAPI Response Put 401 Status Code Error
description: >-
  PUT responses should have a 401 unauthorized HTTP status code, communicating
  that consumers do not have access
message: PUT Responses MUST 401 Status Codes
given: $.paths.*.put.responses
severity: error
tags:
  - OpenAPI
  - Responses
  - PUT
  - 4xx
view_sort: D
guidance: Errors
guidanceUrl: https://guidance.apievangelist.com/errors
rule:
  openapi-response-put-401-status-code-error:
    description: >-
      PUT responses should have a 401 unauthorized HTTP status code,
      communicating that consumers do not have access
    message: PUT Responses MUST 401 Status Codes
    severity: error
    given: $.paths.*.put.responses
    then:
      field: '401'
      function: truthy
slug: openapi-response-put-401-status-code-error
---