---
slug: openapi-operations-post-no-retrieve-verbs-error
icon: edit
name: OpenAPI Operations POST No Retrieve Verbs
description: >-
  POST operations should not use verbs like retrieve, fetch, get, or read in their summaries. If data retrieval is the goal, a GET method should be used instead to follow RESTful conventions.
message: POST operation summaries MUST NOT use retrieve, fetch, get, or read verbs.
given: "$.paths[*].post.summary"
severity: error
view_sort: B
tags:
  - OpenAPI
  - Operations
  - POST
  - REST
  - Design
guidance: Naming
guidanceUrl: https://guidance.apievangelist.com/naming
rule:
  openapi-operations-post-no-retrieve-verbs-error:
    description: >-
      POST operations should not use verbs like retrieve, fetch, get, or read in their summaries. If data retrieval is the goal, a GET method should be used instead to follow RESTful conventions.
    message: POST operation summaries MUST NOT use retrieve, fetch, get, or read verbs.
    given: "$.paths[*].post.summary"
    severity: error
    then:
      function: pattern
      functionOptions:
        notMatch: "(?i)(retrieve|fetch|get|read)"
---
