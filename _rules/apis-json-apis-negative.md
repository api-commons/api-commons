---
apis-json-apis-negative:
  description: The APIs property provides the ability to define one or many APIs, as part of a larger collection or contract. What constitutes an API s up to the maintainer of the collection, and will vary depending on what the APIs.json contract is defining between producer and consumer. Depending on the scope of an API the sweet spot for the number of APIs is about 250, but could go up to 300 or 400 when necessary, keeping API definitions serving the purpose of the APIs.json artifact. You can find details about the <a href="https://apisjson.org/schema/apis/">baseUrl property for APIs.json</a>, and explore <a href="https://apievangelist.com/guidance/bounded-context/apis/" target="_blank">APIs</a> more via API Evangelist.
  message: There MUST be an APIs property.
  given: $
  severity: error
  then:
    field: apis
    function: truthy
---