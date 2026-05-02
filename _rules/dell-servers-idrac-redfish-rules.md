---
api_specs:
- filename: dell-servers-idrac-redfish-openapi.yml
  format: yaml
  label: Dell iDRAC Redfish REST API
  slug: dell-servers-idrac-redfish
  spec_type: OpenAPI
  url: https://raw.githubusercontent.com/api-evangelist/dell-servers/refs/heads/main/openapi/dell-servers-idrac-redfish-openapi.yml
- filename: dell-servers-openmanage-enterprise-openapi.yml
  format: yaml
  label: Dell OpenManage Enterprise API
  slug: dell-servers-openmanage-enterprise
  spec_type: OpenAPI
  url: https://raw.githubusercontent.com/api-evangelist/dell-servers/refs/heads/main/openapi/dell-servers-openmanage-enterprise-openapi.yml
categories:
- dell
description: Spectral linting rules defining API design standards and conventions for Dell Servers.
layout: rules
name: Dell Servers API Rules
provider_name: Dell Servers
provider_slug: dell-servers
rule_count: 5
rules:
- description: Servers should reference the Redfish service root path.
  given: $.servers[*].url
  name: dell-idrac-redfish-server
  severity: warn
- description: API should expose the /Systems collection.
  given: $.paths
  name: dell-idrac-redfish-systems-path
  severity: error
- description: API should expose the /Chassis collection.
  given: $.paths
  name: dell-idrac-redfish-chassis-path
  severity: warn
- description: Operations should declare an operationId.
  given: $.paths[*][*]
  name: dell-idrac-redfish-operation-id
  severity: warn
- description: Operations should include at least one tag.
  given: $.paths[*][*]
  name: dell-idrac-redfish-tags
  severity: warn
rules_file: rules/dell-servers-idrac-redfish-rules.yml
rules_url: https://raw.githubusercontent.com/api-evangelist/dell-servers/refs/heads/main/rules/dell-servers-idrac-redfish-rules.yml
severity_counts:
  error: 1
  hint: 0
  info: 0
  warn: 4
slug: dell-servers-idrac-redfish-rules
source_filename: dell-servers-idrac-redfish-rules.yml
source_heading: Spectral Ruleset
source_yaml: "extends:\n  - spectral:oas\nrules:\n  dell-idrac-redfish-server:\n    description: Servers should reference the Redfish service root path.\n    given: $.servers[*].url\n    severity: warn\n    then:\n      function: pattern\n      functionOptions:\n        match: \"/redfish/v1\"\n  dell-idrac-redfish-systems-path:\n    description: API should expose the /Systems collection.\n    given: $.paths\n    severity: error\n    then:\n      function: pattern\n      functionOptions:\n        match: \"/Systems\"\n  dell-idrac-redfish-chassis-path:\n    description: API should expose the /Chassis collection.\n    given: $.paths\n    severity: warn\n    then:\n      function: pattern\n      functionOptions:\n        match: \"/Chassis\"\n  dell-idrac-redfish-operation-id:\n    description: Operations should declare an operationId.\n    given: $.paths[*][*]\n    severity: warn\n    then:\n      field: operationId\n      function: truthy\n  dell-idrac-redfish-tags:\n    description: Operations\
  \ should include at least one tag.\n    given: $.paths[*][*]\n    severity: warn\n    then:\n      field: tags\n      function: truthy\n"
source_yaml_url: https://raw.githubusercontent.com/api-evangelist/dell-servers/refs/heads/main/rules/dell-servers-idrac-redfish-rules.yml
tags:
- Hardware
- Infrastructure
- Management
- Monitoring
- Servers
- Spectral
- Linting
- API Governance
---
