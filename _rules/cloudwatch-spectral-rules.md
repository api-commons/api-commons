---
api_specs:
- filename: openapi.yaml
  format: yaml
  label: Amazon CloudWatch API
  slug: ''
  spec_type: OpenAPI
  url: https://api.apis.guru/v2/specs/amazonaws.com/monitoring/2010-08-01/openapi.yaml
- filename: openapi.yaml
  format: yaml
  label: Amazon CloudWatch Logs API
  slug: ''
  spec_type: OpenAPI
  url: https://api.apis.guru/v2/specs/amazonaws.com/logs/2014-03-28/openapi.yaml
- filename: openapi.yaml
  format: yaml
  label: Amazon CloudWatch Events API
  slug: ''
  spec_type: OpenAPI
  url: https://api.apis.guru/v2/specs/amazonaws.com/events/2015-10-07/openapi.yaml
- filename: openapi.yaml
  format: yaml
  label: Amazon CloudWatch Application Insights API
  slug: ''
  spec_type: OpenAPI
  url: https://api.apis.guru/v2/specs/amazonaws.com/application-insights/2018-11-25/openapi.yaml
- filename: openapi.yaml
  format: yaml
  label: Amazon CloudWatch Synthetics API
  slug: ''
  spec_type: OpenAPI
  url: https://api.apis.guru/v2/specs/amazonaws.com/synthetics/2017-10-11/openapi.yaml
- filename: openapi.yaml
  format: yaml
  label: Amazon CloudWatch Internet Monitor API
  slug: ''
  spec_type: OpenAPI
  url: https://api.apis.guru/v2/specs/amazonaws.com/internetmonitor/2021-06-03/openapi.yaml
- filename: openapi.yaml
  format: yaml
  label: Amazon CloudWatch RUM API
  slug: ''
  spec_type: OpenAPI
  url: https://api.apis.guru/v2/specs/amazonaws.com/rum/2018-05-10/openapi.yaml
- filename: openapi.yaml
  format: yaml
  label: Amazon CloudWatch Observability Access Manager API
  slug: ''
  spec_type: OpenAPI
  url: https://api.apis.guru/v2/specs/amazonaws.com/oam/2022-06-10/openapi.yaml
categories:
- info
- 'no'
- operation
- response
description: Spectral linting rules defining API design standards and conventions for AWS CloudWatch.
layout: rules
name: AWS CloudWatch API Rules
provider_name: AWS CloudWatch
provider_slug: cloudwatch
rule_count: 7
rules:
- description: Info title must be present
  given: $.info
  name: info-title-required
  severity: error
- description: Info description must be present
  given: $.info
  name: info-description-required
  severity: error
- description: Every operation must have an operationId
  given: $.paths[*][get,post,put,patch,delete]
  name: operation-operationid-required
  severity: error
- description: Every operation must have a summary
  given: $.paths[*][get,post,put,patch,delete]
  name: operation-summary-required
  severity: error
- description: Every operation must have tags
  given: $.paths[*][get,post,put,patch,delete]
  name: operation-tags-required
  severity: error
- description: Every response must have a description
  given: $.paths[*][get,post,put,patch,delete].responses[*]
  name: response-description-required
  severity: error
- description: Descriptions must not be empty
  given: $..description
  name: no-empty-descriptions
  severity: error
rules_file: rules/cloudwatch-spectral-rules.yml
rules_url: https://raw.githubusercontent.com/api-evangelist/cloudwatch/refs/heads/main/rules/cloudwatch-spectral-rules.yml
severity_counts:
  error: 7
  hint: 0
  info: 0
  warn: 0
slug: cloudwatch-spectral-rules
source_filename: cloudwatch-spectral-rules.yml
source_heading: Spectral Ruleset
source_yaml: "rules:\n  info-title-required:\n    description: Info title must be present\n    severity: error\n    given: $.info\n    then: {field: title, function: truthy}\n  info-description-required:\n    description: Info description must be present\n    severity: error\n    given: $.info\n    then: {field: description, function: truthy}\n  operation-operationid-required:\n    description: Every operation must have an operationId\n    severity: error\n    given: $.paths[*][get,post,put,patch,delete]\n    then: {field: operationId, function: truthy}\n  operation-summary-required:\n    description: Every operation must have a summary\n    severity: error\n    given: $.paths[*][get,post,put,patch,delete]\n    then: {field: summary, function: truthy}\n  operation-tags-required:\n    description: Every operation must have tags\n    severity: error\n    given: $.paths[*][get,post,put,patch,delete]\n    then: {field: tags, function: truthy}\n  response-description-required:\n    description:\
  \ Every response must have a description\n    severity: error\n    given: $.paths[*][get,post,put,patch,delete].responses[*]\n    then: {field: description, function: truthy}\n  no-empty-descriptions:\n    description: Descriptions must not be empty\n    severity: error\n    given: $..description\n    then: {function: truthy}\n"
source_yaml_url: https://raw.githubusercontent.com/api-evangelist/cloudwatch/refs/heads/main/rules/cloudwatch-spectral-rules.yml
tags:
- Alarms
- Aws
- Dashboards
- Logs
- Metrics
- Monitoring
- Observability
- Spectral
- Linting
- API Governance
---
