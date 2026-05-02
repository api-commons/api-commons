---
name: OpenAPI Request Body Have Application X Www Form Url Encoded Info
description: >-
  Request bodies use the application/x-www-form-urlencoded media type to encode
  the request payload is a common data format
message: Request Body Application X WWW Form URL Encoded
given: $.paths.*.*.requestBody.content
severity: info
tags:
  - OpenAPI
  - Request Bodies
  - Media Types  
view_sort: J
guidance: OpenAPI
guidanceUrl: https://guidance.apievangelist.com/openapi
rule:
  openapi-request-bodies-application-x-www-form-url-encoded-info:
    description: >-
      Request bodies use the application/x-www-form-urlencoded media type to
      encode the request payload is a common data format
    message: Request Body Application X WWW Form URL Encoded
    given: $.paths.*.*.requestBody.content
    severity: info
    then:
      field: application/x-www-form-urlencoded
      function: falsy
slug: openapi-request-bodies-application-x-www-form-url-encoded-info
---