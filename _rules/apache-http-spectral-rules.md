---
api_specs:
- filename: apache-http-client-openapi.yml
  format: yaml
  label: Apache HttpComponents Client API
  slug: apache-http-client-api
  spec_type: OpenAPI
  url: https://raw.githubusercontent.com/api-evangelist/apache-http/refs/heads/main/openapi/apache-http-client-openapi.yml
categories:
- http
description: Spectral linting rules defining API design standards and conventions for Apache HttpComponents.
layout: rules
name: Apache HttpComponents API Rules
provider_name: Apache HttpComponents
provider_slug: apache-http
rule_count: 7
rules:
- description: All Apache HttpComponents API operations must have a summary
  given: $.paths[*][get,put,post,delete,patch]
  name: http-client-operation-summary
  severity: error
- description: All Apache HttpComponents API operations must have an operationId
  given: $.paths[*][get,put,post,delete,patch]
  name: http-client-operation-id
  severity: error
- description: All Apache HttpComponents API operations must have at least one tag
  given: $.paths[*][get,put,post,delete,patch]
  name: http-client-operation-tags
  severity: warn
- description: All Apache HttpComponents schema components must have a description
  given: $.components.schemas[*]
  name: http-client-schema-description
  severity: warn
- description: All Apache HttpComponents schema properties should have descriptions
  given: $.components.schemas[*].properties[*]
  name: http-client-property-description
  severity: info
- description: API info must include contact information
  given: $.info
  name: http-client-info-contact
  severity: warn
- description: API info must include license information
  given: $.info
  name: http-client-info-license
  severity: warn
rules_file: rules/apache-http-spectral-rules.yml
rules_url: https://raw.githubusercontent.com/api-evangelist/apache-http/refs/heads/main/rules/apache-http-spectral-rules.yml
severity_counts:
  error: 2
  hint: 0
  info: 1
  warn: 4
slug: apache-http-spectral-rules
source_filename: apache-http-spectral-rules.yml
source_heading: Spectral Ruleset
source_yaml: "rules:\n  http-client-operation-summary:\n    description: All Apache HttpComponents API operations must have a summary\n    severity: error\n    given: \"$.paths[*][get,put,post,delete,patch]\"\n    then:\n      field: summary\n      function: truthy\n\n  http-client-operation-id:\n    description: All Apache HttpComponents API operations must have an operationId\n    severity: error\n    given: \"$.paths[*][get,put,post,delete,patch]\"\n    then:\n      field: operationId\n      function: truthy\n\n  http-client-operation-tags:\n    description: All Apache HttpComponents API operations must have at least one tag\n    severity: warn\n    given: \"$.paths[*][get,put,post,delete,patch]\"\n    then:\n      field: tags\n      function: truthy\n\n  http-client-schema-description:\n    description: All Apache HttpComponents schema components must have a description\n    severity: warn\n    given: \"$.components.schemas[*]\"\n    then:\n      field: description\n      function: truthy\n\
  \n  http-client-property-description:\n    description: All Apache HttpComponents schema properties should have descriptions\n    severity: info\n    given: \"$.components.schemas[*].properties[*]\"\n    then:\n      field: description\n      function: truthy\n\n  http-client-info-contact:\n    description: API info must include contact information\n    severity: warn\n    given: \"$.info\"\n    then:\n      field: contact\n      function: truthy\n\n  http-client-info-license:\n    description: API info must include license information\n    severity: warn\n    given: \"$.info\"\n    then:\n      field: license\n      function: truthy\n"
source_yaml_url: https://raw.githubusercontent.com/api-evangelist/apache-http/refs/heads/main/rules/apache-http-spectral-rules.yml
tags:
- Apache
- HTTP Client
- Java
- Open Source
- SDK
- Spectral
- Linting
- API Governance
---
