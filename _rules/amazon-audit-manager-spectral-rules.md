---
api_specs:
- filename: amazon-audit-manager-openapi.yml
  format: yaml
  label: Amazon Audit Manager API
  slug: amazon-audit-manager-api
  spec_type: OpenAPI
  url: https://raw.githubusercontent.com/api-evangelist/amazon-audit-manager/refs/heads/main/openapi/amazon-audit-manager-openapi.yml
categories:
- audit
description: Spectral linting rules defining API design standards and conventions for Amazon Audit Manager.
layout: rules
name: Amazon Audit Manager API Rules
provider_name: Amazon Audit Manager
provider_slug: amazon-audit-manager
rule_count: 15
rules:
- description: All operationIds must be camelCase
  given: $.paths[*][*].operationId
  name: audit-manager-operation-id-camel-case
  severity: warn
- description: All operation summaries must start with Amazon Audit Manager
  given: $.paths[*][*].summary
  name: audit-manager-summary-prefix
  severity: warn
- description: All operations must have tags
  given: $.paths[*][*]
  name: audit-manager-has-tags
  severity: warn
- description: All operations must have a 200 response
  given: $.paths[*][*].responses
  name: audit-manager-response-200
  severity: error
- description: CreateAssessmentRequest must require name
  given: $.components.schemas.CreateAssessmentRequest
  name: audit-manager-assessment-name-required
  severity: error
- description: AssessmentMetadata Status must use valid enum values
  given: $.components.schemas.AssessmentMetadata.properties.status
  name: audit-manager-assessment-status-enum
  severity: error
- description: AssessmentReport status must use valid enum values
  given: $.components.schemas.AssessmentReport.properties.status
  name: audit-manager-assessment-report-status-enum
  severity: error
- description: Framework type must use valid enum values
  given: $.components.schemas.Framework.properties.type
  name: audit-manager-framework-type-enum
  severity: error
- description: Control type must use valid enum values
  given: $.components.schemas.Control.properties.type
  name: audit-manager-control-type-enum
  severity: error
- description: Role roleType must use valid enum values
  given: $.components.schemas.Role.properties.roleType
  name: audit-manager-role-type-enum
  severity: error
- description: AssessmentReportsDestination type must use valid enum values
  given: $.components.schemas.AssessmentReportsDestination.properties.destinationType
  name: audit-manager-destination-type-enum
  severity: error
- description: API must use sigv4 security scheme
  given: $.security[*]
  name: audit-manager-security-sigv4
  severity: error
- description: Server URL must be fixed without variables
  given: $.servers[*]
  name: audit-manager-server-url-fixed
  severity: warn
- description: All examples must have x-microcks-default set to true
  given: $.paths[*][*].responses[*].content[*].examples.default
  name: audit-manager-example-microcks-default
  severity: warn
- description: Delegation status must use valid enum values
  given: $.components.schemas.Delegation.properties.status
  name: audit-manager-delegation-status-enum
  severity: error
rules_file: rules/amazon-audit-manager-spectral-rules.yml
rules_url: https://raw.githubusercontent.com/api-evangelist/amazon-audit-manager/refs/heads/main/rules/amazon-audit-manager-spectral-rules.yml
severity_counts:
  error: 10
  hint: 0
  info: 0
  warn: 5
slug: amazon-audit-manager-spectral-rules
source_filename: amazon-audit-manager-spectral-rules.yml
source_heading: Spectral Ruleset
source_yaml: "rules:\n  audit-manager-operation-id-camel-case:\n    description: All operationIds must be camelCase\n    message: \"{{property}} must be camelCase\"\n    severity: warn\n    given: \"$.paths[*][*].operationId\"\n    then:\n      function: pattern\n      functionOptions:\n        match: \"^[a-z][a-zA-Z0-9]*$\"\n\n  audit-manager-summary-prefix:\n    description: All operation summaries must start with Amazon Audit Manager\n    message: Summary must start with Amazon Audit Manager\n    severity: warn\n    given: \"$.paths[*][*].summary\"\n    then:\n      function: pattern\n      functionOptions:\n        match: \"^Amazon Audit Manager\"\n\n  audit-manager-has-tags:\n    description: All operations must have tags\n    message: Operation must have at least one tag\n    severity: warn\n    given: \"$.paths[*][*]\"\n    then:\n      field: tags\n      function: truthy\n\n  audit-manager-response-200:\n    description: All operations must have a 200 response\n    message: Operation\
  \ must define a 200 response\n    severity: error\n    given: \"$.paths[*][*].responses\"\n    then:\n      field: \"200\"\n      function: truthy\n\n  audit-manager-assessment-name-required:\n    description: CreateAssessmentRequest must require name\n    message: CreateAssessmentRequest must have name as required\n    severity: error\n    given: \"$.components.schemas.CreateAssessmentRequest\"\n    then:\n      field: required\n      function: truthy\n\n  audit-manager-assessment-status-enum:\n    description: AssessmentMetadata Status must use valid enum values\n    message: Status must be ACTIVE or INACTIVE\n    severity: error\n    given: \"$.components.schemas.AssessmentMetadata.properties.status\"\n    then:\n      field: enum\n      function: truthy\n\n  audit-manager-assessment-report-status-enum:\n    description: AssessmentReport status must use valid enum values\n    message: Status must be COMPLETE, IN_PROGRESS, or FAILED\n    severity: error\n    given: \"$.components.schemas.AssessmentReport.properties.status\"\
  \n    then:\n      field: enum\n      function: truthy\n\n  audit-manager-framework-type-enum:\n    description: Framework type must use valid enum values\n    message: Framework type must be Standard or Custom\n    severity: error\n    given: \"$.components.schemas.Framework.properties.type\"\n    then:\n      field: enum\n      function: truthy\n\n  audit-manager-control-type-enum:\n    description: Control type must use valid enum values\n    message: Control type must be Standard or Custom\n    severity: error\n    given: \"$.components.schemas.Control.properties.type\"\n    then:\n      field: enum\n      function: truthy\n\n  audit-manager-role-type-enum:\n    description: Role roleType must use valid enum values\n    message: roleType must be PROCESS_OWNER or RESOURCE_OWNER\n    severity: error\n    given: \"$.components.schemas.Role.properties.roleType\"\n    then:\n      field: enum\n      function: truthy\n\n  audit-manager-destination-type-enum:\n    description: AssessmentReportsDestination\
  \ type must use valid enum values\n    message: destinationType must be S3\n    severity: error\n    given: \"$.components.schemas.AssessmentReportsDestination.properties.destinationType\"\n    then:\n      field: enum\n      function: truthy\n\n  audit-manager-security-sigv4:\n    description: API must use sigv4 security scheme\n    message: Security must include sigv4\n    severity: error\n    given: \"$.security[*]\"\n    then:\n      field: sigv4\n      function: defined\n\n  audit-manager-server-url-fixed:\n    description: Server URL must be fixed without variables\n    message: Server URL must not use variables\n    severity: warn\n    given: \"$.servers[*]\"\n    then:\n      field: variables\n      function: falsy\n\n  audit-manager-example-microcks-default:\n    description: All examples must have x-microcks-default set to true\n    message: Example must have x-microcks-default true\n    severity: warn\n    given: \"$.paths[*][*].responses[*].content[*].examples.default\"\n \
  \   then:\n      field: x-microcks-default\n      function: truthy\n\n  audit-manager-delegation-status-enum:\n    description: Delegation status must use valid enum values\n    message: Delegation status must be IN_PROGRESS, UNDER_REVIEW, or COMPLETE\n    severity: error\n    given: \"$.components.schemas.Delegation.properties.status\"\n    then:\n      field: enum\n      function: truthy\n"
source_yaml_url: https://raw.githubusercontent.com/api-evangelist/amazon-audit-manager/refs/heads/main/rules/amazon-audit-manager-spectral-rules.yml
tags:
- Amazon Audit Manager
- Compliance
- Audit
- Risk Management
- Spectral
- Linting
- API Governance
---
