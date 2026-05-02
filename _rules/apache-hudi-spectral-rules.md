---
api_specs:
- filename: apache-hudi-timeline-openapi.yml
  format: yaml
  label: Apache Hudi Timeline Server API
  slug: apache-hudi-timeline-api
  spec_type: OpenAPI
  url: https://raw.githubusercontent.com/api-evangelist/apache-hudi/refs/heads/main/openapi/apache-hudi-timeline-openapi.yml
categories:
- hudi
description: Spectral linting rules defining API design standards and conventions for Apache Hudi.
layout: rules
name: Apache Hudi API Rules
provider_name: Apache Hudi
provider_slug: apache-hudi
rule_count: 8
rules:
- description: All Hudi Timeline Server API operations must have a summary
  given: $.paths[*][get,put,post,delete,patch]
  name: hudi-operation-summary
  severity: error
- description: All Hudi Timeline Server API operations must have an operationId
  given: $.paths[*][get,put,post,delete,patch]
  name: hudi-operation-id
  severity: error
- description: All Hudi Timeline Server API operations must have at least one tag
  given: $.paths[*][get,put,post,delete,patch]
  name: hudi-operation-tags
  severity: warn
- description: All Hudi schema components must have a description
  given: $.components.schemas[*]
  name: hudi-schema-description
  severity: warn
- description: All Hudi schema properties should have descriptions
  given: $.components.schemas[*].properties[*]
  name: hudi-property-description
  severity: info
- description: API info must include contact information
  given: $.info
  name: hudi-info-contact
  severity: warn
- description: API info must include license information
  given: $.info
  name: hudi-info-license
  severity: warn
- description: All Hudi path parameters must have descriptions
  given: $.paths[*][*].parameters[?(@.in=='path')]
  name: hudi-path-parameters-described
  severity: warn
rules_file: rules/apache-hudi-spectral-rules.yml
rules_url: https://raw.githubusercontent.com/api-evangelist/apache-hudi/refs/heads/main/rules/apache-hudi-spectral-rules.yml
severity_counts:
  error: 2
  hint: 0
  info: 1
  warn: 5
slug: apache-hudi-spectral-rules
source_filename: apache-hudi-spectral-rules.yml
source_heading: Spectral Ruleset
source_yaml: "rules:\n  hudi-operation-summary:\n    description: All Hudi Timeline Server API operations must have a summary\n    severity: error\n    given: \"$.paths[*][get,put,post,delete,patch]\"\n    then:\n      field: summary\n      function: truthy\n\n  hudi-operation-id:\n    description: All Hudi Timeline Server API operations must have an operationId\n    severity: error\n    given: \"$.paths[*][get,put,post,delete,patch]\"\n    then:\n      field: operationId\n      function: truthy\n\n  hudi-operation-tags:\n    description: All Hudi Timeline Server API operations must have at least one tag\n    severity: warn\n    given: \"$.paths[*][get,put,post,delete,patch]\"\n    then:\n      field: tags\n      function: truthy\n\n  hudi-schema-description:\n    description: All Hudi schema components must have a description\n    severity: warn\n    given: \"$.components.schemas[*]\"\n    then:\n      field: description\n      function: truthy\n\n  hudi-property-description:\n    description:\
  \ All Hudi schema properties should have descriptions\n    severity: info\n    given: \"$.components.schemas[*].properties[*]\"\n    then:\n      field: description\n      function: truthy\n\n  hudi-info-contact:\n    description: API info must include contact information\n    severity: warn\n    given: \"$.info\"\n    then:\n      field: contact\n      function: truthy\n\n  hudi-info-license:\n    description: API info must include license information\n    severity: warn\n    given: \"$.info\"\n    then:\n      field: license\n      function: truthy\n\n  hudi-path-parameters-described:\n    description: All Hudi path parameters must have descriptions\n    severity: warn\n    given: \"$.paths[*][*].parameters[?(@.in=='path')]\"\n    then:\n      field: description\n      function: truthy\n"
source_yaml_url: https://raw.githubusercontent.com/api-evangelist/apache-hudi/refs/heads/main/rules/apache-hudi-spectral-rules.yml
tags:
- ACID
- Apache
- Big Data
- Data Lake
- Incremental Processing
- Lakehouse
- Open Source
- Spectral
- Linting
- API Governance
---
