---
slug: apis-json-apis-properties-about-info
icon: tune
name: APIs.json APIs Properties Info
description: >-
  Each individual API included in an APIs.json file can have a properties collection, which contains specific properties relevant to that API. These properties often start with human-readable elements, such as documentation links, and can also include machine-readable properties to enhance functionality and integration.
message: Has About
given:
  - $.apis.*.properties.*
  - $.common.*
severity: info
tags:
  - APIs.json
  - APIs
  - Metadata
view_sort: J  
guidance: APIs Metadata
guidanceUrl: https://guidance.apievangelist.com/apis/metadata
rule:
  apis-json-apis-properties-about-info:
    description: >-
      Each individual API included in an APIs.json file can have a properties collection, which contains specific properties relevant to that API. These properties often start with human-readable elements, such as documentation links, and can also include machine-readable properties to enhance functionality and integration.
    message: Has About
    severity: info
    given:
      - $.apis.*.properties.*
      - $.common.*
    then:
      - field: type
        function: pattern
        functionOptions:
          notMatch: \b(about|About)\b
---