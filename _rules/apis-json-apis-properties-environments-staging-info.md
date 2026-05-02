---
name: APIs.json Apis Properties Environments Staging Info
description: >-
  This property ensures that there is a staging environment available for an
  API, providing base URL, tokens, keys, and other key / value pairs that are
  needed to integrate with an API
message: Has a Stage Environment
given:
  - $.apis.*.properties.*
  - $.common.*
severity: info
tags:
  - APIs.json
  - APIs
  - Properties
  - Additional
view_sort: JA
guidance: Environments
guidanceUrl: https://guidance.apievangelist.com/environments
rule:
  apis-json-apis-properties-environments-staging-info:
    description: >-
      This property ensures that there is a staging environment available for an
      API, providing base URL, tokens, keys, and other key / value pairs that
      are needed to integrate with an API
    message: Has a Stage Environment
    severity: info
    given:
      - $.apis.*.properties.*
      - $.common.*
    then:
      - field: type
        function: pattern
        functionOptions:
          notMatch: \b(StagingEnvironment)\b
slug: apis-json-apis-properties-environments-staging-info
---