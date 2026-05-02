---
name: APIs.json Apis Properties APIOps Cycles Business Impact Canvas
description: >-
  This ensures that an API has had the [APIOps Business Impact Canvas](https://www.apiopscycles.com/resources/business-impact-canvas) applied to the API, requiring that the canvas is present in the repository and registered in the APIs.json index for the API, helping with discovery and governance.
message: Has APIOps Cycles Business Impact Canvas
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

  apis-json-apis-properties-apiop-cycles-business-impact-canvas-info:
    description: >-
      This ensures that an API has had the APIOps Business Impact Canvas applied to the API, requiring that the canvas is present in the repository and registered in the APIs.json index for the API, helping with discovery and governance.
    message: Has APIOps Cycles Business Impact Canvas
    severity: info
    given:
      - $.common.*
    then:
      - field: type
        function: pattern
        functionOptions:
          notMatch: \b(APIOpsBusinessImpactCanvas)\b

slug: apis-json-apis-properties-apiop-cycles-business-impact-canvas-info
---