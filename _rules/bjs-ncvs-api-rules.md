---
api_specs:
- filename: bjs-ncvs-api-openapi.yml
  format: yaml
  label: BJS NCVS API
  slug: ncvs-api
  spec_type: OpenAPI
  url: https://raw.githubusercontent.com/api-evangelist/data-analysis-tools-bureau-of-justice-statistics/refs/heads/main/openapi/bjs-ncvs-api-openapi.yml
- filename: bjs-nibrs-api-openapi.yml
  format: yaml
  label: BJS NIBRS National Estimates API
  slug: nibrs-api
  spec_type: OpenAPI
  url: https://raw.githubusercontent.com/api-evangelist/data-analysis-tools-bureau-of-justice-statistics/refs/heads/main/openapi/bjs-nibrs-api-openapi.yml
categories:
- bjs
description: Spectral linting rules defining API design standards and conventions for Bureau of Justice Statistics Data Analysis Tools.
layout: rules
name: Bureau of Justice Statistics Data Analysis Tools API Rules
provider_name: Bureau of Justice Statistics Data Analysis Tools
provider_slug: data-analysis-tools-bureau-of-justice-statistics
rule_count: 5
rules:
- description: API info should include a contact for the Bureau of Justice Statistics.
  given: $.info
  name: bjs-info-contact
  severity: warn
- description: Servers should reference the api.ojp.gov BJS dataset base URL.
  given: $.servers[*].url
  name: bjs-server-base
  severity: error
- description: Endpoints should expose Socrata $select, $where, $limit query parameters.
  given: $.paths[*].get
  name: bjs-soda-query-params
  severity: warn
- description: datasetId path parameter must follow the four-and-four Socrata code pattern.
  given: $.paths[*].get.parameters[?(@.name == 'datasetId')].schema
  name: bjs-dataset-id-pattern
  severity: error
- description: API should declare the optional X-App-Token security scheme.
  given: $.components.securitySchemes
  name: bjs-app-token-scheme
  severity: warn
rules_file: rules/bjs-ncvs-api-rules.yml
rules_url: https://raw.githubusercontent.com/api-evangelist/data-analysis-tools-bureau-of-justice-statistics/refs/heads/main/rules/bjs-ncvs-api-rules.yml
severity_counts:
  error: 2
  hint: 0
  info: 0
  warn: 3
slug: bjs-ncvs-api-rules
source_filename: bjs-ncvs-api-rules.yml
source_heading: Spectral Ruleset
source_yaml: "extends:\n  - spectral:oas\nrules:\n  bjs-info-contact:\n    description: API info should include a contact for the Bureau of Justice Statistics.\n    given: $.info\n    severity: warn\n    then:\n      field: contact\n      function: truthy\n  bjs-server-base:\n    description: Servers should reference the api.ojp.gov BJS dataset base URL.\n    given: $.servers[*].url\n    severity: error\n    then:\n      function: pattern\n      functionOptions:\n        match: \"api\\\\.ojp\\\\.gov/bjsdataset\"\n  bjs-soda-query-params:\n    description: Endpoints should expose Socrata $select, $where, $limit query parameters.\n    given: $.paths[*].get\n    severity: warn\n    then:\n      field: parameters\n      function: truthy\n  bjs-dataset-id-pattern:\n    description: datasetId path parameter must follow the four-and-four Socrata code pattern.\n    given: $.paths[*].get.parameters[?(@.name == 'datasetId')].schema\n    severity: error\n    then:\n      field: pattern\n      function:\
  \ truthy\n  bjs-app-token-scheme:\n    description: API should declare the optional X-App-Token security scheme.\n    given: $.components.securitySchemes\n    severity: warn\n    then:\n      field: appToken\n      function: truthy\n"
source_yaml_url: https://raw.githubusercontent.com/api-evangelist/data-analysis-tools-bureau-of-justice-statistics/refs/heads/main/rules/bjs-ncvs-api-rules.yml
tags:
- Crime Statistics
- Federal Government
- NCVS
- NIBRS
- Open Data
- SODA
- Statistics
- Victimization
- Spectral
- Linting
- API Governance
---
