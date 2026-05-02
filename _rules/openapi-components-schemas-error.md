---
name: OpenAPI Components Schemas Error
description: >-
  Utilizing the schema object in the centralized OpenAPI components library
  helps make schema reusable across API requests and responses
message: Components MUST Have a Schema Property
given: $.components
severity: error
tags:
  - OpenAPI
  - Components
  - Default
guidance: OpenAPI
guidanceUrl: https://guidance.apievangelist.com/openapi
rule:
  openapi-components-schemas-error:
    description: >-
      Utilizing the schema object in the centralized OpenAPI components library
      helps make schema reusable across API requests and responses
    message: Components MUST Have a Schema Property
    severity: error
    given: $.components
    then:
      field: schemas
      function: truthy
slug: openapi-components-schemas-error
---