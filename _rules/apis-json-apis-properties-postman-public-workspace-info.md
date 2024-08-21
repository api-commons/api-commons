---
apis-json-apis-properties-postman-public-workspace-info:
  description: API Properties Postman Public Workspace
  message: Providing a public Postman workspace 
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