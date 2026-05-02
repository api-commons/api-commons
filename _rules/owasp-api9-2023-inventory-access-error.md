---
slug: owasp-api9-2023-inventory-access-error
icon: server
name: OWASP API9 2023 Inventory Access
description: >-
  Servers should use the x-internal vendor extension set to true or false to
  explicitly declare the intended audience for the API, which will be picked up
  by most documentation tools.
message: Declare intended audience of every server by defining x-internal as true or false.
given: $.servers.*
severity: error
view_sort: B
tags:
  - OWASP
  - Security
  - Servers
  - Inventory
  - OpenAPI
guidance: Security
guidanceUrl: https://guidance.apievangelist.com/security
rule:
  owasp-api9-2023-inventory-access-error:
    description: >-
      Servers should use the x-internal vendor extension set to true or false to
      explicitly declare the intended audience for the API, which will be picked up
      by most documentation tools.
    message: Declare intended audience of every server by defining x-internal as true or false.
    given: $.servers.*
    severity: error
    then:
      field: x-internal
      function: defined
---
