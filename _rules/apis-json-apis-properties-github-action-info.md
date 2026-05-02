---
name: APIs.json Apis Properties Github Action Info
description: >-
  This property ensures that a GitHub Actions CI/CD pipeline is available for an
  API, providing a link to the pipeline YAML artifact, which can be used to
  automate and govern the API as part of the build process
message: Has a GitHub Action
given:
  - $.apis.*.properties.*
  - $.common.*
severity: info
tags:
  - APIs.json
  - APIs
  - Properties
guidance: Pipelines
guidanceUrl: https://guidance.apievangelist.com/pipelines
rule:
  apis-json-apis-properties-github-action-info:
    description: >-
      This property ensures that a GitHub Actions CI/CD pipeline is available
      for an API, providing a link to the pipeline YAML artifact, which can be
      used to automate and govern the API as part of the build process
    message: Has a GitHub Action
    severity: info
    given:
      - $.apis.*.properties.*
      - $.common.*
    then:
      - field: type
        function: pattern
        functionOptions:
          notMatch: \b(github-actions|GitHubActions)\b
slug: apis-json-apis-properties-github-action-info
---