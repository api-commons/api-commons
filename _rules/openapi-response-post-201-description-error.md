---
name: OpenAPI Response Post 201 Description Error
description: >-
  POST 201 success HTTP status codes should have a description, describing what
  an API consumer can expect as a result
message: POST 201 Responses MUST Have Description
given: $.paths.*.post.responses.201
severity: error
tags:
  - OpenAPI
  - Responses
  - POST
  - 2xx
view_sort: C
guidance: Errors
guidanceUrl: https://guidance.apievangelist.com/errors
rule:
  openapi-response-post-201-description-error:
    description: >-
      POST 201 success HTTP status codes should have a description, describing
      what an API consumer can expect as a result
    message: POST 201 Responses MUST Have Description
    severity: error
    given: $.paths.*.post.responses.201
    then:
      field: description
      function: truthy
slug: openapi-response-post-201-description-error
---