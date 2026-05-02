---
api_specs:
- filename: apache-apisix-admin-api-openapi.yml
  format: yaml
  label: Apache APISIX Admin API
  slug: apache-apisix-admin-api
  spec_type: OpenAPI
  url: https://raw.githubusercontent.com/api-evangelist/apache-apisix/refs/heads/main/openapi/apache-apisix-admin-api-openapi.yml
- filename: apache-apisix-control-api-openapi.yml
  format: yaml
  label: Apache APISIX Control API
  slug: apache-apisix-control-api
  spec_type: OpenAPI
  url: https://raw.githubusercontent.com/api-evangelist/apache-apisix/refs/heads/main/openapi/apache-apisix-control-api-openapi.yml
categories:
- apikey
- delete
- get
- info
- operation
- parameter
- paths
- response
- schema
- security
- servers
description: Spectral linting rules defining API design standards and conventions for Apache APISIX.
layout: rules
name: Apache APISIX API Rules
provider_name: Apache APISIX
provider_slug: apache-apisix
rule_count: 19
rules:
- description: API title must start with "Apache APISIX"
  given: $.info.title
  name: info-title-prefix
  severity: warn
- description: API must have a description.
  given: $.info
  name: info-description-required
  severity: error
- description: API must declare a version.
  given: $.info
  name: info-version-required
  severity: error
- description: At least one server must be defined.
  given: $
  name: servers-defined
  severity: error
- description: Every operation must have a summary.
  given: $.paths[*][get,post,put,patch,delete]
  name: operation-summary-required
  severity: error
- description: Operation summaries must start with "Apache APISIX".
  given: $.paths[*][get,post,put,patch,delete].summary
  name: operation-summary-starts-with-apache-apisix
  severity: warn
- description: Every operation must have an operationId.
  given: $.paths[*][get,post,put,patch,delete]
  name: operation-operationId-required
  severity: error
- description: operationId must be camelCase.
  given: $.paths[*][get,post,put,patch,delete].operationId
  name: operation-operationId-camelCase
  severity: warn
- description: Every operation must have at least one tag.
  given: $.paths[*][get,post,put,patch,delete]
  name: operation-tags-required
  severity: warn
- description: Every operation should have a description.
  given: $.paths[*][get,post,put,patch,delete]
  name: operation-description-required
  severity: warn
- description: Path segments must use kebab-case or standard patterns.
  given: $.paths
  name: paths-kebab-case
  severity: info
- description: Every parameter must have a description.
  given: $.paths[*][get,post,put,patch,delete].parameters[*]
  name: parameter-description-required
  severity: warn
- description: Every operation must define at least one 2xx response.
  given: $.paths[*][get,post,put,patch,delete].responses
  name: response-success-required
  severity: error
- description: Every response must have a description.
  given: $.paths[*][get,post,put,patch,delete].responses[*]
  name: response-description-required
  severity: error
- description: Security schemes must be defined in components.
  given: $.components
  name: security-schemes-defined
  severity: warn
- description: API key authentication should use a header, not a query parameter.
  given: $.components.securitySchemes[?(@.type=='apiKey')]
  name: apikey-in-header
  severity: warn
- description: GET operations must not have a request body.
  given: $.paths[*].get
  name: get-no-request-body
  severity: error
- description: DELETE operations should return 200 or 204.
  given: $.paths[*].delete.responses
  name: delete-returns-200-or-204
  severity: info
- description: Schema components must have a type defined.
  given: $.components.schemas[*]
  name: schema-type-defined
  severity: warn
rules_file: rules/apache-apisix-spectral-rules.yml
rules_url: https://raw.githubusercontent.com/api-evangelist/apache-apisix/refs/heads/main/rules/apache-apisix-spectral-rules.yml
severity_counts:
  error: 8
  hint: 0
  info: 2
  warn: 9
slug: apache-apisix-spectral-rules
source_filename: apache-apisix-spectral-rules.yml
source_heading: Spectral Ruleset
source_yaml: "extends: spectral:oas\nrules:\n  info-title-prefix:\n    description: API title must start with \"Apache APISIX\"\n    severity: warn\n    given: \"$.info.title\"\n    then:\n      function: pattern\n      functionOptions:\n        match: \"^Apache APISIX\"\n  info-description-required:\n    description: API must have a description.\n    severity: error\n    given: \"$.info\"\n    then:\n      field: description\n      function: truthy\n  info-version-required:\n    description: API must declare a version.\n    severity: error\n    given: \"$.info\"\n    then:\n      field: version\n      function: truthy\n  servers-defined:\n    description: At least one server must be defined.\n    severity: error\n    given: \"$\"\n    then:\n      field: servers\n      function: truthy\n  operation-summary-required:\n    description: Every operation must have a summary.\n    severity: error\n    given: \"$.paths[*][get,post,put,patch,delete]\"\n    then:\n      field: summary\n      function:\
  \ truthy\n  operation-summary-starts-with-apache-apisix:\n    description: Operation summaries must start with \"Apache APISIX\".\n    severity: warn\n    given: \"$.paths[*][get,post,put,patch,delete].summary\"\n    then:\n      function: pattern\n      functionOptions:\n        match: \"^Apache APISIX\"\n  operation-operationId-required:\n    description: Every operation must have an operationId.\n    severity: error\n    given: \"$.paths[*][get,post,put,patch,delete]\"\n    then:\n      field: operationId\n      function: truthy\n  operation-operationId-camelCase:\n    description: operationId must be camelCase.\n    severity: warn\n    given: \"$.paths[*][get,post,put,patch,delete].operationId\"\n    then:\n      function: pattern\n      functionOptions:\n        match: \"^[a-z][a-zA-Z0-9]*$\"\n  operation-tags-required:\n    description: Every operation must have at least one tag.\n    severity: warn\n    given: \"$.paths[*][get,post,put,patch,delete]\"\n    then:\n      field: tags\n\
  \      function: truthy\n  operation-description-required:\n    description: Every operation should have a description.\n    severity: warn\n    given: \"$.paths[*][get,post,put,patch,delete]\"\n    then:\n      field: description\n      function: truthy\n  paths-kebab-case:\n    description: Path segments must use kebab-case or standard patterns.\n    severity: info\n    given: \"$.paths\"\n    then:\n      function: pattern\n      functionOptions:\n        match: \"^(/[a-z0-9{}_\\\\-*]+)+\"\n  parameter-description-required:\n    description: Every parameter must have a description.\n    severity: warn\n    given: \"$.paths[*][get,post,put,patch,delete].parameters[*]\"\n    then:\n      field: description\n      function: truthy\n  response-success-required:\n    description: Every operation must define at least one 2xx response.\n    severity: error\n    given: \"$.paths[*][get,post,put,patch,delete].responses\"\n    then:\n      function: schema\n      functionOptions:\n        schema:\n\
  \          anyOf:\n            - required: ['200']\n            - required: ['201']\n            - required: ['204']\n  response-description-required:\n    description: Every response must have a description.\n    severity: error\n    given: \"$.paths[*][get,post,put,patch,delete].responses[*]\"\n    then:\n      field: description\n      function: truthy\n  security-schemes-defined:\n    description: Security schemes must be defined in components.\n    severity: warn\n    given: \"$.components\"\n    then:\n      field: securitySchemes\n      function: truthy\n  apikey-in-header:\n    description: API key authentication should use a header, not a query parameter.\n    severity: warn\n    given: \"$.components.securitySchemes[?(@.type=='apiKey')]\"\n    then:\n      field: in\n      function: enumeration\n      functionOptions:\n        values:\n          - header\n  get-no-request-body:\n    description: GET operations must not have a request body.\n    severity: error\n    given: \"\
  $.paths[*].get\"\n    then:\n      field: requestBody\n      function: falsy\n  delete-returns-200-or-204:\n    description: DELETE operations should return 200 or 204.\n    severity: info\n    given: \"$.paths[*].delete.responses\"\n    then:\n      function: schema\n      functionOptions:\n        schema:\n          anyOf:\n            - required: ['200']\n            - required: ['204']\n  schema-type-defined:\n    description: Schema components must have a type defined.\n    severity: warn\n    given: \"$.components.schemas[*]\"\n    then:\n      field: type\n      function: truthy\n"
source_yaml_url: https://raw.githubusercontent.com/api-evangelist/apache-apisix/refs/heads/main/rules/apache-apisix-spectral-rules.yml
tags:
- Apache
- API Gateway
- Cloud Native
- Kubernetes
- Lua
- NGINX
- Open Source
- Traffic Management
- Spectral
- Linting
- API Governance
---
