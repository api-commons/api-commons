---
api_specs:
- filename: architecture-pattern-api.yaml
  format: yaml
  label: Architecture Pattern API
  slug: architecture-pattern-api
  spec_type: OpenAPI
  url: https://raw.githubusercontent.com/api-evangelist/architecture-pattern/refs/heads/main/openapi/architecture-pattern-api.yaml
categories:
- ap
description: Spectral linting rules defining API design standards and conventions for Architecture Pattern.
layout: rules
name: Architecture Pattern API Rules
provider_name: Architecture Pattern
provider_slug: architecture-pattern
rule_count: 12
rules:
- description: Pattern must have an id field
  given: $.components.schemas.Pattern.properties
  name: ap-pattern-id-required
  severity: error
- description: Pattern must have a name field
  given: $.components.schemas.Pattern.properties
  name: ap-pattern-name-required
  severity: error
- description: Pattern must have a problem statement
  given: $.components.schemas.Pattern.properties
  name: ap-pattern-problem-required
  severity: warn
- description: Pattern must have a solution description
  given: $.components.schemas.Pattern.properties
  name: ap-pattern-solution-required
  severity: warn
- description: Pattern confidence must be a valid enum value
  given: $.components.schemas.Pattern.properties.confidence
  name: ap-pattern-confidence-enum
  severity: error
- description: Tradeoff severity must be a valid enum value
  given: $.components.schemas.Tradeoff.properties.severity
  name: ap-tradeoff-severity-enum
  severity: error
- description: List responses must include a total count
  given: $.components.schemas[*List].properties
  name: ap-list-responses-have-total
  severity: warn
- description: All API operations must have tags
  given: $.paths[*][get,post,put,patch,delete]
  name: ap-operations-have-tags
  severity: warn
- description: All API operations must have a summary
  given: $.paths[*][get,post,put,patch,delete]
  name: ap-operations-have-summary
  severity: error
- description: All API operations must have an operationId
  given: $.paths[*][get,post,put,patch,delete]
  name: ap-operations-have-operation-id
  severity: error
- description: API info must include contact information
  given: $.info
  name: ap-info-contact-required
  severity: warn
- description: API must define at least one server
  given: $
  name: ap-servers-defined
  severity: error
rules_file: rules/architecture-pattern-spectral-rules.yml
rules_url: https://raw.githubusercontent.com/api-evangelist/architecture-pattern/refs/heads/main/rules/architecture-pattern-spectral-rules.yml
severity_counts:
  error: 7
  hint: 0
  info: 0
  warn: 5
slug: architecture-pattern-spectral-rules
source_filename: architecture-pattern-spectral-rules.yml
source_heading: Spectral Ruleset
source_yaml: "rules:\n  ap-pattern-id-required:\n    description: Pattern must have an id field\n    message: Pattern object must have an id property\n    severity: error\n    given: \"$.components.schemas.Pattern.properties\"\n    then:\n      field: id\n      function: truthy\n\n  ap-pattern-name-required:\n    description: Pattern must have a name field\n    message: Pattern object must have a name property\n    severity: error\n    given: \"$.components.schemas.Pattern.properties\"\n    then:\n      field: name\n      function: truthy\n\n  ap-pattern-problem-required:\n    description: Pattern must have a problem statement\n    message: Pattern object must have a problem property\n    severity: warn\n    given: \"$.components.schemas.Pattern.properties\"\n    then:\n      field: problem\n      function: truthy\n\n  ap-pattern-solution-required:\n    description: Pattern must have a solution description\n    message: Pattern object must have a solution property\n    severity: warn\n \
  \   given: \"$.components.schemas.Pattern.properties\"\n    then:\n      field: solution\n      function: truthy\n\n  ap-pattern-confidence-enum:\n    description: Pattern confidence must be a valid enum value\n    message: Pattern confidence must be proven, candidate, or experimental\n    severity: error\n    given: \"$.components.schemas.Pattern.properties.confidence\"\n    then:\n      field: enum\n      function: truthy\n\n  ap-tradeoff-severity-enum:\n    description: Tradeoff severity must be a valid enum value\n    message: Tradeoff severity must be low, medium, or high\n    severity: error\n    given: \"$.components.schemas.Tradeoff.properties.severity\"\n    then:\n      field: enum\n      function: truthy\n\n  ap-list-responses-have-total:\n    description: List responses must include a total count\n    message: List schema must include a total property\n    severity: warn\n    given: \"$.components.schemas[*List].properties\"\n    then:\n      field: total\n      function: truthy\n\
  \n  ap-operations-have-tags:\n    description: All API operations must have tags\n    message: Operation must include at least one tag\n    severity: warn\n    given: \"$.paths[*][get,post,put,patch,delete]\"\n    then:\n      field: tags\n      function: truthy\n\n  ap-operations-have-summary:\n    description: All API operations must have a summary\n    message: Operation must include a summary\n    severity: error\n    given: \"$.paths[*][get,post,put,patch,delete]\"\n    then:\n      field: summary\n      function: truthy\n\n  ap-operations-have-operation-id:\n    description: All API operations must have an operationId\n    message: Operation must include an operationId\n    severity: error\n    given: \"$.paths[*][get,post,put,patch,delete]\"\n    then:\n      field: operationId\n      function: truthy\n\n  ap-info-contact-required:\n    description: API info must include contact information\n    message: Info object must have a contact field\n    severity: warn\n    given: \"$.info\"\
  \n    then:\n      field: contact\n      function: truthy\n\n  ap-servers-defined:\n    description: API must define at least one server\n    message: Servers array must be defined\n    severity: error\n    given: \"$\"\n    then:\n      field: servers\n      function: truthy\n"
source_yaml_url: https://raw.githubusercontent.com/api-evangelist/architecture-pattern/refs/heads/main/rules/architecture-pattern-spectral-rules.yml
tags:
- Architecture Patterns
- Software Architecture
- Design Patterns
- System Design
- Microservices
- Cloud Native
- Spectral
- Linting
- API Governance
---
