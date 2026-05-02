---
name: OpenAPI Operations Operation Ids Special Characters Info
description: >-
  Operation identifiers provide a unique way to identify each individual API,
  and requiring them to have consistent casing reduces friction when generating
  SDKs and automating around APIs.
message: Operation Identifier Does Not Have Special Characters
given: $.paths.*[get,post,patch,put,delete].operationId
severity: info
tags:
  - OpenAPI
  - Operations
  - Metadata
  - Default
view_sort: CA  
guidance: Naming
guidanceUrl: https://guidance.apievangelist.com/naming
rule:
  openapi-operations-operation-ids-camel-case-info:
    description: >-
      Operation identifiers provide a unique way to identify each individual
      API, and requiring them to have consistent casing reduces friction when
      generating SDKs and automating around APIs.
    message: OpenAPI Operations Operation Ids Special Characters Info
    severity: info
    given: $.paths.*[get,post,patch,put,delete].operationId
    then:
      - function: pattern
        functionOptions:
          notMatch: ^[A-Za-z0-9-._~:/?#\\[\\]@!\\$&'()*+,;=]*$
slug: openapi-operations-operation-ids-characters-info
---