---
api_specs:
- filename: hcm.yml
  format: yaml
  label: Workday HCM API
  slug: hcm-api
  spec_type: OpenAPI
  url: https://raw.githubusercontent.com/api-evangelist/workday/refs/heads/main/openapi/hcm.yml
- filename: financialManagement.yml
  format: yaml
  label: Workday Financial Management API
  slug: financial-management-api
  spec_type: OpenAPI
  url: https://raw.githubusercontent.com/api-evangelist/workday/refs/heads/main/openapi/financialManagement.yml
- filename: recruiting.yml
  format: yaml
  label: Workday Recruiting API
  slug: recruiting-api
  spec_type: OpenAPI
  url: https://raw.githubusercontent.com/api-evangelist/workday/refs/heads/main/openapi/recruiting.yml
- filename: timeTracking.yml
  format: yaml
  label: Workday Time Tracking API
  slug: time-tracking-api
  spec_type: OpenAPI
  url: https://raw.githubusercontent.com/api-evangelist/workday/refs/heads/main/openapi/timeTracking.yml
- filename: benefits.yml
  format: yaml
  label: Workday Benefits API
  slug: benefits-api
  spec_type: OpenAPI
  url: https://raw.githubusercontent.com/api-evangelist/workday/refs/heads/main/openapi/benefits.yml
- filename: absenceManagement.yml
  format: yaml
  label: Workday Absence Management API
  slug: absence-management-api
  spec_type: OpenAPI
  url: https://raw.githubusercontent.com/api-evangelist/workday/refs/heads/main/openapi/absenceManagement.yml
- filename: compensation.yml
  format: yaml
  label: Workday Compensation API
  slug: compensation-api
  spec_type: OpenAPI
  url: https://raw.githubusercontent.com/api-evangelist/workday/refs/heads/main/openapi/compensation.yml
- filename: payroll.yml
  format: yaml
  label: Workday Payroll API
  slug: payroll-api
  spec_type: OpenAPI
  url: https://raw.githubusercontent.com/api-evangelist/workday/refs/heads/main/openapi/payroll.yml
- filename: person.yml
  format: yaml
  label: Workday Person API
  slug: person-api
  spec_type: OpenAPI
  url: https://raw.githubusercontent.com/api-evangelist/workday/refs/heads/main/openapi/person.yml
- filename: performanceManagement.yml
  format: yaml
  label: Workday Performance Management API
  slug: performance-management-api
  spec_type: OpenAPI
  url: https://raw.githubusercontent.com/api-evangelist/workday/refs/heads/main/openapi/performanceManagement.yml
- filename: talent.yml
  format: yaml
  label: Workday Talent Management API
  slug: talent-management-api
  spec_type: OpenAPI
  url: https://raw.githubusercontent.com/api-evangelist/workday/refs/heads/main/openapi/talent.yml
- filename: common.yml
  format: yaml
  label: Workday Common API
  slug: common-api
  spec_type: OpenAPI
  url: https://raw.githubusercontent.com/api-evangelist/workday/refs/heads/main/openapi/common.yml
- filename: staffing.yml
  format: yaml
  label: Workday Staffing API
  slug: staffing-api
  spec_type: OpenAPI
  url: https://raw.githubusercontent.com/api-evangelist/workday/refs/heads/main/openapi/staffing.yml
- filename: prismAnalytics.yml
  format: yaml
  label: Workday Prism Analytics API
  slug: prism-analytics-api
  spec_type: OpenAPI
  url: https://raw.githubusercontent.com/api-evangelist/workday/refs/heads/main/openapi/prismAnalytics.yml
- filename: raas.yml
  format: yaml
  label: Workday Report-as-a-Service API
  slug: raas-api
  spec_type: OpenAPI
  url: https://raw.githubusercontent.com/api-evangelist/workday/refs/heads/main/openapi/raas.yml
- filename: wql.yml
  format: yaml
  label: Workday WQL API
  slug: wql-api
  spec_type: OpenAPI
  url: https://raw.githubusercontent.com/api-evangelist/workday/refs/heads/main/openapi/wql.yml
categories:
- info
- 'no'
- operation
- response
description: Spectral linting rules defining API design standards and conventions for Workday.
layout: rules
name: Workday API Rules
provider_name: Workday
provider_slug: workday
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
rules_file: rules/workday-spectral-rules.yml
rules_url: https://raw.githubusercontent.com/api-evangelist/workday/refs/heads/main/rules/workday-spectral-rules.yml
severity_counts:
  error: 7
  hint: 0
  info: 0
  warn: 0
slug: workday-spectral-rules
source_filename: workday-spectral-rules.yml
source_heading: Spectral Ruleset
source_yaml: "rules:\n  info-title-required:\n    description: Info title must be present\n    severity: error\n    given: $.info\n    then: {field: title, function: truthy}\n  info-description-required:\n    description: Info description must be present\n    severity: error\n    given: $.info\n    then: {field: description, function: truthy}\n  operation-operationid-required:\n    description: Every operation must have an operationId\n    severity: error\n    given: $.paths[*][get,post,put,patch,delete]\n    then: {field: operationId, function: truthy}\n  operation-summary-required:\n    description: Every operation must have a summary\n    severity: error\n    given: $.paths[*][get,post,put,patch,delete]\n    then: {field: summary, function: truthy}\n  operation-tags-required:\n    description: Every operation must have tags\n    severity: error\n    given: $.paths[*][get,post,put,patch,delete]\n    then: {field: tags, function: truthy}\n  response-description-required:\n    description:\
  \ Every response must have a description\n    severity: error\n    given: $.paths[*][get,post,put,patch,delete].responses[*]\n    then: {field: description, function: truthy}\n  no-empty-descriptions:\n    description: Descriptions must not be empty\n    severity: error\n    given: $..description\n    then: {function: truthy}\n"
source_yaml_url: https://raw.githubusercontent.com/api-evangelist/workday/refs/heads/main/rules/workday-spectral-rules.yml
tags:
- Cloud Computing
- Enterprise Software
- Financial Management
- HCM
- SaaS
- Spectral
- Linting
- API Governance
---
