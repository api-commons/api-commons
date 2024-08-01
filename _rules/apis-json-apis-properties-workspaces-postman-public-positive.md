---
apis-json-apis-properties-workspaces-postman-public-positive:
  description: API Properties Workspaces Postman Public
  message: Has a Postman public workspace.
  severity: info
  given:
    - $.apis.*.properties.*
    - $.common.*
  then:
    - field: type
      function: pattern
      functionOptions:
        notMatch: \b(postman-public-workspace)\b
---