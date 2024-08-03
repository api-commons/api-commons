---
apis-json-description-negative:
  description: The description property is where you provide full details the purpose an APIs.json serves. This description is likely more higher level than any of the descriptions for any single API, and be more about the contract, index, blueprint, or the other reasons why the APIs.json is of value. Don't make the description too long, but also don't make it too short--it is likely the first impression you will make via portals, repos, and other ways an APIs.json will be discovered. You can find details about the <a href="https://apisjson.org/schema/description/">description property for APIs.json</a>, and explore <a href="https://apievangelist.com/guidance/descriptions/apis-json-descriptions/" target="_blank">APIs.json</a> more via API Evangelist.
  message: There MUST be a description.
  given: $
  severity: error
  then:
    field: description
    function: truthy
---