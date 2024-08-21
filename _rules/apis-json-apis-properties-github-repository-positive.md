---
apis-json-apis-properties-workspaces-github-public-positive:
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