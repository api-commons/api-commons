---
api_specs:
- filename: block-square-api-openapi.yaml
  format: yaml
  label: Square API
  slug: block-square-api
  spec_type: OpenAPI
  url: https://raw.githubusercontent.com/api-evangelist/block/refs/heads/main/openapi/block-square-api-openapi.yaml
categories:
- block
description: Spectral linting rules defining API design standards and conventions for Block.
layout: rules
name: Block API Rules
provider_name: Block
provider_slug: block
rule_count: 29
rules:
- description: API must have a title
  given: $.info
  name: block-info-title
  severity: error
- description: API must have a description
  given: $.info
  name: block-info-description
  severity: error
- description: API must have a version
  given: $.info
  name: block-info-version
  severity: error
- description: API must have contact information
  given: $.info
  name: block-info-contact
  severity: warn
- description: API must have at least one server defined
  given: $
  name: block-servers-exist
  severity: error
- description: Production server must use HTTPS
  given: $.servers[*]
  name: block-server-https
  severity: error
- description: Each server must have a description
  given: $.servers[*]
  name: block-server-description
  severity: warn
- description: Path segments must use kebab-case or snake_case
  given: $.paths[*]~
  name: block-path-kebab-case
  severity: warn
- description: Paths must not have trailing slashes
  given: $.paths[*]~
  name: block-path-no-trailing-slash
  severity: error
- description: Every operation must have an operationId
  given: $.paths[*][get,post,put,patch,delete,head,options,trace]
  name: block-operation-id-exists
  severity: error
- description: OperationId must use kebab-case
  given: $.paths[*][get,post,put,patch,delete,head,options,trace]
  name: block-operation-id-kebab-case
  severity: warn
- description: Every operation must have a summary
  given: $.paths[*][get,post,put,patch,delete,head,options,trace]
  name: block-operation-summary-exists
  severity: error
- description: Operation summary must use title case and start with Block Square
  given: $.paths[*][get,post,put,patch,delete,head,options,trace]
  name: block-operation-summary-title-case
  severity: warn
- description: Every operation must have a description
  given: $.paths[*][get,post,put,patch,delete,head,options,trace]
  name: block-operation-description-exists
  severity: warn
- description: Every operation must have at least one tag
  given: $.paths[*][get,post,put,patch,delete,head,options,trace]
  name: block-operation-tags
  severity: warn
- description: All parameters must have a description
  given: $.paths[*][*].parameters[*]
  name: block-parameter-description
  severity: warn
- description: All parameters must have a schema
  given: $.paths[*][*].parameters[*]
  name: block-parameter-schema
  severity: error
- description: Request bodies should have a description
  given: $.paths[*][*].requestBody
  name: block-request-body-description
  severity: warn
- description: Operations must have at least one 2xx response
  given: $.paths[*][get,post,put,patch,delete]
  name: block-response-success-exists
  severity: error
- description: Success responses must have a content schema
  given: $.paths[*][*].responses[200,201].content[*]
  name: block-response-schema-exists
  severity: warn
- description: Responses should include examples
  given: $.paths[*][*].responses[200,201].content[*]
  name: block-response-examples
  severity: warn
- description: API must define security schemes
  given: $.components
  name: block-security-scheme-defined
  severity: error
- description: API should have global security defined
  given: $
  name: block-global-security
  severity: warn
- description: All schema objects must have a type
  given: $.components.schemas[*]
  name: block-schema-type
  severity: warn
- description: All schema components must have a description
  given: $.components.schemas[*]
  name: block-schema-description
  severity: warn
- description: Schema properties should have descriptions
  given: $.components.schemas[*].properties[*]
  name: block-property-description
  severity: info
- description: POST operations creating resources should require idempotency_key
  given: $.paths[*].post.requestBody.content[*].schema.required[*]
  name: block-idempotency-key
  severity: warn
- description: Money amounts should use the Money object pattern with amount and currency
  given: $.components.schemas[*].properties[*_money]
  name: block-money-object
  severity: info
- description: List operations should support cursor-based pagination
  given: $.paths[*].get.parameters[*]
  name: block-cursor-pagination
  severity: info
rules_file: rules/block-spectral-rules.yml
rules_url: https://raw.githubusercontent.com/api-evangelist/block/refs/heads/main/rules/block-spectral-rules.yml
severity_counts:
  error: 11
  hint: 0
  info: 3
  warn: 15
slug: block-spectral-rules
source_filename: block-spectral-rules.yml
source_heading: Spectral Ruleset
source_yaml: "rules:\n  # Info rules\n  block-info-title:\n    description: API must have a title\n    severity: error\n    given: \"$.info\"\n    then:\n      field: title\n      function: truthy\n\n  block-info-description:\n    description: API must have a description\n    severity: error\n    given: \"$.info\"\n    then:\n      field: description\n      function: truthy\n\n  block-info-version:\n    description: API must have a version\n    severity: error\n    given: \"$.info\"\n    then:\n      field: version\n      function: truthy\n\n  block-info-contact:\n    description: API must have contact information\n    severity: warn\n    given: \"$.info\"\n    then:\n      field: contact\n      function: truthy\n\n  # Server rules\n  block-servers-exist:\n    description: API must have at least one server defined\n    severity: error\n    given: \"$\"\n    then:\n      field: servers\n      function: truthy\n\n  block-server-https:\n    description: Production server must use HTTPS\n  \
  \  severity: error\n    given: \"$.servers[*]\"\n    then:\n      field: url\n      function: pattern\n      functionOptions:\n        match: \"^https://\"\n\n  block-server-description:\n    description: Each server must have a description\n    severity: warn\n    given: \"$.servers[*]\"\n    then:\n      field: description\n      function: truthy\n\n  # Path rules\n  block-path-kebab-case:\n    description: Path segments must use kebab-case or snake_case\n    severity: warn\n    given: \"$.paths[*]~\"\n    then:\n      function: pattern\n      functionOptions:\n        match: \"^(/[a-z0-9_-{}]+)+$\"\n\n  block-path-no-trailing-slash:\n    description: Paths must not have trailing slashes\n    severity: error\n    given: \"$.paths[*]~\"\n    then:\n      function: pattern\n      functionOptions:\n        notMatch: \"/$\"\n\n  # Operation rules\n  block-operation-id-exists:\n    description: Every operation must have an operationId\n    severity: error\n    given: \"$.paths[*][get,post,put,patch,delete,head,options,trace]\"\
  \n    then:\n      field: operationId\n      function: truthy\n\n  block-operation-id-kebab-case:\n    description: OperationId must use kebab-case\n    severity: warn\n    given: \"$.paths[*][get,post,put,patch,delete,head,options,trace]\"\n    then:\n      field: operationId\n      function: pattern\n      functionOptions:\n        match: \"^[a-z][a-z0-9-]+$\"\n\n  block-operation-summary-exists:\n    description: Every operation must have a summary\n    severity: error\n    given: \"$.paths[*][get,post,put,patch,delete,head,options,trace]\"\n    then:\n      field: summary\n      function: truthy\n\n  block-operation-summary-title-case:\n    description: Operation summary must use title case and start with Block Square\n    severity: warn\n    given: \"$.paths[*][get,post,put,patch,delete,head,options,trace]\"\n    then:\n      field: summary\n      function: pattern\n      functionOptions:\n        match: \"^Block Square\"\n\n  block-operation-description-exists:\n    description:\
  \ Every operation must have a description\n    severity: warn\n    given: \"$.paths[*][get,post,put,patch,delete,head,options,trace]\"\n    then:\n      field: description\n      function: truthy\n\n  block-operation-tags:\n    description: Every operation must have at least one tag\n    severity: warn\n    given: \"$.paths[*][get,post,put,patch,delete,head,options,trace]\"\n    then:\n      field: tags\n      function: truthy\n\n  # Parameter rules\n  block-parameter-description:\n    description: All parameters must have a description\n    severity: warn\n    given: \"$.paths[*][*].parameters[*]\"\n    then:\n      field: description\n      function: truthy\n\n  block-parameter-schema:\n    description: All parameters must have a schema\n    severity: error\n    given: \"$.paths[*][*].parameters[*]\"\n    then:\n      field: schema\n      function: truthy\n\n  # Request body rules\n  block-request-body-description:\n    description: Request bodies should have a description\n    severity:\
  \ warn\n    given: \"$.paths[*][*].requestBody\"\n    then:\n      field: description\n      function: truthy\n\n  # Response rules\n  block-response-success-exists:\n    description: Operations must have at least one 2xx response\n    severity: error\n    given: \"$.paths[*][get,post,put,patch,delete]\"\n    then:\n      field: responses\n      function: schema\n      functionOptions:\n        schema:\n          type: object\n          anyOf:\n            - required: [\"200\"]\n            - required: [\"201\"]\n            - required: [\"202\"]\n            - required: [\"204\"]\n\n  block-response-schema-exists:\n    description: Success responses must have a content schema\n    severity: warn\n    given: \"$.paths[*][*].responses[200,201].content[*]\"\n    then:\n      field: schema\n      function: truthy\n\n  block-response-examples:\n    description: Responses should include examples\n    severity: warn\n    given: \"$.paths[*][*].responses[200,201].content[*]\"\n    then:\n   \
  \   field: examples\n      function: truthy\n\n  # Security rules\n  block-security-scheme-defined:\n    description: API must define security schemes\n    severity: error\n    given: \"$.components\"\n    then:\n      field: securitySchemes\n      function: truthy\n\n  block-global-security:\n    description: API should have global security defined\n    severity: warn\n    given: \"$\"\n    then:\n      field: security\n      function: truthy\n\n  # Schema rules\n  block-schema-type:\n    description: All schema objects must have a type\n    severity: warn\n    given: \"$.components.schemas[*]\"\n    then:\n      field: type\n      function: truthy\n\n  block-schema-description:\n    description: All schema components must have a description\n    severity: warn\n    given: \"$.components.schemas[*]\"\n    then:\n      field: description\n      function: truthy\n\n  block-property-description:\n    description: Schema properties should have descriptions\n    severity: info\n    given:\
  \ \"$.components.schemas[*].properties[*]\"\n    then:\n      field: description\n      function: truthy\n\n  # Square-specific rules\n  block-idempotency-key:\n    description: POST operations creating resources should require idempotency_key\n    severity: warn\n    given: \"$.paths[*].post.requestBody.content[*].schema.required[*]\"\n    then:\n      function: pattern\n      functionOptions:\n        match: \"idempotency_key\"\n\n  block-money-object:\n    description: Money amounts should use the Money object pattern with amount and currency\n    severity: info\n    given: \"$.components.schemas[*].properties[*_money]\"\n    then:\n      function: truthy\n\n  block-cursor-pagination:\n    description: List operations should support cursor-based pagination\n    severity: info\n    given: \"$.paths[*].get.parameters[*]\"\n    then:\n      function: truthy\n"
source_yaml_url: https://raw.githubusercontent.com/api-evangelist/block/refs/heads/main/rules/block-spectral-rules.yml
tags:
- Commerce
- Cryptocurrency
- eCommerce
- Fintech
- Payments
- Point Of Sale
- Square
- Spectral
- Linting
- API Governance
---
