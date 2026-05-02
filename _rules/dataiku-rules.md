---
api_specs:
- filename: index.html
  format: yaml
  label: Dataiku Public API
  slug: dataiku-public-api
  spec_type: OpenAPI
  url: https://doc.dataiku.com/dss/latest/publicapi/rest/index.html
- filename: dataiku-api-node-admin-openapi.yml
  format: yaml
  label: Dataiku API Node Administration API
  slug: dataiku-api-node-administration-api
  spec_type: OpenAPI
  url: https://raw.githubusercontent.com/api-evangelist/dataiku/refs/heads/main/openapi/dataiku-api-node-admin-openapi.yml
- filename: dataiku-govern-api-openapi.yml
  format: yaml
  label: Dataiku Govern API
  slug: dataiku-govern-api
  spec_type: OpenAPI
  url: https://raw.githubusercontent.com/api-evangelist/dataiku/refs/heads/main/openapi/dataiku-govern-api-openapi.yml
categories:
- dataiku
description: Spectral linting rules defining API design standards and conventions for Dataiku.
layout: rules
name: Dataiku API Rules
provider_name: Dataiku
provider_slug: dataiku
rule_count: 5
rules:
- description: API info should include a contact for Dataiku support.
  given: $.info
  name: dataiku-info-contact
  severity: warn
- description: Public API paths must be served under /public/api.
  given: $.paths
  name: dataiku-public-api-prefix
  severity: warn
- description: Every operation must declare at least one tag.
  given: $.paths[*][*]
  name: dataiku-operation-tags
  severity: error
- description: Server URLs must use HTTPS.
  given: $.servers[*].url
  name: dataiku-server-https
  severity: error
- description: ProjectKey path parameters must follow the upper-case alphanumeric convention.
  given: $.paths.*.*.parameters[?(@.name=='projectKey')].schema
  name: dataiku-project-key-pattern
  severity: warn
rules_file: rules/dataiku-rules.yml
rules_url: https://raw.githubusercontent.com/api-evangelist/dataiku/refs/heads/main/rules/dataiku-rules.yml
severity_counts:
  error: 2
  hint: 0
  info: 0
  warn: 3
slug: dataiku-rules
source_filename: dataiku-rules.yml
source_heading: Spectral Ruleset
source_yaml: "extends:\n  - spectral:oas\nrules:\n  dataiku-info-contact:\n    description: API info should include a contact for Dataiku support.\n    given: $.info\n    severity: warn\n    then:\n      field: contact\n      function: truthy\n  dataiku-public-api-prefix:\n    description: Public API paths must be served under /public/api.\n    given: $.paths\n    severity: warn\n    then:\n      function: pattern\n      functionOptions:\n        match: \"^/public/api\"\n  dataiku-operation-tags:\n    description: Every operation must declare at least one tag.\n    given: $.paths[*][*]\n    severity: error\n    then:\n      field: tags\n      function: truthy\n  dataiku-server-https:\n    description: Server URLs must use HTTPS.\n    given: $.servers[*].url\n    severity: error\n    then:\n      function: pattern\n      functionOptions:\n        match: \"^https://\"\n  dataiku-project-key-pattern:\n    description: ProjectKey path parameters must follow the upper-case alphanumeric convention.\n\
  \    given: $.paths.*.*.parameters[?(@.name=='projectKey')].schema\n    severity: warn\n    then:\n      field: pattern\n      function: truthy\n"
source_yaml_url: https://raw.githubusercontent.com/api-evangelist/dataiku/refs/heads/main/rules/dataiku-rules.yml
tags:
- Analytics
- Artificial Intelligence
- Data Platform
- Data Science
- Machine Learning
- Spectral
- Linting
- API Governance
---
