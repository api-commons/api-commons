---
name: OpenAPI Components Parameters Name Info
description: >-
  Providing a simple, intuitive, and consistent names for your parameters helps
  make it easier for API consumers to understand how they are able to configure
  their API requests
message: Parameters Have a Name
given: $.components.parameters.*
severity: info
tags:
  - OpenAPI
  - Components
  - Parameters
  - Metadata
  - Default
  - Default
view_sort: B  
guidance: OpenAPI
guidanceUrl: https://guidance.apievangelist.com/openapi
rule:
  openapi-components-parameters-name-info:
    description: >-
      Providing a simple, intuitive, and consistent names for your parameters
      helps make it easier for API consumers to understand how they are able to
      configure their API requests
    message: Parameters Have a Name
    severity: info
    given: $.components.parameters.*
    then:
      field: name
      function: falsy
slug: openapi-components-parameters-name-info
---