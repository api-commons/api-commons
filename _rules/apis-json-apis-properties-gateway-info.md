---
name: APIs.json Apis Properties Gateway Info
description: >-
  This property ensures that there is a reference to the gateway for an API,
  referencing where you can manage the configuration for each API
message: Has Staging Gateway for API
given:
  - $.apis.*.properties.*
  - $.common.*
severity: info
tags:
  - APIs.json
  - APIs
  - Properties
guidance: Gateways
guidanceUrl: https://guidance.apievangelist.com/gateways
rule:
  apis-json-apis-properties-gateway-info:
    description: >-
      This property ensures that there is a reference to the gateway for an API,
      referencing where you can manage the configuration for each API
    message: Has Staging Gateway for API
    severity: info
    given:
      - $.apis.*.properties.*
      - $.common.*
    then:
      - field: type
        function: pattern
        functionOptions:
          notMatch: \b(gateway|Gateway)\b
slug: apis-json-apis-properties-gateway-info
---