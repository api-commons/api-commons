---
name: OpenAPI Response Delete 429 Status Code Error
description: >-
  DELETE responses should have a 429 too many requests HTTP status code,
  communicating a consumer has made too may requests
message: DELETE Responses MUST Have 429 Status Codes
given: $.paths.*.delete.responses
severity: error
tags:
  - OpenAPI
  - Responses
  - DELETE
  - 4xx
view_sort: J
guidance: Errors
guidanceUrl: https://guidance.apievangelist.com/errors
rule:
  openapi-response-delete-429-status-code-error:
    description: >-
      DELETE responses should have a 429 too many requests HTTP status code,
      communicating a consumer has made too may requests
    message: DELETE Responses MUST Have 429 Status Codes
    severity: error
    given: $.paths.*.delete.responses
    then:
      field: '429'
      function: truthy
slug: openapi-response-delete-429-status-code-error
---