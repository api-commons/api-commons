---
api_specs:
- filename: cockroach-labs-cloud-api-openapi.yml
  format: yaml
  label: CockroachDB Cloud API
  slug: cockroach-labs-cloud-api
  spec_type: OpenAPI
  url: https://raw.githubusercontent.com/api-evangelist/cockroach-labs/refs/heads/main/openapi/cockroach-labs-cloud-api-openapi.yml
- filename: cockroach-labs-cluster-api-openapi.yml
  format: yaml
  label: CockroachDB Cluster API
  slug: cockroach-labs-cluster-api
  spec_type: OpenAPI
  url: https://raw.githubusercontent.com/api-evangelist/cockroach-labs/refs/heads/main/openapi/cockroach-labs-cluster-api-openapi.yml
categories:
- cockroach
description: Spectral linting rules defining API design standards and conventions for Cockroach Labs.
layout: rules
name: Cockroach Labs API Rules
provider_name: Cockroach Labs
provider_slug: cockroach-labs
rule_count: 10
rules:
- description: API contact information must be present.
  given: $.info
  name: cockroach-labs-info-contact
  severity: error
- description: termsOfService must reference cockroachlabs.com.
  given: $.info.termsOfService
  name: cockroach-labs-terms-of-service
  severity: warn
- description: Public server URLs must use HTTPS (cluster API loopback exempt).
  given: $.servers[?(@.url && @.url.indexOf('localhost') === -1)].url
  name: cockroach-labs-server-https
  severity: warn
- description: Cloud API server URL must point to cockroachlabs.cloud.
  given: $.servers[?(@.url && @.url.indexOf('cockroachlabs.cloud') > -1)].url
  name: cockroach-labs-cloud-base-host
  severity: info
- description: Cloud API operations must define a bearer-token security scheme.
  given: $.components.securitySchemes[*]
  name: cockroach-labs-bearer-security
  severity: error
- description: Every operation must declare a unique operationId.
  given: $.paths[*][get,post,put,patch,delete]
  name: cockroach-labs-operation-id
  severity: error
- description: Operations must declare at least one tag.
  given: $.paths[*][get,post,put,patch,delete]
  name: cockroach-labs-operation-tags
  severity: warn
- description: Mutating operations should declare 4xx/5xx error responses.
  given: $.paths[*][post,put,patch,delete].responses
  name: cockroach-labs-error-responses
  severity: warn
- description: Path parameters named cluster_id should be UUIDs.
  given: $.paths[*].*.parameters[?(@.in == 'path' && @.name == 'cluster_id')].schema
  name: cockroach-labs-uuid-cluster-id
  severity: info
- description: Cloud API requests should support the Cc-Version versioning header.
  given: $.paths[*][get,post,put,patch,delete].parameters[?(@.in == 'header')]
  name: cockroach-labs-cc-version-header
  severity: info
rules_file: rules/cockroach-labs-rules.yml
rules_url: https://raw.githubusercontent.com/api-evangelist/cockroach-labs/refs/heads/main/rules/cockroach-labs-rules.yml
severity_counts:
  error: 3
  hint: 0
  info: 3
  warn: 4
slug: cockroach-labs-rules
source_filename: cockroach-labs-rules.yml
source_heading: Spectral Ruleset
source_yaml: "extends:\n  - spectral:oas\n\n# Spectral linting rules for Cockroach Labs APIs.\n# Tuned to cockroachlabs.cloud (Cloud API) and per-node /api/v2 (Cluster API)\n# conventions: HTTPS for cloud, bearer tokens, Cc-Version header, UUID\n# resource identifiers, and standardized error envelopes.\nrules:\n  cockroach-labs-info-contact:\n    description: API contact information must be present.\n    severity: error\n    given: \"$.info\"\n    then:\n      field: contact\n      function: truthy\n\n  cockroach-labs-terms-of-service:\n    description: termsOfService must reference cockroachlabs.com.\n    severity: warn\n    given: \"$.info.termsOfService\"\n    then:\n      function: pattern\n      functionOptions:\n        match: \"cockroachlabs.com\"\n\n  cockroach-labs-server-https:\n    description: Public server URLs must use HTTPS (cluster API loopback exempt).\n    severity: warn\n    given: \"$.servers[?(@.url && @.url.indexOf('localhost') === -1)].url\"\n    then:\n      function:\
  \ pattern\n      functionOptions:\n        match: \"^https://\"\n\n  cockroach-labs-cloud-base-host:\n    description: Cloud API server URL must point to cockroachlabs.cloud.\n    severity: info\n    given: \"$.servers[?(@.url && @.url.indexOf('cockroachlabs.cloud') > -1)].url\"\n    then:\n      function: pattern\n      functionOptions:\n        match: \"cockroachlabs.cloud\"\n\n  cockroach-labs-bearer-security:\n    description: Cloud API operations must define a bearer-token security scheme.\n    severity: error\n    given: \"$.components.securitySchemes[*]\"\n    then:\n      function: schema\n      functionOptions:\n        schema:\n          type: object\n          properties:\n            type:\n              enum: [\"http\", \"apiKey\", \"oauth2\"]\n\n  cockroach-labs-operation-id:\n    description: Every operation must declare a unique operationId.\n    severity: error\n    given: \"$.paths[*][get,post,put,patch,delete]\"\n    then:\n      field: operationId\n      function: truthy\n\
  \n  cockroach-labs-operation-tags:\n    description: Operations must declare at least one tag.\n    severity: warn\n    given: \"$.paths[*][get,post,put,patch,delete]\"\n    then:\n      field: tags\n      function: schema\n      functionOptions:\n        schema:\n          type: array\n          minItems: 1\n\n  cockroach-labs-error-responses:\n    description: Mutating operations should declare 4xx/5xx error responses.\n    severity: warn\n    given: \"$.paths[*][post,put,patch,delete].responses\"\n    then:\n      function: schema\n      functionOptions:\n        schema:\n          type: object\n          anyOf:\n            - required: [\"400\"]\n            - required: [\"401\"]\n            - required: [\"403\"]\n            - required: [\"404\"]\n            - required: [\"429\"]\n\n  cockroach-labs-uuid-cluster-id:\n    description: Path parameters named cluster_id should be UUIDs.\n    severity: info\n    given: \"$.paths[*].*.parameters[?(@.in == 'path' && @.name == 'cluster_id')].schema\"\
  \n    then:\n      field: format\n      function: enumeration\n      functionOptions:\n        values:\n          - uuid\n\n  cockroach-labs-cc-version-header:\n    description: Cloud API requests should support the Cc-Version versioning header.\n    severity: info\n    given: \"$.paths[*][get,post,put,patch,delete].parameters[?(@.in == 'header')]\"\n    then:\n      field: name\n      function: enumeration\n      functionOptions:\n        values:\n          - Cc-Version\n          - X-Cockroach-API-Session\n          - Authorization\n"
source_yaml_url: https://raw.githubusercontent.com/api-evangelist/cockroach-labs/refs/heads/main/rules/cockroach-labs-rules.yml
tags:
- Cluster Management
- Cloud
- Database
- Distributed SQL
- Infrastructure
- PostgreSQL Compatible
- SQL
- Spectral
- Linting
- API Governance
---
