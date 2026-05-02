---
api_specs:
- filename: customer-io-track-api-openapi.yml
  format: yaml
  label: Customer.io Track API
  slug: track-api
  spec_type: OpenAPI
  url: https://raw.githubusercontent.com/api-evangelist/customer-io/refs/heads/main/openapi/customer-io-track-api-openapi.yml
- filename: customer-io-app-api-openapi.yml
  format: yaml
  label: Customer.io App API
  slug: app-api
  spec_type: OpenAPI
  url: https://raw.githubusercontent.com/api-evangelist/customer-io/refs/heads/main/openapi/customer-io-app-api-openapi.yml
- filename: customer-io-pipelines-api-openapi.yml
  format: yaml
  label: Customer.io Pipelines API
  slug: pipelines-api
  spec_type: OpenAPI
  url: https://raw.githubusercontent.com/api-evangelist/customer-io/refs/heads/main/openapi/customer-io-pipelines-api-openapi.yml
categories:
- customer
description: Spectral linting rules defining API design standards and conventions for Customer.io.
layout: rules
name: Customer.io API Rules
provider_name: Customer.io
provider_slug: customer-io
rule_count: 6
rules:
- description: Customer.io API specs must declare a contact.
  given: $.info
  name: customer-io-info-contact
  severity: warn
- description: Customer.io API server URLs must use HTTPS.
  given: $.servers[*].url
  name: customer-io-server-https
  severity: error
- description: Customer.io API base URLs must point to a customer.io host.
  given: $.servers[*].url
  name: customer-io-base-host
  severity: error
- description: Every operation must declare at least one tag.
  given: $.paths[*][get,post,put,patch,delete]
  name: customer-io-tags-required
  severity: warn
- description: Every operation must declare an operationId.
  given: $.paths[*][get,post,put,patch,delete]
  name: customer-io-operation-id-required
  severity: error
- description: Every operation must declare security requirements.
  given: $.paths[*][get,post,put,patch,delete]
  name: customer-io-security-required
  severity: warn
rules_file: rules/customer-io-rules.yml
rules_url: https://raw.githubusercontent.com/api-evangelist/customer-io/refs/heads/main/rules/customer-io-rules.yml
severity_counts:
  error: 3
  hint: 0
  info: 0
  warn: 3
slug: customer-io-rules
source_filename: customer-io-rules.yml
source_heading: Spectral Ruleset
source_yaml: "extends: spectral:oas\nrules:\n  customer-io-info-contact:\n    description: Customer.io API specs must declare a contact.\n    severity: warn\n    given: $.info\n    then:\n      field: contact\n      function: truthy\n  customer-io-server-https:\n    description: Customer.io API server URLs must use HTTPS.\n    severity: error\n    given: $.servers[*].url\n    then:\n      function: pattern\n      functionOptions:\n        match: '^https://'\n  customer-io-base-host:\n    description: Customer.io API base URLs must point to a customer.io host.\n    severity: error\n    given: $.servers[*].url\n    then:\n      function: pattern\n      functionOptions:\n        match: '^https://([a-z]+\\.)?customer\\.io'\n  customer-io-tags-required:\n    description: Every operation must declare at least one tag.\n    severity: warn\n    given: $.paths[*][get,post,put,patch,delete]\n    then:\n      field: tags\n      function: truthy\n  customer-io-operation-id-required:\n    description:\
  \ Every operation must declare an operationId.\n    severity: error\n    given: $.paths[*][get,post,put,patch,delete]\n    then:\n      field: operationId\n      function: truthy\n  customer-io-security-required:\n    description: Every operation must declare security requirements.\n    severity: warn\n    given: $.paths[*][get,post,put,patch,delete]\n    then:\n      field: security\n      function: truthy\n"
source_yaml_url: https://raw.githubusercontent.com/api-evangelist/customer-io/refs/heads/main/rules/customer-io-rules.yml
tags:
- Behavioral Data
- Broadcasts
- Campaigns
- CDP
- Customer Data
- Customer Data Platform
- Data Ingestion
- Email
- Event Tracking
- Marketing Automation
- Messaging
- Push Notifications
- Segments
- SMS
- Transactional Email
- Spectral
- Linting
- API Governance
---
