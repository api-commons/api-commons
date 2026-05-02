---
name: OpenAPI Components Parameters Name Length Error
description: >-
  Providing short and concise names for your parameters helps make it easier for
  API consumers to understand how they are able to configure their API requests
message: Parameters Name Length MUST Be Less Than 25 Characters
given: $.components.parameters[?(@.in=='path')].name
tags:
  - OpenAPI
  - Components
  - Parameters
  - Metadata
  - Default
view_sort: BA  
guidance: OpenAPI
guidanceUrl: https://guidance.apievangelist.com/openapi
rule:
  openapi-components-parameters-name-length-error:
    description: >-
      Providing short and concise names for your parameters helps make it easier
      for API consumers to understand how they are able to configure their API
      requests
    message: Parameters Name Length MUST Be Less Than 25 Characters
    given: $.components.parameters[?(@.in=='path')].name
    then:
      field: summary
      function: length
      functionOptions:
        max: 25
slug: openapi-components-parameters-name-length-error
---