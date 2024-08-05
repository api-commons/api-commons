---
openapi-response-get-200-application-xml-error:
  description: Require XML media type for GET.
  message: XML Media Type GET
  severity: error
  given: $.paths.*.get.responses.200.content
  then:
    field: application/xml
    function: truthy
---