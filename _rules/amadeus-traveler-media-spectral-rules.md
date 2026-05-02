---
api_specs:
- filename: amadeus-traveler-media-points-of-interest-openapi.yaml
  format: yaml
  label: Points of Interest API
  slug: points-of-interest-api
  spec_type: OpenAPI
  url: https://raw.githubusercontent.com/api-evangelist/amadeus-traveler-media/refs/heads/main/openapi/amadeus-traveler-media-points-of-interest-openapi.yaml
- filename: amadeus-traveler-media-hotel-ratings-openapi.yaml
  format: yaml
  label: Hotel Ratings API
  slug: hotel-ratings-api
  spec_type: OpenAPI
  url: https://raw.githubusercontent.com/api-evangelist/amadeus-traveler-media/refs/heads/main/openapi/amadeus-traveler-media-hotel-ratings-openapi.yaml
- filename: amadeus-traveler-media-travel-recommendations-openapi.yaml
  format: yaml
  label: Travel Recommendations API
  slug: travel-recommendations-api
  spec_type: OpenAPI
  url: https://raw.githubusercontent.com/api-evangelist/amadeus-traveler-media/refs/heads/main/openapi/amadeus-traveler-media-travel-recommendations-openapi.yaml
- filename: amadeus-traveler-media-location-score-openapi.yaml
  format: yaml
  label: Location Score API
  slug: location-score-api
  spec_type: OpenAPI
  url: https://raw.githubusercontent.com/api-evangelist/amadeus-traveler-media/refs/heads/main/openapi/amadeus-traveler-media-location-score-openapi.yaml
categories:
- get
- info
- operation
- parameter
- response
- schema
- servers
description: Spectral linting rules defining API design standards and conventions for Amadeus Traveler Media.
layout: rules
name: Amadeus Traveler Media API Rules
provider_name: Amadeus Traveler Media
provider_slug: amadeus-traveler-media
rule_count: 12
rules:
- description: API title must be present.
  given: $.info
  name: info-title-required
  severity: error
- description: API must have a description.
  given: $.info
  name: info-description-required
  severity: error
- description: API version must be present.
  given: $.info
  name: info-version-required
  severity: error
- description: Server URLs must use HTTPS.
  given: $.servers[*].url
  name: servers-https
  severity: error
- description: Every operation must have a summary.
  given: $.paths[*][get,post,put,patch,delete]
  name: operation-summary-required
  severity: error
- description: Operation summaries must start with Amadeus.
  given: $.paths[*][get,post,put,patch,delete].summary
  name: operation-summary-amadeus-prefix
  severity: warn
- description: Every operation must have an operationId.
  given: $.paths[*][get,post,put,patch,delete]
  name: operation-id-required
  severity: error
- description: Every operation must have tags.
  given: $.paths[*][get,post,put,patch,delete]
  name: operation-tags-required
  severity: error
- description: Parameters should have descriptions.
  given: $.paths[*][*].parameters[*]
  name: parameter-description-required
  severity: warn
- description: Responses must have descriptions.
  given: $.paths[*][*].responses[*]
  name: response-description-required
  severity: error
- description: GET operations must not have request bodies.
  given: $.paths[*].get
  name: get-no-request-body
  severity: error
- description: Top-level schemas should have descriptions.
  given: $.components.schemas[*]
  name: schema-description
  severity: info
rules_file: rules/amadeus-traveler-media-spectral-rules.yml
rules_url: https://raw.githubusercontent.com/api-evangelist/amadeus-traveler-media/refs/heads/main/rules/amadeus-traveler-media-spectral-rules.yml
severity_counts:
  error: 9
  hint: 0
  info: 1
  warn: 2
slug: amadeus-traveler-media-spectral-rules
source_filename: amadeus-traveler-media-spectral-rules.yml
source_heading: Spectral Ruleset
source_yaml: "rules:\n  info-title-required:\n    description: API title must be present.\n    severity: error\n    given: $.info\n    then:\n      field: title\n      function: truthy\n  info-description-required:\n    description: API must have a description.\n    severity: error\n    given: $.info\n    then:\n      field: description\n      function: truthy\n  info-version-required:\n    description: API version must be present.\n    severity: error\n    given: $.info\n    then:\n      field: version\n      function: truthy\n  servers-https:\n    description: Server URLs must use HTTPS.\n    severity: error\n    given: $.servers[*].url\n    then:\n      function: pattern\n      functionOptions:\n        match: \"^https://\"\n  operation-summary-required:\n    description: Every operation must have a summary.\n    severity: error\n    given: $.paths[*][get,post,put,patch,delete]\n    then:\n      field: summary\n      function: truthy\n  operation-summary-amadeus-prefix:\n    description:\
  \ Operation summaries must start with Amadeus.\n    severity: warn\n    given: $.paths[*][get,post,put,patch,delete].summary\n    then:\n      function: pattern\n      functionOptions:\n        match: \"^Amadeus \"\n  operation-id-required:\n    description: Every operation must have an operationId.\n    severity: error\n    given: $.paths[*][get,post,put,patch,delete]\n    then:\n      field: operationId\n      function: truthy\n  operation-tags-required:\n    description: Every operation must have tags.\n    severity: error\n    given: $.paths[*][get,post,put,patch,delete]\n    then:\n      field: tags\n      function: truthy\n  parameter-description-required:\n    description: Parameters should have descriptions.\n    severity: warn\n    given: $.paths[*][*].parameters[*]\n    then:\n      field: description\n      function: truthy\n  response-description-required:\n    description: Responses must have descriptions.\n    severity: error\n    given: $.paths[*][*].responses[*]\n    then:\n\
  \      field: description\n      function: truthy\n  get-no-request-body:\n    description: GET operations must not have request bodies.\n    severity: error\n    given: $.paths[*].get\n    then:\n      field: requestBody\n      function: falsy\n  schema-description:\n    description: Top-level schemas should have descriptions.\n    severity: info\n    given: $.components.schemas[*]\n    then:\n      field: description\n      function: truthy\n"
source_yaml_url: https://raw.githubusercontent.com/api-evangelist/amadeus-traveler-media/refs/heads/main/rules/amadeus-traveler-media-spectral-rules.yml
tags:
- Content
- Destination
- Media
- Photos
- Points of Interest
- Tourism
- Travel
- Spectral
- Linting
- API Governance
---
