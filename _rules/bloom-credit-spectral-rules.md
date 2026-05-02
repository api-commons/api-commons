---
api_specs:
- filename: bloom-credit-api-openapi.yaml
  format: yaml
  label: Bloom Credit API
  slug: bloom-credit-api
  spec_type: OpenAPI
  url: https://raw.githubusercontent.com/api-evangelist/bloom-credit/refs/heads/main/openapi/bloom-credit-api-openapi.yaml
categories:
- bloom
description: Spectral linting rules defining API design standards and conventions for Bloom Credit.
layout: rules
name: Bloom Credit API Rules
provider_name: Bloom Credit
provider_slug: bloom-credit
rule_count: 30
rules:
- description: API must have a title
  given: $.info
  name: bloom-credit-info-title
  severity: error
- description: API must have a description
  given: $.info
  name: bloom-credit-info-description
  severity: error
- description: API must have a version
  given: $.info
  name: bloom-credit-info-version
  severity: error
- description: API must have contact information
  given: $.info
  name: bloom-credit-info-contact
  severity: warn
- description: API must have at least one server defined
  given: $
  name: bloom-credit-servers-exist
  severity: error
- description: All servers must use HTTPS
  given: $.servers[*]
  name: bloom-credit-server-https
  severity: error
- description: Each server must have a description
  given: $.servers[*]
  name: bloom-credit-server-description
  severity: warn
- description: Path segments must use kebab-case
  given: $.paths[*]~
  name: bloom-credit-path-kebab-case
  severity: warn
- description: Paths must not have trailing slashes
  given: $.paths[*]~
  name: bloom-credit-path-no-trailing-slash
  severity: error
- description: Every operation must have an operationId
  given: $.paths[*][get,post,put,patch,delete,head,options,trace]
  name: bloom-credit-operation-id-exists
  severity: error
- description: OperationId must use kebab-case
  given: $.paths[*][get,post,put,patch,delete,head,options,trace]
  name: bloom-credit-operation-id-kebab-case
  severity: warn
- description: Every operation must have a summary
  given: $.paths[*][get,post,put,patch,delete,head,options,trace]
  name: bloom-credit-operation-summary-exists
  severity: error
- description: Operation summaries must start with Bloom Credit
  given: $.paths[*][get,post,put,patch,delete,head,options,trace]
  name: bloom-credit-operation-summary-prefix
  severity: warn
- description: Every operation must have a description
  given: $.paths[*][get,post,put,patch,delete,head,options,trace]
  name: bloom-credit-operation-description-exists
  severity: warn
- description: Every operation must have at least one tag
  given: $.paths[*][get,post,put,patch,delete,head,options,trace]
  name: bloom-credit-operation-tags
  severity: warn
- description: All parameters must have a description
  given: $.paths[*][*].parameters[*]
  name: bloom-credit-parameter-description
  severity: warn
- description: All parameters must have a schema
  given: $.paths[*][*].parameters[*]
  name: bloom-credit-parameter-schema
  severity: error
- description: Operations must have at least one 2xx response
  given: $.paths[*][get,post,put,patch,delete]
  name: bloom-credit-response-success-exists
  severity: error
- description: Success responses must have a content schema
  given: $.paths[*][*].responses[200,201].content[*]
  name: bloom-credit-response-schema-exists
  severity: warn
- description: Responses should include examples
  given: $.paths[*][*].responses[200,201].content[*]
  name: bloom-credit-response-examples
  severity: warn
- description: API must define security schemes
  given: $.components
  name: bloom-credit-security-scheme-defined
  severity: error
- description: API should have global security defined
  given: $
  name: bloom-credit-global-security
  severity: warn
- description: API should use API key authentication via X-API-Key header
  given: $.components.securitySchemes[*]
  name: bloom-credit-apikey-auth
  severity: info
- description: All schema objects must have a type
  given: $.components.schemas[*]
  name: bloom-credit-schema-type
  severity: warn
- description: All schema components must have a description
  given: $.components.schemas[*]
  name: bloom-credit-schema-description
  severity: warn
- description: Schema properties should have descriptions
  given: $.components.schemas[*].properties[*]
  name: bloom-credit-property-description
  severity: info
- description: Consumer endpoints should be nested under /consumers/{consumer_id}
  given: $.paths[/consumers/{consumer_id}*]~
  name: bloom-credit-consumer-id-path
  severity: info
- description: Bureau fields should use valid bureau names
  given: $.components.schemas[*].properties.bureau.enum
  name: bloom-credit-bureau-enum
  severity: info
- description: Credit score schemas should define min/max range
  given: $.components.schemas.CreditScore.properties.score
  name: bloom-credit-score-range
  severity: info
- description: API should have a sandbox server for testing
  given: $.servers
  name: bloom-credit-sandbox-server
  severity: warn
rules_file: rules/bloom-credit-spectral-rules.yml
rules_url: https://raw.githubusercontent.com/api-evangelist/bloom-credit/refs/heads/main/rules/bloom-credit-spectral-rules.yml
severity_counts:
  error: 11
  hint: 0
  info: 5
  warn: 14
slug: bloom-credit-spectral-rules
source_filename: bloom-credit-spectral-rules.yml
source_heading: Spectral Ruleset
source_yaml: "rules:\n  # Info rules\n  bloom-credit-info-title:\n    description: API must have a title\n    severity: error\n    given: \"$.info\"\n    then:\n      field: title\n      function: truthy\n\n  bloom-credit-info-description:\n    description: API must have a description\n    severity: error\n    given: \"$.info\"\n    then:\n      field: description\n      function: truthy\n\n  bloom-credit-info-version:\n    description: API must have a version\n    severity: error\n    given: \"$.info\"\n    then:\n      field: version\n      function: truthy\n\n  bloom-credit-info-contact:\n    description: API must have contact information\n    severity: warn\n    given: \"$.info\"\n    then:\n      field: contact\n      function: truthy\n\n  # Server rules\n  bloom-credit-servers-exist:\n    description: API must have at least one server defined\n    severity: error\n    given: \"$\"\n    then:\n      field: servers\n      function: truthy\n\n  bloom-credit-server-https:\n    description:\
  \ All servers must use HTTPS\n    severity: error\n    given: \"$.servers[*]\"\n    then:\n      field: url\n      function: pattern\n      functionOptions:\n        match: \"^https://\"\n\n  bloom-credit-server-description:\n    description: Each server must have a description\n    severity: warn\n    given: \"$.servers[*]\"\n    then:\n      field: description\n      function: truthy\n\n  # Path rules\n  bloom-credit-path-kebab-case:\n    description: Path segments must use kebab-case\n    severity: warn\n    given: \"$.paths[*]~\"\n    then:\n      function: pattern\n      functionOptions:\n        match: \"^(/[a-z0-9-{}]+)+$\"\n\n  bloom-credit-path-no-trailing-slash:\n    description: Paths must not have trailing slashes\n    severity: error\n    given: \"$.paths[*]~\"\n    then:\n      function: pattern\n      functionOptions:\n        notMatch: \"/$\"\n\n  # Operation rules\n  bloom-credit-operation-id-exists:\n    description: Every operation must have an operationId\n    severity:\
  \ error\n    given: \"$.paths[*][get,post,put,patch,delete,head,options,trace]\"\n    then:\n      field: operationId\n      function: truthy\n\n  bloom-credit-operation-id-kebab-case:\n    description: OperationId must use kebab-case\n    severity: warn\n    given: \"$.paths[*][get,post,put,patch,delete,head,options,trace]\"\n    then:\n      field: operationId\n      function: pattern\n      functionOptions:\n        match: \"^[a-z][a-z0-9-]+$\"\n\n  bloom-credit-operation-summary-exists:\n    description: Every operation must have a summary\n    severity: error\n    given: \"$.paths[*][get,post,put,patch,delete,head,options,trace]\"\n    then:\n      field: summary\n      function: truthy\n\n  bloom-credit-operation-summary-prefix:\n    description: Operation summaries must start with Bloom Credit\n    severity: warn\n    given: \"$.paths[*][get,post,put,patch,delete,head,options,trace]\"\n    then:\n      field: summary\n      function: pattern\n      functionOptions:\n        match:\
  \ \"^Bloom Credit\"\n\n  bloom-credit-operation-description-exists:\n    description: Every operation must have a description\n    severity: warn\n    given: \"$.paths[*][get,post,put,patch,delete,head,options,trace]\"\n    then:\n      field: description\n      function: truthy\n\n  bloom-credit-operation-tags:\n    description: Every operation must have at least one tag\n    severity: warn\n    given: \"$.paths[*][get,post,put,patch,delete,head,options,trace]\"\n    then:\n      field: tags\n      function: truthy\n\n  # Parameter rules\n  bloom-credit-parameter-description:\n    description: All parameters must have a description\n    severity: warn\n    given: \"$.paths[*][*].parameters[*]\"\n    then:\n      field: description\n      function: truthy\n\n  bloom-credit-parameter-schema:\n    description: All parameters must have a schema\n    severity: error\n    given: \"$.paths[*][*].parameters[*]\"\n    then:\n      field: schema\n      function: truthy\n\n  # Response rules\n \
  \ bloom-credit-response-success-exists:\n    description: Operations must have at least one 2xx response\n    severity: error\n    given: \"$.paths[*][get,post,put,patch,delete]\"\n    then:\n      field: responses\n      function: schema\n      functionOptions:\n        schema:\n          type: object\n          anyOf:\n            - required: [\"200\"]\n            - required: [\"201\"]\n            - required: [\"202\"]\n            - required: [\"204\"]\n\n  bloom-credit-response-schema-exists:\n    description: Success responses must have a content schema\n    severity: warn\n    given: \"$.paths[*][*].responses[200,201].content[*]\"\n    then:\n      field: schema\n      function: truthy\n\n  bloom-credit-response-examples:\n    description: Responses should include examples\n    severity: warn\n    given: \"$.paths[*][*].responses[200,201].content[*]\"\n    then:\n      field: examples\n      function: truthy\n\n  # Security rules\n  bloom-credit-security-scheme-defined:\n    description:\
  \ API must define security schemes\n    severity: error\n    given: \"$.components\"\n    then:\n      field: securitySchemes\n      function: truthy\n\n  bloom-credit-global-security:\n    description: API should have global security defined\n    severity: warn\n    given: \"$\"\n    then:\n      field: security\n      function: truthy\n\n  bloom-credit-apikey-auth:\n    description: API should use API key authentication via X-API-Key header\n    severity: info\n    given: \"$.components.securitySchemes[*]\"\n    then:\n      function: truthy\n\n  # Schema rules\n  bloom-credit-schema-type:\n    description: All schema objects must have a type\n    severity: warn\n    given: \"$.components.schemas[*]\"\n    then:\n      field: type\n      function: truthy\n\n  bloom-credit-schema-description:\n    description: All schema components must have a description\n    severity: warn\n    given: \"$.components.schemas[*]\"\n    then:\n      field: description\n      function: truthy\n\n  bloom-credit-property-description:\n\
  \    description: Schema properties should have descriptions\n    severity: info\n    given: \"$.components.schemas[*].properties[*]\"\n    then:\n      field: description\n      function: truthy\n\n  # Bloom Credit-specific rules\n  bloom-credit-consumer-id-path:\n    description: Consumer endpoints should be nested under /consumers/{consumer_id}\n    severity: info\n    given: \"$.paths[/consumers/{consumer_id}*]~\"\n    then:\n      function: truthy\n\n  bloom-credit-bureau-enum:\n    description: Bureau fields should use valid bureau names\n    severity: info\n    given: \"$.components.schemas[*].properties.bureau.enum\"\n    then:\n      function: truthy\n\n  bloom-credit-score-range:\n    description: Credit score schemas should define min/max range\n    severity: info\n    given: \"$.components.schemas.CreditScore.properties.score\"\n    then:\n      function: truthy\n\n  bloom-credit-sandbox-server:\n    description: API should have a sandbox server for testing\n    severity: warn\n\
  \    given: \"$.servers\"\n    then:\n      function: schema\n      functionOptions:\n        schema:\n          type: array\n          minItems: 2\n"
source_yaml_url: https://raw.githubusercontent.com/api-evangelist/bloom-credit/refs/heads/main/rules/bloom-credit-spectral-rules.yml
tags:
- Credit Bureau
- Credit Reports
- Credit Scores
- Fintech
- Lending
- Personal Finance
- Spectral
- Linting
- API Governance
---
