---
slug: owasp-api2-2023-no-credentials-in-url-error
icon: shield
name: OWASP API2 2023 No Credentials in URL
description: >-
  URL parameters MUST NOT contain credentials such as API key, password, or
  secret. This is a security risk as URLs are often logged and cached.
message: Security credentials detected in path parameter.
given: $..parameters[?(@.in.match(/query|path/))].name
severity: error
view_sort: B
tags:
  - OWASP
  - Security
  - Credentials
  - OpenAPI
guidance: Security
guidanceUrl: https://guidance.apievangelist.com/security
rule:
  owasp-api2-2023-no-credentials-in-url-error:
    description: >-
      URL parameters MUST NOT contain credentials such as API key, password,
      or secret. This is a security risk as URLs are often logged and cached.
    message: Security credentials detected in path parameter.
    given: $..parameters[?(@.in.match(/query|path/))].name
    severity: error
    then:
      function: pattern
      functionOptions:
        notMatch: "(?i)(password|secret|token|apikey|api_key|api-key|credential)"
---
