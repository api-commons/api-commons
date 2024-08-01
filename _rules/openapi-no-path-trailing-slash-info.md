---
openapi-no-path-trailing-slash-info:
  description: Info trailing slash on path.
  message: Path Trailing Slash
  severity: info
  given: $.paths.*~
  then:
    function: pattern
    functionOptions:
      match: /$
---