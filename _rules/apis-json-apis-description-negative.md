---
apis-json-apis-description-negative:
  description: The description of each API is how you make your first impression on consumers, and is what will likely show in portals, networks, search, and other ways that API consumers discover APIs and onboard with them. Make the description of an API talk about what it does, and the value it brings to consumers, not about the structure and standards used--those can be expressed in other ways. You can find details about the <a href="https://apisjson.org/schema/description/">description property for APIs.json</a>, and explore <a href="https://apievangelist.com/guidance/descriptions/api-descriptions/" target="_blank">API descriptons</a> more via API Evangelist.
  message: APIs MUST have a description.
  given: $.apis.*
  severity: error
  then:
    field: description
    function: truthy
---