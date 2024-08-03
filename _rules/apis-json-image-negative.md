---
apis-json-image-negative:
  description: Images for APIs.json help make them more visible when rendered as a search or individual node, used as part of an API portal, or other ways. The image should represent the entity logo, line of business, or other meaningful visual representation of the bounded context represented within the APis.json. You can find details about the <a href="https://apisjson.org/schema/images/">images property for APIs.json</a>, and explore <a href="https://apievangelist.com/guidance/images/apis-json-images/" target="_blank">using images</a> more via API Evangelist.
  message: There MUST be an image.
  given: $
  severity: error
  then:
    field: image
    function: truthy
---