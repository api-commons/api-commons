---
apis-json-apis-properties-road-map-info:
  description: API Properties Road Map
  message: Has road map.
  severity: info
  given:
    - $.apis.*.properties.*
    - $.common.*
  then:
    - field: type
      function: pattern
      functionOptions:
        notMatch: \b(api-road-map|road-map|Roadmap|Road Map|RoadMap)\b
---