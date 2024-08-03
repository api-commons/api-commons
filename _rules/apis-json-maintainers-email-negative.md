---
apis-json-maintainers-email-negative:
  description: The maintainers email is to provide a quick way to contact the maintainer of an APIs.json contract. The email is just one of multiple vCard properties that can exist, but provides the simplest way to engage with stakeholders involved in maintaining an APIs.json artifact. You can find details about the <a href="https://apisjson.org/schema/maintainers-email/">maintainers email property for APIs.json</a>, and explore <a href="https://apievangelist.com/guidance/support/email/" target="_blank">email support</a> more via API Evangelist.
  message: There MUST be an email property for maintainers.
  given: $.maintainers.*
  severity: error
  then:
    field: email
    function: truthy
---