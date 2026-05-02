---
name: OpenAPI Components Parameters Description Length Error
description: >-
  Limiting the length of parameters description forces us to be more concise in
  how we describe each parameter, while keeping our documentation and other ways
  descriptions show up in discovery and portals more consistent
message: Parameters Description MUST Be Less Than 500 Characters
given: $.components.parameters.*
tags:
  - OpenAPI
  - Components
  - Parameters
  - Metadata
  - Default
view_sort: EA  
guidance: OpenAPI
guidanceUrl: https://guidance.apievangelist.com/openapi
rule:
  openapi-components-parameters-description-length-error:
    description: >-
      Limiting the length of parameters description forces us to be more concise
      in how we describe each parameter, while keeping our documentation and
      other ways descriptions show up in discovery and portals more consistent
    message: Parameters Description MUST Be Less Than 500 Characters
    given: $.components.parameters.*
    then:
      field: summary
      function: length
      functionOptions:
        max: 500
slug: openapi-components-parameters-description-length-error
---