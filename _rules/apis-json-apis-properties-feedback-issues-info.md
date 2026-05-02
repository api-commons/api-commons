---
name: APIs.json Apis Properties Feedback Issues Info
description: >-
  This property ensures there is a URL to Git issues specifically for providing
  feedback
message: Has Feedback Issues URL
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
  apis-json-apis-properties-feedback-issues-info:
    description: >-
      This property ensures there is a URL to Git issues specifically for
      providing feedback
    message: Has Feedback Issues URL
    severity: info
    given:
      - $.apis.*.properties.*
      - $.common.*
    then:
      - field: type
        function: pattern
        functionOptions:
          notMatch: \b(FeedbackIssues|FeedbackGitHubIssues)\b
slug: apis-json-apis-properties-feedback-issues-info
---