---
apis-json-apis-properties-forum-info:
  description: API Properties Forum
  message: Provides a dedicated forum to supporting an API and the community of consumers, ensuring that discussions around API usage is self-service.
  severity: info
  given:
    - $.apis.*.properties.*
    - $.common.*
  then:
    - field: type
      function: pattern
      functionOptions:
        notMatch: \b(Forums|Forums|Discussions)\b
---