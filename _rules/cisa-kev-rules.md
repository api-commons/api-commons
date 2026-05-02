---
api_specs:
- filename: cisa-kev-openapi.yml
  format: yaml
  label: CISA Known Exploited Vulnerabilities (KEV) Catalog
  slug: kev
  spec_type: OpenAPI
  url: https://raw.githubusercontent.com/api-evangelist/cybersecurity-and-infrastructure-security-agency/refs/heads/main/openapi/cisa-kev-openapi.yml
categories:
- cisa
description: Spectral linting rules defining API design standards and conventions for Cybersecurity and Infrastructure Security Agency.
layout: rules
name: Cybersecurity and Infrastructure Security Agency API Rules
provider_name: Cybersecurity and Infrastructure Security Agency
provider_slug: cybersecurity-and-infrastructure-security-agency
rule_count: 5
rules:
- description: CISA KEV API spec must declare a contact.
  given: $.info
  name: cisa-kev-info-contact
  severity: warn
- description: All KEV servers must use HTTPS.
  given: $.servers[*].url
  name: cisa-kev-server-https
  severity: error
- description: Every operation must declare at least one tag.
  given: $.paths[*][get,post,put,patch,delete]
  name: cisa-kev-tags-required
  severity: warn
- description: Every operation must declare an operationId.
  given: $.paths[*][get,post,put,patch,delete]
  name: cisa-kev-operation-id-required
  severity: error
- description: KEV feed is public; spec must not declare a global security requirement.
  given: $
  name: cisa-kev-public-no-auth
  severity: warn
rules_file: rules/cisa-kev-rules.yml
rules_url: https://raw.githubusercontent.com/api-evangelist/cybersecurity-and-infrastructure-security-agency/refs/heads/main/rules/cisa-kev-rules.yml
severity_counts:
  error: 2
  hint: 0
  info: 0
  warn: 3
slug: cisa-kev-rules
source_filename: cisa-kev-rules.yml
source_heading: Spectral Ruleset
source_yaml: "extends: spectral:oas\nrules:\n  cisa-kev-info-contact:\n    description: CISA KEV API spec must declare a contact.\n    severity: warn\n    given: $.info\n    then:\n      field: contact\n      function: truthy\n  cisa-kev-server-https:\n    description: All KEV servers must use HTTPS.\n    severity: error\n    given: $.servers[*].url\n    then:\n      function: pattern\n      functionOptions:\n        match: '^https://'\n  cisa-kev-tags-required:\n    description: Every operation must declare at least one tag.\n    severity: warn\n    given: $.paths[*][get,post,put,patch,delete]\n    then:\n      field: tags\n      function: truthy\n  cisa-kev-operation-id-required:\n    description: Every operation must declare an operationId.\n    severity: error\n    given: $.paths[*][get,post,put,patch,delete]\n    then:\n      field: operationId\n      function: truthy\n  cisa-kev-public-no-auth:\n    description: KEV feed is public; spec must not declare a global security requirement.\n\
  \    severity: warn\n    given: $\n    then:\n      field: security\n      function: falsy\n"
source_yaml_url: https://raw.githubusercontent.com/api-evangelist/cybersecurity-and-infrastructure-security-agency/refs/heads/main/rules/cisa-kev-rules.yml
tags:
- Advisories
- AIS
- Binding Operational Directive
- CSAF
- CVE
- CWE
- Cybersecurity
- Federal Government
- Government
- ICS-CERT
- Information Sharing
- KEV
- Known Exploited Vulnerabilities
- Risk Management
- Security
- STIX
- TAXII
- Threat Intelligence
- Vulnerability Management
- Spectral
- Linting
- API Governance
---
