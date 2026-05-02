---
slug: openapi-version-date-format-info
icon: calendar
name: OpenAPI Version Date Format
description: >-
  API versions using date-based format should follow the YYYY-MM-DD pattern, optionally followed by a -preview suffix for pre-release versions.
message: API version SHOULD follow YYYY-MM-DD format.
given: $.info.version
severity: info
view_sort: B
tags:
  - OpenAPI
  - Info
  - Version
  - Date
guidance: Change Management
guidanceUrl: https://guidance.apievangelist.com/change
rule:
  openapi-version-date-format-info:
    description: >-
      API versions using date-based format should follow the YYYY-MM-DD pattern, optionally followed by a -preview suffix for pre-release versions.
    message: API version SHOULD follow YYYY-MM-DD format.
    given: $.info.version
    severity: info
    then:
      function: pattern
      functionOptions:
        match: "^\\d{4}-\\d{2}-\\d{2}(-preview)?$"
---
