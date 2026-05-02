---
name: OpenAPI Security Schemes API Keys Type Info
description: >-
  Having components security schemes which possesses an api-key property that allows to configure how API keys are applied to operations have a type of apiKey set.
message: Components Have a Security Schemes
given: $.components
severity: info
tags:
  - OpenAPI
  - Security
  - Default
view_sort: A
guidance: Security
guidanceUrl: https://guidance.apievangelist.com/security
rule:
  openapi-security-schemes-api-key-type-info:
    description: >-
      Having components security schemes which possesses an api-key property that allows to configure how API keys are applied to operations have a type of apiKey set.
    message: Components Have a Security Schemes API Keys Type
    severity: info
    given: $.components.securitySchemes.apiKeys
    then:
      - field: type
        function: pattern
        functionOptions:
          notMatch: >-
            \b(apiKey)\b
slug: openapi-security-schemes-api-key-type-info
---