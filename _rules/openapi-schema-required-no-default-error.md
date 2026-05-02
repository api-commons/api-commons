---
slug: openapi-schema-required-no-default-error
icon: alert-circle
name: OpenAPI Schema Required No Default
description: >-
  Required properties should not have default values. If a property is required, the client must provide it explicitly. Having a default on a required property creates confusion about whether the client needs to send it.
message: Required properties MUST NOT have default values.
given: $..[?(@.required)]..properties[?(@.default)]
severity: error
view_sort: B
tags:
  - OpenAPI
  - Schema
  - Required
  - Defaults
guidance: Descriptions
guidanceUrl: https://guidance.apievangelist.com/descriptions
rule:
  openapi-schema-required-no-default-error:
    description: >-
      Required properties should not have default values. If a property is required, the client must provide it explicitly. Having a default on a required property creates confusion about whether the client needs to send it.
    message: Required properties MUST NOT have default values.
    given: $..[?(@.required)]..properties[?(@.default)]
    severity: error
    then:
      field: default
      function: falsy
---
