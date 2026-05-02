---
slug: openapi-schema-properties-datetime-naming-warn
icon: calendar
name: OpenAPI Schema Properties DateTime Naming
description: >-
  DateTime properties (format date-time) should include a temporal suffix such as At, Date, Time, or On to clearly communicate that the value represents a point in time.
message: DateTime properties SHOULD use a temporal suffix (At, Date, Time, On).
given: $..[?(@.format=="date-time")]~
severity: warn
view_sort: B
tags:
  - OpenAPI
  - Schema
  - Properties
  - Naming
  - DateTime
guidance: Descriptions
guidanceUrl: https://guidance.apievangelist.com/descriptions
rule:
  openapi-schema-properties-datetime-naming-warn:
    description: >-
      DateTime properties (format date-time) should include a temporal suffix such as At, Date, Time, or On to clearly communicate that the value represents a point in time.
    message: DateTime properties SHOULD use a temporal suffix (At, Date, Time, On).
    given: $..[?(@.format=="date-time")]~
    severity: warn
    then:
      function: pattern
      functionOptions:
        match: "(?i)(At|Date|Time|On|Timestamp)$"
---
