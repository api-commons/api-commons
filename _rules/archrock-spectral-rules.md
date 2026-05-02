---
api_specs:
- filename: archrock-investor-relations-api.yaml
  format: yaml
  label: Archrock Investor Relations API
  slug: archrock-investor-relations-api
  spec_type: OpenAPI
  url: https://raw.githubusercontent.com/api-evangelist/archrock/refs/heads/main/openapi/archrock-investor-relations-api.yaml
categories:
- archrock
description: Spectral linting rules defining API design standards and conventions for Archrock.
layout: rules
name: Archrock API Rules
provider_name: Archrock
provider_slug: archrock
rule_count: 12
rules:
- description: Quarterly financials must include year
  given: $.components.schemas.QuarterlyFinancials.properties
  name: archrock-quarterly-year-required
  severity: error
- description: Fleet statistics must include utilization rate
  given: $.components.schemas.FleetStatistics.properties
  name: archrock-fleet-utilization-rate
  severity: error
- description: Equipment status must be a valid enum value
  given: $.components.schemas.Equipment.properties.status
  name: archrock-equipment-status-enum
  severity: error
- description: SEC filing type must be a valid enum value
  given: $.components.schemas.SecFiling.properties.type
  name: archrock-sec-filing-type-enum
  severity: error
- description: List responses must include a total count
  given: $.components.schemas[*List].properties
  name: archrock-list-responses-have-total
  severity: warn
- description: List responses must include a limit field
  given: $.components.schemas[*List].properties
  name: archrock-list-responses-have-limit
  severity: warn
- description: All API operations must have tags
  given: $.paths[*][get,post,put,patch,delete]
  name: archrock-operations-have-tags
  severity: warn
- description: All API operations must have a summary
  given: $.paths[*][get,post,put,patch,delete]
  name: archrock-operations-have-summary
  severity: error
- description: All API operations must have an operationId
  given: $.paths[*][get,post,put,patch,delete]
  name: archrock-operations-have-operation-id
  severity: error
- description: API must use API key security scheme
  given: $.components.securitySchemes
  name: archrock-api-key-security
  severity: warn
- description: API info must include contact information
  given: $.info
  name: archrock-info-contact-required
  severity: warn
- description: API must define at least one server
  given: $
  name: archrock-servers-defined
  severity: error
rules_file: rules/archrock-spectral-rules.yml
rules_url: https://raw.githubusercontent.com/api-evangelist/archrock/refs/heads/main/rules/archrock-spectral-rules.yml
severity_counts:
  error: 7
  hint: 0
  info: 0
  warn: 5
slug: archrock-spectral-rules
source_filename: archrock-spectral-rules.yml
source_heading: Spectral Ruleset
source_yaml: "rules:\n  archrock-quarterly-year-required:\n    description: Quarterly financials must include year\n    message: QuarterlyFinancials must have a year property\n    severity: error\n    given: \"$.components.schemas.QuarterlyFinancials.properties\"\n    then:\n      field: year\n      function: truthy\n\n  archrock-fleet-utilization-rate:\n    description: Fleet statistics must include utilization rate\n    message: FleetStatistics must have a utilizationRate property\n    severity: error\n    given: \"$.components.schemas.FleetStatistics.properties\"\n    then:\n      field: utilizationRate\n      function: truthy\n\n  archrock-equipment-status-enum:\n    description: Equipment status must be a valid enum value\n    message: Equipment status must be active, idle, or maintenance\n    severity: error\n    given: \"$.components.schemas.Equipment.properties.status\"\n    then:\n      field: enum\n      function: truthy\n\n  archrock-sec-filing-type-enum:\n    description: SEC\
  \ filing type must be a valid enum value\n    message: SecFiling type must be a valid SEC form type\n    severity: error\n    given: \"$.components.schemas.SecFiling.properties.type\"\n    then:\n      field: enum\n      function: truthy\n\n  archrock-list-responses-have-total:\n    description: List responses must include a total count\n    message: List schema must include a total property\n    severity: warn\n    given: \"$.components.schemas[*List].properties\"\n    then:\n      field: total\n      function: truthy\n\n  archrock-list-responses-have-limit:\n    description: List responses must include a limit field\n    message: List schema must include a limit property\n    severity: warn\n    given: \"$.components.schemas[*List].properties\"\n    then:\n      field: limit\n      function: truthy\n\n  archrock-operations-have-tags:\n    description: All API operations must have tags\n    message: Operation must include at least one tag\n    severity: warn\n    given: \"$.paths[*][get,post,put,patch,delete]\"\
  \n    then:\n      field: tags\n      function: truthy\n\n  archrock-operations-have-summary:\n    description: All API operations must have a summary\n    message: Operation must include a summary\n    severity: error\n    given: \"$.paths[*][get,post,put,patch,delete]\"\n    then:\n      field: summary\n      function: truthy\n\n  archrock-operations-have-operation-id:\n    description: All API operations must have an operationId\n    message: Operation must include an operationId\n    severity: error\n    given: \"$.paths[*][get,post,put,patch,delete]\"\n    then:\n      field: operationId\n      function: truthy\n\n  archrock-api-key-security:\n    description: API must use API key security scheme\n    message: API should define an ApiKey security scheme\n    severity: warn\n    given: \"$.components.securitySchemes\"\n    then:\n      field: ApiKeyAuth\n      function: truthy\n\n  archrock-info-contact-required:\n    description: API info must include contact information\n    message:\
  \ Info object must have a contact field\n    severity: warn\n    given: \"$.info\"\n    then:\n      field: contact\n      function: truthy\n\n  archrock-servers-defined:\n    description: API must define at least one server\n    message: Servers array must be defined\n    severity: error\n    given: \"$\"\n    then:\n      field: servers\n      function: truthy\n"
source_yaml_url: https://raw.githubusercontent.com/api-evangelist/archrock/refs/heads/main/rules/archrock-spectral-rules.yml
tags:
- Natural Gas
- Compression Services
- Oil And Gas
- Energy
- Industrial
- 'NYSE: AROC'
- Spectral
- Linting
- API Governance
---
