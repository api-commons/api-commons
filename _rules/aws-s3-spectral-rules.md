---
api_specs:
- filename: aws-s3-openapi.yaml
  format: yaml
  label: Amazon S3 REST API
  slug: amazon-s3-rest-api
  spec_type: OpenAPI
  url: https://raw.githubusercontent.com/api-evangelist/aws-s3/refs/heads/main/openapi/aws-s3-openapi.yaml
categories:
- s3
description: Spectral linting rules defining API design standards and conventions for Amazon S3 API.
layout: rules
name: Amazon S3 API API Rules
provider_name: Amazon S3 API
provider_slug: aws-s3
rule_count: 10
rules:
- description: All operations must have a summary starting with "Amazon S3"
  given: $.paths[*][get,post,put,delete,patch,head]
  name: s3-operation-summary
  severity: warn
- description: All operations must have an operationId
  given: $.paths[*][get,post,put,delete,patch,head]
  name: s3-operation-id
  severity: error
- description: Info object must have a title
  given: $.info
  name: s3-info-title
  severity: error
- description: Info object must have a version
  given: $.info
  name: s3-info-version
  severity: error
- description: All responses must have a description
  given: $.paths[*][*].responses[*]
  name: s3-response-description
  severity: error
- description: All parameters should have a description
  given: $.paths[*][*].parameters[*]
  name: s3-parameter-description
  severity: warn
- description: Operations should have x-microcks-operation annotation
  given: $.paths[*][get,post,put,delete,patch,head]
  name: s3-microcks-annotation
  severity: info
- description: Schema components should have a type
  given: $.components.schemas[*]
  name: s3-schema-type
  severity: warn
- description: API security schemes should be defined
  given: $
  name: s3-security-defined
  severity: warn
- description: Servers array should be defined
  given: $
  name: s3-servers-defined
  severity: warn
rules_file: rules/aws-s3-spectral-rules.yml
rules_url: https://raw.githubusercontent.com/api-evangelist/aws-s3/refs/heads/main/rules/aws-s3-spectral-rules.yml
severity_counts:
  error: 4
  hint: 0
  info: 1
  warn: 5
slug: aws-s3-spectral-rules
source_filename: aws-s3-spectral-rules.yml
source_heading: Spectral Ruleset
source_yaml: "rules:\n  s3-operation-summary:\n    description: All operations must have a summary starting with \"Amazon S3\"\n    severity: warn\n    given: \"$.paths[*][get,post,put,delete,patch,head]\"\n    then:\n      field: summary\n      function: pattern\n      functionOptions:\n        match: \"^Amazon S3\"\n  s3-operation-id:\n    description: All operations must have an operationId\n    severity: error\n    given: \"$.paths[*][get,post,put,delete,patch,head]\"\n    then:\n      field: operationId\n      function: truthy\n  s3-info-title:\n    description: Info object must have a title\n    severity: error\n    given: \"$.info\"\n    then:\n      field: title\n      function: truthy\n  s3-info-version:\n    description: Info object must have a version\n    severity: error\n    given: \"$.info\"\n    then:\n      field: version\n      function: truthy\n  s3-response-description:\n    description: All responses must have a description\n    severity: error\n    given: \"$.paths[*][*].responses[*]\"\
  \n    then:\n      field: description\n      function: truthy\n  s3-parameter-description:\n    description: All parameters should have a description\n    severity: warn\n    given: \"$.paths[*][*].parameters[*]\"\n    then:\n      field: description\n      function: truthy\n  s3-microcks-annotation:\n    description: Operations should have x-microcks-operation annotation\n    severity: info\n    given: \"$.paths[*][get,post,put,delete,patch,head]\"\n    then:\n      field: x-microcks-operation\n      function: truthy\n  s3-schema-type:\n    description: Schema components should have a type\n    severity: warn\n    given: \"$.components.schemas[*]\"\n    then:\n      field: type\n      function: truthy\n  s3-security-defined:\n    description: API security schemes should be defined\n    severity: warn\n    given: \"$\"\n    then:\n      field: components.securitySchemes\n      function: truthy\n  s3-servers-defined:\n    description: Servers array should be defined\n    severity: warn\n\
  \    given: \"$\"\n    then:\n      field: servers\n      function: truthy\n"
source_yaml_url: https://raw.githubusercontent.com/api-evangelist/aws-s3/refs/heads/main/rules/aws-s3-spectral-rules.yml
tags:
- Cloud Storage
- Object Storage
- Storage
- Spectral
- Linting
- API Governance
---
