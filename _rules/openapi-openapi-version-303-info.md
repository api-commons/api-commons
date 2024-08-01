---
openapi-openapi-version-303-info:
  description: Warn latest version of OpenAPI.
  message: 3.0.3 Version of OpenAPI
  severity: warn
  given: $
  then:
    field: openapi
    function: pattern
    functionOptions:
      notMatch: 3.0.3
---