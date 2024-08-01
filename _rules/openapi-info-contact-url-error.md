---
openapi-info-contact-url-error:
  description: Requires contact url.
  message: Contact URL
  given: $.info.contact
  severity: error
  then:
    field: url
    function: truthy
---