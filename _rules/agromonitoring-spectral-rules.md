---
api_specs:
- filename: agromonitoring-openapi.yml
  format: yaml
  label: Agromonitoring
  slug: agromonitoring
  spec_type: OpenAPI
  url: https://raw.githubusercontent.com/api-evangelist/agromonitoring/refs/heads/main/openapi/agromonitoring-openapi.yml
categories:
- agromonitoring
description: Spectral linting rules defining API design standards and conventions for Agromonitoring.
layout: rules
name: Agromonitoring API Rules
provider_name: Agromonitoring
provider_slug: agromonitoring
rule_count: 20
rules:
- description: Operation summaries must use Title Case
  given: $.paths[*][*].summary
  name: agromonitoring-operation-summary-title-case
  severity: warn
- description: Operation summaries should start with a verb
  given: $.paths[*][*].summary
  name: agromonitoring-operation-summary-prefix
  severity: warn
- description: OperationId must use camelCase
  given: $.paths[*][*].operationId
  name: agromonitoring-operationid-camelcase
  severity: error
- description: All operations must require the appid query parameter for authentication
  given: $.paths[*][get,post,put,delete,patch]
  name: agromonitoring-appid-query-required
  severity: error
- description: All operations must define a 200 response
  given: $.paths[*][*].responses
  name: agromonitoring-response-200-defined
  severity: error
- description: All operations should define a 400 error response
  given: $.paths[*][*].responses
  name: agromonitoring-response-400-defined
  severity: warn
- description: All operations should define a 401 unauthorized response
  given: $.paths[*][*].responses
  name: agromonitoring-response-401-defined
  severity: warn
- description: Response schemas should use $ref to components/schemas
  given: $.paths[*][*].responses[*].content[*].schema
  name: agromonitoring-schema-ref-components
  severity: warn
- description: API info must include contact details
  given: $.info
  name: agromonitoring-info-contact
  severity: warn
- description: API info must include version
  given: $.info
  name: agromonitoring-info-version
  severity: error
- description: All operations must have at least one tag
  given: $.paths[*][*]
  name: agromonitoring-tags-defined
  severity: warn
- description: Schema properties should use snake_case
  given: $.components.schemas[*].properties
  name: agromonitoring-property-snake-case
  severity: warn
- description: Polygon schema must include an id field
  given: $.components.schemas.Polygon.properties
  name: agromonitoring-polygon-id-field
  severity: error
- description: GeoJson schema must include coordinates field
  given: $.components.schemas.GeoJson.properties
  name: agromonitoring-geo-json-coordinates
  severity: error
- description: NDVI values should include minimum/maximum bounds
  given: $.components.schemas.NdviRecord.properties.ndvi
  name: agromonitoring-ndvi-value-range
  severity: warn
- description: WeatherData schema must include temp field
  given: $.components.schemas.WeatherData.properties
  name: agromonitoring-weather-temp-field
  severity: error
- description: SoilData schema must include moisture field
  given: $.components.schemas.SoilData.properties
  name: agromonitoring-soil-moisture-field
  severity: error
- description: API must define at least one server URL
  given: $.servers
  name: agromonitoring-server-url-defined
  severity: error
- description: API must define an API key security scheme
  given: $.components.securitySchemes
  name: agromonitoring-security-scheme-apikey
  severity: error
- description: Path segments should use lowercase
  given: $.paths
  name: agromonitoring-path-lowercase
  severity: warn
rules_file: rules/agromonitoring-spectral-rules.yml
rules_url: https://raw.githubusercontent.com/api-evangelist/agromonitoring/refs/heads/main/rules/agromonitoring-spectral-rules.yml
severity_counts:
  error: 10
  hint: 0
  info: 0
  warn: 10
slug: agromonitoring-spectral-rules
source_filename: agromonitoring-spectral-rules.yml
source_heading: Spectral Ruleset
source_yaml: "rules:\n  agromonitoring-operation-summary-title-case:\n    description: Operation summaries must use Title Case\n    severity: warn\n    given: \"$.paths[*][*].summary\"\n    then:\n      function: pattern\n      functionOptions:\n        match: \"^[A-Z][a-zA-Z0-9 ]+$\"\n\n  agromonitoring-operation-summary-prefix:\n    description: Operation summaries should start with a verb\n    severity: warn\n    given: \"$.paths[*][*].summary\"\n    then:\n      function: pattern\n      functionOptions:\n        match: \"^(List|Get|Create|Update|Delete|Search|Post|Put|Patch|Fetch)\"\n\n  agromonitoring-operationid-camelcase:\n    description: OperationId must use camelCase\n    severity: error\n    given: \"$.paths[*][*].operationId\"\n    then:\n      function: pattern\n      functionOptions:\n        match: \"^[a-z][a-zA-Z0-9]+$\"\n\n  agromonitoring-appid-query-required:\n    description: All operations must require the appid query parameter for authentication\n    severity: error\n\
  \    given: \"$.paths[*][get,post,put,delete,patch]\"\n    then:\n      function: truthy\n\n  agromonitoring-response-200-defined:\n    description: All operations must define a 200 response\n    severity: error\n    given: \"$.paths[*][*].responses\"\n    then:\n      field: \"200\"\n      function: defined\n\n  agromonitoring-response-400-defined:\n    description: All operations should define a 400 error response\n    severity: warn\n    given: \"$.paths[*][*].responses\"\n    then:\n      field: \"400\"\n      function: defined\n\n  agromonitoring-response-401-defined:\n    description: All operations should define a 401 unauthorized response\n    severity: warn\n    given: \"$.paths[*][*].responses\"\n    then:\n      field: \"401\"\n      function: defined\n\n  agromonitoring-schema-ref-components:\n    description: Response schemas should use $ref to components/schemas\n    severity: warn\n    given: \"$.paths[*][*].responses[*].content[*].schema\"\n    then:\n      function: schema\n\
  \      functionOptions:\n        schema:\n          oneOf:\n            - required: [\"$ref\"]\n            - required: [\"type\"]\n\n  agromonitoring-info-contact:\n    description: API info must include contact details\n    severity: warn\n    given: \"$.info\"\n    then:\n      field: contact\n      function: defined\n\n  agromonitoring-info-version:\n    description: API info must include version\n    severity: error\n    given: \"$.info\"\n    then:\n      field: version\n      function: defined\n\n  agromonitoring-tags-defined:\n    description: All operations must have at least one tag\n    severity: warn\n    given: \"$.paths[*][*]\"\n    then:\n      field: tags\n      function: defined\n\n  agromonitoring-property-snake-case:\n    description: Schema properties should use snake_case\n    severity: warn\n    given: \"$.components.schemas[*].properties\"\n    then:\n      function: pattern\n      functionOptions:\n        match: \"^[a-z][a-z0-9_]*$\"\n\n  agromonitoring-polygon-id-field:\n\
  \    description: Polygon schema must include an id field\n    severity: error\n    given: \"$.components.schemas.Polygon.properties\"\n    then:\n      field: id\n      function: defined\n\n  agromonitoring-geo-json-coordinates:\n    description: GeoJson schema must include coordinates field\n    severity: error\n    given: \"$.components.schemas.GeoJson.properties\"\n    then:\n      field: coordinates\n      function: defined\n\n  agromonitoring-ndvi-value-range:\n    description: NDVI values should include minimum/maximum bounds\n    severity: warn\n    given: \"$.components.schemas.NdviRecord.properties.ndvi\"\n    then:\n      function: truthy\n\n  agromonitoring-weather-temp-field:\n    description: WeatherData schema must include temp field\n    severity: error\n    given: \"$.components.schemas.WeatherData.properties\"\n    then:\n      field: temp\n      function: defined\n\n  agromonitoring-soil-moisture-field:\n    description: SoilData schema must include moisture field\n\
  \    severity: error\n    given: \"$.components.schemas.SoilData.properties\"\n    then:\n      field: moisture\n      function: defined\n\n  agromonitoring-server-url-defined:\n    description: API must define at least one server URL\n    severity: error\n    given: \"$.servers\"\n    then:\n      function: length\n      functionOptions:\n        min: 1\n\n  agromonitoring-security-scheme-apikey:\n    description: API must define an API key security scheme\n    severity: error\n    given: \"$.components.securitySchemes\"\n    then:\n      function: defined\n\n  agromonitoring-path-lowercase:\n    description: Path segments should use lowercase\n    severity: warn\n    given: \"$.paths\"\n    then:\n      function: pattern\n      functionOptions:\n        match: \"^/[a-z0-9/{}_-]+$\"\n"
source_yaml_url: https://raw.githubusercontent.com/api-evangelist/agromonitoring/refs/heads/main/rules/agromonitoring-spectral-rules.yml
tags:
- Agriculture
- Satellite Imagery
- Vegetation Indices
- Weather
- Precision Agriculture
- Remote Sensing
- Spectral
- Linting
- API Governance
---
