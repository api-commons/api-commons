---
apis-json-apis-image-error:
  description: A dedicated image for each API, providing a visual representation of the resource or capability being made available via an API helps make it more approachable and visually appealing in portals, documentation, and via other content format. Images should be simple, consistent, and should avoid just being company logos and other less precise visual representations. You can find details about the <a href="https://apisjson.org/schema/images/">images property for APIs.json</a>, and explore <a href="https://apievangelist.com/guidance/images/apis-json-images/" target="_blank">API images</a> more via API Evangelist.
  message: APIs MUST have an image.
  given: $.apis.*
  severity: error
  then:
    field: image
    function: truthy
---