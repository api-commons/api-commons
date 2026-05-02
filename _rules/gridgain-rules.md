---
api_specs:
- filename: gridgain-openapi.yml
  format: yaml
  label: GridGain 9 Management API
  slug: gridgain-management-api
  spec_type: OpenAPI
  url: https://raw.githubusercontent.com/api-evangelist/gridgain/refs/heads/main/openapi/gridgain-openapi.yml
categories:
- gridgain
description: Spectral linting rules defining API design standards and conventions for GridGain.
layout: rules
name: GridGain API Rules
provider_name: GridGain
provider_slug: gridgain
rule_count: 3
rules:
- description: GridGain spec must declare a version.
  given: $.info
  name: gridgain-info-version-required
  severity: error
- description: GridGain management API must declare security schemes (bearer/basic).
  given: $.components.securitySchemes
  name: gridgain-security-defined
  severity: error
- description: Each GridGain operation must be tagged so it groups under a capability.
  given: $.paths[*][get,post,put,delete,patch]
  name: gridgain-operation-tag-required
  severity: warn
rules_file: rules/gridgain-rules.yml
rules_url: https://raw.githubusercontent.com/api-evangelist/gridgain/refs/heads/main/rules/gridgain-rules.yml
severity_counts:
  error: 2
  hint: 0
  info: 0
  warn: 1
slug: gridgain-rules
source_filename: gridgain-rules.yml
source_heading: Spectral Ruleset
source_yaml: "rules:\n  gridgain-info-version-required:\n    description: GridGain spec must declare a version.\n    given: $.info\n    severity: error\n    then:\n      field: version\n      function: truthy\n  gridgain-security-defined:\n    description: GridGain management API must declare security schemes (bearer/basic).\n    given: $.components.securitySchemes\n    severity: error\n    then:\n      function: truthy\n  gridgain-operation-tag-required:\n    description: Each GridGain operation must be tagged so it groups under a capability.\n    given: $.paths[*][get,post,put,delete,patch]\n    severity: warn\n    then:\n      field: tags\n      function: truthy\n"
source_yaml_url: https://raw.githubusercontent.com/api-evangelist/gridgain/refs/heads/main/rules/gridgain-rules.yml
tags:
- Caching
- Data Grid
- Distributed Database
- In-Memory Computing
- Real-Time
- Spectral
- Linting
- API Governance
---
