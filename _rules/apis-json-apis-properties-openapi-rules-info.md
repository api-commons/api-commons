---
name: APIs.json Apis Properties OpenAPI Rules Info
description: >-
  This property ensures that an OpenAPI has support governance rules, that can
  be applied during design time via editors, development time via IDE, and
  run-time via CI/CD pipelines
message: Has API Rules
given:
  - $.apis.*.properties.*
  - $.common.*
severity: info
tags:
  - APIs.json
  - APIs
  - Properties
guidance: OpenAPI
guidanceUrl: https://guidance.apievangelist.com/openapi
rule:
  apis-json-apis-properties-openapi-rules-info:
    description: >-
      This property ensures that an OpenAPI has support governance rules, that
      can be applied during design time via editors, development time via IDE,
      and run-time via CI/CD pipelines
    message: Has API Rules
    severity: info
    given:
      - $.apis.*.properties.*
      - $.common.*
    then:
      - field: type
        function: pattern
        functionOptions:
          notMatch: \b(api-rules|ApiRules)\b
slug: apis-json-apis-properties-openapi-rules-info
---