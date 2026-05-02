---
api_specs:
- filename: avaloq-banking-openapi.yml
  format: yaml
  label: Avaloq Banking API
  slug: avaloq-banking-api
  spec_type: OpenAPI
  url: https://raw.githubusercontent.com/api-evangelist/avaloq/refs/heads/main/openapi/avaloq-banking-openapi.yml
- filename: avaloq-wealth-management-openapi.yml
  format: yaml
  label: Avaloq Wealth Management API
  slug: avaloq-wealth-management-api
  spec_type: OpenAPI
  url: https://raw.githubusercontent.com/api-evangelist/avaloq/refs/heads/main/openapi/avaloq-wealth-management-openapi.yml
- filename: avaloq-payments-openapi.yml
  format: yaml
  label: Avaloq Payments API
  slug: avaloq-payments-api
  spec_type: OpenAPI
  url: https://raw.githubusercontent.com/api-evangelist/avaloq/refs/heads/main/openapi/avaloq-payments-openapi.yml
- filename: avaloq-client-management-openapi.yml
  format: yaml
  label: Avaloq Client Management API
  slug: avaloq-client-management-api
  spec_type: OpenAPI
  url: https://raw.githubusercontent.com/api-evangelist/avaloq/refs/heads/main/openapi/avaloq-client-management-openapi.yml
- filename: avaloq-trading-openapi.yml
  format: yaml
  label: Avaloq Trading API
  slug: avaloq-trading-api
  spec_type: OpenAPI
  url: https://raw.githubusercontent.com/api-evangelist/avaloq/refs/heads/main/openapi/avaloq-trading-openapi.yml
- filename: avaloq-compliance-openapi.yml
  format: yaml
  label: Avaloq Compliance & Risk API
  slug: avaloq-compliance-api
  spec_type: OpenAPI
  url: https://raw.githubusercontent.com/api-evangelist/avaloq/refs/heads/main/openapi/avaloq-compliance-openapi.yml
categories:
- avaloq
description: Spectral linting rules defining API design standards and conventions for Avaloq.
layout: rules
name: Avaloq API Rules
provider_name: Avaloq
provider_slug: avaloq
rule_count: 25
rules:
- description: Avaloq APIs must have a title in the info object.
  given: $.info
  name: avaloq-info-title-required
  severity: error
- description: Avaloq APIs must define a version.
  given: $.info
  name: avaloq-info-version-required
  severity: error
- description: Avaloq APIs must have a description.
  given: $.info
  name: avaloq-info-description-required
  severity: warn
- description: Avaloq APIs must include contact information.
  given: $.info
  name: avaloq-info-contact-required
  severity: warn
- description: Avaloq APIs must define at least one server.
  given: $
  name: avaloq-servers-required
  severity: error
- description: Avaloq server URLs must use HTTPS.
  given: $.servers[*]
  name: avaloq-server-url-https
  severity: error
- description: Avaloq path segments must use kebab-case.
  given: $.paths
  name: avaloq-paths-kebab-case
  severity: warn
- description: All Avaloq operations must have a summary.
  given: $.paths[*][get,post,put,patch,delete]
  name: avaloq-operation-summary-required
  severity: error
- description: All Avaloq operations must have a description.
  given: $.paths[*][get,post,put,patch,delete]
  name: avaloq-operation-description-required
  severity: warn
- description: All Avaloq operations must have an operationId.
  given: $.paths[*][get,post,put,patch,delete]
  name: avaloq-operation-id-required
  severity: error
- description: All Avaloq operations must have at least one tag.
  given: $.paths[*][get,post,put,patch,delete]
  name: avaloq-operation-tags-required
  severity: warn
- description: All Avaloq parameters must have a description.
  given: $.paths[*][get,post,put,patch,delete].parameters[*]
  name: avaloq-parameters-description-required
  severity: warn
- description: Avaloq request bodies must have a description.
  given: $.paths[*][post,put,patch].requestBody
  name: avaloq-request-body-description
  severity: warn
- description: Avaloq GET operations must have a 200 response.
  given: $.paths[*].get.responses
  name: avaloq-response-200-required
  severity: error
- description: Avaloq operations must document 400 errors.
  given: $.paths[*][get,post,put,patch,delete].responses
  name: avaloq-response-400-required
  severity: warn
- description: Avaloq operations must document 401 unauthorized.
  given: $.paths[*][get,post,put,patch,delete].responses
  name: avaloq-response-401-required
  severity: warn
- description: Avaloq schema properties must have descriptions.
  given: $.components.schemas[*].properties[*]
  name: avaloq-schema-properties-described
  severity: warn
- description: Avaloq schema properties must have a type.
  given: $.components.schemas[*].properties[*]
  name: avaloq-schema-type-required
  severity: warn
- description: Avaloq APIs must define security schemes.
  given: $.components
  name: avaloq-security-defined
  severity: error
- description: Avaloq APIs must use Bearer/JWT authentication.
  given: $.components.securitySchemes[*]
  name: avaloq-bearer-auth-required
  severity: warn
- description: Avaloq GET operations must not have a request body.
  given: $.paths[*].get
  name: avaloq-get-no-request-body
  severity: error
- description: Avaloq DELETE operations must not have a request body.
  given: $.paths[*].delete
  name: avaloq-delete-no-request-body
  severity: warn
- description: Avaloq POST creation operations should return 201.
  given: $.paths[*].post.responses
  name: avaloq-post-returns-201
  severity: warn
- description: Avaloq schemas should have examples.
  given: $.components.schemas[*]
  name: avaloq-schema-example-provided
  severity: info
- description: Avaloq API responses must specify content type.
  given: $.paths[*][get,post,put,patch].responses[*]
  name: avaloq-response-content-type
  severity: warn
rules_file: rules/avaloq-spectral-rules.yml
rules_url: https://raw.githubusercontent.com/api-evangelist/avaloq/refs/heads/main/rules/avaloq-spectral-rules.yml
severity_counts:
  error: 9
  hint: 0
  info: 1
  warn: 15
slug: avaloq-spectral-rules
source_filename: avaloq-spectral-rules.yml
source_heading: Spectral Ruleset
source_yaml: "rules:\n  avaloq-info-title-required:\n    description: \"Avaloq APIs must have a title in the info object.\"\n    message: \"Info object must have a title.\"\n    severity: error\n    given: \"$.info\"\n    then:\n      field: title\n      function: truthy\n\n  avaloq-info-version-required:\n    description: \"Avaloq APIs must define a version.\"\n    message: \"Info object must have a version.\"\n    severity: error\n    given: \"$.info\"\n    then:\n      field: version\n      function: truthy\n\n  avaloq-info-description-required:\n    description: \"Avaloq APIs must have a description.\"\n    message: \"Info object must have a description.\"\n    severity: warn\n    given: \"$.info\"\n    then:\n      field: description\n      function: truthy\n\n  avaloq-info-contact-required:\n    description: \"Avaloq APIs must include contact information.\"\n    message: \"Info object must have a contact.\"\n    severity: warn\n    given: \"$.info\"\n    then:\n      field: contact\n\
  \      function: truthy\n\n  avaloq-servers-required:\n    description: \"Avaloq APIs must define at least one server.\"\n    message: \"Servers array must be defined and non-empty.\"\n    severity: error\n    given: \"$\"\n    then:\n      field: servers\n      function: truthy\n\n  avaloq-server-url-https:\n    description: \"Avaloq server URLs must use HTTPS.\"\n    message: \"Server URL must use HTTPS protocol.\"\n    severity: error\n    given: \"$.servers[*]\"\n    then:\n      field: url\n      function: pattern\n      functionOptions:\n        match: \"^https://\"\n\n  avaloq-paths-kebab-case:\n    description: \"Avaloq path segments must use kebab-case.\"\n    message: \"Path segments must use lowercase kebab-case.\"\n    severity: warn\n    given: \"$.paths\"\n    then:\n      function: pattern\n      functionOptions:\n        match: \"^(\\\\/[a-z0-9-{}]+)+$\"\n\n  avaloq-operation-summary-required:\n    description: \"All Avaloq operations must have a summary.\"\n    message:\
  \ \"Operation must have a summary.\"\n    severity: error\n    given: \"$.paths[*][get,post,put,patch,delete]\"\n    then:\n      field: summary\n      function: truthy\n\n  avaloq-operation-description-required:\n    description: \"All Avaloq operations must have a description.\"\n    message: \"Operation must have a description.\"\n    severity: warn\n    given: \"$.paths[*][get,post,put,patch,delete]\"\n    then:\n      field: description\n      function: truthy\n\n  avaloq-operation-id-required:\n    description: \"All Avaloq operations must have an operationId.\"\n    message: \"Operation must have an operationId.\"\n    severity: error\n    given: \"$.paths[*][get,post,put,patch,delete]\"\n    then:\n      field: operationId\n      function: truthy\n\n  avaloq-operation-tags-required:\n    description: \"All Avaloq operations must have at least one tag.\"\n    message: \"Operation must have at least one tag.\"\n    severity: warn\n    given: \"$.paths[*][get,post,put,patch,delete]\"\
  \n    then:\n      field: tags\n      function: truthy\n\n  avaloq-parameters-description-required:\n    description: \"All Avaloq parameters must have a description.\"\n    message: \"Parameter must have a description.\"\n    severity: warn\n    given: \"$.paths[*][get,post,put,patch,delete].parameters[*]\"\n    then:\n      field: description\n      function: truthy\n\n  avaloq-request-body-description:\n    description: \"Avaloq request bodies must have a description.\"\n    message: \"Request body must have a description.\"\n    severity: warn\n    given: \"$.paths[*][post,put,patch].requestBody\"\n    then:\n      field: description\n      function: truthy\n\n  avaloq-response-200-required:\n    description: \"Avaloq GET operations must have a 200 response.\"\n    message: \"GET operation must define a 200 response.\"\n    severity: error\n    given: \"$.paths[*].get.responses\"\n    then:\n      field: \"200\"\n      function: truthy\n\n  avaloq-response-400-required:\n    description:\
  \ \"Avaloq operations must document 400 errors.\"\n    message: \"Operation must define a 400 error response.\"\n    severity: warn\n    given: \"$.paths[*][get,post,put,patch,delete].responses\"\n    then:\n      field: \"400\"\n      function: truthy\n\n  avaloq-response-401-required:\n    description: \"Avaloq operations must document 401 unauthorized.\"\n    message: \"Operation must define a 401 response.\"\n    severity: warn\n    given: \"$.paths[*][get,post,put,patch,delete].responses\"\n    then:\n      field: \"401\"\n      function: truthy\n\n  avaloq-schema-properties-described:\n    description: \"Avaloq schema properties must have descriptions.\"\n    message: \"Schema property must have a description.\"\n    severity: warn\n    given: \"$.components.schemas[*].properties[*]\"\n    then:\n      field: description\n      function: truthy\n\n  avaloq-schema-type-required:\n    description: \"Avaloq schema properties must have a type.\"\n    message: \"Schema property must have\
  \ a type.\"\n    severity: warn\n    given: \"$.components.schemas[*].properties[*]\"\n    then:\n      field: type\n      function: truthy\n\n  avaloq-security-defined:\n    description: \"Avaloq APIs must define security schemes.\"\n    message: \"Components must include securitySchemes.\"\n    severity: error\n    given: \"$.components\"\n    then:\n      field: securitySchemes\n      function: truthy\n\n  avaloq-bearer-auth-required:\n    description: \"Avaloq APIs must use Bearer/JWT authentication.\"\n    message: \"Security scheme must be OAuth2 or bearer type.\"\n    severity: warn\n    given: \"$.components.securitySchemes[*]\"\n    then:\n      field: type\n      function: enumeration\n      functionOptions:\n        values: [oauth2, http, apiKey]\n\n  avaloq-get-no-request-body:\n    description: \"Avaloq GET operations must not have a request body.\"\n    message: \"GET operations must not include a requestBody.\"\n    severity: error\n    given: \"$.paths[*].get\"\n    then:\n\
  \      field: requestBody\n      function: falsy\n\n  avaloq-delete-no-request-body:\n    description: \"Avaloq DELETE operations must not have a request body.\"\n    message: \"DELETE operations must not include a requestBody.\"\n    severity: warn\n    given: \"$.paths[*].delete\"\n    then:\n      field: requestBody\n      function: falsy\n\n  avaloq-post-returns-201:\n    description: \"Avaloq POST creation operations should return 201.\"\n    message: \"POST operations creating resources should return 201.\"\n    severity: warn\n    given: \"$.paths[*].post.responses\"\n    then:\n      field: \"201\"\n      function: truthy\n\n  avaloq-schema-example-provided:\n    description: \"Avaloq schemas should have examples.\"\n    message: \"Schema should include an example.\"\n    severity: info\n    given: \"$.components.schemas[*]\"\n    then:\n      field: example\n      function: truthy\n\n  avaloq-response-content-type:\n    description: \"Avaloq API responses must specify content\
  \ type.\"\n    message: \"Response must define a content type.\"\n    severity: warn\n    given: \"$.paths[*][get,post,put,patch].responses[*]\"\n    then:\n      field: content\n      function: truthy\n"
source_yaml_url: https://raw.githubusercontent.com/api-evangelist/avaloq/refs/heads/main/rules/avaloq-spectral-rules.yml
tags:
- Banking
- Digital Banking
- Financial Services
- Fintech
- Payments
- Wealth Management
- Spectral
- Linting
- API Governance
---
