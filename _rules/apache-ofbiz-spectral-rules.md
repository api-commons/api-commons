---
api_specs:
- filename: apache-ofbiz-rest-api-openapi.yaml
  format: yaml
  label: Apache OFBiz REST API
  slug: apache-ofbiz-rest-api
  spec_type: OpenAPI
  url: https://raw.githubusercontent.com/api-evangelist/apache-ofbiz/refs/heads/main/openapi/apache-ofbiz-rest-api-openapi.yaml
categories:
- auth
- get
- info
- 'no'
- openapi
- operation
- parameter
- request
- response
- schema
- security
- servers
- tags
description: Spectral linting rules defining API design standards and conventions for Apache OFBiz.
layout: rules
name: Apache OFBiz API Rules
provider_name: Apache OFBiz
provider_slug: apache-ofbiz
rule_count: 31
rules:
- description: OpenAPI info must have a title.
  given: $.info
  name: info-title-required
  severity: error
- description: OpenAPI info must have a description.
  given: $.info
  name: info-description-required
  severity: warn
- description: OpenAPI info must define a version.
  given: $.info
  name: info-version-required
  severity: error
- description: OpenAPI info should include contact information.
  given: $.info
  name: info-contact-required
  severity: warn
- description: OpenAPI info should include license information.
  given: $.info
  name: info-license-required
  severity: warn
- description: Specs must use OpenAPI 3.x.
  given: $
  name: openapi-version-3
  severity: error
- description: At least one server must be defined.
  given: $
  name: servers-defined
  severity: error
- description: Server URLs should use HTTPS.
  given: $.servers[*].url
  name: servers-https
  severity: warn
- description: Each server should have a description.
  given: $.servers[*]
  name: servers-description
  severity: warn
- description: Every operation must have a summary.
  given: $.paths[*][get,post,put,patch,delete]
  name: operation-summary-required
  severity: error
- description: Every operation should have a description.
  given: $.paths[*][get,post,put,patch,delete]
  name: operation-description-required
  severity: warn
- description: Every operation must have an operationId.
  given: $.paths[*][get,post,put,patch,delete]
  name: operation-operationid-required
  severity: error
- description: operationId should use camelCase.
  given: $.paths[*][get,post,put,patch,delete].operationId
  name: operation-operationid-camel-case
  severity: warn
- description: Every operation must have at least one tag.
  given: $.paths[*][get,post,put,patch,delete]
  name: operation-tags-required
  severity: error
- description: Operation summaries should start with "Apache OFBiz".
  given: $.paths[*][get,post,put,patch,delete].summary
  name: operation-summary-apache-ofbiz-prefix
  severity: info
- description: Global tags array should be defined.
  given: $
  name: tags-global-defined
  severity: warn
- description: Each global tag should have a description.
  given: $.tags[*]
  name: tags-description
  severity: warn
- description: Every parameter must have a description.
  given: $.paths[*][get,post,put,patch,delete].parameters[*]
  name: parameter-description-required
  severity: warn
- description: Every parameter must have a schema.
  given: $.paths[*][get,post,put,patch,delete].parameters[*]
  name: parameter-schema-required
  severity: error
- description: Request bodies should have a description.
  given: $.paths[*][post,put,patch].requestBody
  name: request-body-description
  severity: warn
- description: Every operation must define at least one 2xx response.
  given: $.paths[*][get,post,put,patch,delete].responses
  name: response-success-required
  severity: error
- description: Secured operations should document 401 Unauthorized response.
  given: $.paths[*][get,post,put,patch,delete].responses
  name: response-401-required
  severity: warn
- description: Every response must have a description.
  given: $.paths[*][get,post,put,patch,delete].responses[*]
  name: response-description-required
  severity: error
- description: Top-level component schemas should have a description.
  given: $.components.schemas[*]
  name: schema-description-required
  severity: warn
- description: Schema properties should have descriptions.
  given: $.components.schemas[*].properties[*]
  name: schema-property-description
  severity: info
- description: Security schemes must be defined in components.
  given: $.components
  name: security-schemes-defined
  severity: error
- description: Global security requirements should be defined.
  given: $
  name: security-global-defined
  severity: warn
- description: GET operations must not have a request body.
  given: $.paths[*].get
  name: get-no-request-body
  severity: error
- description: Bearer authentication should specify JWT format.
  given: $.components.securitySchemes[?(@.scheme == 'bearer')]
  name: auth-bearer-jwt
  severity: info
- description: Descriptions must not be empty strings.
  given: $..description
  name: no-empty-descriptions
  severity: warn
- description: OFBiz API responses should include statusCode, statusDescription, and data fields.
  given: $.components.schemas[*].properties
  name: response-status-code-standard
  severity: info
rules_file: rules/apache-ofbiz-spectral-rules.yml
rules_url: https://raw.githubusercontent.com/api-evangelist/apache-ofbiz/refs/heads/main/rules/apache-ofbiz-spectral-rules.yml
severity_counts:
  error: 12
  hint: 0
  info: 4
  warn: 15
slug: apache-ofbiz-spectral-rules
source_filename: apache-ofbiz-spectral-rules.yml
source_heading: Spectral Ruleset
source_yaml: "# Apache OFBiz REST API Spectral Ruleset\n# Enforces conventions observed across the Apache OFBiz REST API OpenAPI specification.\n\nrules:\n\n  # INFO / METADATA\n  info-title-required:\n    description: OpenAPI info must have a title.\n    severity: error\n    given: \"$.info\"\n    then:\n      field: title\n      function: truthy\n\n  info-description-required:\n    description: OpenAPI info must have a description.\n    severity: warn\n    given: \"$.info\"\n    then:\n      field: description\n      function: truthy\n\n  info-version-required:\n    description: OpenAPI info must define a version.\n    severity: error\n    given: \"$.info\"\n    then:\n      field: version\n      function: truthy\n\n  info-contact-required:\n    description: OpenAPI info should include contact information.\n    severity: warn\n    given: \"$.info\"\n    then:\n      field: contact\n      function: truthy\n\n  info-license-required:\n    description: OpenAPI info should include license\
  \ information.\n    severity: warn\n    given: \"$.info\"\n    then:\n      field: license\n      function: truthy\n\n  # OPENAPI VERSION\n  openapi-version-3:\n    description: Specs must use OpenAPI 3.x.\n    severity: error\n    given: \"$\"\n    then:\n      field: openapi\n      function: pattern\n      functionOptions:\n        match: \"^3\\\\.\"\n\n  # SERVERS\n  servers-defined:\n    description: At least one server must be defined.\n    severity: error\n    given: \"$\"\n    then:\n      field: servers\n      function: truthy\n\n  servers-https:\n    description: Server URLs should use HTTPS.\n    severity: warn\n    given: \"$.servers[*].url\"\n    then:\n      function: pattern\n      functionOptions:\n        match: \"^https://\"\n\n  servers-description:\n    description: Each server should have a description.\n    severity: warn\n    given: \"$.servers[*]\"\n    then:\n      field: description\n      function: truthy\n\n  # OPERATIONS\n  operation-summary-required:\n    description:\
  \ Every operation must have a summary.\n    severity: error\n    given: \"$.paths[*][get,post,put,patch,delete]\"\n    then:\n      field: summary\n      function: truthy\n\n  operation-description-required:\n    description: Every operation should have a description.\n    severity: warn\n    given: \"$.paths[*][get,post,put,patch,delete]\"\n    then:\n      field: description\n      function: truthy\n\n  operation-operationid-required:\n    description: Every operation must have an operationId.\n    severity: error\n    given: \"$.paths[*][get,post,put,patch,delete]\"\n    then:\n      field: operationId\n      function: truthy\n\n  operation-operationid-camel-case:\n    description: operationId should use camelCase.\n    severity: warn\n    given: \"$.paths[*][get,post,put,patch,delete].operationId\"\n    then:\n      function: pattern\n      functionOptions:\n        match: \"^[a-z][a-zA-Z0-9]*$\"\n\n  operation-tags-required:\n    description: Every operation must have at least one\
  \ tag.\n    severity: error\n    given: \"$.paths[*][get,post,put,patch,delete]\"\n    then:\n      field: tags\n      function: truthy\n\n  operation-summary-apache-ofbiz-prefix:\n    description: Operation summaries should start with \"Apache OFBiz\".\n    severity: info\n    given: \"$.paths[*][get,post,put,patch,delete].summary\"\n    then:\n      function: pattern\n      functionOptions:\n        match: \"^Apache OFBiz \"\n\n  # TAGS\n  tags-global-defined:\n    description: Global tags array should be defined.\n    severity: warn\n    given: \"$\"\n    then:\n      field: tags\n      function: truthy\n\n  tags-description:\n    description: Each global tag should have a description.\n    severity: warn\n    given: \"$.tags[*]\"\n    then:\n      field: description\n      function: truthy\n\n  # PARAMETERS\n  parameter-description-required:\n    description: Every parameter must have a description.\n    severity: warn\n    given: \"$.paths[*][get,post,put,patch,delete].parameters[*]\"\
  \n    then:\n      field: description\n      function: truthy\n\n  parameter-schema-required:\n    description: Every parameter must have a schema.\n    severity: error\n    given: \"$.paths[*][get,post,put,patch,delete].parameters[*]\"\n    then:\n      field: schema\n      function: truthy\n\n  # REQUEST BODIES\n  request-body-description:\n    description: Request bodies should have a description.\n    severity: warn\n    given: \"$.paths[*][post,put,patch].requestBody\"\n    then:\n      field: description\n      function: truthy\n\n  # RESPONSES\n  response-success-required:\n    description: Every operation must define at least one 2xx response.\n    severity: error\n    given: \"$.paths[*][get,post,put,patch,delete].responses\"\n    then:\n      function: schema\n      functionOptions:\n        schema:\n          type: object\n          anyOf:\n            - required: [\"200\"]\n            - required: [\"201\"]\n            - required: [\"204\"]\n\n  response-401-required:\n  \
  \  description: Secured operations should document 401 Unauthorized response.\n    severity: warn\n    given: \"$.paths[*][get,post,put,patch,delete].responses\"\n    then:\n      function: schema\n      functionOptions:\n        schema:\n          type: object\n          required: [\"401\"]\n\n  response-description-required:\n    description: Every response must have a description.\n    severity: error\n    given: \"$.paths[*][get,post,put,patch,delete].responses[*]\"\n    then:\n      field: description\n      function: truthy\n\n  # SCHEMAS\n  schema-description-required:\n    description: Top-level component schemas should have a description.\n    severity: warn\n    given: \"$.components.schemas[*]\"\n    then:\n      field: description\n      function: truthy\n\n  schema-property-description:\n    description: Schema properties should have descriptions.\n    severity: info\n    given: \"$.components.schemas[*].properties[*]\"\n    then:\n      field: description\n      function:\
  \ truthy\n\n  # SECURITY\n  security-schemes-defined:\n    description: Security schemes must be defined in components.\n    severity: error\n    given: \"$.components\"\n    then:\n      field: securitySchemes\n      function: truthy\n\n  security-global-defined:\n    description: Global security requirements should be defined.\n    severity: warn\n    given: \"$\"\n    then:\n      field: security\n      function: truthy\n\n  # HTTP METHOD CONVENTIONS\n  get-no-request-body:\n    description: GET operations must not have a request body.\n    severity: error\n    given: \"$.paths[*].get\"\n    then:\n      field: requestBody\n      function: falsy\n\n  # AUTHENTICATION\n  auth-bearer-jwt:\n    description: Bearer authentication should specify JWT format.\n    severity: info\n    given: \"$.components.securitySchemes[?(@.scheme == 'bearer')]\"\n    then:\n      field: bearerFormat\n      function: truthy\n\n  # GENERAL QUALITY\n  no-empty-descriptions:\n    description: Descriptions must\
  \ not be empty strings.\n    severity: warn\n    given: \"$..description\"\n    then:\n      function: pattern\n      functionOptions:\n        match: \".+\"\n\n  response-status-code-standard:\n    description: OFBiz API responses should include statusCode, statusDescription, and data fields.\n    severity: info\n    given: \"$.components.schemas[*].properties\"\n    then:\n      function: schema\n      functionOptions:\n        schema:\n          type: object\n          anyOf:\n            - required: [\"statusCode\"]\n"
source_yaml_url: https://raw.githubusercontent.com/api-evangelist/apache-ofbiz/refs/heads/main/rules/apache-ofbiz-spectral-rules.yml
tags:
- ERP
- CRM
- E-Commerce
- Business Applications
- Apache
- Java
- Open Source
- Supply Chain
- Spectral
- Linting
- API Governance
---
