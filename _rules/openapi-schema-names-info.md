---
name: OpenAPI Schema Names Info
description: >-
  Schema names, keeping the naming of them consistent across APIs, standardizing how consumers can use in their applications.
message: Schema Names Exist
given: $.components.schemas
severity: info
tags:
  - OpenAPI
  - Schema
  - Metadata
  - Default
  - Documentation
view_sort: A
guidance: Descriptions
guidanceUrl: https://guidance.apievangelist.com/descriptions
rule:
  openapi-schema-names-info:
    description: >-
      Schema names, keeping the naming of them consistent across APIs, standardizing how consumers can use in their applications.
    message: Schema Names Exist
    severity: info
    given: $.components.schemas
    then:
      field: '@key'
      function: falsy
slug: openapi-schema-names-info
---