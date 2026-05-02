---
api_specs:
- filename: apache-helix-rest-openapi.yml
  format: yaml
  label: Apache Helix REST API
  slug: apache-helix-rest-api
  spec_type: OpenAPI
  url: https://raw.githubusercontent.com/api-evangelist/apache-helix/refs/heads/main/openapi/apache-helix-rest-openapi.yml
categories:
- helix
description: Spectral linting rules defining API design standards and conventions for Apache Helix.
layout: rules
name: Apache Helix API Rules
provider_name: Apache Helix
provider_slug: apache-helix
rule_count: 8
rules:
- description: All Helix REST API operations must have a summary
  given: $.paths[*][get,put,post,delete,patch]
  name: helix-operation-summary
  severity: error
- description: All Helix REST API operations must have an operationId
  given: $.paths[*][get,put,post,delete,patch]
  name: helix-operation-id
  severity: error
- description: All Helix REST API operations must have at least one tag
  given: $.paths[*][get,put,post,delete,patch]
  name: helix-operation-tags
  severity: warn
- description: All Helix schema components must have a description
  given: $.components.schemas[*]
  name: helix-schema-description
  severity: warn
- description: All Helix schema properties should have descriptions
  given: $.components.schemas[*].properties[*]
  name: helix-property-description
  severity: info
- description: API info must include contact information
  given: $.info
  name: helix-info-contact
  severity: warn
- description: API info must include license information
  given: $.info
  name: helix-info-license
  severity: warn
- description: All Helix path parameters must have descriptions
  given: $.paths[*][*].parameters[?(@.in=='path')]
  name: helix-path-parameters-described
  severity: warn
rules_file: rules/apache-helix-spectral-rules.yml
rules_url: https://raw.githubusercontent.com/api-evangelist/apache-helix/refs/heads/main/rules/apache-helix-spectral-rules.yml
severity_counts:
  error: 2
  hint: 0
  info: 1
  warn: 5
slug: apache-helix-spectral-rules
source_filename: apache-helix-spectral-rules.yml
source_heading: Spectral Ruleset
source_yaml: "rules:\n  helix-operation-summary:\n    description: All Helix REST API operations must have a summary\n    severity: error\n    given: \"$.paths[*][get,put,post,delete,patch]\"\n    then:\n      field: summary\n      function: truthy\n\n  helix-operation-id:\n    description: All Helix REST API operations must have an operationId\n    severity: error\n    given: \"$.paths[*][get,put,post,delete,patch]\"\n    then:\n      field: operationId\n      function: truthy\n\n  helix-operation-tags:\n    description: All Helix REST API operations must have at least one tag\n    severity: warn\n    given: \"$.paths[*][get,put,post,delete,patch]\"\n    then:\n      field: tags\n      function: truthy\n\n  helix-schema-description:\n    description: All Helix schema components must have a description\n    severity: warn\n    given: \"$.components.schemas[*]\"\n    then:\n      field: description\n      function: truthy\n\n  helix-property-description:\n    description: All Helix schema\
  \ properties should have descriptions\n    severity: info\n    given: \"$.components.schemas[*].properties[*]\"\n    then:\n      field: description\n      function: truthy\n\n  helix-info-contact:\n    description: API info must include contact information\n    severity: warn\n    given: \"$.info\"\n    then:\n      field: contact\n      function: truthy\n\n  helix-info-license:\n    description: API info must include license information\n    severity: warn\n    given: \"$.info\"\n    then:\n      field: license\n      function: truthy\n\n  helix-path-parameters-described:\n    description: All Helix path parameters must have descriptions\n    severity: warn\n    given: \"$.paths[*][*].parameters[?(@.in=='path')]\"\n    then:\n      field: description\n      function: truthy\n"
source_yaml_url: https://raw.githubusercontent.com/api-evangelist/apache-helix/refs/heads/main/rules/apache-helix-spectral-rules.yml
tags:
- Apache
- Cluster Management
- Distributed Systems
- Open Source
- Partitioning
- Replication
- Spectral
- Linting
- API Governance
---
