---
apis-json-apis-contact-positive:
  description: The contact object provides the ability to associate a vCard that represents an individual or any organization entity with common contact information like a name, email, or other reference, providing a standardized way of supporting an API. You can find details about the <a href="https://apisjson.org/schema/apis-contact/">API contact property for APIs.json</a>, and explore <a href="https://apievangelist.com/guidance/support/contact/" target="_blank">support contact</a> more via API Evangelist.
  message: API has a contact.
  severity: info
  given:
    - $.apis.*
  then:
    field: contact
    function: falsy
---