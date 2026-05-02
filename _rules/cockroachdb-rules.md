---
api_specs:
- filename: cockroachdb-cloud-api-openapi.yml
  format: yaml
  label: CockroachDB Cloud API
  slug: cloud-api
  spec_type: OpenAPI
  url: https://raw.githubusercontent.com/api-evangelist/cockroachdb/refs/heads/main/openapi/cockroachdb-cloud-api-openapi.yml
- filename: cockroachdb-cluster-api-openapi.yml
  format: yaml
  label: CockroachDB Cluster API
  slug: cluster-api
  spec_type: OpenAPI
  url: https://raw.githubusercontent.com/api-evangelist/cockroachdb/refs/heads/main/openapi/cockroachdb-cluster-api-openapi.yml
categories:
- cockroachdb
description: Spectral linting rules defining API design standards and conventions for CockroachDB.
layout: rules
name: CockroachDB API Rules
provider_name: CockroachDB
provider_slug: cockroachdb
rule_count: 10
rules:
- description: API contact information must be present.
  given: $.info
  name: cockroachdb-info-contact
  severity: error
- description: termsOfService must reference cockroachlabs.com.
  given: $.info.termsOfService
  name: cockroachdb-terms-of-service
  severity: warn
- description: Public server URLs must use HTTPS (cluster API loopback exempt).
  given: $.servers[?(@.url && @.url.indexOf('localhost') === -1)].url
  name: cockroachdb-server-https
  severity: warn
- description: Cloud API server URL must point to cockroachlabs.cloud.
  given: $.servers[?(@.url && @.url.indexOf('cockroachlabs.cloud') > -1)].url
  name: cockroachdb-cloud-base-host
  severity: info
- description: Cloud API operations must define a bearer-token security scheme.
  given: $.components.securitySchemes[*]
  name: cockroachdb-bearer-security
  severity: error
- description: Every operation must declare a unique operationId.
  given: $.paths[*][get,post,put,patch,delete]
  name: cockroachdb-operation-id
  severity: error
- description: Operations must declare at least one tag.
  given: $.paths[*][get,post,put,patch,delete]
  name: cockroachdb-operation-tags
  severity: warn
- description: Mutating operations should declare 4xx/5xx error responses.
  given: $.paths[*][post,put,patch,delete].responses
  name: cockroachdb-error-responses
  severity: warn
- description: Path parameters named cluster_id should be UUIDs.
  given: $.paths[*].*.parameters[?(@.in == 'path' && @.name == 'cluster_id')].schema
  name: cockroachdb-uuid-cluster-id
  severity: info
- description: Use canonical CockroachDB request headers (Cc-Version, X-Cockroach-API-Session, Authorization).
  given: $.paths[*][get,post,put,patch,delete].parameters[?(@.in == 'header')]
  name: cockroachdb-headers-allowlist
  severity: info
rules_file: rules/cockroachdb-rules.yml
rules_url: https://raw.githubusercontent.com/api-evangelist/cockroachdb/refs/heads/main/rules/cockroachdb-rules.yml
severity_counts:
  error: 3
  hint: 0
  info: 3
  warn: 4
slug: cockroachdb-rules
source_filename: cockroachdb-rules.yml
source_heading: Spectral Ruleset
source_yaml: "extends:\n  - spectral:oas\n\n# Spectral linting rules for CockroachDB APIs.\n# Tuned to cockroachlabs.cloud (Cloud API) and per-node /api/v2 (Cluster API)\n# conventions: bearer tokens, Cc-Version header, X-Cockroach-API-Session for\n# the cluster API, UUID resource identifiers, and standardized error responses.\nrules:\n  cockroachdb-info-contact:\n    description: API contact information must be present.\n    severity: error\n    given: \"$.info\"\n    then:\n      field: contact\n      function: truthy\n\n  cockroachdb-terms-of-service:\n    description: termsOfService must reference cockroachlabs.com.\n    severity: warn\n    given: \"$.info.termsOfService\"\n    then:\n      function: pattern\n      functionOptions:\n        match: \"cockroachlabs.com\"\n\n  cockroachdb-server-https:\n    description: Public server URLs must use HTTPS (cluster API loopback exempt).\n    severity: warn\n    given: \"$.servers[?(@.url && @.url.indexOf('localhost') === -1)].url\"\n    then:\n\
  \      function: pattern\n      functionOptions:\n        match: \"^https://\"\n\n  cockroachdb-cloud-base-host:\n    description: Cloud API server URL must point to cockroachlabs.cloud.\n    severity: info\n    given: \"$.servers[?(@.url && @.url.indexOf('cockroachlabs.cloud') > -1)].url\"\n    then:\n      function: pattern\n      functionOptions:\n        match: \"cockroachlabs.cloud\"\n\n  cockroachdb-bearer-security:\n    description: Cloud API operations must define a bearer-token security scheme.\n    severity: error\n    given: \"$.components.securitySchemes[*]\"\n    then:\n      function: schema\n      functionOptions:\n        schema:\n          type: object\n          properties:\n            type:\n              enum: [\"http\", \"apiKey\", \"oauth2\"]\n\n  cockroachdb-operation-id:\n    description: Every operation must declare a unique operationId.\n    severity: error\n    given: \"$.paths[*][get,post,put,patch,delete]\"\n    then:\n      field: operationId\n      function:\
  \ truthy\n\n  cockroachdb-operation-tags:\n    description: Operations must declare at least one tag.\n    severity: warn\n    given: \"$.paths[*][get,post,put,patch,delete]\"\n    then:\n      field: tags\n      function: schema\n      functionOptions:\n        schema:\n          type: array\n          minItems: 1\n\n  cockroachdb-error-responses:\n    description: Mutating operations should declare 4xx/5xx error responses.\n    severity: warn\n    given: \"$.paths[*][post,put,patch,delete].responses\"\n    then:\n      function: schema\n      functionOptions:\n        schema:\n          type: object\n          anyOf:\n            - required: [\"400\"]\n            - required: [\"401\"]\n            - required: [\"403\"]\n            - required: [\"404\"]\n            - required: [\"429\"]\n\n  cockroachdb-uuid-cluster-id:\n    description: Path parameters named cluster_id should be UUIDs.\n    severity: info\n    given: \"$.paths[*].*.parameters[?(@.in == 'path' && @.name == 'cluster_id')].schema\"\
  \n    then:\n      field: format\n      function: enumeration\n      functionOptions:\n        values:\n          - uuid\n\n  cockroachdb-headers-allowlist:\n    description: Use canonical CockroachDB request headers (Cc-Version, X-Cockroach-API-Session, Authorization).\n    severity: info\n    given: \"$.paths[*][get,post,put,patch,delete].parameters[?(@.in == 'header')]\"\n    then:\n      field: name\n      function: enumeration\n      functionOptions:\n        values:\n          - Cc-Version\n          - X-Cockroach-API-Session\n          - Authorization\n"
source_yaml_url: https://raw.githubusercontent.com/api-evangelist/cockroachdb/refs/heads/main/rules/cockroachdb-rules.yml
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
