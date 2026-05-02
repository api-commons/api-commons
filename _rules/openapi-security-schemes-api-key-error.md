---
name: OpenAPI Security Schemes API Keys Error
description: >-
  Having components security schemes which possesses an api-key property that allows to configure how API keys are applied to operations.
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
  openapi-security-schemes-api-key-error:
    description: >-
      Having components security schemes which possesses an api-key property that allows to configure how API keys are applied to operations.
    message: Components MUST Have a Security Schemes API Keys 
    severity: error
    given: $.components.securitySchemes
    then:
      field: apiKeys
      function: truthy
slug: openapi-security-schemes-api-key-error
---