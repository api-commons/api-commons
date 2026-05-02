---
name: APIs.json Apis Properties APIOps Cycles Event Canvas
description: >-
  This ensures that an API has had the [APIOps Event Canvas](https://www.apiopscycles.com/resources/event-canvas) applied to the API, requiring that the canvas is present in the repository and registered in the APIs.json index for the API, helping with discovery and governance.
message: Has APIOps Cycles Event Canvas
given:
  - $.common.*
severity: info
tags:
  - APIs.json
  - APIs
  - Properties
  - APIOps Cycles
guidance: APIs Lifecycle
guidanceUrl: https://guidance.apievangelist.com/lifecycle
rule:

  apis-json-apis-properties-apiop-cycles-event-canvas-info:
    description: >-
      This ensures that an API has had the APIOps Event Canvas applied to the API, requiring that the canvas is present in the repository and registered in the APIs.json index for the API, helping with discovery and governance.
    message: Has APIOps Cycles Event Canvas
    severity: info
    given:
      - $.common.*
    then:
      - field: type
        function: pattern
        functionOptions:
          notMatch: \b(APIOpsEventCanvas)\b

slug: apis-json-apis-properties-apiop-cycles-event-canvas-info
---