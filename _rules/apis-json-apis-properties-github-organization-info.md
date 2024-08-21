---
apis-json-apis-properties-github-organization-info:
  description: API Properties GitHub Organization
  message: Provides a dedicated GitHub organizations as part API operations, offering up a link to all of the resources available across all APIs being made available.
  severity: info
  given:
    - $.apis.*.properties.*
    - $.common.*
  then:
    - field: type
      function: pattern
      functionOptions:
        notMatch: \b(github-organization|GitHubOrganization)\b
---