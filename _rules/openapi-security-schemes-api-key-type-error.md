---
name: OpenAPI Security Schemes API Keys Type Error
description: >-
  Having components security schemes which possesses an api-key property that allows to configure how API keys are applied to operations have a type of apiKey set.
message: Components MUST Have a Security Schemes API Keys 
given: $.components
severity: error
tags:
  - OpenAPI
  - Security
  - Default
view_sort: A
guidance: Security
guidanceUrl: https://guidance.apievangelist.com/security
rule:
  openapi-security-schemes-api-key-type-error:
    description: >-
      Having components security schemes which possesses an api-key property that allows to configure how API keys are applied to operations have a type of apiKey set.
    message: Components MUST Have a Security Schemes API Keys Type
    severity: error
    given: $.components.securitySchemes.apiKeys
    then:
      - field: type
        function: pattern
        functionOptions:
          match: >-
            \b(apiKey)\b
slug: openapi-security-schemes-api-key-type-error
---