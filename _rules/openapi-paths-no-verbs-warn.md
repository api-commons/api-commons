---
slug: openapi-paths-no-verbs-warn
icon: link
name: OpenAPI Paths No Verbs
description: >-
  RESTful API path segments should not contain action verbs. HTTP methods already convey the action, so verbs in paths indicate a non-RESTful design. Paths should describe resources, not actions.
message: Paths SHOULD NOT contain action verbs.
given: "$.paths.*~"
severity: warn
view_sort: B
tags:
  - OpenAPI
  - Paths
  - REST
  - Design
guidance: Naming
guidanceUrl: https://guidance.apievangelist.com/naming
rule:
  openapi-paths-no-verbs-warn:
    description: >-
      RESTful API path segments should not contain action verbs. HTTP methods already convey the action, so verbs in paths indicate a non-RESTful design. Paths should describe resources, not actions.
    message: Paths SHOULD NOT contain action verbs.
    given: "$.paths.*~"
    severity: warn
    then:
      function: pattern
      functionOptions:
        notMatch: "(?i)(get|put|post|delete|patch|create|update|remove|fetch|retrieve|list|add|edit|modify|search|find|save|execute|run|start|stop)"
---
