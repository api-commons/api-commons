---
name: OpenAPI Response Put 403 Schema Ref Info
description: >-
  PUT 403 forbidden HTTP status codes have a schema references to standardize
  the response payload returned for the error response
message: PUT 403 Responses Uses Schema Reference
given: $.paths.*.put.responses.403
severity: info
tags:
  - OpenAPI
  - Responses
  - PUT
  - 4xx
  - Schema
view_sort: G
guidance: Errors
guidanceUrl: https://guidance.apievangelist.com/errors
rule:
  openapi-response-put-403-schema-ref-info:
    description: >-
      PUT 403 forbidden HTTP status codes have a schema references to
      standardize the response payload returned for the error response
    message: PUT 403 Responses Uses Schema Reference
    severity: info
    given: $.paths.*.put.responses.403
    then:
      field: $ref
      function: truthy
slug: openapi-response-put-403-schema-ref-info
---