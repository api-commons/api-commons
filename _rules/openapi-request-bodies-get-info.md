---
name: OpenAPI No Request Body On Get Info
description: >-
  GET HTTP methods should not have a request body, keeping API requests
  compliant with the HTTP standard
message: GET Request Body
given: $.paths.*.get
severity: info
tags:
  - OpenAPI
  - Request Bodies
  - GET  
  - Default
view_sort: A
guidance: OpenAPI
guidanceUrl: https://guidance.apievangelist.com/openapi
rule:
  openapi-request-bodies-get-info:
    description: >-
      GET HTTP methods should not have a request body, keeping API requests
      compliant with the HTTP standard
    message: GET Request Body
    given: $.paths.*.get
    severity: info
    then:
      field: requestBody
      function: truthy
slug: openapi-request-bodies-get-info
---