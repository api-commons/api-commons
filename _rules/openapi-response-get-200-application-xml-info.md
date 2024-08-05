---
openapi-response-get-200-application-xml-info:
  description: Has XML media type for GET.
  message: XML Media Type GET
  severity: info
  given: $.paths.*.get.responses.200.content
  then:
    field: application/xml
    function: falsy
---