---
apis-json-created-info:
  description: The created property is all about setting the timestamp for when an APIs.json index, contract, or other type is established--drawing a line in the sand for when everything started. The created property works in concert with the modified property and other change manage properties to understand and get a handle on the inevitable change that occurs across any API platform. You can find details about the <a href="https://apisjson.org/schema/created/">created property for APIs.json</a>, and explore <a href="https://apievangelist.com/guidance/change/created/" target="_blank">how created property is used to manage change</a> more via API Evangelist.
  message: There is a created date.
  given: $
  severity: info
  then:
    field: created
    function: falsy
---