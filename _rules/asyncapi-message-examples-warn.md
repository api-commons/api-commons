---
slug: asyncapi-message-examples-warn
icon: message-square
name: AsyncAPI Message Examples
description: >-
  AsyncAPI messages should include examples to support event-driven API mocking, testing, and documentation. Examples help consumers understand message payloads and enable tools to generate realistic mock events.
message: AsyncAPI messages SHOULD include examples.
given: $.channels[*].subscribe.message,$.channels[*].publish.message
severity: warn
view_sort: B
tags:
  - AsyncAPI
  - Messages
  - Examples
  - Mocking
guidance: Documentation
guidanceUrl: https://guidance.apievangelist.com/documentation
rule:
  asyncapi-message-examples-warn:
    description: >-
      AsyncAPI messages should include examples to support event-driven API mocking, testing, and documentation. Examples help consumers understand message payloads and enable tools to generate realistic mock events.
    message: AsyncAPI messages SHOULD include examples.
    given: $.channels[*].subscribe.message,$.channels[*].publish.message
    severity: warn
    then:
      field: examples
      function: truthy
---
