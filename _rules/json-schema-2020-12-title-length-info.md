---
name: JSON Schema Draft 2020-12 Title Length info
description: The title of JSON Schema objects should be concise yet accurately describe the object's purpose. Keeping the title short ensures clarity and minimizes downstream impact on other items using the object.
slug: json-schema-2020-12-title-length-error
engine: Unknown
specification: Unknown
specificationUrl: https://example.com
guidance: API Evangelist
guidanceUrl: https://guidance.apievangelist.com
severity: info
type: Default
tags:
  - JSON Schema
  - Metadata
view_sort: EA
rule:
  json-schema-2020-12-title-length-info:
    description: Schema names and resulting title should be kept to greater than 3 characters.
    message: Schema Names MUST Be Greater Than 3 Characters
    severity: info
    given: $
    then:
      field: title
      function: length
      functionOptions:
        min: 3                 

---