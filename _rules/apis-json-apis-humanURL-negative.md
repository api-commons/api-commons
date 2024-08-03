---
apis-json-apis-humanURL-negative:
  description: The human URL for an API provides a link for any business or technical consumer to use when learning more about an API and onboarding with it. In some cases it can be directly to documentation, but ideally each API has its own landing page with a simple and intuitive URL, and has links to all of the properties API consumers will need for an API. You can find details about the <a href="https://apisjson.org/schema/human-url/">humanUrl property for APIs.json</a>, and explore <a href="https://apievangelist.com/guidance/documentation/human-url/" target="_blank">Human URLs</a> more via API Evangelist.
  message: APIs MUST have a human URL.
  given: $.apis.*
  severity: error
  then:
    field: humanURL
    function: truthy
---