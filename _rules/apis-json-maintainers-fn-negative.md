---
apis-json-maintainers-fn-error:
  description: The purpose of the FN is to specify the formatted text corresponding to the contact name in the vCard for an APIs.json contract or index. It could be a persons name or wider for a domain, team, or other bounded context, providing the reference needed for support or feedback. You can find details about the <a href="https://apisjson.org/schema/maintainers-fn/">API contact property for APIs.json</a>, and explore <a href="https://apievangelist.com/guidance/support/name/" target="_blank">support name</a> more via API Evangelist.
  message: There MUST be a FN property for maintainers.
  given: $.maintainers.*
  severity: error
  then:
    field: FN
    function: truthy
---