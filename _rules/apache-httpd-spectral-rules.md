---
api_specs:
- filename: apache-httpd-status-openapi.yml
  format: yaml
  label: Apache HTTP Server Status API
  slug: apache-httpd-status-api
  spec_type: OpenAPI
  url: https://raw.githubusercontent.com/api-evangelist/apache-httpd/refs/heads/main/openapi/apache-httpd-status-openapi.yml
categories:
- httpd
description: Spectral linting rules defining API design standards and conventions for Apache HTTP Server.
layout: rules
name: Apache HTTP Server API Rules
provider_name: Apache HTTP Server
provider_slug: apache-httpd
rule_count: 7
rules:
- description: All Apache httpd API operations must have a summary
  given: $.paths[*][get,put,post,delete,patch]
  name: httpd-operation-summary
  severity: error
- description: All Apache httpd API operations must have an operationId
  given: $.paths[*][get,put,post,delete,patch]
  name: httpd-operation-id
  severity: error
- description: All Apache httpd API operations must have at least one tag
  given: $.paths[*][get,put,post,delete,patch]
  name: httpd-operation-tags
  severity: warn
- description: All Apache httpd schema components must have a description
  given: $.components.schemas[*]
  name: httpd-schema-description
  severity: warn
- description: All Apache httpd schema properties should have descriptions
  given: $.components.schemas[*].properties[*]
  name: httpd-property-description
  severity: info
- description: API info must include contact information
  given: $.info
  name: httpd-info-contact
  severity: warn
- description: API info must include license information
  given: $.info
  name: httpd-info-license
  severity: warn
rules_file: rules/apache-httpd-spectral-rules.yml
rules_url: https://raw.githubusercontent.com/api-evangelist/apache-httpd/refs/heads/main/rules/apache-httpd-spectral-rules.yml
severity_counts:
  error: 2
  hint: 0
  info: 1
  warn: 4
slug: apache-httpd-spectral-rules
source_filename: apache-httpd-spectral-rules.yml
source_heading: Spectral Ruleset
source_yaml: "rules:\n  httpd-operation-summary:\n    description: All Apache httpd API operations must have a summary\n    severity: error\n    given: \"$.paths[*][get,put,post,delete,patch]\"\n    then:\n      field: summary\n      function: truthy\n\n  httpd-operation-id:\n    description: All Apache httpd API operations must have an operationId\n    severity: error\n    given: \"$.paths[*][get,put,post,delete,patch]\"\n    then:\n      field: operationId\n      function: truthy\n\n  httpd-operation-tags:\n    description: All Apache httpd API operations must have at least one tag\n    severity: warn\n    given: \"$.paths[*][get,put,post,delete,patch]\"\n    then:\n      field: tags\n      function: truthy\n\n  httpd-schema-description:\n    description: All Apache httpd schema components must have a description\n    severity: warn\n    given: \"$.components.schemas[*]\"\n    then:\n      field: description\n      function: truthy\n\n  httpd-property-description:\n    description: All\
  \ Apache httpd schema properties should have descriptions\n    severity: info\n    given: \"$.components.schemas[*].properties[*]\"\n    then:\n      field: description\n      function: truthy\n\n  httpd-info-contact:\n    description: API info must include contact information\n    severity: warn\n    given: \"$.info\"\n    then:\n      field: contact\n      function: truthy\n\n  httpd-info-license:\n    description: API info must include license information\n    severity: warn\n    given: \"$.info\"\n    then:\n      field: license\n      function: truthy\n"
source_yaml_url: https://raw.githubusercontent.com/api-evangelist/apache-httpd/refs/heads/main/rules/apache-httpd-spectral-rules.yml
tags:
- Apache
- Load Balancer
- Open Source
- Proxy
- Reverse Proxy
- Web Server
- Spectral
- Linting
- API Governance
---
