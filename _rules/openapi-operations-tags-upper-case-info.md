---
name: OpenAPI Operations Tags Upper Case Info
description: >-
  Having the first letter of each word applied as a tag to API operations helps
  keep a consistent layout when published via search, documentation, and other
  ways APIs are made available
message: Operation Tag Names Have First Letter in Each Word Capitalized
given: $.paths.*[get,post,patch,put,delete].tags.*
severity: info
tags:
  - OpenAPI
  - Operations
  - Tags
  - Default
  - Documentation
view_sort: DB   
guidance: OpenAPI
guidanceUrl: https://guidance.apievangelist.com/openapi
rule:
  openapi-operations-tags-upper-case-info:
    description: >-
      Having the first letter of each word applied as a tag to API operations
      helps keep a consistent layout when published via search, documentation,
      and other ways APIs are made available
    message: Operation Tag Names Have First Letter in Each Word Capitalized
    severity: info
    given: $.paths.*[get,post,patch,put,delete].tags.*
    then:
      function: pattern
      functionOptions:
        notMatch: '[A-Z]\w*'
slug: openapi-operations-tags-upper-case-info
---