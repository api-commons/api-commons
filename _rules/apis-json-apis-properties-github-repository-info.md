---
apis-json-apis-properties-github-repository-info:
  description: API Properties GitHub Repository
  message: Has a GitHub repository.
  severity: info
  given:
    - $.apis.*.properties.*
    - $.common.*
  then:
    - field: type
      function: pattern
      functionOptions:
        notMatch: \b(github-repository|GitHubRepository)\b
---