---
apis-json-specification-type-positive:
  description: The specification type for an APIs.json sets the tone for how the APIs.json will be processed, providing a way to namespace different ways of leveraging the machine-readable contents of the APIs/json. The most common is a simple index of one or many APIs, but originally templates and examples were also allowed. Contracts, blueprints, and a handful of other types have recently been added, expanding the ways in which the APIs.json specification can be used beyond just API discovery. You can find details about the <a href="https://apisjson.org/schema/type/">type property for APIs.json</a>.
  message: There is a specification type.
  severity: info
  given: $
  then:
    field: type
    function: falsy
---