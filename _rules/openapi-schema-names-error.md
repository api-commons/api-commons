---
name: OpenAPI Schema Names Pascal Case Error
description: >-
  Schema names, keeping the naming of them consistent across APIs, standardizing how consumers can use in their applications.
message: Schema Names MUST Exist
given: $.components.schemas
severity: error
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
  openapi-schema-names-error:
    description: >-
      Schema names, keeping the naming of them consistent across APIs, standardizing how consumers can use in their applications.
    message: Schema Names MUST Exist
    severity: error
    given: $.components.schemas
    then:
      field: '@key'
      function: truthy
slug: openapi-schema-names-error
---