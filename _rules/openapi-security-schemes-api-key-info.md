---
name: OpenAPI Security Schemes API Keys Info
description: >-
  Having components security schemes which possesses an api-key property that allows to configure how API keys are applied to operations.
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
  openapi-security-schemes-api-key-info:
    description: >-
      Having components security schemes which possesses an api-key property that allows to configure how API keys are applied to operations.
    message: Components Have a Security Schemes API Keys 
    severity: info
    given: $.components.securitySchemes
    then:
      field: apiKeys
      function: falsy
slug: openapi-security-schemes-api-key-info
---