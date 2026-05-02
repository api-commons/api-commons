---
categories:
- info
- operation
- response
- security
description: Spectral linting rules defining API design standards and conventions for Ansible Automation Platform.
layout: rules
name: Ansible Automation Platform API Rules
provider_name: Ansible Automation Platform
provider_slug: ansible-automation-platform
rule_count: 6
rules:
- description: Info title should start with "Ansible"
  given: $.info
  name: info-title-prefix
  severity: warn
- description: Every operation must have an operationId
  given: $.paths[*][get,post,put,patch,delete]
  name: operation-operationId-required
  severity: error
- description: Every operation must have a summary
  given: $.paths[*][get,post,put,patch,delete]
  name: operation-summary-required
  severity: error
- description: Every operation must have tags
  given: $.paths[*][get,post,put,patch,delete]
  name: operation-tags-required
  severity: warn
- description: Operations must have success responses
  given: $.paths[*][get,post,put,patch,delete].responses
  name: response-success-required
  severity: error
- description: Global security must be defined
  given: $
  name: security-global-defined
  severity: error
rules_file: rules/ansible-automation-platform-spectral-rules.yml
rules_url: https://raw.githubusercontent.com/api-evangelist/ansible-automation-platform/refs/heads/main/rules/ansible-automation-platform-spectral-rules.yml
severity_counts:
  error: 4
  hint: 0
  info: 0
  warn: 2
slug: ansible-automation-platform-spectral-rules
source_filename: ansible-automation-platform-spectral-rules.yml
source_heading: Spectral Ruleset
source_yaml: "rules:\n  info-title-prefix:\n    description: Info title should start with \"Ansible\"\n    given: $.info\n    severity: warn\n    then:\n      field: title\n      function: pattern\n      functionOptions:\n        match: \"^Ansible\"\n\n  operation-operationId-required:\n    description: Every operation must have an operationId\n    given: \"$.paths[*][get,post,put,patch,delete]\"\n    severity: error\n    then:\n      field: operationId\n      function: truthy\n\n  operation-summary-required:\n    description: Every operation must have a summary\n    given: \"$.paths[*][get,post,put,patch,delete]\"\n    severity: error\n    then:\n      field: summary\n      function: truthy\n\n  operation-tags-required:\n    description: Every operation must have tags\n    given: \"$.paths[*][get,post,put,patch,delete]\"\n    severity: warn\n    then:\n      field: tags\n      function: truthy\n\n  response-success-required:\n    description: Operations must have success responses\n   \
  \ given: \"$.paths[*][get,post,put,patch,delete].responses\"\n    severity: error\n    then:\n      function: schema\n      functionOptions:\n        schema:\n          type: object\n          anyOf:\n            - required: [\"200\"]\n            - required: [\"201\"]\n\n  security-global-defined:\n    description: Global security must be defined\n    given: \"$\"\n    severity: error\n    then:\n      field: security\n      function: truthy\n"
source_yaml_url: https://raw.githubusercontent.com/api-evangelist/ansible-automation-platform/refs/heads/main/rules/ansible-automation-platform-spectral-rules.yml
tags:
- Automation
- Configuration Management
- DevOps
- Infrastructure as Code
- Orchestration
- Spectral
- Linting
- API Governance
---
