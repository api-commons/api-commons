---
api_specs:
- filename: dell-technologies-dell-api-openapi.yml
  format: yaml
  label: Dell Technologies API
  slug: dell-api
  spec_type: OpenAPI
  url: https://raw.githubusercontent.com/api-evangelist/dell-technologies/refs/heads/main/openapi/dell-technologies-dell-api-openapi.yml
categories:
- dell
description: Spectral linting rules defining API design standards and conventions for Dell Technologies.
layout: rules
name: Dell Technologies API Rules
provider_name: Dell Technologies
provider_slug: dell-technologies
rule_count: 5
rules:
- description: API info should include Dell developer support contact.
  given: $.info
  name: dell-info-contact
  severity: warn
- description: Servers should reference developer.dell.com.
  given: $.servers[*].url
  name: dell-base-url
  severity: warn
- description: API should declare bearer-token authentication.
  given: $.components.securitySchemes
  name: dell-bearer-auth
  severity: error
- description: Operations should be tagged with infrastructure categories.
  given: $.paths[*][*]
  name: dell-operation-tags
  severity: warn
- description: API should expose a /status resource for health checks.
  given: $.paths
  name: dell-status-resource
  severity: info
rules_file: rules/dell-technologies-dell-api-rules.yml
rules_url: https://raw.githubusercontent.com/api-evangelist/dell-technologies/refs/heads/main/rules/dell-technologies-dell-api-rules.yml
severity_counts:
  error: 1
  hint: 0
  info: 1
  warn: 3
slug: dell-technologies-dell-api-rules
source_filename: dell-technologies-dell-api-rules.yml
source_heading: Spectral Ruleset
source_yaml: "extends:\n  - spectral:oas\nrules:\n  dell-info-contact:\n    description: API info should include Dell developer support contact.\n    given: $.info\n    severity: warn\n    then:\n      field: contact\n      function: truthy\n  dell-base-url:\n    description: Servers should reference developer.dell.com.\n    given: $.servers[*].url\n    severity: warn\n    then:\n      function: pattern\n      functionOptions:\n        match: \"developer\\\\.dell\\\\.com\"\n  dell-bearer-auth:\n    description: API should declare bearer-token authentication.\n    given: $.components.securitySchemes\n    severity: error\n    then:\n      field: bearerAuth\n      function: truthy\n  dell-operation-tags:\n    description: Operations should be tagged with infrastructure categories.\n    given: $.paths[*][*]\n    severity: warn\n    then:\n      field: tags\n      function: truthy\n  dell-status-resource:\n    description: API should expose a /status resource for health checks.\n    given: $.paths\n\
  \    severity: info\n    then:\n      function: pattern\n      functionOptions:\n        match: \"/status\"\n"
source_yaml_url: https://raw.githubusercontent.com/api-evangelist/dell-technologies/refs/heads/main/rules/dell-technologies-dell-api-rules.yml
tags:
- Enterprise IT
- Infrastructure
- Servers
- Storage
- Cloud
- Automation
- Spectral
- Linting
- API Governance
---
