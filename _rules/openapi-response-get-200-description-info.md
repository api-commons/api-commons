---
name: OpenAPI Response Get 200 Description Info
description: >-
  GET 200 success HTTP status codes should have a description, describing what
  an API consumer can expect as a result
message: GET 200 Response has description.
given: $.paths.*.get.responses.200
severity: info
tags:
  - OpenAPI
  - Responses
  - GET
  - 2xx
view_sort: B
guidance: Errors
guidanceUrl: https://guidance.apievangelist.com/errors
rule:
  openapi-response-get-200-description-info:
    description: >-
      GET 200 success HTTP status codes should have a description, describing
      what an API consumer can expect as a result
    message: GET 200 Response has description.
    severity: info
    given: $.paths.*.get.responses.200
    then:
      field: description
      function: falsy
slug: openapi-response-get-200-description-info
---