---
categories:
- api
- common
- documentation
- maintainer
- 'no'
- openapi
- property
- root
- specification
description: Spectral linting rules defining API design standards and conventions for APIs.json.
layout: rules
name: APIs.json API Rules
provider_name: APIs.json
provider_slug: apis-json
rule_count: 34
rules:
- description: APIs.json root must have a name field
  given: $
  name: root-name-required
  severity: error
- description: APIs.json root must have a description field
  given: $
  name: root-description-required
  severity: error
- description: APIs.json root must have a url field pointing to the file location
  given: $
  name: root-url-required
  severity: error
- description: APIs.json root url should use HTTPS
  given: $.url
  name: root-url-https
  severity: warn
- description: APIs.json root must have a created date
  given: $
  name: root-created-required
  severity: error
- description: APIs.json root must have a modified date
  given: $
  name: root-modified-required
  severity: error
- description: APIs.json root must have a specificationVersion field
  given: $
  name: root-specification-version-required
  severity: error
- description: APIs.json root should have an aid (unique identifier) field
  given: $
  name: root-aid-recommended
  severity: warn
- description: APIs.json aid should follow the format domain:string
  given: $.aid
  name: root-aid-format
  severity: warn
- description: APIs.json root should have maintainers defined
  given: $
  name: root-maintainers-recommended
  severity: warn
- description: APIs.json root should have tags for discoverability
  given: $
  name: root-tags-recommended
  severity: info
- description: APIs.json root should have an image URL for visual representation
  given: $
  name: root-image-recommended
  severity: info
- description: Maintainer entries must have an FN (full name) field
  given: $.maintainers[*]
  name: maintainer-fn-required
  severity: error
- description: Maintainer FN must not be empty
  given: $.maintainers[*].FN
  name: maintainer-fn-not-empty
  severity: error
- description: Maintainer email should be a valid email format
  given: $.maintainers[*].email
  name: maintainer-email-format
  severity: warn
- description: Each API entry must have an aid (unique identifier)
  given: $.apis[*]
  name: api-aid-required
  severity: error
- description: API aid should follow the format domain:string
  given: $.apis[*].aid
  name: api-aid-format
  severity: warn
- description: Each API entry must have a name
  given: $.apis[*]
  name: api-name-required
  severity: error
- description: Each API entry must have a description
  given: $.apis[*]
  name: api-description-required
  severity: error
- description: API description should be descriptive (at least 20 characters)
  given: $.apis[*].description
  name: api-description-min-length
  severity: warn
- description: Each API entry should have a humanURL
  given: $.apis[*]
  name: api-human-url-required
  severity: warn
- description: API humanURL should use HTTPS
  given: $.apis[*].humanURL
  name: api-human-url-https
  severity: warn
- description: API baseURL should use HTTPS
  given: $.apis[*].baseURL
  name: api-base-url-https
  severity: warn
- description: Each API entry should have tags for discoverability
  given: $.apis[*]
  name: api-tags-recommended
  severity: info
- description: Each API entry should have at least one property
  given: $.apis[*]
  name: api-properties-recommended
  severity: warn
- description: Common properties should include a Website entry
  given: $.common
  name: common-website-recommended
  severity: info
- description: Each property entry must have a type field
  given: $..properties[*]
  name: property-type-required
  severity: error
- description: Each property entry must have either a url or data field
  given: $..properties[*]
  name: property-url-or-data-required
  severity: error
- description: Property URLs should use HTTPS
  given: $..properties[*].url
  name: property-url-https
  severity: warn
- description: Name fields must not be empty strings
  given: $..name
  name: no-empty-names
  severity: error
- description: Description fields must not be empty strings
  given: $..description
  name: no-empty-descriptions
  severity: error
- description: specificationVersion should use the latest stable version (0.19)
  given: $.specificationVersion
  name: specification-version-current
  severity: info
- description: APIs should have a Documentation property for human-readable reference
  given: $.apis[*].properties[*].type
  name: documentation-property-recommended
  severity: info
- description: APIs should have an OpenAPI property for machine-readable interface definition
  given: $.apis[*].properties[*].type
  name: openapi-property-recommended
  severity: info
rules_file: rules/apis-json-spectral-rules.yml
rules_url: https://raw.githubusercontent.com/api-evangelist/apis-json/refs/heads/main/rules/apis-json-spectral-rules.yml
severity_counts:
  error: 15
  hint: 0
  info: 7
  warn: 12
slug: apis-json-spectral-rules
source_filename: apis-json-spectral-rules.yml
source_heading: Spectral Ruleset
source_yaml: "rules:\n  # ROOT LEVEL — REQUIRED FIELDS\n  root-name-required:\n    description: APIs.json root must have a name field\n    severity: error\n    given: \"$\"\n    then:\n      field: name\n      function: truthy\n\n  root-description-required:\n    description: APIs.json root must have a description field\n    severity: error\n    given: \"$\"\n    then:\n      field: description\n      function: truthy\n\n  root-url-required:\n    description: APIs.json root must have a url field pointing to the file location\n    severity: error\n    given: \"$\"\n    then:\n      field: url\n      function: truthy\n\n  root-url-https:\n    description: APIs.json root url should use HTTPS\n    severity: warn\n    given: \"$.url\"\n    then:\n      function: pattern\n      functionOptions:\n        match: \"^https://\"\n\n  root-created-required:\n    description: APIs.json root must have a created date\n    severity: error\n    given: \"$\"\n    then:\n      field: created\n      function:\
  \ truthy\n\n  root-modified-required:\n    description: APIs.json root must have a modified date\n    severity: error\n    given: \"$\"\n    then:\n      field: modified\n      function: truthy\n\n  root-specification-version-required:\n    description: APIs.json root must have a specificationVersion field\n    severity: error\n    given: \"$\"\n    then:\n      field: specificationVersion\n      function: truthy\n\n  root-aid-recommended:\n    description: APIs.json root should have an aid (unique identifier) field\n    severity: warn\n    given: \"$\"\n    then:\n      field: aid\n      function: truthy\n\n  root-aid-format:\n    description: APIs.json aid should follow the format domain:string\n    severity: warn\n    given: \"$.aid\"\n    then:\n      function: pattern\n      functionOptions:\n        match: \"^[a-z0-9.-]+:[a-z0-9._-]+$\"\n\n  root-maintainers-recommended:\n    description: APIs.json root should have maintainers defined\n    severity: warn\n    given: \"$\"\n    then:\n\
  \      field: maintainers\n      function: truthy\n\n  root-tags-recommended:\n    description: APIs.json root should have tags for discoverability\n    severity: info\n    given: \"$\"\n    then:\n      field: tags\n      function: truthy\n\n  root-image-recommended:\n    description: APIs.json root should have an image URL for visual representation\n    severity: info\n    given: \"$\"\n    then:\n      field: image\n      function: truthy\n\n  # MAINTAINERS\n  maintainer-fn-required:\n    description: Maintainer entries must have an FN (full name) field\n    severity: error\n    given: \"$.maintainers[*]\"\n    then:\n      field: FN\n      function: truthy\n\n  maintainer-fn-not-empty:\n    description: Maintainer FN must not be empty\n    severity: error\n    given: \"$.maintainers[*].FN\"\n    then:\n      function: minLength\n      functionOptions:\n        limit: 1\n\n  maintainer-email-format:\n    description: Maintainer email should be a valid email format\n    severity: warn\n\
  \    given: \"$.maintainers[*].email\"\n    then:\n      function: pattern\n      functionOptions:\n        match: \"^[^@]+@[^@]+\\\\.[^@]+$\"\n\n  # APIs ENTRIES\n  api-aid-required:\n    description: Each API entry must have an aid (unique identifier)\n    severity: error\n    given: \"$.apis[*]\"\n    then:\n      field: aid\n      function: truthy\n\n  api-aid-format:\n    description: API aid should follow the format domain:string\n    severity: warn\n    given: \"$.apis[*].aid\"\n    then:\n      function: pattern\n      functionOptions:\n        match: \"^[a-z0-9.-]+:[a-z0-9._-]+$\"\n\n  api-name-required:\n    description: Each API entry must have a name\n    severity: error\n    given: \"$.apis[*]\"\n    then:\n      field: name\n      function: truthy\n\n  api-description-required:\n    description: Each API entry must have a description\n    severity: error\n    given: \"$.apis[*]\"\n    then:\n      field: description\n      function: truthy\n\n  api-description-min-length:\n\
  \    description: API description should be descriptive (at least 20 characters)\n    severity: warn\n    given: \"$.apis[*].description\"\n    then:\n      function: minLength\n      functionOptions:\n        limit: 20\n\n  api-human-url-required:\n    description: Each API entry should have a humanURL\n    severity: warn\n    given: \"$.apis[*]\"\n    then:\n      field: humanURL\n      function: truthy\n\n  api-human-url-https:\n    description: API humanURL should use HTTPS\n    severity: warn\n    given: \"$.apis[*].humanURL\"\n    then:\n      function: pattern\n      functionOptions:\n        match: \"^https://\"\n\n  api-base-url-https:\n    description: API baseURL should use HTTPS\n    severity: warn\n    given: \"$.apis[*].baseURL\"\n    then:\n      function: pattern\n      functionOptions:\n        match: \"^https://\"\n\n  api-tags-recommended:\n    description: Each API entry should have tags for discoverability\n    severity: info\n    given: \"$.apis[*]\"\n    then:\n\
  \      field: tags\n      function: truthy\n\n  api-properties-recommended:\n    description: Each API entry should have at least one property\n    severity: warn\n    given: \"$.apis[*]\"\n    then:\n      field: properties\n      function: truthy\n\n  # COMMON PROPERTIES\n  common-website-recommended:\n    description: Common properties should include a Website entry\n    severity: info\n    given: \"$.common\"\n    then:\n      function: truthy\n\n  # PROPERTY ENTRIES\n  property-type-required:\n    description: Each property entry must have a type field\n    severity: error\n    given: \"$..properties[*]\"\n    then:\n      field: type\n      function: truthy\n\n  property-url-or-data-required:\n    description: Each property entry must have either a url or data field\n    severity: error\n    given: \"$..properties[*]\"\n    then:\n      function: truthy\n\n  property-url-https:\n    description: Property URLs should use HTTPS\n    severity: warn\n    given: \"$..properties[*].url\"\
  \n    then:\n      function: pattern\n      functionOptions:\n        match: \"^https://\"\n\n  # GENERAL QUALITY\n  no-empty-names:\n    description: Name fields must not be empty strings\n    severity: error\n    given: \"$..name\"\n    then:\n      function: pattern\n      functionOptions:\n        match: \".+\"\n\n  no-empty-descriptions:\n    description: Description fields must not be empty strings\n    severity: error\n    given: \"$..description\"\n    then:\n      function: pattern\n      functionOptions:\n        match: \".+\"\n\n  specification-version-current:\n    description: specificationVersion should use the latest stable version (0.19)\n    severity: info\n    given: \"$.specificationVersion\"\n    then:\n      function: pattern\n      functionOptions:\n        match: \"^0\\\\.(1[5-9]|[2-9][0-9])\"\n\n  documentation-property-recommended:\n    description: APIs should have a Documentation property for human-readable reference\n    severity: info\n    given: \"$.apis[*].properties[*].type\"\
  \n    then:\n      function: enumeration\n      functionOptions:\n        values:\n          - Documentation\n          - APIReference\n\n  openapi-property-recommended:\n    description: APIs should have an OpenAPI property for machine-readable interface definition\n    severity: info\n    given: \"$.apis[*].properties[*].type\"\n    then:\n      function: enumeration\n      functionOptions:\n        values:\n          - OpenAPI\n          - Swagger\n          - AsyncAPI\n"
source_yaml_url: https://raw.githubusercontent.com/api-evangelist/apis-json/refs/heads/main/rules/apis-json-spectral-rules.yml
tags:
- API Aggregation
- API Cataloging
- API Commons
- API Discovery
- API Governance
- API Operations
- Machine Readable
- Specification
- Standard
- Spectral
- Linting
- API Governance
---
