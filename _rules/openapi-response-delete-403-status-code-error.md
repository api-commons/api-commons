---
name: OpenAPI Response Delete 403 Status Code Error
description: >-
  DELETE responses should have a 403 forbidden HTTP status code, communicating
  that consumers are not allowed to access
message: DELETE Responses MUST Have 403 Status Codes
given: $.paths.*.delete.responses
severity: error
tags:
  - OpenAPI
  - Responses
  - DELETE
  - 4xx
view_sort: F
guidance: Errors
guidanceUrl: https://guidance.apievangelist.com/errors
rule:
  openapi-response-delete-403-status-code-error:
    description: >-
      DELETE responses should have a 403 forbidden HTTP status code,
      communicating that consumers are not allowed to access
    message: DELETE Responses MUST Have 403 Status Codes
    severity: error
    given: $.paths.*.delete.responses
    then:
      field: '403'
      function: truthy
slug: openapi-response-delete-403-status-code-error
---