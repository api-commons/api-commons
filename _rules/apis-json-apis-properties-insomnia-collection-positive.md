---
apis-json-apis-properties-documentation-insomnia-collection-positive:
  description: API Properties Insomnia Collection
  message: Has a Insomnia Collection.
  severity: info
  given:
    - $.apis.*.properties.*
    - $.common.*
  then:
    - field: type
      function: pattern
      functionOptions:
        notMatch: \b(RunInInsomnia)\b
---