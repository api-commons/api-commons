---
apis-json-apis-aid-negative:
  description:  >-
    This property ensures that each APIs indexed within an APIs.json can have a unique identifier expressed as an `aid`. API identifiers (AID) are a standardized format for allowing API producers to establish a unique identifier for each API they publish using APIs.json, which will have the aid for the APIs.json prepended to each APIs aid. You can find details about the <a href="https://apisjson.org/schema/aid/">aid property for APIs.json</a>, and explore <a href="https://apievangelist.com/guidance/identifiers/api-identifier/" target="_blank">API Unique Identifiers</a> more via API Evangelist.
  message: APIs MUST have a aid property.
  given: $.apis.*
  severity: error
  then:
    field: aid
    function: truthy
---