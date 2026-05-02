---
api_specs:
- filename: aoc-data-api.yaml
  format: yaml
  label: Architect of the Capitol Data API
  slug: aoc-data-api
  spec_type: OpenAPI
  url: https://raw.githubusercontent.com/api-evangelist/architect-of-the-capitol/refs/heads/main/openapi/aoc-data-api.yaml
categories:
- aoc
description: Spectral linting rules defining API design standards and conventions for Architect of the Capitol.
layout: rules
name: Architect of the Capitol API Rules
provider_name: Architect of the Capitol
provider_slug: architect-of-the-capitol
rule_count: 13
rules:
- description: Building responses must include an id field
  given: $.components.schemas.Building.properties
  name: aoc-building-id-required
  severity: error
- description: Building responses must include a name field
  given: $.components.schemas.Building.properties
  name: aoc-building-name-required
  severity: error
- description: Artwork responses must include a title field
  given: $.components.schemas.Artwork.properties
  name: aoc-artwork-title-required
  severity: error
- description: Artwork responses must include an artist field
  given: $.components.schemas.Artwork.properties
  name: aoc-artwork-artist-required
  severity: error
- description: Preservation project status must be a valid enum value
  given: $.components.schemas.PreservationProject.properties.status
  name: aoc-preservation-status-enum
  severity: error
- description: List responses must include a total count
  given: $.components.schemas[*List].properties
  name: aoc-list-responses-have-total
  severity: warn
- description: List responses must include a limit field
  given: $.components.schemas[*List].properties
  name: aoc-list-responses-have-limit
  severity: warn
- description: All API operations must have tags
  given: $.paths[*][get,post,put,patch,delete]
  name: aoc-operations-have-tags
  severity: warn
- description: All API operations must have a summary
  given: $.paths[*][get,post,put,patch,delete]
  name: aoc-operations-have-summary
  severity: error
- description: All API operations must have an operationId
  given: $.paths[*][get,post,put,patch,delete]
  name: aoc-operations-have-operation-id
  severity: error
- description: Path parameters must have descriptions
  given: $.paths[*][*].parameters[?(@.in=='path')]
  name: aoc-path-parameters-described
  severity: warn
- description: API info must include contact information
  given: $.info
  name: aoc-info-contact-required
  severity: warn
- description: API must define at least one server
  given: $
  name: aoc-servers-defined
  severity: error
rules_file: rules/aoc-spectral-rules.yml
rules_url: https://raw.githubusercontent.com/api-evangelist/architect-of-the-capitol/refs/heads/main/rules/aoc-spectral-rules.yml
severity_counts:
  error: 8
  hint: 0
  info: 0
  warn: 5
slug: aoc-spectral-rules
source_filename: aoc-spectral-rules.yml
source_heading: Spectral Ruleset
source_yaml: "rules:\n  aoc-building-id-required:\n    description: Building responses must include an id field\n    message: Building object must have an id property\n    severity: error\n    given: \"$.components.schemas.Building.properties\"\n    then:\n      field: id\n      function: truthy\n\n  aoc-building-name-required:\n    description: Building responses must include a name field\n    message: Building object must have a name property\n    severity: error\n    given: \"$.components.schemas.Building.properties\"\n    then:\n      field: name\n      function: truthy\n\n  aoc-artwork-title-required:\n    description: Artwork responses must include a title field\n    message: Artwork object must have a title property\n    severity: error\n    given: \"$.components.schemas.Artwork.properties\"\n    then:\n      field: title\n      function: truthy\n\n  aoc-artwork-artist-required:\n    description: Artwork responses must include an artist field\n    message: Artwork object must have\
  \ an artist property\n    severity: error\n    given: \"$.components.schemas.Artwork.properties\"\n    then:\n      field: artist\n      function: truthy\n\n  aoc-preservation-status-enum:\n    description: Preservation project status must be a valid enum value\n    message: PreservationProject status must be planned, active, or completed\n    severity: error\n    given: \"$.components.schemas.PreservationProject.properties.status\"\n    then:\n      field: enum\n      function: truthy\n\n  aoc-list-responses-have-total:\n    description: List responses must include a total count\n    message: List schema must include a total property\n    severity: warn\n    given: \"$.components.schemas[*List].properties\"\n    then:\n      field: total\n      function: truthy\n\n  aoc-list-responses-have-limit:\n    description: List responses must include a limit field\n    message: List schema must include a limit property\n    severity: warn\n    given: \"$.components.schemas[*List].properties\"\n\
  \    then:\n      field: limit\n      function: truthy\n\n  aoc-operations-have-tags:\n    description: All API operations must have tags\n    message: Operation must include at least one tag\n    severity: warn\n    given: \"$.paths[*][get,post,put,patch,delete]\"\n    then:\n      field: tags\n      function: truthy\n\n  aoc-operations-have-summary:\n    description: All API operations must have a summary\n    message: Operation must include a summary\n    severity: error\n    given: \"$.paths[*][get,post,put,patch,delete]\"\n    then:\n      field: summary\n      function: truthy\n\n  aoc-operations-have-operation-id:\n    description: All API operations must have an operationId\n    message: Operation must include an operationId\n    severity: error\n    given: \"$.paths[*][get,post,put,patch,delete]\"\n    then:\n      field: operationId\n      function: truthy\n\n  aoc-path-parameters-described:\n    description: Path parameters must have descriptions\n    message: Path parameter\
  \ should include a description\n    severity: warn\n    given: \"$.paths[*][*].parameters[?(@.in=='path')]\"\n    then:\n      field: description\n      function: truthy\n\n  aoc-info-contact-required:\n    description: API info must include contact information\n    message: Info object must have a contact field\n    severity: warn\n    given: \"$.info\"\n    then:\n      field: contact\n      function: truthy\n\n  aoc-servers-defined:\n    description: API must define at least one server\n    message: Servers array must be defined and non-empty\n    severity: error\n    given: \"$\"\n    then:\n      field: servers\n      function: truthy\n"
source_yaml_url: https://raw.githubusercontent.com/api-evangelist/architect-of-the-capitol/refs/heads/main/rules/aoc-spectral-rules.yml
tags:
- Federal Government
- Capitol Hill
- Congress
- Historic Preservation
- Government Services
- Spectral
- Linting
- API Governance
---
