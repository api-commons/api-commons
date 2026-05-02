---
name: APIs.json Apis Properties Vocabulary Info
description: >-
  This property ensures that there is a centralized vocabulary in use for
  guiding the creation and usage of tags, path segments, and other metadata
  associated with an APIs
message: Has Vocabulary
given:
  - $.apis.*.properties.*
  - $.common.*
severity: info
tags:
  - APIs.json
  - APIs
  - Properties
guidance: Governance
guidanceUrl: https://guidance.apievangelist.com/governance
rule:
  apis-json-apis-properties-vocabulary-info:
    description: >-
      This property ensures that there is a centralized vocabulary in use for
      guiding the creation and usage of tags, path segments, and other metadata
      associated with an APIs
    message: Has Vocabulary
    severity: info
    given:
      - $.apis.*.properties.*
      - $.common.*
    then:
      - field: type
        function: pattern
        functionOptions:
          notMatch: \b(vocabulary|vocabularies|Vocabulary|Vocabularies)\b
slug: apis-json-apis-properties-vocabulary-info
---