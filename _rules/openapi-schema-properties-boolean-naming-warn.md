---
slug: openapi-schema-properties-boolean-naming-warn
icon: toggle-left
name: OpenAPI Schema Properties Boolean Naming
description: >-
  Boolean properties should not use an "is" prefix in their names. The property type already indicates it is a boolean, and the "is" prefix adds unnecessary verbosity.
message: Boolean properties SHOULD NOT use an "is" prefix.
given: $..[?(@.type=="boolean")]~
severity: warn
view_sort: B
tags:
  - OpenAPI
  - Schema
  - Properties
  - Naming
  - Boolean
guidance: Descriptions
guidanceUrl: https://guidance.apievangelist.com/descriptions
rule:
  openapi-schema-properties-boolean-naming-warn:
    description: >-
      Boolean properties should not use an "is" prefix in their names. The property type already indicates it is a boolean, and the "is" prefix adds unnecessary verbosity.
    message: Boolean properties SHOULD NOT use an "is" prefix.
    given: $..[?(@.type=="boolean")]~
    severity: warn
    then:
      function: pattern
      functionOptions:
        notMatch: "^is[A-Z]"
---
