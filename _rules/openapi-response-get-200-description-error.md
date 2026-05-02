---
name: OpenAPI Response Get 200 Description Error
description: >-
  GET 200 success HTTP status codes should have a description, describing what
  an API consumer can expect as a result
message: GET 200 Response MUST have description.
given: $.paths.*.get.responses.200
severity: error
tags:
  - OpenAPI
  - Responses
  - GET
  - 2xx
view_sort: B
guidance: Errors
guidanceUrl: https://guidance.apievangelist.com/errors
rule:
  openapi-response-get-200-description-error:
    description: >-
      GET 200 success HTTP status codes should have a description, describing
      what an API consumer can expect as a result
    message: GET 200 Response MUST have description.
    severity: error
    given: $.paths.*.get.responses.200
    then:
      field: description
      function: truthy
slug: openapi-response-get-200-description-error
---