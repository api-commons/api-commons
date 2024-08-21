---
apis-json-modified-info:
  description: The modified property of an APIs.json is meant to be updated with the date of when any changes were made to the contract or index. The modified properties works in concert with the created property, as well as other change management properties employed to help get a handle on the changes that are inevitable across API operations. You can find details about the <a href="https://apisjson.org/schema/modified/">modified property for APIs.json</a>, and explore <a href="https://apievangelist.com/guidance/change/modified/" target="_blank">modified property and change management</a> more via API Evangelist.
  message: There is a modified date.
  given: $
  severity: info
  then:
    field: modified
    function: falsy
---