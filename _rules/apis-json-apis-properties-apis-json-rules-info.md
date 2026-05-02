---
name: APIs.json Apis Properties Apis Json Rules Info
description: This property ensures that an API has operational level rules for APIs
message: Has Operational Rules
given:
  - $.apis.*.properties.*
  - $.common.*
severity: info
tags:
  - APIs.json
  - APIs
  - Properties
guidance: API Governance Rules
guidanceUrl: https://guidance.apievangelist.com/rules
rule:
  apis-json-apis-properties-apis-json-rules-info:
    description: This property ensures that an API has operational level rules for APIs
    message: Has Operational Rules
    severity: info
    given:
      - $.apis.*.properties.*
      - $.common.*
    then:
      - field: type
        function: pattern
        functionOptions:
          notMatch: \b(operational-rules|OperationalRules)\b
slug: apis-json-apis-properties-apis-json-rules-info
---