---
apis-json-url-negative:
  description: The URL for an APIs.json provides a link to the source of an APIs.json, but also determines whether or not an APIs.json is authoritative or not. The URL is a locator, but can also be used as an identifier that can be used to ensure the authenticity and origin of APIs.json. The URL is regularly validated as part of API operations and the solutions using the APIs.json. You can find details about the <a href="https://apisjson.org/schema/url/">url property for APIs.json</a>.
  message: There MUST be a URL.
  given: $
  severity: error
  then:
    field: url
    function: truthy
---