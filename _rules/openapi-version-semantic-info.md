---
openapi-version-semantic-info:
  description: Has semantic versioning.
  message: Semantic Versioning
  severity: info
  given: $.info.version
  then:
    function: pattern
    functionOptions:
      notMatch: >-
        ^(0|[1-9][0-9]*)\.(0|[1-9][0-9]*)\.(0|[1-9][0-9]*)(-(0|[1-9A-Za-z-][0-9A-Za-z-]*)(\.[0-9A-Za-z-]+)*)?(\+[0-9A-Za-z-]+(\.[0-9A-Za-z-]+)*)?$
---