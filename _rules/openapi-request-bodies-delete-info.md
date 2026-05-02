---
name: OpenAPI No Request Body On Delete Info
description: >-
  DELETE HTTP methods should not have a request body, keeping API requests
  compliant with the HTTP standard
message: DELETE Request Body
given: $.paths.*.delete
severity: info
tags:
  - OpenAPI
  - Request Bodies
  - DELETE  
  - Default
view_sort: E
guidance: OpenAPI
guidanceUrl: https://guidance.apievangelist.com/openapi
rule:
  openapi-request-bodies-delete-info:
    description: >-
      DELETE HTTP methods should not have a request body, keeping API requests
      compliant with the HTTP standard
    message: DELETE Request Body
    given: $.paths.*.delete
    severity: info
    then:
      field: requestBody
      function: truthy
slug: openapi-request-bodies-delete-info
---