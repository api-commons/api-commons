---
apis-json-apis-properties-change-road-map-positive:
  description: API Properties Change Road Map
  message: Has road map.
  severity: info
  given:
    - $.apis.*.properties.*
    - $.common.*
  then:
    - field: type
      function: pattern
      functionOptions:
        notMatch: \b(api-road-map|road-map|Roadmap|Road Map)\b
---