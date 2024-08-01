---
openapi-openapi-version-300-info:
  description: Warn latest version of OpenAPI.
  message: 3.0.0 Version of OpenAPI
  severity: warn
  given: $
  then:
    field: openapi
    function: pattern
    functionOptions:
      notMatch: 3.0.0
---