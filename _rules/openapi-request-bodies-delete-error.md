---
name: OpenAPI No Request Body On Delete Error
description: >-
  DELETE HTTP methods should not have a request body, keeping API requests
  compliant with the HTTP standard
message: DELETE Request Body
given: $.paths.*.delete
severity: error
tags:
  - OpenAPI
  - Request Bodies
  - DELETE  
  - Default
view_sort: E
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
  openapi-request-bodies-delete-error:
    description: >-
      DELETE HTTP methods should not have a request body, keeping API requests
      compliant with the HTTP standard
    message: DELETE Request Body
    given: $.paths.*.delete
    severity: error
    then:
      field: requestBody
      function: falsy
slug: openapi-request-bodies-delete-error
---