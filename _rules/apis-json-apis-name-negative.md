---
apis-json-apis-name-negative:
  description: The name of your API is one of the most important design decision you can make, and will be one you will have to live with throughout the life of your API. Take the time to make sure the API accurately describes the API, and avoid using common words about the patterns and infrastructure used--keep the name of the API simple, easy to read, and meaningful to the consumer of the API. You can find details about the <a href="https://apisjson.org/schema/name/">name property for APIs.json</a>, and explore <a href="https://apievangelist.com/guidance/naming/api-names/" target="_blank">API names</a> more via API Evangelist.
  message: APIs MUST have a name.
  given: $.apis.*
  severity: error
  then:
    field: name
    function: truthy
---