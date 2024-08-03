---
apis-json-name-positive:
  description: The name of an APIs.json file is different than the name of your API, and is intended to describe the purpose of the APIs.json artifact, and what it provides for API producers, consumers, and other stakeholders. The name should be short and concise, describing the intent in bringing the the collection together, leaving the names of APIs to describe what each API does. You can find details about the <a href="https://apisjson.org/schema/names/">names property for APIs.json</a>, and explore <a href="https://apievangelist.com/guidance/naming/apis-json-names/" target="_blank">APIs.json names</a> more via API Evangelist.
  message: There is a name.
  severity: info
  given: $
  then:
    field: name
    function: falsy
---