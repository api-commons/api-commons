---
api_specs:
- filename: amazon-healthimaging-openapi.yaml
  format: yaml
  label: AWS HealthImaging API
  slug: aws-healthimaging-api
  spec_type: OpenAPI
  url: https://raw.githubusercontent.com/api-evangelist/amazon-healthimaging/refs/heads/main/openapi/amazon-healthimaging-openapi.yaml
categories:
- healthimaging
description: Spectral linting rules defining API design standards and conventions for Amazon HealthImaging.
layout: rules
name: Amazon HealthImaging API Rules
provider_name: Amazon HealthImaging
provider_slug: amazon-healthimaging
rule_count: 8
rules:
- description: All operations must have a summary
  given: $.paths.*[get,post,put,patch,delete]
  name: healthimaging-operation-summary
  severity: error
- description: All operations must have an operationId
  given: $.paths.*[get,post,put,patch,delete]
  name: healthimaging-operation-id
  severity: error
- description: All operations should have tags
  given: $.paths.*[get,post,put,patch,delete]
  name: healthimaging-operation-tags
  severity: warn
- description: All operations should have a 200 response
  given: $.paths.*[get,post,put,patch,delete].responses
  name: healthimaging-response-200
  severity: warn
- description: Schema components should have descriptions
  given: $.components.schemas.*
  name: healthimaging-schema-description
  severity: info
- description: Datastore operations should have consistent naming
  given: $.paths.*[get,post,put,patch,delete]
  name: healthimaging-datastore-naming
  severity: info
- description: HIPAA-eligible service must document security requirements
  given: $.components.securitySchemes
  name: healthimaging-hipaa-security
  severity: error
- description: Tag operations should follow consistent patterns
  given: $.paths.*[get,post,put,patch,delete][?(@property == 'tags')]
  name: healthimaging-tag-management
  severity: info
rules_file: rules/amazon-healthimaging-spectral-rules.yml
rules_url: https://raw.githubusercontent.com/api-evangelist/amazon-healthimaging/refs/heads/main/rules/amazon-healthimaging-spectral-rules.yml
severity_counts:
  error: 3
  hint: 0
  info: 3
  warn: 2
slug: amazon-healthimaging-spectral-rules
source_filename: amazon-healthimaging-spectral-rules.yml
source_heading: Spectral Ruleset
source_yaml: "rules:\n  healthimaging-operation-summary:\n    description: All operations must have a summary\n    severity: error\n    given: \"$.paths.*[get,post,put,patch,delete]\"\n    then:\n      field: summary\n      function: truthy\n  healthimaging-operation-id:\n    description: All operations must have an operationId\n    severity: error\n    given: \"$.paths.*[get,post,put,patch,delete]\"\n    then:\n      field: operationId\n      function: truthy\n  healthimaging-operation-tags:\n    description: All operations should have tags\n    severity: warn\n    given: \"$.paths.*[get,post,put,patch,delete]\"\n    then:\n      field: tags\n      function: truthy\n  healthimaging-response-200:\n    description: All operations should have a 200 response\n    severity: warn\n    given: \"$.paths.*[get,post,put,patch,delete].responses\"\n    then:\n      field: \"200\"\n      function: truthy\n  healthimaging-schema-description:\n    description: Schema components should have descriptions\n\
  \    severity: info\n    given: \"$.components.schemas.*\"\n    then:\n      field: description\n      function: truthy\n  healthimaging-datastore-naming:\n    description: Datastore operations should have consistent naming\n    severity: info\n    given: \"$.paths.*[get,post,put,patch,delete]\"\n    then:\n      field: operationId\n      function: truthy\n  healthimaging-hipaa-security:\n    description: HIPAA-eligible service must document security requirements\n    severity: error\n    given: \"$.components.securitySchemes\"\n    then:\n      function: truthy\n  healthimaging-tag-management:\n    description: Tag operations should follow consistent patterns\n    severity: info\n    given: \"$.paths.*[get,post,put,patch,delete][?(@property == 'tags')]\"\n    then:\n      function: truthy\n"
source_yaml_url: https://raw.githubusercontent.com/api-evangelist/amazon-healthimaging/refs/heads/main/rules/amazon-healthimaging-spectral-rules.yml
tags:
- Healthcare
- HIPAA
- Machine Learning
- Medical Imaging
- DICOM
- Spectral
- Linting
- API Governance
---
