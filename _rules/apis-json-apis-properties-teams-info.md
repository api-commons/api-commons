---
name: APIs.json Apis Properties Teams Info
description: >-
  This property ensures that there is a reference to the team behind an API,
  providing a reference to business and engineering stakeholders
message: Has a Team Defined
given:
  - $.apis.*.properties.*
  - $.common.*
severity: info
tags:
  - APIs.json
  - APIs
  - Properties
  - Additional
view_sort: E
guidance: Organizations
guidanceUrl: https://guidance.apievangelist.com/organizations
rule:
  apis-json-apis-properties-teams-info:
    description: >-
      This property ensures that there is a reference to the team behind an API,
      providing a reference to business and engineering stakeholders
    message: Has a Team Defined
    severity: info
    given:
      - $.apis.*.properties.*
      - $.common.*
    then:
      - field: type
        function: pattern
        functionOptions:
          notMatch: \b(team|teams|Team|Teams)\b
slug: apis-json-apis-properties-teams-info
---