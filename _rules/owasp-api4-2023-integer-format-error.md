---
slug: owasp-api4-2023-integer-format-error
icon: hash
name: OWASP API4 2023 Integer Format
description: >-
  Integers should be limited to mitigate resource exhaustion attacks.
  Specifying whether int32 or int64 is expected via format helps enforce
  proper constraints.
message: Schema of type integer must specify format (int32 or int64).
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
  owasp-api4-2023-integer-format-error:
    description: >-
      Integers should be limited to mitigate resource exhaustion attacks.
      Specifying whether int32 or int64 is expected via format helps enforce
      proper constraints.
    message: Schema of type integer must specify format (int32 or int64).
    given: $..[?(@.type=="integer")]
    severity: error
    then:
      field: format
      function: truthy
---
