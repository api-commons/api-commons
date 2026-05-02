---
slug: owasp-api2-2023-no-api-keys-in-url-error
icon: key
name: OWASP API2 2023 No API Keys in URL
description: >-
  API Keys are passed in headers, cookies or query parameters to access APIs.
  Those keys can be eavesdropped, especially when they are passed in the URL
  as logging or history tools will keep track of them and potentially expose
  them.
message: API Key MUST NOT be passed in URL (path or query parameters).
given: $.components.securitySchemes[?(@.type=="apiKey")].in
severity: error
view_sort: B
tags:
  - OWASP
  - Security
  - API Keys
  - OpenAPI
guidance: Security
guidanceUrl: https://guidance.apievangelist.com/security
rule:
  owasp-api2-2023-no-api-keys-in-url-error:
    description: >-
      API Keys are passed in headers, cookies or query parameters to access
      APIs. Those keys can be eavesdropped, especially when they are passed
      in the URL as logging or history tools will keep track of them and
      potentially expose them.
    message: API Key MUST NOT be passed in URL (path or query parameters).
    given: $.components.securitySchemes[?(@.type=="apiKey")].in
    severity: error
    then:
      function: pattern
      functionOptions:
        notMatch: "^(path|query)$"
---
