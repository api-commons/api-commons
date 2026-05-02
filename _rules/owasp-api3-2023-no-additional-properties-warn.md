---
slug: owasp-api3-2023-no-additional-properties-warn
icon: shield
name: OWASP API3 2023 No Additional Properties
description: >-
  By default JSON Schema allows additional properties, which can potentially
  lead to mass assignment issues, where unspecified fields are passed to the
  API without validation. Disable them with additionalProperties set to false
  or add maxProperties.
message: If the additionalProperties keyword is used it must be set to false.
given: $..[?(@.type=="object" && @.additionalProperties)]
severity: warn
view_sort: B
tags:
  - OWASP
  - Security
  - Schema
  - OpenAPI
guidance: Security
guidanceUrl: https://guidance.apievangelist.com/security
rule:
  owasp-api3-2023-no-additional-properties-warn:
    description: >-
      By default JSON Schema allows additional properties, which can potentially
      lead to mass assignment issues, where unspecified fields are passed to the
      API without validation. Disable them with additionalProperties set to false
      or add maxProperties.
    message: If the additionalProperties keyword is used it must be set to false.
    given: $..[?(@.type=="object" && @.additionalProperties)]
    severity: warn
    then:
      field: additionalProperties
      function: falsy
---
