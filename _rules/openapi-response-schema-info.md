---
name: OpenAPI Response Schemas Info
description: >-
  Have schemas to show one or many schemas
  of responses for different types of API requests
message: ResponseHas Schemas
given: $.paths.*.get.responses.200.content['application/json']
severity: info
tags:
  - OpenAPI
  - Responses
  - Schemas
view_sort: D
guidance: Errors
guidanceUrl: https://guidance.apievangelist.com/errors
rule:
  openapi-response-schemas-info:
    description: >-
      Have schemas to show one or many
      schemas of responses for different types of API requests
    message: ResponseHas Schemas
    severity: info
    given: $.paths.*.get.responses.*.*.*
    then:
      field: schemas
      function: falsy
slug: openapi-response-schemas-info
---