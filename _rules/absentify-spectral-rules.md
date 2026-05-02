---
api_specs:
- filename: absentify-openapi.yml
  format: yaml
  label: Absentify API
  slug: absentify
  spec_type: OpenAPI
  url: https://raw.githubusercontent.com/api-evangelist/absentify/refs/heads/main/openapi/absentify-openapi.yml
categories:
- absentify
description: Spectral linting rules defining API design standards and conventions for Absentify.
layout: rules
name: Absentify API Rules
provider_name: Absentify
provider_slug: absentify
rule_count: 15
rules:
- description: Every operation must have a summary
  given: $.paths[*][get,post,put,patch,delete]
  name: absentify-operation-must-have-summary
  severity: error
- description: Every operation must have a description
  given: $.paths[*][get,post,put,patch,delete]
  name: absentify-operation-must-have-description
  severity: warn
- description: Every operation must have an operationId
  given: $.paths[*][get,post,put,patch,delete]
  name: absentify-operation-must-have-operation-id
  severity: error
- description: Every operation must have at least one tag
  given: $.paths[*][get,post,put,patch,delete]
  name: absentify-operation-must-have-tags
  severity: warn
- description: Operation summaries should be in Title Case
  given: $.paths[*][get,post,put,patch,delete].summary
  name: absentify-summary-title-case
  severity: warn
- description: All parameters must have a description
  given: $.paths[*][get,post,put,patch,delete].parameters[*]
  name: absentify-parameters-must-have-description
  severity: warn
- description: Request body content must define a schema
  given: $.paths[*][post,put,patch].requestBody.content[*]
  name: absentify-request-body-must-have-schema
  severity: error
- description: Successful responses should define a schema
  given: $.paths[*][get,post,put,patch,delete].responses[200,201]
  name: absentify-response-must-have-schema
  severity: warn
- description: Operations should use ApiKeyAuth security
  given: $.paths[*][get,post,put,patch,delete]
  name: absentify-security-must-use-api-key
  severity: warn
- description: Schema properties must define a type
  given: $.components.schemas[*].properties[*]
  name: absentify-schema-properties-must-have-type
  severity: warn
- description: API info must have contact information
  given: $.info
  name: absentify-info-must-have-contact
  severity: warn
- description: API info must have license information
  given: $.info
  name: absentify-info-must-have-license
  severity: info
- description: At least one server must be defined
  given: $
  name: absentify-server-must-be-defined
  severity: error
- description: Components section should define reusable schemas
  given: $.components
  name: absentify-components-schemas-must-exist
  severity: warn
- description: Path segments should use kebab-case
  given: $.paths
  name: absentify-paths-must-use-kebab-case
  severity: info
rules_file: rules/absentify-spectral-rules.yml
rules_url: https://raw.githubusercontent.com/api-evangelist/absentify/refs/heads/main/rules/absentify-spectral-rules.yml
severity_counts:
  error: 4
  hint: 0
  info: 2
  warn: 9
slug: absentify-spectral-rules
source_filename: absentify-spectral-rules.yml
source_heading: Spectral Ruleset
source_yaml: "extends: [[spectral:oas, recommended]]\nrules:\n  absentify-operation-must-have-summary:\n    description: Every operation must have a summary\n    message: \"Operation {{path}} is missing a summary\"\n    severity: error\n    given: \"$.paths[*][get,post,put,patch,delete]\"\n    then:\n      field: summary\n      function: truthy\n\n  absentify-operation-must-have-description:\n    description: Every operation must have a description\n    message: \"Operation {{path}} is missing a description\"\n    severity: warn\n    given: \"$.paths[*][get,post,put,patch,delete]\"\n    then:\n      field: description\n      function: truthy\n\n  absentify-operation-must-have-operation-id:\n    description: Every operation must have an operationId\n    message: \"Operation {{path}} is missing an operationId\"\n    severity: error\n    given: \"$.paths[*][get,post,put,patch,delete]\"\n    then:\n      field: operationId\n      function: truthy\n\n  absentify-operation-must-have-tags:\n  \
  \  description: Every operation must have at least one tag\n    message: \"Operation {{path}} must have at least one tag\"\n    severity: warn\n    given: \"$.paths[*][get,post,put,patch,delete]\"\n    then:\n      field: tags\n      function: truthy\n\n  absentify-summary-title-case:\n    description: Operation summaries should be in Title Case\n    message: \"Summary '{{value}}' should start with 'Absentify'\"\n    severity: warn\n    given: \"$.paths[*][get,post,put,patch,delete].summary\"\n    then:\n      function: pattern\n      functionOptions:\n        match: \"^Absentify\"\n\n  absentify-parameters-must-have-description:\n    description: All parameters must have a description\n    message: \"Parameter {{path}} is missing a description\"\n    severity: warn\n    given: \"$.paths[*][get,post,put,patch,delete].parameters[*]\"\n    then:\n      field: description\n      function: truthy\n\n  absentify-request-body-must-have-schema:\n    description: Request body content must define\
  \ a schema\n    message: \"Request body at {{path}} must define a schema\"\n    severity: error\n    given: \"$.paths[*][post,put,patch].requestBody.content[*]\"\n    then:\n      field: schema\n      function: truthy\n\n  absentify-response-must-have-schema:\n    description: Successful responses should define a schema\n    message: \"Response at {{path}} should define a schema\"\n    severity: warn\n    given: \"$.paths[*][get,post,put,patch,delete].responses[200,201]\"\n    then:\n      field: content\n      function: truthy\n\n  absentify-security-must-use-api-key:\n    description: Operations should use ApiKeyAuth security\n    message: \"Operation {{path}} should specify security requirements\"\n    severity: warn\n    given: \"$.paths[*][get,post,put,patch,delete]\"\n    then:\n      field: security\n      function: truthy\n\n  absentify-schema-properties-must-have-type:\n    description: Schema properties must define a type\n    message: \"Schema property {{path}} must have a type\"\
  \n    severity: warn\n    given: \"$.components.schemas[*].properties[*]\"\n    then:\n      field: type\n      function: truthy\n\n  absentify-info-must-have-contact:\n    description: API info must have contact information\n    message: \"API info is missing contact information\"\n    severity: warn\n    given: \"$.info\"\n    then:\n      field: contact\n      function: truthy\n\n  absentify-info-must-have-license:\n    description: API info must have license information\n    message: \"API info is missing license information\"\n    severity: info\n    given: \"$.info\"\n    then:\n      field: license\n      function: truthy\n\n  absentify-server-must-be-defined:\n    description: At least one server must be defined\n    message: \"API must define at least one server\"\n    severity: error\n    given: \"$\"\n    then:\n      field: servers\n      function: truthy\n\n  absentify-components-schemas-must-exist:\n    description: Components section should define reusable schemas\n    message:\
  \ \"API should define component schemas for reusability\"\n    severity: warn\n    given: \"$.components\"\n    then:\n      field: schemas\n      function: truthy\n\n  absentify-paths-must-use-kebab-case:\n    description: Path segments should use kebab-case\n    message: \"Path {{path}} should use kebab-case or underscores for readability\"\n    severity: info\n    given: \"$.paths\"\n    then:\n      function: pattern\n      functionOptions:\n        match: \"^/[a-z0-9_/-{}]*$\"\n"
source_yaml_url: https://raw.githubusercontent.com/api-evangelist/absentify/refs/heads/main/rules/absentify-spectral-rules.yml
tags:
- Absence Management
- HR
- Leave Management
- Microsoft Teams
- Human Resources
- Spectral
- Linting
- API Governance
---
