---
slug: owasp-api4-2023-array-limit-error
icon: list
name: OWASP API4 2023 Array Limit
description: >-
  Array size should be limited to mitigate resource exhaustion attacks. This
  can be done using maxItems. You should ensure that the subschema in items
  is constrained too.
message: Schema of type array must specify maxItems.
given: $..[?(@.type=="array")]
severity: error
view_sort: B
tags:
  - OWASP
  - Security
  - Schema
  - Arrays
  - OpenAPI
guidance: Security
guidanceUrl: https://guidance.apievangelist.com/security
rule:
  owasp-api4-2023-array-limit-error:
    description: >-
      Array size should be limited to mitigate resource exhaustion attacks. This
      can be done using maxItems. You should ensure that the subschema in items
      is constrained too.
    message: Schema of type array must specify maxItems.
    given: $..[?(@.type=="array")]
    severity: error
    then:
      field: maxItems
      function: truthy
---
