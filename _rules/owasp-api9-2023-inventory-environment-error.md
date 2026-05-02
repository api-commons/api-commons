---
slug: owasp-api9-2023-inventory-environment-error
icon: server
name: OWASP API9 2023 Inventory Environment
description: >-
  Make it clear which servers are expected to run in which environment to avoid
  unexpected problems, exposing test data to the public, or letting bad actors
  bypass security measures to reach production-like environments.
message: Declare intended environment in server descriptions using terms like local, staging, or production.
given: $.servers.*.description
severity: error
view_sort: B
tags:
  - OWASP
  - Security
  - Servers
  - Inventory
  - OpenAPI
guidance: Environments
guidanceUrl: https://guidance.apievangelist.com/environments
rule:
  owasp-api9-2023-inventory-environment-error:
    description: >-
      Make it clear which servers are expected to run in which environment to avoid
      unexpected problems, exposing test data to the public, or letting bad actors
      bypass security measures to reach production-like environments.
    message: Declare intended environment in server descriptions using terms like local, staging, or production.
    given: $.servers.*.description
    severity: error
    then:
      function: pattern
      functionOptions:
        match: "(?i)(local|sandbox|staging|production|development|test)"
---
