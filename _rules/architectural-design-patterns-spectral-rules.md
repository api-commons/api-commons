---
api_specs:
- filename: architectural-design-patterns-api.yaml
  format: yaml
  label: Architectural Design Patterns API
  slug: architectural-design-patterns-api
  spec_type: OpenAPI
  url: https://raw.githubusercontent.com/api-evangelist/architectural-design-patterns/refs/heads/main/openapi/architectural-design-patterns-api.yaml
categories:
- adp
description: Spectral linting rules defining API design standards and conventions for Architectural Design Patterns.
layout: rules
name: Architectural Design Patterns API Rules
provider_name: Architectural Design Patterns
provider_slug: architectural-design-patterns
rule_count: 12
rules:
- description: Pattern must have an id field
  given: $.components.schemas.Pattern.properties
  name: adp-pattern-id-required
  severity: error
- description: Pattern must have a name field
  given: $.components.schemas.Pattern.properties
  name: adp-pattern-name-required
  severity: error
- description: Pattern must have a description field
  given: $.components.schemas.Pattern.properties
  name: adp-pattern-description-required
  severity: error
- description: Relationship type must be a valid enum value
  given: $.components.schemas.Relationship.properties.relationshipType
  name: adp-relationship-type-enum
  severity: error
- description: Pattern category must be a valid enum value
  given: $.paths./patterns.get.parameters[?(@.name=='category')].schema
  name: adp-category-enum
  severity: warn
- description: All API operations must have tags
  given: $.paths[*][get,post,put,patch,delete]
  name: adp-operations-have-tags
  severity: warn
- description: All API operations must have a summary
  given: $.paths[*][get,post,put,patch,delete]
  name: adp-operations-have-summary
  severity: error
- description: All API operations must have an operationId
  given: $.paths[*][get,post,put,patch,delete]
  name: adp-operations-have-operation-id
  severity: error
- description: List responses must include a total count
  given: $.components.schemas[*List].properties
  name: adp-list-responses-have-total
  severity: warn
- description: Anti-pattern must have a name field
  given: $.components.schemas.AntiPattern.properties
  name: adp-anti-pattern-name-required
  severity: error
- description: API info must include contact information
  given: $.info
  name: adp-info-contact-required
  severity: warn
- description: API must define at least one server
  given: $
  name: adp-servers-defined
  severity: error
rules_file: rules/architectural-design-patterns-spectral-rules.yml
rules_url: https://raw.githubusercontent.com/api-evangelist/architectural-design-patterns/refs/heads/main/rules/architectural-design-patterns-spectral-rules.yml
severity_counts:
  error: 8
  hint: 0
  info: 0
  warn: 4
slug: architectural-design-patterns-spectral-rules
source_filename: architectural-design-patterns-spectral-rules.yml
source_heading: Spectral Ruleset
source_yaml: "rules:\n  adp-pattern-id-required:\n    description: Pattern must have an id field\n    message: Pattern object must have an id property\n    severity: error\n    given: \"$.components.schemas.Pattern.properties\"\n    then:\n      field: id\n      function: truthy\n\n  adp-pattern-name-required:\n    description: Pattern must have a name field\n    message: Pattern object must have a name property\n    severity: error\n    given: \"$.components.schemas.Pattern.properties\"\n    then:\n      field: name\n      function: truthy\n\n  adp-pattern-description-required:\n    description: Pattern must have a description field\n    message: Pattern object must have a description property\n    severity: error\n    given: \"$.components.schemas.Pattern.properties\"\n    then:\n      field: description\n      function: truthy\n\n  adp-relationship-type-enum:\n    description: Relationship type must be a valid enum value\n    message: Relationship type must be uses, extends, alternative,\
  \ related, or conflicts\n    severity: error\n    given: \"$.components.schemas.Relationship.properties.relationshipType\"\n    then:\n      field: enum\n      function: truthy\n\n  adp-category-enum:\n    description: Pattern category must be a valid enum value\n    message: Pattern category must be a valid value\n    severity: warn\n    given: \"$.paths./patterns.get.parameters[?(@.name=='category')].schema\"\n    then:\n      field: enum\n      function: truthy\n\n  adp-operations-have-tags:\n    description: All API operations must have tags\n    message: Operation must include at least one tag\n    severity: warn\n    given: \"$.paths[*][get,post,put,patch,delete]\"\n    then:\n      field: tags\n      function: truthy\n\n  adp-operations-have-summary:\n    description: All API operations must have a summary\n    message: Operation must include a summary\n    severity: error\n    given: \"$.paths[*][get,post,put,patch,delete]\"\n    then:\n      field: summary\n      function: truthy\n\
  \n  adp-operations-have-operation-id:\n    description: All API operations must have an operationId\n    message: Operation must include an operationId\n    severity: error\n    given: \"$.paths[*][get,post,put,patch,delete]\"\n    then:\n      field: operationId\n      function: truthy\n\n  adp-list-responses-have-total:\n    description: List responses must include a total count\n    message: List schema must include a total property\n    severity: warn\n    given: \"$.components.schemas[*List].properties\"\n    then:\n      field: total\n      function: truthy\n\n  adp-anti-pattern-name-required:\n    description: Anti-pattern must have a name field\n    message: AntiPattern object must have a name property\n    severity: error\n    given: \"$.components.schemas.AntiPattern.properties\"\n    then:\n      field: name\n      function: truthy\n\n  adp-info-contact-required:\n    description: API info must include contact information\n    message: Info object must have a contact field\n\
  \    severity: warn\n    given: \"$.info\"\n    then:\n      field: contact\n      function: truthy\n\n  adp-servers-defined:\n    description: API must define at least one server\n    message: Servers array must be defined\n    severity: error\n    given: \"$\"\n    then:\n      field: servers\n      function: truthy\n"
source_yaml_url: https://raw.githubusercontent.com/api-evangelist/architectural-design-patterns/refs/heads/main/rules/architectural-design-patterns-spectral-rules.yml
tags:
- Design Patterns
- Software Architecture
- Best Practices
- Software Engineering
- System Design
- Microservices
- Spectral
- Linting
- API Governance
---
