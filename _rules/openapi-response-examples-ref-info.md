---
name: OpenAPI Response Examples Ref Info
description: >-
  Have example references to show one or many
  examples of responses for different types of API requests
message: Responses Uses Examples Reference
given: $.paths.*.get.responses.200.content['application/json'].examples.*
severity: info
tags:
  - OpenAPI
  - Responses
  - Examples
view_sort: E
guidance: Errors
guidanceUrl: https://guidance.apievangelist.com/errors
rule:
  openapi-response-examples-ref-info:
    description: >-
      Have example references to show one or
      many examples of responses for different types of API requests
    message: Responses Uses Examples Reference
    severity: info
    given: $.paths.*.get.responses.*.*.*.examples.*
    then:
      field: $ref
      function: truthy
slug: openapi-response-examples-ref-error
---