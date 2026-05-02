---
name: OpenAPI Response Delete 401 Status Code Error
description: >-
  DELETE responses should have a 401 unauthorized HTTP status code,
  communicating that consumers do not have access
message: DELETE Responses MUST Have 401 Status Codes
given: $.paths.*.delete.responses
severity: error
tags:
  - OpenAPI
  - Responses
  - DELETE
  - 4xx
view_sort: D
guidance: Errors
guidanceUrl: https://guidance.apievangelist.com/errors
rule:
  openapi-response-delete-401-status-code-error:
    description: >-
      DELETE responses should have a 401 unauthorized HTTP status code,
      communicating that consumers do not have access
    message: DELETE Responses MUST Have 401 Status Codes
    severity: error
    given: $.paths.*.delete.responses
    then:
      field: '401'
      function: truthy
slug: openapi-response-delete-401-status-code-error
---