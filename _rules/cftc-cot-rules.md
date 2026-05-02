---
api_specs:
- filename: cftc-cot-openapi.yml
  format: yaml
  label: CFTC Commitments of Traders SODA API
  slug: cftc-cot-api
  spec_type: OpenAPI
  url: https://raw.githubusercontent.com/api-evangelist/commodity-futures-trading-commission/refs/heads/main/openapi/cftc-cot-openapi.yml
categories:
- cftc
description: Spectral linting rules defining API design standards and conventions for Commodity Futures Trading Commission.
layout: rules
name: Commodity Futures Trading Commission API Rules
provider_name: Commodity Futures Trading Commission
provider_slug: commodity-futures-trading-commission
rule_count: 6
rules:
- description: COT OpenAPI info.title must reference Commitments of Traders or CFTC
  given: $.info.title
  name: cftc-cot-info-title
  severity: error
- description: At least one server URL must be defined for the SODA endpoint
  given: $.servers
  name: cftc-cot-server-defined
  severity: error
- description: Server URL must point to publicreporting.cftc.gov
  given: $.servers[*].url
  name: cftc-cot-server-publicreporting
  severity: error
- description: COT-related tags must be declared at the document level
  given: $.tags[*].name
  name: cftc-cot-tag-required
  severity: warn
- description: Every operation must define an operationId using camelCase
  given: $.paths.*[get,put,post,delete,patch].operationId
  name: cftc-cot-operation-id-camelcase
  severity: error
- description: COT paths should resolve to a Socrata four-by-four .json resource path
  given: $.paths
  name: cftc-cot-soda-resource-path
  severity: warn
rules_file: rules/cftc-cot-rules.yml
rules_url: https://raw.githubusercontent.com/api-evangelist/commodity-futures-trading-commission/refs/heads/main/rules/cftc-cot-rules.yml
severity_counts:
  error: 4
  hint: 0
  info: 0
  warn: 2
slug: cftc-cot-rules
source_filename: cftc-cot-rules.yml
source_heading: Spectral Ruleset
source_yaml: "extends:\n  - \"spectral:oas\"\ndocumentationUrl: https://publicreporting.cftc.gov/\nrules:\n  cftc-cot-info-title:\n    description: COT OpenAPI info.title must reference Commitments of Traders or CFTC\n    severity: error\n    given: \"$.info.title\"\n    then:\n      function: pattern\n      functionOptions:\n        match: \"(?i)(CFTC|Commitments\\\\s+of\\\\s+Traders)\"\n  cftc-cot-server-defined:\n    description: At least one server URL must be defined for the SODA endpoint\n    severity: error\n    given: \"$.servers\"\n    then:\n      function: length\n      functionOptions:\n        min: 1\n  cftc-cot-server-publicreporting:\n    description: Server URL must point to publicreporting.cftc.gov\n    severity: error\n    given: \"$.servers[*].url\"\n    then:\n      function: pattern\n      functionOptions:\n        match: \"publicreporting\\\\.cftc\\\\.gov\"\n  cftc-cot-tag-required:\n    description: COT-related tags must be declared at the document level\n    severity:\
  \ warn\n    given: \"$.tags[*].name\"\n    then:\n      function: enumeration\n      functionOptions:\n        values:\n          - COT\n          - Legacy\n          - Disaggregated\n          - TFF\n          - Supplemental\n  cftc-cot-operation-id-camelcase:\n    description: Every operation must define an operationId using camelCase\n    severity: error\n    given: \"$.paths.*[get,put,post,delete,patch].operationId\"\n    then:\n      function: pattern\n      functionOptions:\n        match: \"^[a-z][a-zA-Z0-9]+$\"\n  cftc-cot-soda-resource-path:\n    description: COT paths should resolve to a Socrata four-by-four .json resource path\n    severity: warn\n    given: \"$.paths\"\n    then:\n      function: pattern\n      functionOptions:\n        match: \"/[a-z0-9]{4}-[a-z0-9]{4}\\\\.json\"\n"
source_yaml_url: https://raw.githubusercontent.com/api-evangelist/commodity-futures-trading-commission/refs/heads/main/rules/cftc-cot-rules.yml
tags:
- CFTC
- Commitments of Traders
- Federal Government
- Financial
- Futures
- Open Data
- SODA
- Trading
- Spectral
- Linting
- API Governance
---
