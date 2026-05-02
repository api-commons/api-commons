---
name: OpenAPI Operation Security Definitions API Keys Info
description: >-
  Each API operation should have a security definition referencing the central security scheme express for an OpenAPI referencing apiKeys property.
message: Operations MUST Have a Security Definition for API Keys
given: $.paths.*[get,post,patch,put,delete]
severity: info
tags:
  - OpenAPI
  - Operations
  - Security
  - Default
view_sort: E   
guidance: Security
guidanceUrl: https://guidance.apievangelist.com/security
rule:
  openapi-operation-security-definitions-keys-info:
    description: >-
      Each API operation should have a security definition referencing the central security scheme express for an OpenAPI referencing apiKeys property.
    message: Operations Have a Security Definition for API Keys
    severity: info
    given: $.paths.*[get,post,patch,put,delete].security[*]
    then:
      field: '@key'
      function: pattern
      functionOptions:
        match: >-
          \b(apiKeys)\b 
slug: openapi-operation-security-definitions-keys-info
---