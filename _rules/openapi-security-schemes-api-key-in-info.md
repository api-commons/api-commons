---
name: OpenAPI Security Schemes API Keys In Header Info
description: >-
  Having components security schemes which possesses an api-key property that allows to configure how API keys are applied to operations have a in of header set.
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
  openapi-security-schemes-api-key-in-info:
    description: >-
      Having components security schemes which possesses an api-key property that allows to configure how API keys are applied to operations have a in of header set.
    message: Components Have a Security Schemes API Keys In Header 
    severity: info
    given: $.components.securitySchemes.apiKeys
    then:
      - field: in
        function: pattern
        functionOptions:
          notMatch: >-
            \b(header)\b
slug: openapi-security-schemes-api-key-info
---