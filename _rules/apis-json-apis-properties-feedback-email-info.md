---
name: APIs.json Apis Properties Feedback Email Info
description: >-
  This property ensures that there is an email available for API consumers to
  provide feedback
message: Has Feedback Email
given:
  - $.apis.*.properties.*
  - $.common.*
severity: info
tags:
  - APIs.json
  - APIs
  - Properties
guidance: Feedback
guidanceUrl: https://guidance.apievangelist.com/feedback
rule:
  apis-json-apis-properties-feedback-email-info:
    description: >-
      This property ensures that there is an email available for API consumers
      to provide feedback
    message: Has Feedback Email
    severity: info
    given:
      - $.apis.*.properties.*
      - $.common.*
    then:
      - field: type
        function: pattern
        functionOptions:
          notMatch: \b(feedback-email|FeedbackEmail)\b
slug: apis-json-apis-properties-feedback-email-info
---