---
openapi-response-get-200-application-xml-schema-info:
  description: Has schema for GET.
  message: Application XML Schema for GET
  severity: info
  given: $.paths.*.get.responses.200.content.application/xml
  then:
    field: schema
    function: falsy
---