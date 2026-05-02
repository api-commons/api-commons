---
name: OpenAPI Security Schemes API Keys Name Error
description: >-
  Having components security schemes which possesses an api-key property that allows to configure how API keys are applied to operations have a name of api_key set.
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
  openapi-security-schemes-api-key-name-error:
    description: >-
      Having components security schemes which possesses an api-key property that allows to configure how API keys are applied to operations have a name of api_key set.
    message: Components MUST Have a Security Schemes API Keys Name 
    severity: error
    given: $.components.securitySchemes.apiKeys
    then:
      - field: name
        function: pattern
        functionOptions:
          match: >-
            \b(api-key)\b
slug: openapi-security-schemes-api-key-name-error
---