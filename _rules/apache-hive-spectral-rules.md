---
api_specs:
- filename: apache-hive-webhcat-openapi.yml
  format: yaml
  label: Apache Hive WebHCat REST API
  slug: apache-hive-webhcat-api
  spec_type: OpenAPI
  url: https://raw.githubusercontent.com/api-evangelist/apache-hive/refs/heads/main/openapi/apache-hive-webhcat-openapi.yml
categories:
- hive
description: Spectral linting rules defining API design standards and conventions for Apache Hive.
layout: rules
name: Apache Hive API Rules
provider_name: Apache Hive
provider_slug: apache-hive
rule_count: 8
rules:
- description: All Hive WebHCat API operations must have a summary
  given: $.paths[*][get,put,post,delete,patch]
  name: hive-operation-summary
  severity: error
- description: All Hive WebHCat API operations must have an operationId
  given: $.paths[*][get,put,post,delete,patch]
  name: hive-operation-id
  severity: error
- description: All Hive WebHCat API operations must have at least one tag
  given: $.paths[*][get,put,post,delete,patch]
  name: hive-operation-tags
  severity: warn
- description: All Hive schema components must have a description
  given: $.components.schemas[*]
  name: hive-schema-description
  severity: warn
- description: All Hive schema properties should have descriptions
  given: $.components.schemas[*].properties[*]
  name: hive-property-description
  severity: info
- description: API info must include contact information
  given: $.info
  name: hive-info-contact
  severity: warn
- description: API info must include license information
  given: $.info
  name: hive-info-license
  severity: warn
- description: All Hive path parameters must have descriptions
  given: $.paths[*][*].parameters[?(@.in=='path')]
  name: hive-path-parameters-described
  severity: warn
rules_file: rules/apache-hive-spectral-rules.yml
rules_url: https://raw.githubusercontent.com/api-evangelist/apache-hive/refs/heads/main/rules/apache-hive-spectral-rules.yml
severity_counts:
  error: 2
  hint: 0
  info: 1
  warn: 5
slug: apache-hive-spectral-rules
source_filename: apache-hive-spectral-rules.yml
source_heading: Spectral Ruleset
source_yaml: "rules:\n  hive-operation-summary:\n    description: All Hive WebHCat API operations must have a summary\n    severity: error\n    given: \"$.paths[*][get,put,post,delete,patch]\"\n    then:\n      field: summary\n      function: truthy\n\n  hive-operation-id:\n    description: All Hive WebHCat API operations must have an operationId\n    severity: error\n    given: \"$.paths[*][get,put,post,delete,patch]\"\n    then:\n      field: operationId\n      function: truthy\n\n  hive-operation-tags:\n    description: All Hive WebHCat API operations must have at least one tag\n    severity: warn\n    given: \"$.paths[*][get,put,post,delete,patch]\"\n    then:\n      field: tags\n      function: truthy\n\n  hive-schema-description:\n    description: All Hive schema components must have a description\n    severity: warn\n    given: \"$.components.schemas[*]\"\n    then:\n      field: description\n      function: truthy\n\n  hive-property-description:\n    description: All Hive schema\
  \ properties should have descriptions\n    severity: info\n    given: \"$.components.schemas[*].properties[*]\"\n    then:\n      field: description\n      function: truthy\n\n  hive-info-contact:\n    description: API info must include contact information\n    severity: warn\n    given: \"$.info\"\n    then:\n      field: contact\n      function: truthy\n\n  hive-info-license:\n    description: API info must include license information\n    severity: warn\n    given: \"$.info\"\n    then:\n      field: license\n      function: truthy\n\n  hive-path-parameters-described:\n    description: All Hive path parameters must have descriptions\n    severity: warn\n    given: \"$.paths[*][*].parameters[?(@.in=='path')]\"\n    then:\n      field: description\n      function: truthy\n"
source_yaml_url: https://raw.githubusercontent.com/api-evangelist/apache-hive/refs/heads/main/rules/apache-hive-spectral-rules.yml
tags:
- Apache
- Big Data
- Data Warehouse
- ETL
- Hadoop
- Open Source
- SQL
- Spectral
- Linting
- API Governance
---
