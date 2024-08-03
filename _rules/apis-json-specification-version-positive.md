---
apis-json-specification-version-positive:
  description: The specification version of an APIs.json defines what properties are supported by the APIs.json artifact. New core properties, as well as property types are being added with each version to support a variety of solutions, and expand how APIs.json is used across API operations. You can find details about the <a href="https://apisjson.org/schema/specification-version/">specification version property for APIs.json</a>.
  message: There is a specification version.
  severity: info
  given: $
  then:
    field: specificationVersion
    function: falsy
---