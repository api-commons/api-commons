---
name: OpenAPI Operation Security Definitions API Keys Error
description: >-
  Each API operation should have a security definition referencing the central security scheme express for an OpenAPI referencing apiKeys property.
message: Operations MUST Have a Security Definition for API Keys 
given: $.paths.*[get,post,patch,put,delete]
severity: error
tags:
  - OpenAPI
  - Operations
  - Security
  - Default
view_sort: E  
guidance: Security
guidanceUrl: https://guidance.apievangelist.com/security
rule:
  openapi-operation-security-definitions-keys-error:
    description: >-
      Each API operation should have a security definition referencing the central security scheme express for an OpenAPI referencing apiKeys property.
    message: Operations MUST Have a Security Definition for API Keys
    severity: error
    given: $.paths.*[get,post,patch,put,delete]
    then:
      field: '@key'
      function: pattern
      functionOptions:
        notMatch: >-
          \b(apiKeys)\b  
slug: openapi-operation-security-definitions-keys-error
---