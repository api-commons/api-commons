---
name: APIs.json API Properties Mock Server Info
description: >-
  This property ensures that an API has a reference to a mock servers for individual APIs or as part of common properties, providing mocked deployments of an API that can be used for making test API calls.
message: Has a Mock Server
given:
  - $.apis.*.properties.*
  - $.common.*
severity: info
tags:
  - APIs.json
  - APIs
  - Properties
  - Sandbox
  - Mock Servers
view_sort: AA
guidance: Virtualization
guidanceUrl: https://guidance.apievangelist.com/virtualization
rule:
  apis-json-apis-properties-mock-server-info:
    description: >-
      This property ensures that an API has a reference to a mock servers for individual APIs or as part of common properties, providing mocked deployments of an API that can be used for making test API calls.
    message: Has a Mock Server
    severity: info
    given:
      - $.apis.*.properties.*
      - $.common.*
    then:
      - field: type
        function: pattern
        functionOptions:
          notMatch: \b(mocks|Mocks|MockServers)\b
slug: apis-json-apis-properties-mock-server-info
---