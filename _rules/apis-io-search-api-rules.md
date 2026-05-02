---
api_specs:
- filename: openapi.yml
  format: yaml
  label: APIs.io Search API
  slug: apis-io-search-api
  spec_type: OpenAPI
  url: https://raw.githubusercontent.com/api-evangelist/demo-openapi/refs/heads/main/openapi/openapi.yml
categories:
- apis
description: Spectral linting rules defining API design standards and conventions for Manage OpenAPI via GitHub Demo.
layout: rules
name: Manage OpenAPI via GitHub Demo API Rules
provider_name: Manage OpenAPI via GitHub Demo
provider_slug: demo-openapi
rule_count: 5
rules:
- description: API info should include a contact for APIs.io.
  given: $.info
  name: apis-io-info-contact
  severity: warn
- description: Servers should reference search-api.apis.io.
  given: $.servers[*].url
  name: apis-io-base-url
  severity: warn
- description: OpenAPI should declare externalDocs.
  given: $
  name: apis-io-external-docs
  severity: error
- description: API should expose /search/apis as primary search resource.
  given: $.paths
  name: apis-io-search-resource
  severity: warn
- description: Operations should be tagged Search and APIs.
  given: $.paths[*][*]
  name: apis-io-operation-tags
  severity: warn
rules_file: rules/apis-io-search-api-rules.yml
rules_url: https://raw.githubusercontent.com/api-evangelist/demo-openapi/refs/heads/main/rules/apis-io-search-api-rules.yml
severity_counts:
  error: 1
  hint: 0
  info: 0
  warn: 4
slug: apis-io-search-api-rules
source_filename: apis-io-search-api-rules.yml
source_heading: Spectral Ruleset
source_yaml: "extends:\n  - spectral:oas\nrules:\n  apis-io-info-contact:\n    description: API info should include a contact for APIs.io.\n    given: $.info\n    severity: warn\n    then:\n      field: contact\n      function: truthy\n  apis-io-base-url:\n    description: Servers should reference search-api.apis.io.\n    given: $.servers[*].url\n    severity: warn\n    then:\n      function: pattern\n      functionOptions:\n        match: \"search-api\\\\.apis\\\\.io\"\n  apis-io-external-docs:\n    description: OpenAPI should declare externalDocs.\n    given: $\n    severity: error\n    then:\n      field: externalDocs\n      function: truthy\n  apis-io-search-resource:\n    description: API should expose /search/apis as primary search resource.\n    given: $.paths\n    severity: warn\n    then:\n      function: pattern\n      functionOptions:\n        match: \"/search/apis\"\n  apis-io-operation-tags:\n    description: Operations should be tagged Search and APIs.\n    given: $.paths[*][*]\n\
  \    severity: warn\n    then:\n      field: tags\n      function: truthy\n"
source_yaml_url: https://raw.githubusercontent.com/api-evangelist/demo-openapi/refs/heads/main/rules/apis-io-search-api-rules.yml
tags:
- APIs.json
- Demo
- GitHub
- OpenAPI
- Reference
- Search
- Spectral
- Linting
- API Governance
---
