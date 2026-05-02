---
name: APIs.json Apis Properties APIOps Cycles Business Model Canvas
description: >-
  This ensures that an API has had the [APIOps Business Model Canvas](https://www.apiopscycles.com/resources/api-business-model-canvas) applied to the API, requiring that the canvas is present in the repository and registered in the APIs.json index for the API, helping with discovery and governance.
message: Has APIOps Cycles Business Model Canvas
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

  apis-json-apis-properties-apiop-cycles-business-model-canvas-info:
    description: >-
      This ensures that an API has had the APIOps Business Model Canvas applied to the API, requiring that the canvas is present in the repository and registered in the APIs.json index for the API, helping with discovery and governance.
    message: Has APIOps Cycles Business Model Canvas
    severity: info
    given:
      - $.common.*
    then:
      - field: type
        function: pattern
        functionOptions:
          notMatch: \b(APIOpsBusinessModelCanvas)\b

slug: apis-json-apis-properties-apiop-cycles-business-model-canvas-info
---