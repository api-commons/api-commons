---
slug: openapi-response-error-problem-json-info
icon: alert-circle
name: OpenAPI Response Error Problem JSON
description: >-
  Error responses (4XX and 5XX) should use application/problem+json media type as defined in RFC 7807, providing a consistent, machine-readable format for conveying error details to API consumers.
message: Error responses SHOULD use application/problem+json media type (RFC 7807).
given: "$.paths[*][*].responses[?(@property.match(/^(4|5)/))].content"
severity: info
view_sort: B
tags:
  - OpenAPI
  - Responses
  - Errors
  - Problem JSON
guidance: Errors
guidanceUrl: https://guidance.apievangelist.com/errors
rule:
  openapi-response-error-problem-json-info:
    description: >-
      Error responses (4XX and 5XX) should use application/problem+json media type as defined in RFC 7807, providing a consistent, machine-readable format for conveying error details to API consumers.
    message: Error responses SHOULD use application/problem+json media type (RFC 7807).
    given: "$.paths[*][*].responses[?(@property.match(/^(4|5)/))].content"
    severity: info
    then:
      field: application/problem+json
      function: truthy
---
