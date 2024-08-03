---
apis-json-specification-aid-negative:
  description:  >-
    Ensures that each APIs.json has a unique identifier expressed as an `aid`. APIs.json identifiers are a standardized format for allowing API producers to establish a unique identifier for each API contract they provide using APIs.json, which will then be prepended to each APIs defined. You can find details about the standard for APIs.json unique identifier on API Commons [need link], and explore <a href="https://apievangelist.com/guidance/identifiers/apis-json-identifier/" target="_blank">APIs.json Unique Identifiers</a> via API Evangelist.
  message: There MUST be a aid.
  severity: error
  given: $
  then:
    field: aid
    function: truthy
---