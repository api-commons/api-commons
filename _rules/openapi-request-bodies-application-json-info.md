---
name: OpenAPI Request Body Have Application Json Info
description: >-
  Request bodies use the application/json media type to encode the request
  payload is a common data format
message: Request Body Application JSON
given: $.paths.*.*.requestBody.content
severity: info
tags:
  - OpenAPI
  - Request Bodies
  - Media Types  
view_sort: I
guidance: OpenAPI
guidanceUrl: https://guidance.apievangelist.com/openapi
rule:
  openapi-request-bodies-application-json-info:
    description: >-
      Request bodies use the application/json media type to encode the request
      payload is a common data format
    message: Request Body Application JSON
    given: $.paths.*.*.requestBody.content
    severity: info
    then:
      field: application/json
      function: falsy
slug: openapi-request-bodies-application-json-info
---