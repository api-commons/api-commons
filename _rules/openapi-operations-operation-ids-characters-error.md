---
name: OpenAPI Operations Operation Ids Special Characters Error
description: >-
  Operation identifiers provide a unique way to identify each individual API,
  and requiring them to have consistent casing reduces friction when generating
  SDKs and automating around APIs
message: Operation Identifier MUST Not Have Special Characters
given: $.paths.*[get,post,patch,put,delete].operationId
severity: error
tags:
  - OpenAPI
  - Operations
  - Metadata
  - Default
view_sort: CA  
references:
  - name: Doctor
    type: Editor
    url: https://pb33f.io/doctor/
  - name: Spectral
    type: Linter
    url: https://github.com/stoplightio/spectral/blob/develop/packages/rulesets/src/oas/index.ts  
guidance: Naming
guidanceUrl: https://guidance.apievangelist.com/naming
rule:
  openapi-operations-operation-ids-camel-case-error:
    description: >-
      Operation identifiers provide a unique way to identify each individual
      API, and requiring them to have consistent casing reduces friction when
      generating SDKs and automating around APIs
    message: OpenAPI Operations Operation Ids Special Characters Error
    severity: error
    given: $.paths.*[get,post,patch,put,delete].operationId
    then:
      - function: pattern
        functionOptions:
          match: ^[A-Za-z0-9-._~:/?#\\[\\]@!\\$&'()*+,;=]*$
slug: openapi-operations-operation-ids-characters-error
---