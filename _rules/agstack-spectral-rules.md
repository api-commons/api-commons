---
api_specs:
- filename: agstack-openagri-weather-service-openapi.yml
  format: yaml
  label: OpenAgri Weather Service
  slug: openagri-weather-service
  spec_type: OpenAPI
  url: https://raw.githubusercontent.com/api-evangelist/agstack/refs/heads/main/openapi/agstack-openagri-weather-service-openapi.yml
- filename: agstack-openagri-farm-calendar-openapi.yml
  format: yaml
  label: OpenAgri Farm Calendar
  slug: openagri-farm-calendar
  spec_type: OpenAPI
  url: https://raw.githubusercontent.com/api-evangelist/agstack/refs/heads/main/openapi/agstack-openagri-farm-calendar-openapi.yml
- filename: agstack-asset-registry-openapi.yml
  format: yaml
  label: AgStack Asset Registry
  slug: asset-registry
  spec_type: OpenAPI
  url: https://raw.githubusercontent.com/api-evangelist/agstack/refs/heads/main/openapi/agstack-asset-registry-openapi.yml
categories:
- agstack
description: Spectral linting rules defining API design standards and conventions for AgStack Foundation.
layout: rules
name: AgStack Foundation API Rules
provider_name: AgStack Foundation
provider_slug: agstack
rule_count: 16
rules:
- description: Operation summaries should use Title Case
  given: $.paths[*][*].summary
  name: agstack-operation-summary-title-case
  severity: warn
- description: All operations must define an operationId
  given: $.paths[*][get,post,put,delete,patch]
  name: agstack-operationid-defined
  severity: error
- description: All operations must define a successful response
  given: $.paths[*][*].responses
  name: agstack-response-200-defined
  severity: error
- description: FastAPI operations should document 422 validation errors
  given: $.paths[*][get,post].responses
  name: agstack-response-422-validation-error
  severity: warn
- description: Protected operations must declare Bearer security
  given: $.paths[*][post,put,delete,patch]
  name: agstack-security-bearer-defined
  severity: warn
- description: API must define a version
  given: $.info
  name: agstack-info-version
  severity: error
- description: API must include a description
  given: $.info
  name: agstack-info-description
  severity: warn
- description: API must define at least one server URL
  given: $.servers
  name: agstack-server-url-defined
  severity: error
- description: Schema components must define a type
  given: $.components.schemas[*]
  name: agstack-schema-type-defined
  severity: warn
- description: POST/PUT request bodies should specify application/json content type
  given: $.paths[*][post,put].requestBody.content
  name: agstack-request-body-content-type
  severity: warn
- description: All operations should have tags for grouping
  given: $.paths[*][*]
  name: agstack-tags-on-operations
  severity: warn
- description: Geo ID fields should follow AgStack's 16-character alphanumeric format
  given: $.components.schemas[*].properties.geo_id
  name: agstack-geo-id-format
  severity: warn
- description: API must use OpenAPI 3.x
  given: $.openapi
  name: agstack-openapi-version-3
  severity: error
- description: Operation descriptions should be meaningful (min 10 chars)
  given: $.paths[*][*].description
  name: agstack-description-field-length
  severity: warn
- description: GeoJSON schemas must include a type field
  given: $.components.schemas.GeoJSONOut.properties
  name: agstack-geojson-type-field
  severity: error
- description: API paths should use lowercase and hyphens
  given: $.paths
  name: agstack-paths-lowercase
  severity: warn
rules_file: rules/agstack-spectral-rules.yml
rules_url: https://raw.githubusercontent.com/api-evangelist/agstack/refs/heads/main/rules/agstack-spectral-rules.yml
severity_counts:
  error: 6
  hint: 0
  info: 0
  warn: 10
slug: agstack-spectral-rules
source_filename: agstack-spectral-rules.yml
source_heading: Spectral Ruleset
source_yaml: "rules:\n  agstack-operation-summary-title-case:\n    description: Operation summaries should use Title Case\n    severity: warn\n    given: \"$.paths[*][*].summary\"\n    then:\n      function: pattern\n      functionOptions:\n        match: \"^[A-Z]\"\n\n  agstack-operationid-defined:\n    description: All operations must define an operationId\n    severity: error\n    given: \"$.paths[*][get,post,put,delete,patch]\"\n    then:\n      field: operationId\n      function: defined\n\n  agstack-response-200-defined:\n    description: All operations must define a successful response\n    severity: error\n    given: \"$.paths[*][*].responses\"\n    then:\n      function: truthy\n\n  agstack-response-422-validation-error:\n    description: FastAPI operations should document 422 validation errors\n    severity: warn\n    given: \"$.paths[*][get,post].responses\"\n    then:\n      function: truthy\n\n  agstack-security-bearer-defined:\n    description: Protected operations must declare\
  \ Bearer security\n    severity: warn\n    given: \"$.paths[*][post,put,delete,patch]\"\n    then:\n      field: security\n      function: defined\n\n  agstack-info-version:\n    description: API must define a version\n    severity: error\n    given: \"$.info\"\n    then:\n      field: version\n      function: defined\n\n  agstack-info-description:\n    description: API must include a description\n    severity: warn\n    given: \"$.info\"\n    then:\n      field: description\n      function: defined\n\n  agstack-server-url-defined:\n    description: API must define at least one server URL\n    severity: error\n    given: \"$.servers\"\n    then:\n      function: length\n      functionOptions:\n        min: 1\n\n  agstack-schema-type-defined:\n    description: Schema components must define a type\n    severity: warn\n    given: \"$.components.schemas[*]\"\n    then:\n      field: type\n      function: defined\n\n  agstack-request-body-content-type:\n    description: POST/PUT request bodies\
  \ should specify application/json content type\n    severity: warn\n    given: \"$.paths[*][post,put].requestBody.content\"\n    then:\n      function: truthy\n\n  agstack-tags-on-operations:\n    description: All operations should have tags for grouping\n    severity: warn\n    given: \"$.paths[*][*]\"\n    then:\n      field: tags\n      function: defined\n\n  agstack-geo-id-format:\n    description: Geo ID fields should follow AgStack's 16-character alphanumeric format\n    severity: warn\n    given: \"$.components.schemas[*].properties.geo_id\"\n    then:\n      function: truthy\n\n  agstack-openapi-version-3:\n    description: API must use OpenAPI 3.x\n    severity: error\n    given: \"$.openapi\"\n    then:\n      function: pattern\n      functionOptions:\n        match: \"^3\\\\.\"\n\n  agstack-description-field-length:\n    description: Operation descriptions should be meaningful (min 10 chars)\n    severity: warn\n    given: \"$.paths[*][*].description\"\n    then:\n      function:\
  \ minLength\n      functionOptions:\n        value: 10\n\n  agstack-geojson-type-field:\n    description: GeoJSON schemas must include a type field\n    severity: error\n    given: \"$.components.schemas.GeoJSONOut.properties\"\n    then:\n      field: type\n      function: defined\n\n  agstack-paths-lowercase:\n    description: API paths should use lowercase and hyphens\n    severity: warn\n    given: \"$.paths\"\n    then:\n      function: pattern\n      functionOptions:\n        match: \"^/[a-z0-9/{}_-]+$\"\n"
source_yaml_url: https://raw.githubusercontent.com/api-evangelist/agstack/refs/heads/main/rules/agstack-spectral-rules.yml
tags:
- Agriculture
- Linux Foundation
- Open Source
- Geospatial
- Precision Agriculture
- Linked Data
- Spectral
- Linting
- API Governance
---
