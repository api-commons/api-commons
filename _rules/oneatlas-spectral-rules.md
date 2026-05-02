---
categories:
- oneatlas
description: Spectral linting rules defining API design standards and conventions for Airbus OneAtlas.
layout: rules
name: Airbus OneAtlas API Rules
provider_name: Airbus OneAtlas
provider_slug: airbus-oneatlas
rule_count: 12
rules:
- description: All operation summaries must use Title Case
  given: $.paths[*][get,post,put,patch,delete]
  name: oneatlas-operation-summary-title-case
  severity: warn
- description: All operations must have an operationId
  given: $.paths[*][get,post,put,patch,delete]
  name: oneatlas-require-operation-id
  severity: error
- description: All operations must have tags
  given: $.paths[*][get,post,put,patch,delete]
  name: oneatlas-require-operation-tags
  severity: warn
- description: GET operations must define a 200 response
  given: $.paths[*].get
  name: oneatlas-require-response-200
  severity: error
- description: Component schemas must have a title
  given: $.components.schemas[*]
  name: oneatlas-schema-title-required
  severity: warn
- description: All operations must include API key security
  given: $
  name: oneatlas-require-api-key-security
  severity: error
- description: API must define at least one server
  given: $
  name: oneatlas-require-server-url
  severity: error
- description: API info must have a description
  given: $.info
  name: oneatlas-require-info-description
  severity: warn
- description: API should reference external documentation
  given: $
  name: oneatlas-require-external-docs
  severity: warn
- description: All operations must have a description
  given: $.paths[*][get,post,put,patch,delete]
  name: oneatlas-require-operation-description
  severity: warn
- description: Geometry schemas must specify a type field
  given: $.components.schemas[?(@.description =~ /.*[Gg]eometr.*/)]
  name: oneatlas-geometry-type-required
  severity: warn
- description: CatalogItem schema must include id and geometry
  given: $.components.schemas.CatalogItem.properties
  name: oneatlas-catalog-item-required-fields
  severity: warn
rules_file: rules/oneatlas-spectral-rules.yml
rules_url: https://raw.githubusercontent.com/api-evangelist/airbus-oneatlas/refs/heads/main/rules/oneatlas-spectral-rules.yml
severity_counts:
  error: 4
  hint: 0
  info: 0
  warn: 8
slug: oneatlas-spectral-rules
source_filename: oneatlas-spectral-rules.yml
source_heading: Spectral Ruleset
source_yaml: "rules:\n  oneatlas-operation-summary-title-case:\n    description: All operation summaries must use Title Case\n    severity: warn\n    given: $.paths[*][get,post,put,patch,delete]\n    then:\n      field: summary\n      function: pattern\n      functionOptions:\n        match: ^[A-Z]\n  oneatlas-require-operation-id:\n    description: All operations must have an operationId\n    severity: error\n    given: $.paths[*][get,post,put,patch,delete]\n    then:\n      field: operationId\n      function: truthy\n  oneatlas-require-operation-tags:\n    description: All operations must have tags\n    severity: warn\n    given: $.paths[*][get,post,put,patch,delete]\n    then:\n      field: tags\n      function: truthy\n  oneatlas-require-response-200:\n    description: GET operations must define a 200 response\n    severity: error\n    given: $.paths[*].get\n    then:\n      field: responses.200\n      function: truthy\n  oneatlas-schema-title-required:\n    description: Component schemas\
  \ must have a title\n    severity: warn\n    given: $.components.schemas[*]\n    then:\n      field: title\n      function: truthy\n  oneatlas-require-api-key-security:\n    description: All operations must include API key security\n    severity: error\n    given: $\n    then:\n      field: security\n      function: truthy\n  oneatlas-require-server-url:\n    description: API must define at least one server\n    severity: error\n    given: $\n    then:\n      field: servers\n      function: truthy\n  oneatlas-require-info-description:\n    description: API info must have a description\n    severity: warn\n    given: $.info\n    then:\n      field: description\n      function: truthy\n  oneatlas-require-external-docs:\n    description: API should reference external documentation\n    severity: warn\n    given: $\n    then:\n      field: externalDocs\n      function: truthy\n  oneatlas-require-operation-description:\n    description: All operations must have a description\n    severity:\
  \ warn\n    given: $.paths[*][get,post,put,patch,delete]\n    then:\n      field: description\n      function: truthy\n  oneatlas-geometry-type-required:\n    description: Geometry schemas must specify a type field\n    severity: warn\n    given: $.components.schemas[?(@.description =~ /.*[Gg]eometr.*/)]\n    then:\n      field: properties.type\n      function: truthy\n  oneatlas-catalog-item-required-fields:\n    description: CatalogItem schema must include id and geometry\n    severity: warn\n    given: $.components.schemas.CatalogItem.properties\n    then:\n      function: schema\n      functionOptions:\n        schema: {}\n"
source_yaml_url: https://raw.githubusercontent.com/api-evangelist/airbus-oneatlas/refs/heads/main/rules/oneatlas-spectral-rules.yml
tags:
- Imagery
- Satellites
- Spectral
- Linting
- API Governance
---
