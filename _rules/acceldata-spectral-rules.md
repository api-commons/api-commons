---
api_specs:
- filename: acceldata-adoc-api.yaml
  format: yaml
  label: Acceldata Data Observability Cloud API
  slug: adoc-api
  spec_type: OpenAPI
  url: https://raw.githubusercontent.com/api-evangelist/acceldata/refs/heads/main/openapi/acceldata-adoc-api.yaml
categories:
- acceldata
description: Spectral linting rules defining API design standards and conventions for Acceldata.
layout: rules
name: Acceldata API Rules
provider_name: Acceldata
provider_slug: acceldata
rule_count: 25
rules:
- description: All operations must require the X-API-Key security scheme
  given: $.paths[*][get,post,put,patch,delete]
  name: acceldata-require-api-key-security
  severity: error
- description: API key must use X-API-Key header name
  given: $.components.securitySchemes[*][?(@.in == 'header')]
  name: acceldata-api-key-header-name
  severity: error
- description: API paths must use kebab-case
  given: $.paths[*]~
  name: acceldata-path-kebab-case
  severity: warn
- description: API paths must not have trailing slashes
  given: $.paths[*]~
  name: acceldata-no-trailing-slash
  severity: warn
- description: GET operations must define a 200 response
  given: $.paths[*].get.responses
  name: acceldata-require-200-response
  severity: error
- description: Operations must define a 400 error response
  given: $.paths[*][get,post,put,patch,delete].responses
  name: acceldata-require-400-response
  severity: warn
- description: Operations must define a 401 unauthorized response
  given: $.paths[*][get,post,put,patch,delete].responses
  name: acceldata-require-401-response
  severity: warn
- description: Operations must define a 500 server error response
  given: $.paths[*][get,post,put,patch,delete].responses
  name: acceldata-require-500-response
  severity: warn
- description: All schema components must have a description
  given: $.components.schemas[*]
  name: acceldata-schema-require-description
  severity: warn
- description: Schema properties should have descriptions
  given: $.components.schemas[*].properties[*]
  name: acceldata-schema-properties-require-description
  severity: info
- description: Resource schemas should include an id property
  given: $.components.schemas[?(@.type == 'object' && !@.properties.total)]
  name: acceldata-require-id-property
  severity: info
- description: Timestamp fields must use date-time format
  given: $.components.schemas[*].properties[?(@.description =~ /time|date|at$/i)]
  name: acceldata-timestamp-format
  severity: error
- description: List/collection schemas must include a total count property
  given: $.components.schemas[?(@.title =~ /List$/)]
  name: acceldata-list-schema-require-total
  severity: warn
- description: List/collection schemas must include page and pageSize for pagination
  given: $.components.schemas[?(@.title =~ /List$/)]
  name: acceldata-list-schema-require-page
  severity: warn
- description: All operations must have at least one tag
  given: $.paths[*][get,post,put,patch,delete]
  name: acceldata-operations-require-tags
  severity: warn
- description: All operations must have a summary
  given: $.paths[*][get,post,put,patch,delete]
  name: acceldata-operations-require-summary
  severity: error
- description: All operations must have an operationId
  given: $.paths[*][get,post,put,patch,delete]
  name: acceldata-operations-require-operation-id
  severity: error
- description: OperationIds must use camelCase
  given: $.paths[*][get,post,put,patch,delete].operationId
  name: acceldata-operation-id-camel-case
  severity: warn
- description: List operations should support page and pageSize query parameters
  given: $.paths[?(!@~.match(/\{.*\}/))].get.parameters[*]
  name: acceldata-list-operations-support-pagination
  severity: info
- description: Request bodies must use application/json content type
  given: $.paths[*][post,put,patch].requestBody.content
  name: acceldata-require-json-content-type
  severity: error
- description: Success responses must return application/json
  given: $.paths[*][get,post,put,patch,delete].responses[200,201].content
  name: acceldata-response-require-json-content-type
  severity: error
- description: API info must include a version
  given: $.info
  name: acceldata-info-require-version
  severity: error
- description: API info must include a description
  given: $.info
  name: acceldata-info-require-description
  severity: error
- description: Alert and rule severity must use standard values
  given: $.components.schemas[*].properties.severity
  name: acceldata-severity-values
  severity: warn
- description: Alert status must use standard values
  given: $.components.schemas[*].properties.status
  name: acceldata-status-values
  severity: warn
rules_file: rules/acceldata-spectral-rules.yml
rules_url: https://raw.githubusercontent.com/api-evangelist/acceldata/refs/heads/main/rules/acceldata-spectral-rules.yml
severity_counts:
  error: 10
  hint: 0
  info: 3
  warn: 12
slug: acceldata-spectral-rules
source_filename: acceldata-spectral-rules.yml
source_heading: Spectral Ruleset
source_yaml: "extends: spectral:oas\nrules:\n  # Authentication Rules\n  acceldata-require-api-key-security:\n    description: All operations must require the X-API-Key security scheme\n    message: \"Operation '{{path}}' must include apiKey security requirement\"\n    severity: error\n    given: \"$.paths[*][get,post,put,patch,delete]\"\n    then:\n      field: security\n      function: truthy\n\n  acceldata-api-key-header-name:\n    description: API key must use X-API-Key header name\n    message: \"Security scheme must use 'X-API-Key' as the header name\"\n    severity: error\n    given: \"$.components.securitySchemes[*][?(@.in == 'header')]\"\n    then:\n      field: name\n      function: pattern\n      functionOptions:\n        match: \"^X-API-Key$\"\n\n  # Path Naming Rules\n  acceldata-path-kebab-case:\n    description: API paths must use kebab-case\n    message: \"Path '{{value}}' must use kebab-case (lowercase with hyphens)\"\n    severity: warn\n    given: \"$.paths[*]~\"\n   \
  \ then:\n      function: pattern\n      functionOptions:\n        match: \"^(/[a-z0-9-]+({[a-zA-Z]+})?)*$\"\n\n  acceldata-no-trailing-slash:\n    description: API paths must not have trailing slashes\n    message: \"Path '{{value}}' must not have a trailing slash\"\n    severity: warn\n    given: \"$.paths[*]~\"\n    then:\n      function: pattern\n      functionOptions:\n        notMatch: \"/$\"\n\n  # Response Rules\n  acceldata-require-200-response:\n    description: GET operations must define a 200 response\n    message: \"GET operation at '{{path}}' must define a 200 response\"\n    severity: error\n    given: \"$.paths[*].get.responses\"\n    then:\n      field: \"200\"\n      function: truthy\n\n  acceldata-require-400-response:\n    description: Operations must define a 400 error response\n    message: \"Operation at '{{path}}' must define a 400 response\"\n    severity: warn\n    given: \"$.paths[*][get,post,put,patch,delete].responses\"\n    then:\n      field: \"400\"\n   \
  \   function: truthy\n\n  acceldata-require-401-response:\n    description: Operations must define a 401 unauthorized response\n    message: \"Operation at '{{path}}' must define a 401 response\"\n    severity: warn\n    given: \"$.paths[*][get,post,put,patch,delete].responses\"\n    then:\n      field: \"401\"\n      function: truthy\n\n  acceldata-require-500-response:\n    description: Operations must define a 500 server error response\n    message: \"Operation at '{{path}}' must define a 500 response\"\n    severity: warn\n    given: \"$.paths[*][get,post,put,patch,delete].responses\"\n    then:\n      field: \"500\"\n      function: truthy\n\n  # Schema Rules\n  acceldata-schema-require-description:\n    description: All schema components must have a description\n    message: \"Schema '{{path}}' must have a description\"\n    severity: warn\n    given: \"$.components.schemas[*]\"\n    then:\n      field: description\n      function: truthy\n\n  acceldata-schema-properties-require-description:\n\
  \    description: Schema properties should have descriptions\n    message: \"Property at '{{path}}' should have a description\"\n    severity: info\n    given: \"$.components.schemas[*].properties[*]\"\n    then:\n      field: description\n      function: truthy\n\n  acceldata-require-id-property:\n    description: Resource schemas should include an id property\n    message: \"Schema '{{path}}' should include an 'id' property\"\n    severity: info\n    given: \"$.components.schemas[?(@.type == 'object' && !@.properties.total)]\"\n    then:\n      field: properties.id\n      function: truthy\n\n  acceldata-timestamp-format:\n    description: Timestamp fields must use date-time format\n    message: \"Timestamp property '{{path}}' must use format: date-time\"\n    severity: error\n    given: \"$.components.schemas[*].properties[?(@.description =~ /time|date|at$/i)]\"\n    then:\n      field: format\n      function: enumeration\n      functionOptions:\n        values:\n          - date-time\n\
  \          - date\n\n  # Pagination Rules\n  acceldata-list-schema-require-total:\n    description: List/collection schemas must include a total count property\n    message: \"List schema '{{path}}' must include a 'total' property\"\n    severity: warn\n    given: \"$.components.schemas[?(@.title =~ /List$/)]\"\n    then:\n      field: properties.total\n      function: truthy\n\n  acceldata-list-schema-require-page:\n    description: List/collection schemas must include page and pageSize for pagination\n    message: \"List schema '{{path}}' must include 'page' property\"\n    severity: warn\n    given: \"$.components.schemas[?(@.title =~ /List$/)]\"\n    then:\n      field: properties.page\n      function: truthy\n\n  # Operation Rules\n  acceldata-operations-require-tags:\n    description: All operations must have at least one tag\n    message: \"Operation at '{{path}}' must have at least one tag\"\n    severity: warn\n    given: \"$.paths[*][get,post,put,patch,delete]\"\n    then:\n\
  \      field: tags\n      function: truthy\n\n  acceldata-operations-require-summary:\n    description: All operations must have a summary\n    message: \"Operation at '{{path}}' must have a summary\"\n    severity: error\n    given: \"$.paths[*][get,post,put,patch,delete]\"\n    then:\n      field: summary\n      function: truthy\n\n  acceldata-operations-require-operation-id:\n    description: All operations must have an operationId\n    message: \"Operation at '{{path}}' must have an operationId\"\n    severity: error\n    given: \"$.paths[*][get,post,put,patch,delete]\"\n    then:\n      field: operationId\n      function: truthy\n\n  acceldata-operation-id-camel-case:\n    description: OperationIds must use camelCase\n    message: \"OperationId '{{value}}' must use camelCase\"\n    severity: warn\n    given: \"$.paths[*][get,post,put,patch,delete].operationId\"\n    then:\n      function: pattern\n      functionOptions:\n        match: \"^[a-z][a-zA-Z0-9]*$\"\n\n  # Query Parameter\
  \ Rules\n  acceldata-list-operations-support-pagination:\n    description: List operations should support page and pageSize query parameters\n    message: \"List operation at '{{path}}' should support pagination query parameters\"\n    severity: info\n    given: \"$.paths[?(!@~.match(/\\\\{.*\\\\}/))].get.parameters[*]\"\n    then:\n      field: name\n      function: pattern\n      functionOptions:\n        match: \"^(page|pageSize|limit|offset|filter|sort)$\"\n\n  # Content Type Rules\n  acceldata-require-json-content-type:\n    description: Request bodies must use application/json content type\n    message: \"Request body at '{{path}}' must use application/json\"\n    severity: error\n    given: \"$.paths[*][post,put,patch].requestBody.content\"\n    then:\n      field: application/json\n      function: truthy\n\n  acceldata-response-require-json-content-type:\n    description: Success responses must return application/json\n    message: \"Response at '{{path}}' must return application/json\
  \ content\"\n    severity: error\n    given: \"$.paths[*][get,post,put,patch,delete].responses[200,201].content\"\n    then:\n      field: application/json\n      function: truthy\n\n  # Info Rules\n  acceldata-info-require-version:\n    description: API info must include a version\n    message: \"API info must include a version\"\n    severity: error\n    given: \"$.info\"\n    then:\n      field: version\n      function: truthy\n\n  acceldata-info-require-description:\n    description: API info must include a description\n    message: \"API info must include a description\"\n    severity: error\n    given: \"$.info\"\n    then:\n      field: description\n      function: truthy\n\n  # Data Quality Specific Rules\n  acceldata-severity-values:\n    description: Alert and rule severity must use standard values\n    message: \"Severity at '{{path}}' must be LOW, MEDIUM, HIGH, or CRITICAL\"\n    severity: warn\n    given: \"$.components.schemas[*].properties.severity\"\n    then:\n      field:\
  \ enum\n      function: truthy\n\n  acceldata-status-values:\n    description: Alert status must use standard values\n    message: \"Status at '{{path}}' must use defined enum values\"\n    severity: warn\n    given: \"$.components.schemas[*].properties.status\"\n    then:\n      field: enum\n      function: truthy\n"
source_yaml_url: https://raw.githubusercontent.com/api-evangelist/acceldata/refs/heads/main/rules/acceldata-spectral-rules.yml
tags:
- AI Agents
- Data Management
- Data Observability
- Data Pipeline
- Data Quality
- Intelligence
- Observability
- Spectral
- Linting
- API Governance
---
