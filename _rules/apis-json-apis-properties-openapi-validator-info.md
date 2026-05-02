---
name: APIs.json Apis Properties OpenAPI Validator Info
description: >-
  This property ensures that there is a link to the validator for the OpenAPI
  technical contract, allowing anyone to see the details of governance being
  applied
message: Has OpenAPI (Technical) Validator
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
  apis-json-apis-properties-openapi-validator-info:
    description: >-
      This property ensures that there is a link to the validator for the
      OpenAPI technical contract, allowing anyone to see the details of
      governance being applied
    message: Has OpenAPI (Technical) Validator
    severity: info
    given:
      - $.apis.*.properties.*
      - $.common.*
    then:
      - field: type
        function: pattern
        functionOptions:
          notMatch: \b(APIValidation)\b
slug: apis-json-apis-properties-openapi-validator-info
---