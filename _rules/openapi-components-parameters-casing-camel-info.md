---
name: OpenAPI Components Parameters Casing Camel Info
description: >-
  Providing parameters with consistent naming helps make it easier for API
  consumers to understand how they are able to configure their API requests
message: Parameters Names Are Camel Case
given: $.components.parameters.*
severity: info
tags:
  - OpenAPI
  - Components
  - Parameters
  - Metadata
  - Default
view_sort: D    
guidance: OpenAPI
guidanceUrl: https://guidance.apievangelist.com/openapi
rule:
  openapi-components-parameters-casing-camel-info:
    description: >-
      Providing parameters with consistent naming helps make it easier for API
      consumers to understand how they are able to configure their API requests
    message: Parameters Names Are Camel Case
    severity: info
    given: $.components.parameters.*
    then:
      - field: name
        function: pattern
        functionOptions:
          notMatch: ^[a-z]+(?:[A-Z][a-z]+)*$
      - field: name
        function: pattern
        functionOptions:
          match: ^[A-Z](([a-z0-9]+[A-Z]?)*)$
slug: openapi-components-parameters-casing-camel-info
---