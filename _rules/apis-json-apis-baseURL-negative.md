---
apis-json-apis-baseURL-negative:
  description: This is the base URL used for an API defined using APIs.json, providing a reference for developers to use when onboarding and making calls to an API, but it is also used as a way of referencing an API, and validating what domain it is part of. You can find details about the <a href="https://apisjson.org/schema/base-url/">baseUrl property for APIs.json</a>, and explore <a href="https://apievangelist.com/guidance/environments/base-url/" target="_blank">Base URLs</a> more via API Evangelist.
  message: APIs MUST have a baseUrl property.
  given: $.apis.*
  severity: error
  then:
    field: baseURL
    function: truthy
---