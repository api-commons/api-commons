---
name: OpenAPI Components Parameters Name Error
description: >-
  Providing a simple, intuitive, and consistent names for your parameters helps
  make it easier for API consumers to understand how they are able to configure
  their API requests
message: Parameters MUST Have a Name
given: $.components.parameters.*
severity: error
tags:
  - OpenAPI
  - Components
  - Parameters
  - Metadata
  - Default
view_sort: B
guidance: OpenAPI
guidanceUrl: https://guidance.apievangelist.com/openapi
rule:
  openapi-components-parameters-name-error:
    description: >-
      Providing a simple, intuitive, and consistent names for your parameters
      helps make it easier for API consumers to understand how they are able to
      configure their API requests
    message: Parameters MUST Have a Name
    severity: error
    given: $.components.parameters.*
    then:
      field: name
      function: truthy
slug: openapi-components-parameters-name-error
---