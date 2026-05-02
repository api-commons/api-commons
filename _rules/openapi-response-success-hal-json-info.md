---
slug: openapi-response-success-hal-json-info
icon: file-text
name: OpenAPI Response Success HAL JSON
description: >-
  Success responses (2XX excluding 204) should use application/hal+json media type to provide hypermedia links that enable clients to discover related resources and actions, following the HAL specification.
message: Success responses SHOULD use application/hal+json media type.
given: "$.paths[*][*].responses[?(@property.match(/^2/) && @property != '204')].content"
severity: info
view_sort: B
tags:
  - OpenAPI
  - Responses
  - HAL
  - Hypermedia
guidance: Errors
guidanceUrl: https://guidance.apievangelist.com/errors
rule:
  openapi-response-success-hal-json-info:
    description: >-
      Success responses (2XX excluding 204) should use application/hal+json media type to provide hypermedia links that enable clients to discover related resources and actions, following the HAL specification.
    message: Success responses SHOULD use application/hal+json media type.
    given: "$.paths[*][*].responses[?(@property.match(/^2/) && @property != '204')].content"
    severity: info
    then:
      field: application/hal+json
      function: truthy
---
