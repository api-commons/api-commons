---
slug: owasp-api4-2023-string-restricted-warn
icon: text
name: OWASP API4 2023 String Restricted
description: >-
  To avoid unexpected values being sent or leaked, strings should have a
  format, RegEx pattern, enum, or const to restrict the possible values.
message: Schema of type string should specify a format, pattern, enum, or const.
given: $..[?(@.type=="string")]
severity: warn
view_sort: B
tags:
  - OWASP
  - Security
  - Schema
  - Strings
  - OpenAPI
guidance: Security
guidanceUrl: https://guidance.apievangelist.com/security
rule:
  owasp-api4-2023-string-restricted-warn:
    description: >-
      To avoid unexpected values being sent or leaked, strings should have a
      format, RegEx pattern, enum, or const to restrict the possible values.
    message: Schema of type string should specify a format, pattern, enum, or const.
    given: $..[?(@.type=="string")]
    severity: warn
    then:
      function: schema
      functionOptions:
        schema:
          anyOf:
            - required: ["format"]
            - required: ["pattern"]
            - required: ["enum"]
            - required: ["const"]
---
