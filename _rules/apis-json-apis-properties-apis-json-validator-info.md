---
name: APIs.json Apis Properties Apis Json Validator Info
description: This property ensures that there is a link to the validator for the APIs
message: Has APIs.json (Business) Validator
given:
  - $.apis.*.properties.*
  - $.common.*
severity: info
tags:
  - APIs.json
  - APIs
  - Properties
guidance: API Validator
guidanceUrl: https://guidance.apievangelist.com/validator
rule:
  apis-json-apis-properties-apis-json-validator-info:
    description: This property ensures that there is a link to the validator for the APIs
    message: Has APIs.json (Business) Validator
    severity: info
    given:
      - $.apis.*.properties.*
      - $.common.*
    then:
      - field: type
        function: pattern
        functionOptions:
          notMatch: \b(OperationalValidation)\b
slug: apis-json-apis-properties-apis-json-validator-info
---