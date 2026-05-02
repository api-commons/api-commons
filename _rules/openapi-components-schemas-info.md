---
name: OpenAPI Components Schemas Info
description: >-
  Utilizing the schema object in the centralized OpenAPI components library
  helps make schema reusable across API requests and responses
message: Components Have a Schema Property
given: $.components
severity: info
tags:
  - OpenAPI
  - Components
  - Default
guidance: OpenAPI
guidanceUrl: https://guidance.apievangelist.com/openapi
rule:
  openapi-components-schemas-info:
    description: >-
      Utilizing the schema object in the centralized OpenAPI components library
      helps make schema reusable across API requests and responses
    message: Components Have a Schema Property
    severity: info
    given: $.components
    then:
      field: schemas
      function: falsy
slug: openapi-components-schemas-info
---