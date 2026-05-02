---
api_specs:
- filename: openapi
  format: yaml
  label: Citrix Virtual Apps and Desktops REST API
  slug: ''
  spec_type: OpenAPI
  url: https://developer.citrix.com/citrix-virtual-apps-and-desktops/citrix-cvad-rest-apis/docs/openapi
- filename: citrix-adc-nitro-openapi.yml
  format: yaml
  label: Citrix ADC (NetScaler) NITRO API
  slug: ''
  spec_type: OpenAPI
  url: https://raw.githubusercontent.com/api-evangelist/citrix/refs/heads/main/openapi/citrix-adc-nitro-openapi.yml
- filename: openapi
  format: yaml
  label: Citrix DaaS REST API
  slug: ''
  spec_type: OpenAPI
  url: https://developer.citrix.com/citrix-daas/citrix-daas-rest-apis/docs/openapi
- filename: citrix-cloud-openapi.yml
  format: yaml
  label: Citrix Cloud API
  slug: ''
  spec_type: OpenAPI
  url: https://raw.githubusercontent.com/api-evangelist/citrix/refs/heads/main/openapi/citrix-cloud-openapi.yml
- filename: citrix-storefront-web-openapi.yml
  format: yaml
  label: Citrix StoreFront Web API
  slug: ''
  spec_type: OpenAPI
  url: https://raw.githubusercontent.com/api-evangelist/citrix/refs/heads/main/openapi/citrix-storefront-web-openapi.yml
- filename: citrix-endpoint-management-openapi.yml
  format: yaml
  label: Citrix Endpoint Management REST API
  slug: ''
  spec_type: OpenAPI
  url: https://raw.githubusercontent.com/api-evangelist/citrix/refs/heads/main/openapi/citrix-endpoint-management-openapi.yml
- filename: citrix-secure-private-access-openapi.yml
  format: yaml
  label: Citrix Secure Private Access API
  slug: ''
  spec_type: OpenAPI
  url: https://raw.githubusercontent.com/api-evangelist/citrix/refs/heads/main/openapi/citrix-secure-private-access-openapi.yml
categories:
- citrix
description: Spectral linting rules defining API design standards and conventions for Citrix.
layout: rules
name: Citrix API Rules
provider_name: Citrix
provider_slug: citrix
rule_count: 7
rules:
- description: API info MUST contain a contact email or URL.
  given: $.info
  name: citrix-info-contact
  severity: warn
- description: All Citrix API servers MUST use HTTPS.
  given: $.servers[*].url
  name: citrix-https-only
  severity: error
- description: Operations MUST have an operationId.
  given: $.paths[*][get,post,put,delete,patch]
  name: citrix-operation-id
  severity: error
- description: Operations MUST be tagged for product domain grouping.
  given: $.paths[*][get,post,put,delete,patch].tags
  name: citrix-tag-required
  severity: warn
- description: API MUST define security schemes (OAuth 2.0 bearer for Citrix Cloud).
  given: $.components.securitySchemes
  name: citrix-security-required
  severity: error
- description: API MUST declare at least one server URL.
  given: $.servers
  name: citrix-server-url
  severity: error
- description: Customer-scoped Citrix Cloud paths SHOULD use templated customerId.
  given: $.paths
  name: citrix-customer-id-templating
  severity: warn
rules_file: rules/citrix-rules.yml
rules_url: https://raw.githubusercontent.com/api-evangelist/citrix/refs/heads/main/rules/citrix-rules.yml
severity_counts:
  error: 4
  hint: 0
  info: 0
  warn: 3
slug: citrix-rules
source_filename: citrix-rules.yml
source_heading: Spectral Ruleset
source_yaml: "extends:\n  - spectral:oas\nrules:\n  citrix-info-contact:\n    description: API info MUST contain a contact email or URL.\n    severity: warn\n    given: $.info\n    then:\n      field: contact\n      function: truthy\n  citrix-https-only:\n    description: All Citrix API servers MUST use HTTPS.\n    severity: error\n    given: $.servers[*].url\n    then:\n      function: pattern\n      functionOptions:\n        match: '^https://'\n  citrix-operation-id:\n    description: Operations MUST have an operationId.\n    severity: error\n    given: $.paths[*][get,post,put,delete,patch]\n    then:\n      field: operationId\n      function: truthy\n  citrix-tag-required:\n    description: Operations MUST be tagged for product domain grouping.\n    severity: warn\n    given: $.paths[*][get,post,put,delete,patch].tags\n    then:\n      function: truthy\n  citrix-security-required:\n    description: API MUST define security schemes (OAuth 2.0 bearer for Citrix Cloud).\n    severity: error\n\
  \    given: $.components.securitySchemes\n    then:\n      function: truthy\n  citrix-server-url:\n    description: API MUST declare at least one server URL.\n    severity: error\n    given: $.servers\n    then:\n      function: truthy\n  citrix-customer-id-templating:\n    description: Customer-scoped Citrix Cloud paths SHOULD use templated customerId.\n    severity: warn\n    given: $.paths\n    then:\n      function: truthy\n"
source_yaml_url: https://raw.githubusercontent.com/api-evangelist/citrix/refs/heads/main/rules/citrix-rules.yml
tags:
- Application Delivery
- Desktop-As-A-Service
- Networking
- Virtualization
- Workspace
- Spectral
- Linting
- API Governance
---
