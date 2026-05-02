---
slug: owasp-api8-2023-define-cors-origin-error
icon: globe
name: OWASP API8 2023 Define CORS Origin
description: >-
  Setting up CORS headers will control which websites can make browser-based HTTP
  requests to your API. The Access-Control-Allow-Origin header should be defined
  on all responses.
message: Header Access-Control-Allow-Origin should be defined on all responses.
given: $.paths[*][*].responses[*].headers
severity: error
view_sort: B
tags:
  - OWASP
  - Security
  - CORS
  - Headers
  - OpenAPI
guidance: Security
guidanceUrl: https://guidance.apievangelist.com/security
rule:
  owasp-api8-2023-define-cors-origin-error:
    description: >-
      Setting up CORS headers will control which websites can make browser-based HTTP
      requests to your API. The Access-Control-Allow-Origin header should be defined
      on all responses.
    message: Header Access-Control-Allow-Origin should be defined on all responses.
    given: $.paths[*][*].responses[*].headers
    severity: error
    then:
      field: Access-Control-Allow-Origin
      function: truthy
---
