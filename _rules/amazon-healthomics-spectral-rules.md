---
api_specs:
- filename: amazon-healthomics-openapi.yaml
  format: yaml
  label: AWS HealthOmics API
  slug: aws-healthomics-api
  spec_type: OpenAPI
  url: https://raw.githubusercontent.com/api-evangelist/amazon-healthomics/refs/heads/main/openapi/amazon-healthomics-openapi.yaml
categories:
- healthomics
description: Spectral linting rules defining API design standards and conventions for Amazon HealthOmics.
layout: rules
name: Amazon HealthOmics API Rules
provider_name: Amazon HealthOmics
provider_slug: amazon-healthomics
rule_count: 8
rules:
- description: All operations must have a summary
  given: $.paths.*[get,post,put,patch,delete]
  name: healthomics-operation-summary
  severity: error
- description: All operations must have an operationId
  given: $.paths.*[get,post,put,patch,delete]
  name: healthomics-operation-id
  severity: error
- description: All operations should have tags
  given: $.paths.*[get,post,put,patch,delete]
  name: healthomics-operation-tags
  severity: warn
- description: All operations should have a 200 response
  given: $.paths.*[get,post,put,patch,delete].responses
  name: healthomics-response-200
  severity: warn
- description: Schema components should have descriptions
  given: $.components.schemas.*
  name: healthomics-schema-description
  severity: info
- description: Workflow operations should follow consistent naming
  given: $.paths.*[get,post,put,patch,delete]
  name: healthomics-workflow-operations
  severity: info
- description: Store operations should reference appropriate schemas
  given: $.paths.*[get,post,put,patch,delete][?(@property == 'operationId' && @.match('Store'))]
  name: healthomics-store-naming
  severity: info
- description: HealthOmics must document security requirements
  given: $.components.securitySchemes
  name: healthomics-security
  severity: error
rules_file: rules/amazon-healthomics-spectral-rules.yml
rules_url: https://raw.githubusercontent.com/api-evangelist/amazon-healthomics/refs/heads/main/rules/amazon-healthomics-spectral-rules.yml
severity_counts:
  error: 3
  hint: 0
  info: 3
  warn: 2
slug: amazon-healthomics-spectral-rules
source_filename: amazon-healthomics-spectral-rules.yml
source_heading: Spectral Ruleset
source_yaml: "rules:\n  healthomics-operation-summary:\n    description: All operations must have a summary\n    severity: error\n    given: \"$.paths.*[get,post,put,patch,delete]\"\n    then:\n      field: summary\n      function: truthy\n  healthomics-operation-id:\n    description: All operations must have an operationId\n    severity: error\n    given: \"$.paths.*[get,post,put,patch,delete]\"\n    then:\n      field: operationId\n      function: truthy\n  healthomics-operation-tags:\n    description: All operations should have tags\n    severity: warn\n    given: \"$.paths.*[get,post,put,patch,delete]\"\n    then:\n      field: tags\n      function: truthy\n  healthomics-response-200:\n    description: All operations should have a 200 response\n    severity: warn\n    given: \"$.paths.*[get,post,put,patch,delete].responses\"\n    then:\n      field: \"200\"\n      function: truthy\n  healthomics-schema-description:\n    description: Schema components should have descriptions\n    severity:\
  \ info\n    given: \"$.components.schemas.*\"\n    then:\n      field: description\n      function: truthy\n  healthomics-workflow-operations:\n    description: Workflow operations should follow consistent naming\n    severity: info\n    given: \"$.paths.*[get,post,put,patch,delete]\"\n    then:\n      field: operationId\n      function: truthy\n  healthomics-store-naming:\n    description: Store operations should reference appropriate schemas\n    severity: info\n    given: \"$.paths.*[get,post,put,patch,delete][?(@property == 'operationId' && @.match('Store'))]\"\n    then:\n      function: truthy\n  healthomics-security:\n    description: HealthOmics must document security requirements\n    severity: error\n    given: \"$.components.securitySchemes\"\n    then:\n      function: truthy\n"
source_yaml_url: https://raw.githubusercontent.com/api-evangelist/amazon-healthomics/refs/heads/main/rules/amazon-healthomics-spectral-rules.yml
tags:
- Bioinformatics
- Genomics
- Healthcare
- Life Sciences
- Cloud Computing
- Spectral
- Linting
- API Governance
---
