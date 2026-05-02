---
name: OpenAPI Tags Alphabetical Error
description: >-
  The tags used to organize operations should be available in an alphabetical format keeping easy to navigate for consumers.
message: Tags MUST Be Alphabetical
given: $.tags[*]
severity: error
tags:
  - OpenAPI
  - Tags
  - Default
references:
  - name: Doctor
    type: Editor
    url: https://pb33f.io/doctor/
  - name: Spectral
    type: Linter
    url: https://github.com/stoplightio/spectral/blob/develop/packages/rulesets/src/oas/index.ts    
guidance: OpenAPI
guidanceUrl: https://guidance.apievangelist.com/openapi
rule:
  openapi-tags-name-error:
    description: >-
      The tags used to organize operations should be available in an alphabetical format keeping easy to navigate for consumers.
    message: Tags MUST Be Alphabetical
    given: $.tags[*]
    severity: error
    then:
      field: name
      function: alphabetical
      functionOptions: 
        keyedBy: 'name'
slug: openapi-tags-alphabetical-error
---