---
name: OpenAPI Response Schemas Ref Info
description: >-
  Have example references to show one or many
  schemas of responses for different types of API requests
message: Responses Uses Schemas Reference
given: $.paths.*.get.responses.200.content['application/json'].schemas.*
severity: info
tags:
  - OpenAPI
  - Responses
  - Schemas
view_sort: E
guidance: Errors
guidanceUrl: https://guidance.apievangelist.com/errors
rule:
  openapi-response-schemas-ref-info:
    description: >-
      Have example references to show one or
      many schemas of responses for different types of API requests
    message: Responses Uses Schemas Reference
    severity: info
    given: $.paths.*.get.responses.*.*.*.schemas.*
    then:
      field: $ref
      function: truthy
slug: openapi-response-schemas-ref-error
---