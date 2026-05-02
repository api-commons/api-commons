---
slug: owasp-api8-2023-no-server-http-error
icon: lock
name: OWASP API8 2023 No Server HTTP
description: >-
  Server interactions must not use http:// as it is inherently insecure and can
  lead to PII and other sensitive information being leaked through traffic
  sniffing or man-in-the-middle attacks. Use https:// or wss:// instead.
message: Server URLs must not use http://. Use https:// or wss:// instead.
given: $.servers..url
severity: error
view_sort: B
tags:
  - OWASP
  - Security
  - Transport
  - Servers
  - OpenAPI
guidance: Security
guidanceUrl: https://guidance.apievangelist.com/security
rule:
  owasp-api8-2023-no-server-http-error:
    description: >-
      Server interactions must not use http:// as it is inherently insecure and can
      lead to PII and other sensitive information being leaked through traffic
      sniffing or man-in-the-middle attacks. Use https:// or wss:// instead.
    message: Server URLs must not use http://. Use https:// or wss:// instead.
    given: $.servers..url
    severity: error
    then:
      function: pattern
      functionOptions:
        notMatch: "^http:"
---
