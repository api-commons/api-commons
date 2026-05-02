---
name: APIs.json API Properties Sandbox Info
description: >-
  This property ensures that an API has a reference to a sandbox for individual APIs or as part of common properties, providing sandbox, synthetic data, and mock servers for use in making test requests.
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
view_sort: AA
guidance: Environments
guidanceUrl: https://guidance.apievangelist.com/environments
rule:
  apis-json-apis-properties-sandbox-info:
    description: >-
      This property ensures that an API has a reference to a sandbox for individual APIs or as part of common properties, providing sandbox, synthetic data, and mock servers for use in making test requests.
    message: Has a Blog
    severity: info
    given:
      - $.apis.*.properties.*
      - $.common.*
    then:
      - field: type
        function: pattern
        functionOptions:
          notMatch: \b(sandbox|Sandbox)\b
slug: apis-json-apis-properties-sandbox-info
---