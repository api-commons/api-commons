---
slug: apis-json-apis-tags-error
icon: style
name: APIs.json Apis Tags Error
description: >-
  Each API defined in an APIs.json artifact includes a property for adding one or more tags. These tags provide additional context about the resources or capabilities offered by the API, highlighting its business value and the domain in which it is applied.
message: API MUST Have a Tags Object
given: $.apis.*
severity: info
tags:
  - APIs.json
  - APIs
  - Tags
view_sort: I  
guidance: APIs Metadata
guidanceUrl: https://guidance.apievangelist.com/apis/metadata
rule:
  apis-json-apis-tags-error:
    description: >-
      Each API defined in an APIs.json artifact includes a property for adding one or more tags. These tags provide additional context about the resources or capabilities offered by the API, highlighting its business value and the domain in which it is applied.
    message: API MUST Have a Tags Object
    given: $.apis.*
    severity: info
    then:
      field: tags
      function: truthy
---