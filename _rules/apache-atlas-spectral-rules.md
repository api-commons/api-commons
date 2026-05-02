---
api_specs:
- filename: apache-atlas-rest-openapi.yaml
  format: yaml
  label: Apache Atlas REST API
  slug: apache-atlas-rest-api
  spec_type: OpenAPI
  url: https://raw.githubusercontent.com/api-evangelist/apache-atlas/refs/heads/main/openapi/apache-atlas-rest-openapi.yaml
categories:
- get
- info
- operation
- parameter
- response
- security
- servers
description: Spectral linting rules defining API design standards and conventions for Apache Atlas.
layout: rules
name: Apache Atlas API Rules
provider_name: Apache Atlas
provider_slug: apache-atlas
rule_count: 12
rules:
- description: API title must start with "Apache Atlas"
  given: $.info.title
  name: info-title-prefix
  severity: warn
- description: ''
  given: $.info
  name: info-description-required
  severity: error
- description: ''
  given: $
  name: servers-defined
  severity: error
- description: ''
  given: $.paths[*][get,post,put,patch,delete]
  name: operation-summary-required
  severity: error
- description: ''
  given: $.paths[*][get,post,put,patch,delete].summary
  name: operation-summary-starts-with-apache-atlas
  severity: warn
- description: ''
  given: $.paths[*][get,post,put,patch,delete]
  name: operation-operationId-required
  severity: error
- description: ''
  given: $.paths[*][get,post,put,patch,delete]
  name: operation-tags-required
  severity: warn
- description: ''
  given: $.paths[*][get,post,put,patch,delete].parameters[*]
  name: parameter-description-required
  severity: warn
- description: ''
  given: $.paths[*][get,post,put,patch,delete].responses
  name: response-success-required
  severity: error
- description: ''
  given: $.paths[*][get,post,put,patch,delete].responses[*]
  name: response-description-required
  severity: error
- description: ''
  given: $.components
  name: security-schemes-defined
  severity: warn
- description: ''
  given: $.paths[*].get
  name: get-no-request-body
  severity: error
rules_file: rules/apache-atlas-spectral-rules.yml
rules_url: https://raw.githubusercontent.com/api-evangelist/apache-atlas/refs/heads/main/rules/apache-atlas-spectral-rules.yml
severity_counts:
  error: 7
  hint: 0
  info: 0
  warn: 5
slug: apache-atlas-spectral-rules
source_filename: apache-atlas-spectral-rules.yml
source_heading: Spectral Ruleset
source_yaml: "extends: spectral:oas\nrules:\n  info-title-prefix:\n    description: API title must start with \"Apache Atlas\"\n    severity: warn\n    given: \"$.info.title\"\n    then:\n      function: pattern\n      functionOptions:\n        match: \"^Apache Atlas\"\n  info-description-required:\n    severity: error\n    given: \"$.info\"\n    then:\n      field: description\n      function: truthy\n  servers-defined:\n    severity: error\n    given: \"$\"\n    then:\n      field: servers\n      function: truthy\n  operation-summary-required:\n    severity: error\n    given: \"$.paths[*][get,post,put,patch,delete]\"\n    then:\n      field: summary\n      function: truthy\n  operation-summary-starts-with-apache-atlas:\n    severity: warn\n    given: \"$.paths[*][get,post,put,patch,delete].summary\"\n    then:\n      function: pattern\n      functionOptions:\n        match: \"^Apache Atlas\"\n  operation-operationId-required:\n    severity: error\n    given: \"$.paths[*][get,post,put,patch,delete]\"\
  \n    then:\n      field: operationId\n      function: truthy\n  operation-tags-required:\n    severity: warn\n    given: \"$.paths[*][get,post,put,patch,delete]\"\n    then:\n      field: tags\n      function: truthy\n  parameter-description-required:\n    severity: warn\n    given: \"$.paths[*][get,post,put,patch,delete].parameters[*]\"\n    then:\n      field: description\n      function: truthy\n  response-success-required:\n    severity: error\n    given: \"$.paths[*][get,post,put,patch,delete].responses\"\n    then:\n      function: schema\n      functionOptions:\n        schema:\n          anyOf:\n            - required: ['200']\n            - required: ['201']\n            - required: ['204']\n  response-description-required:\n    severity: error\n    given: \"$.paths[*][get,post,put,patch,delete].responses[*]\"\n    then:\n      field: description\n      function: truthy\n  security-schemes-defined:\n    severity: warn\n    given: \"$.components\"\n    then:\n      field: securitySchemes\n\
  \      function: truthy\n  get-no-request-body:\n    severity: error\n    given: \"$.paths[*].get\"\n    then:\n      field: requestBody\n      function: falsy\n"
source_yaml_url: https://raw.githubusercontent.com/api-evangelist/apache-atlas/refs/heads/main/rules/apache-atlas-spectral-rules.yml
tags:
- Apache
- Big Data
- Compliance
- Data Governance
- Data Lineage
- Hadoop
- Metadata
- Open Source
- Spectral
- Linting
- API Governance
---
