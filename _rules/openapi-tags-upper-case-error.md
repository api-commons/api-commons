---
name: OpenAPI Tags Upper Case Error
description: >-
  The first letter of each word in a tag being applied to APIs needs to be
  capitalized, keeping the tags being applied across APIs the same look and feel
  for organizing and publishing to documentation
message: Tag Names MUST Have First Letter in Each Word Capitalized
given: $.tags.*.name
severity: error
tags:
  - OpenAPI
  - Tags
  - Default
guidance: OpenAPI
guidanceUrl: https://guidance.apievangelist.com/openapi
rule:
  openapi-tags-upper-case-error:
    description: >-
      The first letter of each word in a tag being applied to APIs needs to be
      capitalized, keeping the tags being applied across APIs the same look and
      feel for organizing and publishing to documentation
    message: Tag Names MUST Have First Letter in Each Word Capitalized
    severity: error
    given: $.tags.*.name
    then:
      function: pattern
      functionOptions:
        match: '[A-Z]\w*'
slug: openapi-tags-upper-case-error
---