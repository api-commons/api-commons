---
name: APIs.json Apis Properties Questions Issues Info
description: >-
  This property ensures that an API has a dedicated link to Git issues for
  asking questions
message: Has Questions Issues URL
given:
  - $.apis.*.properties.*
  - $.common.*
severity: info
tags:
  - APIs.json
  - APIs
  - Properties
guidance: Support
guidanceUrl: https://guidance.apievangelist.com/support
rule:
  apis-json-apis-properties-questions-issues-info:
    description: >-
      This property ensures that an API has a dedicated link to Git issues for
      asking questions
    message: Has Questions Issues URL
    severity: info
    given:
      - $.apis.*.properties.*
      - $.common.*
    then:
      - field: type
        function: pattern
        functionOptions:
          notMatch: \b(QuestionsIssues|QuestionsGitHubIssues)\b
slug: apis-json-apis-properties-questions-issues-info
---