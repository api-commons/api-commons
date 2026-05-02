---
slug: owasp-api4-2023-string-limit-error
icon: text
name: OWASP API4 2023 String Limit
description: >-
  String size should be limited to mitigate resource exhaustion attacks. This
  can be done using maxLength, enum, or const.
message: Schema of type string must specify maxLength, enum, or const.
given: $..[?(@.type=="string")]
severity: error
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
  owasp-api4-2023-string-limit-error:
    description: >-
      String size should be limited to mitigate resource exhaustion attacks. This
      can be done using maxLength, enum, or const.
    message: Schema of type string must specify maxLength, enum, or const.
    given: $..[?(@.type=="string")]
    severity: error
    then:
      function: schema
      functionOptions:
        schema:
          anyOf:
            - required: ["maxLength"]
            - required: ["enum"]
            - required: ["const"]
---
