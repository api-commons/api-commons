---
openapi-response-get-200-application-xml-schema-error:
  description: Require schema for GET.
  message: Application XML Schema for GET
  severity: error
  given: $.paths.*.get.responses.200.content.application/xml
  then:
    field: schema
    function: truthy
---