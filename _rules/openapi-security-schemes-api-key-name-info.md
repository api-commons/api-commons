---
name: OpenAPI Security Schemes API Keys Name Info
description: >-
  Having components security schemes which possesses an api-key property that allows to configure how API keys are applied to operations have a name of api_key set.
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
  openapi-security-schemes-api-key-name-info:
    description: >-
      Having components security schemes which possesses an api-key property that allows to configure how API keys are applied to operations have a name of api_key set.
    message: Components Have a Security Schemes API Keys Name
    severity: info
    given: $.components.securitySchemes.apiKeys
    then:
      - field: name
        function: pattern
        functionOptions:
          notMatch: >-
            \b(api-key)\b
slug: openapi-security-schemes-api-key-name-info
---