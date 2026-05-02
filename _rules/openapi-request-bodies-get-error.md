---
name: OpenAPI No Request Body On Get Error
description: >-
  GET HTTP methods should not have a request body, keeping API requests
  compliant with the HTTP standard
message: GET Request Body
given: $.paths.*.get
severity: error
tags:
  - OpenAPI
  - Request Bodies
  - GET  
  - Default
view_sort: A
references:
  - name: Doctor
    type: Editor
    url: https://pb33f.io/doctor/
  - name: Spectral
    type: Linter
    url: https://github.com/stoplightio/spectral/blob/develop/packages/rulesets/src/oas/index.ts  
guidance: OpenAPI
guidanceUrl: https://guidance.apievangelist.com/openapi
rule:
  openapi-request-bodies-get-error:
    description: >-
      GET HTTP methods should not have a request body, keeping API requests
      compliant with the HTTP standard
    message: GET Request Body
    given: $.paths.*.get
    severity: error
    then:
      field: requestBody
      function: falsy
slug: openapi-request-bodies-get-error
---