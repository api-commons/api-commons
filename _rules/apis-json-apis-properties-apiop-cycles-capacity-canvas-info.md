---
name: APIs.json Apis Properties APIOps Cycles Capacity Canvas
description: >-
  This ensures that an API has had the [APIOps Capacity Canvas](https://www.apiopscycles.com/resources/capacity-canvas) applied to the API, requiring that the canvas is present in the repository and registered in the APIs.json index for the API, helping with discovery and governance.
message: Has APIOps Cycles Capacity Canvas
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

  apis-json-apis-properties-apiop-cycles-capacity-canvas-info:
    description: >-
      This ensures that an API has had the APIOps Capacity Canvas applied to the API, requiring that the canvas is present in the repository and registered in the APIs.json index for the API, helping with discovery and governance.
    message: Has APIOps Cycles Capacity Canvas
    severity: info
    given:
      - $.common.*
    then:
      - field: type
        function: pattern
        functionOptions:
          notMatch: \b(APIOpsCapacityCanvas)\b

slug: apis-json-apis-properties-apiop-cycles-capacity-canvas-info
---