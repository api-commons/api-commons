---
slug: owasp-api2-2023-auth-insecure-schemes-error
icon: shield
name: OWASP API2 2023 Auth Insecure Schemes
description: >-
  There are many HTTP authorization schemes but some of them are now
  considered insecure, such as negotiating authentication using
  specifications like NTLM or OAuth v1.
message: Authentication scheme is considered outdated or insecure.
given: $.components.securitySchemes[?(@.type=="http")].scheme
severity: error
view_sort: B
tags:
  - OWASP
  - Security
  - Authentication
  - OpenAPI
guidance: Security
guidanceUrl: https://guidance.apievangelist.com/security
rule:
  owasp-api2-2023-auth-insecure-schemes-error:
    description: >-
      There are many HTTP authorization schemes but some of them are now
      considered insecure, such as negotiating authentication using
      specifications like NTLM or OAuth v1.
    message: Authentication scheme is considered outdated or insecure.
    given: $.components.securitySchemes[?(@.type=="http")].scheme
    severity: error
    then:
      function: pattern
      functionOptions:
        notMatch: "^(negotiate|oauth)$"
---
