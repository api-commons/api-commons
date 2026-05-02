---
categories:
- info
- operation
- servers
description: Spectral linting rules defining API design standards and conventions for Analog Devices.
layout: rules
name: Analog Devices API Rules
provider_name: Analog Devices
provider_slug: analog-devices
rule_count: 4
rules:
- description: All API info objects must have descriptions
  given: $.info
  name: info-description-required
  severity: error
- description: All operations must have summaries
  given: $.paths[*][get,post,put,patch,delete]
  name: operation-summary-required
  severity: error
- description: All operations must have operationIds
  given: $.paths[*][get,post,put,patch,delete]
  name: operation-operationid-required
  severity: error
- description: All servers must use HTTPS
  given: $.servers[*].url
  name: servers-https-only
  severity: error
rules_file: rules/analog-devices-spectral-rules.yml
rules_url: https://raw.githubusercontent.com/api-evangelist/analog-devices/refs/heads/main/rules/analog-devices-spectral-rules.yml
severity_counts:
  error: 4
  hint: 0
  info: 0
  warn: 0
slug: analog-devices-spectral-rules
source_filename: analog-devices-spectral-rules.yml
source_heading: Spectral Ruleset
source_yaml: "rules:\n  info-description-required:\n    description: All API info objects must have descriptions\n    severity: error\n    given: \"$.info\"\n    then:\n      field: description\n      function: truthy\n\n  operation-summary-required:\n    description: All operations must have summaries\n    severity: error\n    given: \"$.paths[*][get,post,put,patch,delete]\"\n    then:\n      field: summary\n      function: truthy\n\n  operation-operationid-required:\n    description: All operations must have operationIds\n    severity: error\n    given: \"$.paths[*][get,post,put,patch,delete]\"\n    then:\n      field: operationId\n      function: truthy\n\n  servers-https-only:\n    description: All servers must use HTTPS\n    severity: error\n    given: \"$.servers[*].url\"\n    then:\n      function: pattern\n      functionOptions:\n        match: \"^https://\"\n"
source_yaml_url: https://raw.githubusercontent.com/api-evangelist/analog-devices/refs/heads/main/rules/analog-devices-spectral-rules.yml
tags:
- Embedded Systems
- Hardware
- IoT
- Semiconductor
- Signal Processing
- Spectral
- Linting
- API Governance
---
