---
api_specs:
- filename: couchbase-server-rest-api-openapi.yml
  format: yaml
  label: Couchbase Server REST API
  slug: couchbase-server-rest-api
  spec_type: OpenAPI
  url: https://raw.githubusercontent.com/api-evangelist/couchbase/refs/heads/main/openapi/couchbase-server-rest-api-openapi.yml
- filename: couchbase-query-service-rest-api-openapi.yml
  format: yaml
  label: Couchbase Query Service REST API
  slug: couchbase-query-service-rest-api
  spec_type: OpenAPI
  url: https://raw.githubusercontent.com/api-evangelist/couchbase/refs/heads/main/openapi/couchbase-query-service-rest-api-openapi.yml
- filename: couchbase-analytics-service-rest-api-openapi.yml
  format: yaml
  label: Couchbase Analytics Service REST API
  slug: couchbase-analytics-service-rest-api
  spec_type: OpenAPI
  url: https://raw.githubusercontent.com/api-evangelist/couchbase/refs/heads/main/openapi/couchbase-analytics-service-rest-api-openapi.yml
- filename: couchbase-search-service-rest-api-openapi.yml
  format: yaml
  label: Couchbase Search Service REST API
  slug: couchbase-search-service-rest-api
  spec_type: OpenAPI
  url: https://raw.githubusercontent.com/api-evangelist/couchbase/refs/heads/main/openapi/couchbase-search-service-rest-api-openapi.yml
- filename: couchbase-eventing-service-rest-api-openapi.yml
  format: yaml
  label: Couchbase Eventing Service REST API
  slug: couchbase-eventing-service-rest-api
  spec_type: OpenAPI
  url: https://raw.githubusercontent.com/api-evangelist/couchbase/refs/heads/main/openapi/couchbase-eventing-service-rest-api-openapi.yml
- filename: couchbase-backup-service-rest-api-openapi.yml
  format: yaml
  label: Couchbase Backup Service REST API
  slug: couchbase-backup-service-rest-api
  spec_type: OpenAPI
  url: https://raw.githubusercontent.com/api-evangelist/couchbase/refs/heads/main/openapi/couchbase-backup-service-rest-api-openapi.yml
- filename: couchbase-xdcr-rest-api-openapi.yml
  format: yaml
  label: Couchbase XDCR REST API
  slug: couchbase-xdcr-rest-api
  spec_type: OpenAPI
  url: https://raw.githubusercontent.com/api-evangelist/couchbase/refs/heads/main/openapi/couchbase-xdcr-rest-api-openapi.yml
- filename: couchbase-capella-management-api-openapi.yml
  format: yaml
  label: Couchbase Capella Management API
  slug: couchbase-capella-management-api
  spec_type: OpenAPI
  url: https://raw.githubusercontent.com/api-evangelist/couchbase/refs/heads/main/openapi/couchbase-capella-management-api-openapi.yml
- filename: couchbase-capella-app-services-public-api-openapi.yml
  format: yaml
  label: Couchbase Capella App Services Public API
  slug: couchbase-capella-app-services-public-api
  spec_type: OpenAPI
  url: https://raw.githubusercontent.com/api-evangelist/couchbase/refs/heads/main/openapi/couchbase-capella-app-services-public-api-openapi.yml
- filename: couchbase-capella-app-services-admin-api-openapi.yml
  format: yaml
  label: Couchbase Capella App Services Admin API
  slug: couchbase-capella-app-services-admin-api
  spec_type: OpenAPI
  url: https://raw.githubusercontent.com/api-evangelist/couchbase/refs/heads/main/openapi/couchbase-capella-app-services-admin-api-openapi.yml
- filename: couchbase-sync-gateway-public-rest-api-openapi.yml
  format: yaml
  label: Couchbase Sync Gateway Public REST API
  slug: couchbase-sync-gateway-public-rest-api
  spec_type: OpenAPI
  url: https://raw.githubusercontent.com/api-evangelist/couchbase/refs/heads/main/openapi/couchbase-sync-gateway-public-rest-api-openapi.yml
- filename: couchbase-sync-gateway-admin-rest-api-openapi.yml
  format: yaml
  label: Couchbase Sync Gateway Admin REST API
  slug: couchbase-sync-gateway-admin-rest-api
  spec_type: OpenAPI
  url: https://raw.githubusercontent.com/api-evangelist/couchbase/refs/heads/main/openapi/couchbase-sync-gateway-admin-rest-api-openapi.yml
categories:
- couchbase
description: Spectral linting rules defining API design standards and conventions for Couchbase.
layout: rules
name: Couchbase API Rules
provider_name: Couchbase
provider_slug: couchbase
rule_count: 4
rules:
- description: API title must mention Query Service.
  given: $.info.title
  name: couchbase-query-info-title
  severity: error
- description: Servers must reference port 8093 by default.
  given: $.servers[*].url
  name: couchbase-query-default-server
  severity: warn
- description: Every operation must define an operationId.
  given: $.paths.*.*
  name: couchbase-query-operation-id
  severity: error
- description: Every operation must define at least one tag.
  given: $.paths.*.*
  name: couchbase-query-operation-tags
  severity: error
rules_file: rules/couchbase-query-rules.yml
rules_url: https://raw.githubusercontent.com/api-evangelist/couchbase/refs/heads/main/rules/couchbase-query-rules.yml
severity_counts:
  error: 3
  hint: 0
  info: 0
  warn: 1
slug: couchbase-query-rules
source_filename: couchbase-query-rules.yml
source_heading: Spectral Ruleset
source_yaml: "extends: [\"spectral:oas\"]\ndocumentationUrl: https://docs.couchbase.com/server/current/n1ql/n1ql-rest-api/index.html\nrules:\n  couchbase-query-info-title:\n    description: API title must mention Query Service.\n    given: \"$.info.title\"\n    severity: error\n    then:\n      function: pattern\n      functionOptions:\n        match: \"Query\"\n  couchbase-query-default-server:\n    description: Servers must reference port 8093 by default.\n    given: \"$.servers[*].url\"\n    severity: warn\n    then:\n      function: pattern\n      functionOptions:\n        match: \"8093\"\n  couchbase-query-operation-id:\n    description: Every operation must define an operationId.\n    given: \"$.paths.*.*\"\n    severity: error\n    then:\n      field: operationId\n      function: truthy\n  couchbase-query-operation-tags:\n    description: Every operation must define at least one tag.\n    given: \"$.paths.*.*\"\n    severity: error\n    then:\n      field: tags\n      function: truthy\n"
source_yaml_url: https://raw.githubusercontent.com/api-evangelist/couchbase/refs/heads/main/rules/couchbase-query-rules.yml
tags:
- Analytics
- App Services
- Backup
- Capella
- Cloud
- Database
- DBaaS
- Eventing
- Full-Text Search
- Gateway
- JSON
- Mobile
- NoSQL
- Replication
- SQL++
- Sync
- Vector Search
- XDCR
- Spectral
- Linting
- API Governance
---
