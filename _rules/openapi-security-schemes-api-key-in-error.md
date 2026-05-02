---
name: OpenAPI Security Schemes API Keys In Header Error
description: >-
  Having components security schemes which possesses an api-key property that allows to configure how API keys are applied to operations have a in of header set.
message: Components MUST Have a Security Schemes API Keys In Header
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
  openapi-security-schemes-api-key-in-error:
    description: >-
      Having components security schemes which possesses an api-key property that allows to configure how API keys are applied to operations have a in of header set.
    message: Components MUST Have a Security Schemes API Keys In Header
    severity: error
    given: $.components.securitySchemes.apiKeys
    then:
      - field: in
        function: pattern
        functionOptions:
          match: >-
            \b(header)\b
slug: openapi-security-schemes-api-key-in-error
---