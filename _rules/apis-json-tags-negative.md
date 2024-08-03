---
apis-json-tags-negative:
  description: Tags applied to an APIs.json should provide a handful of high-level tags that describe the purpose and intent of an APIs.json. These could be tags that describe the search node, or tags specifically for the individual APIs that are of concern for a specific API contract between producer and consumer. Tags provide the bounded context needed to help make APIs more tangible and meaningful for both API producers and consumers. You can find details about the <a href="https://apisjson.org/schema/tags/">tags property for APIs.json</a>, and explore <a href="https://apievangelist.com/guidance/bounded-context/apis-json-tags/" target="_blank">tagging</a> more via API Evangelist.
  message: There MUST be a tags object..
  given: $
  severity: error
  then:
    field: tags
    function: truthy
---