---
apis-json-apis-contact-fn-negative:
  description: The purpose of the FN is to specify the formatted text corresponding to the contact name in the vCard for an API. It could be a persons name or wider for a domain, team, or other bounded context, providing the reference needed for support or feedback. You can find details about the <a href="https://apisjson.org/schema/apis-contact/">API contact property for APIs.json</a>, and explore <a href="https://apievangelist.com/guidance/support/name/" target="_blank">support name</a> more via API Evangelist.
  message: API contact COULD have FN.
  given: $.apis.*.contact.*
  severity: error
  then:
    field: FN
    function: truthy
---