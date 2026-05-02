---
name: APIs.json API Properties Examples Info
description: >-
  This property ensures that an API has a reference to a examples for individual APIs or as part of common properties, providing examples and synthentic data that can be used for APIs.
message: Has a Blog
given:
  - $.apis.*.properties.*
  - $.common.*
severity: info
tags:
  - APIs.json
  - APIs
  - Properties
  - Sandbox
  - Examples
view_sort: AA
guidance: Documentation
guidanceUrl: https://guidance.apievangelist.com/documentation
rule:
  apis-json-apis-properties-examples-info:
    description: >-
      This property ensures that an API has a reference to a examples for individual APIs or as part of common properties, providing examples and synthentic data that can be used for APIs.
    message: Has a Blog
    severity: info
    given:
      - $.apis.*.properties.*
      - $.common.*
    then:
      - field: type
        function: pattern
        functionOptions:
          notMatch: \b(examples|Examples)\b
slug: apis-json-apis-properties-examples-info
---