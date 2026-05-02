---
slug: openapi-headers-hyphenated-pascal-case-error
icon: type
name: OpenAPI Headers Hyphenated Pascal Case
description: >-
  HTTP headers should follow Hyphenated-Pascal-Case naming convention for consistency and readability, such as Content-Type, X-Request-Id, or Accept-Language.
message: HTTP Headers MUST use Hyphenated-Pascal-Case.
given: "$..headers.*~"
severity: error
view_sort: B
tags:
  - OpenAPI
  - Headers
  - Casing
  - Naming
guidance: Naming
guidanceUrl: https://guidance.apievangelist.com/naming
rule:
  openapi-headers-hyphenated-pascal-case-error:
    description: >-
      HTTP headers should follow Hyphenated-Pascal-Case naming convention for consistency and readability, such as Content-Type, X-Request-Id, or Accept-Language.
    message: HTTP Headers MUST use Hyphenated-Pascal-Case.
    given: "$..headers.*~"
    severity: error
    then:
      function: pattern
      functionOptions:
        match: "^([A-Z][a-z0-9]*(-[A-Z][a-z0-9]*)*)$"
---
