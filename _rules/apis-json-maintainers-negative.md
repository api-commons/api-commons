---
apis-json-maintainers-error:
  description: The maintainers property is for identifying the entity who is maintaining an APIs.json contract, index, or other type. The maintainer may or may not be an API producer, and the maintainer property is used to provide access to the contact information for the maintainer, but is also used to validate the authoritative nature of the contract itself. You can find details about the <a href="https://apisjson.org/schema/maintianers/">maintainers property for APIs.json</a>, and explore <a href="https://apievangelist.com/guidance/support/names/" target="_blank">support</a> more via API Evangelist.
  message: There MUST be a maintainer object.
  given: $
  severity: error
  then:
    field: maintainers
    function: truthy
---