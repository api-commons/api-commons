---
api_specs:
- filename: cyberark-conjur-openapi.yml
  format: yaml
  label: CyberArk Conjur Secrets Manager API
  slug: conjur
  spec_type: OpenAPI
  url: https://raw.githubusercontent.com/api-evangelist/cyberark/refs/heads/main/openapi/cyberark-conjur-openapi.yml
categories:
- cyberark
description: Spectral linting rules defining API design standards and conventions for CyberArk.
layout: rules
name: CyberArk API Rules
provider_name: CyberArk
provider_slug: cyberark
rule_count: 6
rules:
- description: CyberArk Conjur API spec must declare a contact.
  given: $.info
  name: cyberark-conjur-info-contact
  severity: warn
- description: Conjur server URLs must use HTTPS.
  given: $.servers[*].url
  name: cyberark-conjur-server-https
  severity: error
- description: Every operation must declare at least one tag.
  given: $.paths[*][get,post,put,patch,delete]
  name: cyberark-conjur-tags-required
  severity: warn
- description: Every operation must declare an operationId.
  given: $.paths[*][get,post,put,patch,delete]
  name: cyberark-conjur-operation-id-required
  severity: error
- description: Conjur paths must include an {account} path parameter.
  given: $.paths
  name: cyberark-conjur-account-path-param
  severity: warn
- description: Conjur uses bearer-token authentication via securitySchemes.
  given: $.components.securitySchemes
  name: cyberark-conjur-bearer-auth
  severity: warn
rules_file: rules/cyberark-conjur-rules.yml
rules_url: https://raw.githubusercontent.com/api-evangelist/cyberark/refs/heads/main/rules/cyberark-conjur-rules.yml
severity_counts:
  error: 2
  hint: 0
  info: 0
  warn: 4
slug: cyberark-conjur-rules
source_filename: cyberark-conjur-rules.yml
source_heading: Spectral Ruleset
source_yaml: "extends: spectral:oas\nrules:\n  cyberark-conjur-info-contact:\n    description: CyberArk Conjur API spec must declare a contact.\n    severity: warn\n    given: $.info\n    then:\n      field: contact\n      function: truthy\n  cyberark-conjur-server-https:\n    description: Conjur server URLs must use HTTPS.\n    severity: error\n    given: $.servers[*].url\n    then:\n      function: pattern\n      functionOptions:\n        match: '^https://'\n  cyberark-conjur-tags-required:\n    description: Every operation must declare at least one tag.\n    severity: warn\n    given: $.paths[*][get,post,put,patch,delete]\n    then:\n      field: tags\n      function: truthy\n  cyberark-conjur-operation-id-required:\n    description: Every operation must declare an operationId.\n    severity: error\n    given: $.paths[*][get,post,put,patch,delete]\n    then:\n      field: operationId\n      function: truthy\n  cyberark-conjur-account-path-param:\n    description: Conjur paths must include\
  \ an {account} path parameter.\n    severity: warn\n    given: $.paths\n    then:\n      function: pattern\n      functionOptions:\n        match: '\\{account\\}'\n  cyberark-conjur-bearer-auth:\n    description: Conjur uses bearer-token authentication via securitySchemes.\n    severity: warn\n    given: $.components.securitySchemes\n    then:\n      field: ConjurAuth\n      function: truthy\n"
source_yaml_url: https://raw.githubusercontent.com/api-evangelist/cyberark/refs/heads/main/rules/cyberark-conjur-rules.yml
tags:
- Authentication
- Cloud Security
- Conjur
- Credential Vault
- DevOps Secrets
- Endpoint Privilege Management
- Identity Security
- Machine Identity
- MFA
- OpenAPI
- PAM
- Privileged Access
- Privileged Access Management
- Secrets Management
- Session Management
- SSO
- Vault
- Zero Trust
- Spectral
- Linting
- API Governance
---
