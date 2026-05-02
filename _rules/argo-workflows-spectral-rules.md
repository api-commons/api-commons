---
api_specs:
- filename: argo-workflows-openapi.json
  format: json
  label: Argo Workflows API
  slug: argo-workflows
  spec_type: OpenAPI
  url: https://raw.githubusercontent.com/api-evangelist/argo-workflows/refs/heads/main/openapi/argo-workflows-openapi.json
categories:
- info
- 'no'
- operation
- parameter
- paths
- response
- security
description: Spectral linting rules defining API design standards and conventions for Argo Workflows.
layout: rules
name: Argo Workflows API Rules
provider_name: Argo Workflows
provider_slug: argo-workflows
rule_count: 13
rules:
- description: API title must start with "Argo Workflows"
  given: $.info.title
  name: info-title-prefix
  severity: warn
- description: API must have a description
  given: $.info
  name: info-description-required
  severity: error
- description: Every operation must have a summary
  given: $.paths[*][get,post,put,delete,patch]
  name: operation-summary-required
  severity: error
- description: Operation summaries must start with "Argo Workflows"
  given: $.paths[*][get,post,put,delete,patch].summary
  name: operation-summary-prefix
  severity: warn
- description: Every operation must have an operationId
  given: $.paths[*][get,post,put,delete,patch]
  name: operation-operationid-required
  severity: error
- description: Every operation must have at least one tag
  given: $.paths[*][get,post,put,delete,patch]
  name: operation-tags-required
  severity: warn
- description: All paths should be versioned
  given: $.paths[*]~
  name: paths-versioned
  severity: info
- description: Path segments should use kebab-case or camelCase
  given: $.paths[*]~
  name: paths-kebab-case
  severity: info
- description: Every operation must define at least one response
  given: $.paths[*][get,post,put,delete,patch].responses
  name: response-success-required
  severity: error
- description: All responses must have a description
  given: $.paths[*][get,post,put,delete,patch].responses[*]
  name: response-description-required
  severity: warn
- description: API must define security schemes
  given: $
  name: security-definitions-required
  severity: warn
- description: Summaries must not be empty
  given: $.paths[*][get,post,put,delete,patch].summary
  name: no-empty-summaries
  severity: error
- description: Parameters should have descriptions
  given: $.paths[*][get,post,put,delete,patch].parameters[*]
  name: parameter-description-required
  severity: warn
rules_file: rules/argo-workflows-spectral-rules.yml
rules_url: https://raw.githubusercontent.com/api-evangelist/argo-workflows/refs/heads/main/rules/argo-workflows-spectral-rules.yml
severity_counts:
  error: 5
  hint: 0
  info: 2
  warn: 6
slug: argo-workflows-spectral-rules
source_filename: argo-workflows-spectral-rules.yml
source_heading: Spectral Ruleset
source_yaml: "# Argo Workflows API Spectral Ruleset\n\nrules:\n\n  info-title-prefix:\n    description: API title must start with \"Argo Workflows\"\n    severity: warn\n    given: \"$.info.title\"\n    then:\n      function: pattern\n      functionOptions:\n        match: \"^Argo Workflows\"\n\n  info-description-required:\n    description: API must have a description\n    severity: error\n    given: \"$.info\"\n    then:\n      field: description\n      function: truthy\n\n  operation-summary-required:\n    description: Every operation must have a summary\n    severity: error\n    given: \"$.paths[*][get,post,put,delete,patch]\"\n    then:\n      field: summary\n      function: truthy\n\n  operation-summary-prefix:\n    description: Operation summaries must start with \"Argo Workflows\"\n    severity: warn\n    given: \"$.paths[*][get,post,put,delete,patch].summary\"\n    then:\n      function: pattern\n      functionOptions:\n        match: \"^Argo Workflows\"\n\n  operation-operationid-required:\n\
  \    description: Every operation must have an operationId\n    severity: error\n    given: \"$.paths[*][get,post,put,delete,patch]\"\n    then:\n      field: operationId\n      function: truthy\n\n  operation-tags-required:\n    description: Every operation must have at least one tag\n    severity: warn\n    given: \"$.paths[*][get,post,put,delete,patch]\"\n    then:\n      field: tags\n      function: truthy\n\n  paths-versioned:\n    description: All paths should be versioned\n    severity: info\n    given: \"$.paths[*]~\"\n    then:\n      function: pattern\n      functionOptions:\n        match: \"^/api/v\"\n\n  paths-kebab-case:\n    description: Path segments should use kebab-case or camelCase\n    severity: info\n    given: \"$.paths[*]~\"\n    then:\n      function: pattern\n      functionOptions:\n        match: \"^(/api/v[0-9]+)?(/[a-zA-Z0-9{}-]+)*$\"\n\n  response-success-required:\n    description: Every operation must define at least one response\n    severity: error\n  \
  \  given: \"$.paths[*][get,post,put,delete,patch].responses\"\n    then:\n      function: schema\n      functionOptions:\n        schema:\n          type: object\n          minProperties: 1\n\n  response-description-required:\n    description: All responses must have a description\n    severity: warn\n    given: \"$.paths[*][get,post,put,delete,patch].responses[*]\"\n    then:\n      field: description\n      function: truthy\n\n  security-definitions-required:\n    description: API must define security schemes\n    severity: warn\n    given: \"$\"\n    then:\n      field: securityDefinitions\n      function: truthy\n\n  no-empty-summaries:\n    description: Summaries must not be empty\n    severity: error\n    given: \"$.paths[*][get,post,put,delete,patch].summary\"\n    then:\n      function: pattern\n      functionOptions:\n        match: \".+\"\n\n  parameter-description-required:\n    description: Parameters should have descriptions\n    severity: warn\n    given: \"$.paths[*][get,post,put,delete,patch].parameters[*]\"\
  \n    then:\n      field: description\n      function: truthy\n"
source_yaml_url: https://raw.githubusercontent.com/api-evangelist/argo-workflows/refs/heads/main/rules/argo-workflows-spectral-rules.yml
tags:
- CNCF
- Containers
- Data Processing
- Kubernetes
- Machine Learning
- Open Source
- Workflow Engine
- Spectral
- Linting
- API Governance
---
