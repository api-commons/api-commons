---
name: JSON Schema Draft 2020-12 Required Info
description: All JSON Schema objects should explicitly define their properties and include at least one required property. Defining required properties enhances the accuracy and reliability of validation for each object.
slug: json-schema-2020-12-required-info
engine: Unknown
specification: Unknown
specificationUrl: https://example.com
guidance: API Evangelist
guidanceUrl: https://guidance.apievangelist.com
severity: info
type: Default
tags:
  - JSON Schema
  - Metadata
  - Required
view_sort: H
rule:
  json-schema-2020-12-required-info:
    description: All JSON Schema objects should explicitly define their properties and include at least one required property. Defining required properties enhances the accuracy and reliability of validation for each object.
    given: $
    severity: error
    then:
      field: name
      function: truthy
---