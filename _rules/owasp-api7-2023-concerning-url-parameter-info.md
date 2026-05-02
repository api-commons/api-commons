---
slug: owasp-api7-2023-concerning-url-parameter-info
icon: globe
name: OWASP API7 2023 Concerning URL Parameter
description: >-
  Using external resource URLs based on user input for webhooks, file fetching,
  custom SSO, URL previews, or redirects can lead to Server Side Request Forgery
  (SSRF) and other security issues.
message: Make sure to review the way this URL parameter is handled to protect against Server Side Request Forgery.
given: $.paths[*].parameters[*].name
severity: info
view_sort: B
tags:
  - OWASP
  - Security
  - SSRF
  - Parameters
  - OpenAPI
guidance: Security
guidanceUrl: https://guidance.apievangelist.com/security
rule:
  owasp-api7-2023-concerning-url-parameter-info:
    description: >-
      Using external resource URLs based on user input for webhooks, file fetching,
      custom SSO, URL previews, or redirects can lead to Server Side Request Forgery
      (SSRF) and other security issues.
    message: Make sure to review the way this URL parameter is handled to protect against Server Side Request Forgery.
    given: $.paths[*].parameters[*].name
    severity: info
    then:
      function: pattern
      functionOptions:
        notMatch: "(?i)(callback|redirect|uri|url|href|link|target|return)"
---
