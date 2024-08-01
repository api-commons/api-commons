---
apis-json-apis-properties-documentation-openapi-positive:
  description: API Properties Documentation OpenAPI
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