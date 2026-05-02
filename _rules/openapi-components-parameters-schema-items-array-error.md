---
name: OpenAPI Components Parameters Schema Items Array Error
description: >-
  Parameters that are of an array type should always have the items defined,
  being explicit about what is continued as part of the array
message: Parameter Schema Array MUST Have Items
given: $.components.parameters.schema[?(@.type=='array')]
severity: error
tags:
  - OpenAPI
  - Components
  - Parameters
  - Schema  
  - Type
  - Default
  - Security
view_sort: M
guidance: OpenAPI
guidanceUrl: https://guidance.apievangelist.com/openapi
rule:
  openapi-components-parameters-schema-items-array-error:
    description: >-
      Parameters that are of an array type should always have the items defined,
      being explicit about what is continued as part of the array
    message: Parameter Schema Array MUST Have Items
    given: $.components.parameters.schema[?(@.type=='array')]
    severity: error
    then:
      field: items
      function: truthy
slug: openapi-components-parameters-schema-items-array-error
---