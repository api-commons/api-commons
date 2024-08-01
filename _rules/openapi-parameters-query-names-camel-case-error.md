---
openapi-parameters-query-names-camel-case-error:
  description: Warn parameter query name camel case.
  message: Parameter Query Name Camel Case
  severity: warn
  given: $.paths.*.*.parameters[?(@.in=='query')].*
  then:
    field: name
    function: casing
    functionOptions:
      type: camel
---