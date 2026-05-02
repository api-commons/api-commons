---
api_specs:
- filename: datafiniti-api.yml
  format: yaml
  label: Datafiniti API
  slug: datafiniti-api
  spec_type: OpenAPI
  url: https://raw.githubusercontent.com/api-evangelist/datafiniti/refs/heads/main/openapi/datafiniti-api.yml
categories:
- datafiniti
description: Spectral linting rules defining API design standards and conventions for Datafiniti.
layout: rules
name: Datafiniti API Rules
provider_name: Datafiniti
provider_slug: datafiniti
rule_count: 5
rules:
- description: Servers must point at api.datafiniti.co with a /v4 base path.
  given: $.servers[*].url
  name: datafiniti-server-base
  severity: error
- description: Operations must use bearer auth except the auth endpoint.
  given: $.components.securitySchemes.bearerAuth
  name: datafiniti-bearer-auth
  severity: error
- description: Search endpoints must use POST.
  given: $.paths[?(@property.match(/search$/))]
  name: datafiniti-search-method-post
  severity: error
- description: Every operation must declare a tag.
  given: $.paths[*][*]
  name: datafiniti-operation-tags
  severity: error
- description: SearchRequest num_records minimum must be 1.
  given: $.components.schemas.SearchRequest.properties.num_records
  name: datafiniti-num-records-min
  severity: warn
rules_file: rules/datafiniti-rules.yml
rules_url: https://raw.githubusercontent.com/api-evangelist/datafiniti/refs/heads/main/rules/datafiniti-rules.yml
severity_counts:
  error: 4
  hint: 0
  info: 0
  warn: 1
slug: datafiniti-rules
source_filename: datafiniti-rules.yml
source_heading: Spectral Ruleset
source_yaml: "extends:\n  - spectral:oas\nrules:\n  datafiniti-server-base:\n    description: Servers must point at api.datafiniti.co with a /v4 base path.\n    given: $.servers[*].url\n    severity: error\n    then:\n      function: pattern\n      functionOptions:\n        match: \"https://api\\\\.datafiniti\\\\.co/v4\"\n  datafiniti-bearer-auth:\n    description: Operations must use bearer auth except the auth endpoint.\n    given: $.components.securitySchemes.bearerAuth\n    severity: error\n    then:\n      field: scheme\n      function: pattern\n      functionOptions:\n        match: \"^bearer$\"\n  datafiniti-search-method-post:\n    description: Search endpoints must use POST.\n    given: $.paths[?(@property.match(/search$/))]\n    severity: error\n    then:\n      function: truthy\n  datafiniti-operation-tags:\n    description: Every operation must declare a tag.\n    given: $.paths[*][*]\n    severity: error\n    then:\n      field: tags\n      function: truthy\n  datafiniti-num-records-min:\n\
  \    description: SearchRequest num_records minimum must be 1.\n    given: $.components.schemas.SearchRequest.properties.num_records\n    severity: warn\n    then:\n      field: minimum\n      function: truthy\n"
source_yaml_url: https://raw.githubusercontent.com/api-evangelist/datafiniti/refs/heads/main/rules/datafiniti-rules.yml
tags:
- Business Data
- Data Aggregation
- Data as a Service
- People Data
- Product Data
- Property Data
- Spectral
- Linting
- API Governance
---
