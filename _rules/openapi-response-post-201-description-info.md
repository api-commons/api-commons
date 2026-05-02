---
name: OpenAPI Response Post 201 Description Info
description: >-
  POST 201 success HTTP status codes should have a description, describing what
  an API consumer can expect as a result
message: POST 201 Responses Has Description
given: $.paths.*.post.responses.201
severity: info
tags:
  - OpenAPI
  - Responses
  - POST
  - 2xx
view_sort: C
guidance: Errors
guidanceUrl: https://guidance.apievangelist.com/errors
rule:
  openapi-response-post-201-description-info:
    description: >-
      POST 201 success HTTP status codes should have a description, describing
      what an API consumer can expect as a result
    message: POST 201 Responses Has Description
    severity: info
    given: $.paths.*.post.responses.201
    then:
      field: description
      function: falsy
slug: openapi-response-post-201-description-info
---