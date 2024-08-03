---
apis-json-common-negative:
  description: The common property is where all of the properties that apply across multiple APIs are stored. If the APIs.json is maintained by the API producer they are usually the common services supported via the developer portal, but if not, they could be external services offered by community, platform, or other entities. You can find details about the <a href="https://apisjson.org/schema/common/">baseUrl property for APIs.json</a>, and explore <a href="https://apievangelist.com/guidance/discovery/common/" target="_blank">common discovery properties</a> more via API Evangelist.
  message: There MUST be a common property.
  given: $
  severity: error
  then:
    field: common
    function: truthy
---