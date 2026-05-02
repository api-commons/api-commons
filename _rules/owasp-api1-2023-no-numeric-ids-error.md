---
slug: owasp-api1-2023-no-numeric-ids-error
icon: fingerprint
name: OWASP API1 2023 No Numeric IDs
description: >-
  Use random IDs that cannot be guessed. UUIDs are preferred but any other
  random string will do. Using numeric IDs can lead to enumeration attacks
  where attackers iterate through possible ID values.
message: Use random IDs that cannot be guessed, UUIDs are preferred.
given: $.paths..parameters[*]
severity: error
view_sort: B
tags:
  - OWASP
  - Security
  - Identifiers
  - OpenAPI
guidance: Security
guidanceUrl: https://guidance.apievangelist.com/security
rule:
  owasp-api1-2023-no-numeric-ids-error:
    description: >-
      Use random IDs that cannot be guessed. UUIDs are preferred but any other
      random string will do. Using numeric IDs can lead to enumeration attacks
      where attackers iterate through possible ID values.
    message: Use random IDs that cannot be guessed, UUIDs are preferred.
    given: $.paths..parameters[*]
    severity: error
    then:
      field: schema.type
      function: pattern
      functionOptions:
        notMatch: "^integer$"
---
