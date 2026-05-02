---
slug: owasp-api2-2023-read-restricted-warn
icon: lock
name: OWASP API2 2023 Read Restricted
description: >-
  Read operations (GET, HEAD) should be secured by at least one security
  scheme to prevent unauthorized access to sensitive data.
message: This read operation is not protected by any security scheme.
given: $.paths[*][get,head]
severity: warn
view_sort: B
tags:
  - OWASP
  - Security
  - Operations
  - OpenAPI
guidance: Security
guidanceUrl: https://guidance.apievangelist.com/security
rule:
  owasp-api2-2023-read-restricted-warn:
    description: >-
      Read operations (GET, HEAD) should be secured by at least one security
      scheme to prevent unauthorized access to sensitive data.
    message: This read operation is not protected by any security scheme.
    given: $.paths[*][get,head]
    severity: warn
    then:
      field: security
      function: truthy
---
