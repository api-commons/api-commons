---
name: OpenAPI Request Bodies Description Info
description: >-
  It is helpful to provide a description for request bodies, providing a simple
  explanation of what can be configured as part of the request payload
message: Request Bodies Have a Description
given: $.paths.*.requestBody
severity: info
tags:
  - OpenAPI
  - Request Bodies
  - Metadata  
view_sort: F
guidance: OpenAPI
guidanceUrl: https://guidance.apievangelist.com/openapi
rule:
  openapi-request-bodies-description-info:
    description: >-
      It is helpful to provide a description for request bodies, providing a
      simple explanation of what can be configured as part of the request
      payload
    message: Request Bodies Have a Description
    severity: info
    given: $.paths.*.requestBody
    then:
      field: description
      function: falsy
slug: openapi-request-bodies-description-info
---