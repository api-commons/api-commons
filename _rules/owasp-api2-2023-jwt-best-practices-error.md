---
slug: owasp-api2-2023-jwt-best-practices-error
icon: lock
name: OWASP API2 2023 JWT Best Practices
description: >-
  JSON Web Token implementations must explicitly declare support for RFC8725
  to address common pitfalls like ignoring algorithms or using insecure
  algorithms in JWT validation.
message: >-
  Security schemes using JWTs must explicitly declare support for RFC8725 in
  the description.
given: >-
  $.components.securitySchemes[?(@.bearerFormat=="jwt" ||
  @.bearerFormat=="JWT")]
severity: error
view_sort: B
tags:
  - OWASP
  - Security
  - JWT
  - Authentication
  - OpenAPI
guidance: Security
guidanceUrl: https://guidance.apievangelist.com/security
rule:
  owasp-api2-2023-jwt-best-practices-error:
    description: >-
      JSON Web Token implementations must explicitly declare support for
      RFC8725 to address common pitfalls like ignoring algorithms or using
      insecure algorithms in JWT validation.
    message: >-
      Security schemes using JWTs must explicitly declare support for RFC8725
      in the description.
    given: >-
      $.components.securitySchemes[?(@.bearerFormat=="jwt" ||
      @.bearerFormat=="JWT")]
    severity: error
    then:
      - field: description
        function: truthy
      - field: description
        function: pattern
        functionOptions:
          match: "RFC8725"
---
