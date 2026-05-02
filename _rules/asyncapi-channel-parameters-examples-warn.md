---
slug: asyncapi-channel-parameters-examples-warn
icon: message-square
name: AsyncAPI Channel Parameters Examples
description: >-
  AsyncAPI channel parameters should include examples to support mocking, testing, and documentation. Examples help consumers understand expected parameter values for channel subscriptions.
message: AsyncAPI channel parameters SHOULD include examples.
given: $.channels[*].parameters.*
severity: warn
view_sort: B
tags:
  - AsyncAPI
  - Channels
  - Parameters
  - Examples
  - Mocking
guidance: Documentation
guidanceUrl: https://guidance.apievangelist.com/documentation
rule:
  asyncapi-channel-parameters-examples-warn:
    description: >-
      AsyncAPI channel parameters should include examples to support mocking, testing, and documentation. Examples help consumers understand expected parameter values for channel subscriptions.
    message: AsyncAPI channel parameters SHOULD include examples.
    given: $.channels[*].parameters.*
    severity: warn
    then:
      field: examples
      function: truthy
---
