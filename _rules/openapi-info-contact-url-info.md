---
openapi-info-contact-url-info:
  description: Has contact url.
  message: Contact URL
  given: $.info.contact
  severity: info
  then:
    field: url
    function: falsy
---