---
slug: owasp-api2-2023-write-restricted-error
icon: lock
name: OWASP API2 2023 Write Restricted
description: >-
  All write operations (POST, PUT, PATCH, DELETE) must be secured by at least
  one security scheme to prevent unauthorized modifications.
message: This write operation is not protected by any security scheme.
given: $.paths[*][post,put,patch,delete]
severity: error
view_sort: B
tags:
  - OWASP
  - Security
  - Operations
  - OpenAPI
guidance: Security
guidanceUrl: https://guidance.apievangelist.com/security
rule:
  owasp-api2-2023-write-restricted-error:
    description: >-
      All write operations (POST, PUT, PATCH, DELETE) must be secured by at
      least one security scheme to prevent unauthorized modifications.
    message: This write operation is not protected by any security scheme.
    given: $.paths[*][post,put,patch,delete]
    severity: error
    then:
      field: security
      function: truthy
---
