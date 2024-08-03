---
apis-json-apis-contact-email-positive:
  description: Providing an email address is a quick way to provide support for each API being indexed. Depending on whether it is public or private, the email may be an individual or wider, and associated with a team. You can find details about the <a href="https://apisjson.org/schema/apis-contact/">API contact property for APIs.json</a>, and explore <a href="https://apievangelist.com/guidance/support/email/" target="_blank">support emails</a> more via API Evangelist.
  message: API contact has email.
  given: $.apis.*.contact.*
  severity: info
  then:
    field: email
    function: falsy
---