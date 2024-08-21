---
apis-json-apis-properties-openapi-info:
  description: API Properties OpenAPI
  message: API has and OpenAPI.
  severity: info
  given:
    - $.apis.*.properties.*
    - $.common.*
  then:
    - field: type
      function: pattern
      functionOptions:
        notMatch: \b(openapi|OpenAPI)\b
---