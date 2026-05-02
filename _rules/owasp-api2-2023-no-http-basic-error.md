---
slug: owasp-api2-2023-no-http-basic-error
icon: lock
name: OWASP API2 2023 No HTTP Basic
description: >-
  Basic authentication credentials transported over network are more
  susceptible to interception than other forms of authentication, and as they
  are not encrypted it means passwords and tokens are more easily leaked.
message: >-
  Security scheme uses HTTP Basic. Use a more secure authentication method,
  like OAuth 2 or OpenID.
given: $.components.securitySchemes[*]
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
  owasp-api2-2023-no-http-basic-error:
    description: >-
      Basic authentication credentials transported over network are more
      susceptible to interception than other forms of authentication, and as
      they are not encrypted it means passwords and tokens are more easily
      leaked.
    message: >-
      Security scheme uses HTTP Basic. Use a more secure authentication
      method, like OAuth 2 or OpenID.
    given: $.components.securitySchemes[*]
    severity: error
    then:
      field: scheme
      function: pattern
      functionOptions:
        notMatch: "basic"
---
