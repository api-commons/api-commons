---
name: OpenAPI Response Schemas Ref Error
description: >-
  Have example references to show one or many
  schemas of responses for different types of API requests
message: Responses MUST Use Schemas Reference
given: $.paths.*.get.responses.200.content['application/json'].schemas.*
severity: error
tags:
  - OpenAPI
  - Responses
  - Schemas
view_sort: E
guidance: Errors
guidanceUrl: https://guidance.apievangelist.com/errors
rule:
  openapi-response-schemas-ref-error:
    description: >-
      Have example references to show one or
      many schemas of responses for different types of API requests
    message: Responses MUST Use Schemas Reference
    severity: error
    given: $.paths.*.get.responses.*.*.*.schemas.*
    then:
      field: $ref
      function: falsy
slug: openapi-response-schemas-ref-error
---