---
slug: owasp-api4-2023-integer-limit-error
icon: hash
name: OWASP API4 2023 Integer Limit
description: >-
  Integers should be limited to mitigate resource exhaustion attacks. This
  can be done using minimum and maximum, which helps avoid negative numbers
  when positive are expected, or reducing unreasonable iterations.
message: Schema of type integer must specify minimum and maximum.
given: $..[?(@.type=="integer")]
severity: error
view_sort: B
tags:
  - OWASP
  - Security
  - Schema
  - Integers
  - OpenAPI
guidance: Security
guidanceUrl: https://guidance.apievangelist.com/security
rule:
  owasp-api4-2023-integer-limit-error:
    description: >-
      Integers should be limited to mitigate resource exhaustion attacks. This
      can be done using minimum and maximum, which helps avoid negative numbers
      when positive are expected, or reducing unreasonable iterations.
    message: Schema of type integer must specify minimum and maximum.
    given: $..[?(@.type=="integer")]
    severity: error
    then:
      - field: minimum
        function: defined
      - field: maximum
        function: defined
---
