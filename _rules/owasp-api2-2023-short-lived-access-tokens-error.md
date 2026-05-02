---
slug: owasp-api2-2023-short-lived-access-tokens-error
icon: clock
name: OWASP API2 2023 Short Lived Access Tokens
description: >-
  Using short-lived access tokens is a good practice. When using OAuth 2,
  this is done by using refresh tokens. If a malicious actor is able to get
  hold of an access token then rotation means that token might not work by
  the time they try to use it.
message: Authentication scheme does not appear to support refresh tokens.
given: >-
  $.components.securitySchemes[?(@.type=="oauth2")].flows[?(@property !=
  "clientCredentials")]
severity: error
view_sort: B
tags:
  - OWASP
  - Security
  - OAuth
  - Tokens
  - OpenAPI
guidance: Security
guidanceUrl: https://guidance.apievangelist.com/security
rule:
  owasp-api2-2023-short-lived-access-tokens-error:
    description: >-
      Using short-lived access tokens is a good practice. When using OAuth 2,
      this is done by using refresh tokens. If a malicious actor is able to
      get hold of an access token then rotation means that token might not
      work by the time they try to use it.
    message: Authentication scheme does not appear to support refresh tokens.
    given: >-
      $.components.securitySchemes[?(@.type=="oauth2")].flows[?(@property !=
      "clientCredentials")]
    severity: error
    then:
      field: refreshUrl
      function: truthy
---
