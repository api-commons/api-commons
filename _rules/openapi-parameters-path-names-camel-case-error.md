---
openapi-parameters-path-names-camel-case-error:
  description: Warn parameter path name camel case.
  message: Parameter Path Name Camel Case
  severity: warn
  given: $.paths.*.*.parameters[?(@.in=='path')].name
  then:
    field: '@key'
    function: casing
    functionOptions:
      type: camel
---