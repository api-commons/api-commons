---
openapi-no-path-trailing-slash-error:
  description: Warn trailing slash on path.
  message: Path Trailing Slash
  severity: error
  given: $.paths.*~
  then:
    function: pattern
    functionOptions:
      notMatch: /$
---