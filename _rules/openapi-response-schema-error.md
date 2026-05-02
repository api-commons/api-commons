---
name: OpenAPI Response Schemas Error
description: >-
  Have schemas to show one or many schemas
  of responses for different types of API requests
message: Response MUST Have Schemas
given: $.paths.*.get.responses.200.content['application/json']
severity: error
tags:
  - OpenAPI
  - Responses
  - Schemas
view_sort: D
guidance: Errors
guidanceUrl: https://guidance.apievangelist.com/errors
rule:
  openapi-response-schemas-error:
    description: >-
      Have schemas to show one or many
      schemas of responses for different types of API requests
    message: Response MUST Have Schemas
    severity: error
    given: $.paths.*.get.responses.*.*.*
    then:
      field: schemas
      function: truthy
slug: openapi-response-schemas-error
---