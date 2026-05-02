---
name: APIs.json Apis Properties APIOps Cycles Value Proposition Canvas
description: >-
  This ensures that an API has had the [APIOps Value Proposition Canvas](https://www.apiopscycles.com/resources/api-value-proposition-canvas) applied to the API, requiring that the canvas is present in the repository and registered in the APIs.json index for the API, helping with discovery and governance.
message: Has APIOps Cycles Value Proposition Canvas
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

  apis-json-apis-properties-apiop-cycles-value-proposition-canvas-info:
    description: >-
      This ensures that an API has had the APIOps Value Proposition Canvas applied to the API, requiring that the canvas is present in the repository and registered in the APIs.json index for the API, helping with discovery and governance.
    message: Has APIOps Cycles Value Proposition Canvas
    severity: info
    given:
      - $.common.*
    then:
      - field: type
        function: pattern
        functionOptions:
          notMatch: \b(APIOpsValuePropositionCanvas)\b
          
slug: apis-json-apis-properties-apiop-cycles-value-proposition-canvas-info
---