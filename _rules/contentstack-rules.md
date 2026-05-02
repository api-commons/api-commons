---
api_specs:
- filename: contentstack-content-delivery-api-openapi.yml
  format: yaml
  label: Contentstack Content Delivery API
  slug: content-delivery-api
  spec_type: OpenAPI
  url: https://raw.githubusercontent.com/api-evangelist/contentstack/refs/heads/main/openapi/contentstack-content-delivery-api-openapi.yml
- filename: contentstack-content-management-api-openapi.yml
  format: yaml
  label: Contentstack Content Management API
  slug: content-management-api
  spec_type: OpenAPI
  url: https://raw.githubusercontent.com/api-evangelist/contentstack/refs/heads/main/openapi/contentstack-content-management-api-openapi.yml
- filename: contentstack-personalize-management-api-openapi.yml
  format: yaml
  label: Contentstack Personalize Management API
  slug: personalize-management-api
  spec_type: OpenAPI
  url: https://raw.githubusercontent.com/api-evangelist/contentstack/refs/heads/main/openapi/contentstack-personalize-management-api-openapi.yml
- filename: contentstack-personalize-edge-api-openapi.yml
  format: yaml
  label: Contentstack Personalize Edge API
  slug: personalize-edge-api
  spec_type: OpenAPI
  url: https://raw.githubusercontent.com/api-evangelist/contentstack/refs/heads/main/openapi/contentstack-personalize-edge-api-openapi.yml
- filename: contentstack-automate-management-api-openapi.yml
  format: yaml
  label: Contentstack Automate Management API
  slug: automate-management-api
  spec_type: OpenAPI
  url: https://raw.githubusercontent.com/api-evangelist/contentstack/refs/heads/main/openapi/contentstack-automate-management-api-openapi.yml
- filename: contentstack-analytics-api-openapi.yml
  format: yaml
  label: Contentstack Analytics API
  slug: analytics-api
  spec_type: OpenAPI
  url: https://raw.githubusercontent.com/api-evangelist/contentstack/refs/heads/main/openapi/contentstack-analytics-api-openapi.yml
- filename: contentstack-scim-api-openapi.yml
  format: yaml
  label: Contentstack SCIM API
  slug: scim-api
  spec_type: OpenAPI
  url: https://raw.githubusercontent.com/api-evangelist/contentstack/refs/heads/main/openapi/contentstack-scim-api-openapi.yml
- filename: contentstack-brand-kit-management-api-openapi.yml
  format: yaml
  label: Contentstack Brand Kit Management API
  slug: brand-kit-management-api
  spec_type: OpenAPI
  url: https://raw.githubusercontent.com/api-evangelist/contentstack/refs/heads/main/openapi/contentstack-brand-kit-management-api-openapi.yml
- filename: contentstack-knowledge-vault-api-openapi.yml
  format: yaml
  label: Contentstack Knowledge Vault API
  slug: knowledge-vault-api
  spec_type: OpenAPI
  url: https://raw.githubusercontent.com/api-evangelist/contentstack/refs/heads/main/openapi/contentstack-knowledge-vault-api-openapi.yml
- filename: contentstack-generative-ai-api-openapi.yml
  format: yaml
  label: Contentstack Generative AI API
  slug: generative-ai-api
  spec_type: OpenAPI
  url: https://raw.githubusercontent.com/api-evangelist/contentstack/refs/heads/main/openapi/contentstack-generative-ai-api-openapi.yml
- filename: contentstack-launch-api-openapi.yml
  format: yaml
  label: Contentstack Launch API
  slug: launch-api
  spec_type: OpenAPI
  url: https://raw.githubusercontent.com/api-evangelist/contentstack/refs/heads/main/openapi/contentstack-launch-api-openapi.yml
categories:
- contentstack
description: Spectral linting rules defining API design standards and conventions for contentstack.
layout: rules
name: contentstack API Rules
provider_name: contentstack
provider_slug: contentstack
rule_count: 8
rules:
- description: All Contentstack OpenAPI info.title fields must start with "Contentstack"
  given: $.info.title
  name: contentstack-info-title-prefix
  severity: error
- description: Info contact information should be present
  given: $.info
  name: contentstack-info-contact
  severity: warn
- description: At least one server URL must be defined
  given: $.servers
  name: contentstack-server-defined
  severity: error
- description: Every operation must define an operationId in camelCase
  given: $.paths.*[get,put,post,delete,patch].operationId
  name: contentstack-operation-id-camelcase
  severity: error
- description: Every operation must include a non-empty summary
  given: $.paths.*[get,put,post,delete,patch]
  name: contentstack-operation-summary-required
  severity: error
- description: Operations must reference at least one tag
  given: $.paths.*[get,put,post,delete,patch].tags
  name: contentstack-tag-defined
  severity: warn
- description: Paths should not end with a trailing slash
  given: $.paths
  name: contentstack-no-trailing-slash
  severity: warn
- description: Every operation must define a 2xx response
  given: $.paths.*[get,put,post,delete,patch].responses
  name: contentstack-success-response-defined
  severity: error
rules_file: rules/contentstack-rules.yml
rules_url: https://raw.githubusercontent.com/api-evangelist/contentstack/refs/heads/main/rules/contentstack-rules.yml
severity_counts:
  error: 5
  hint: 0
  info: 0
  warn: 3
slug: contentstack-rules
source_filename: contentstack-rules.yml
source_heading: Spectral Ruleset
source_yaml: "extends:\n  - \"spectral:oas\"\ndocumentationUrl: https://www.contentstack.com/docs/developers/apis\nrules:\n  contentstack-info-title-prefix:\n    description: All Contentstack OpenAPI info.title fields must start with \"Contentstack\"\n    severity: error\n    given: \"$.info.title\"\n    then:\n      function: pattern\n      functionOptions:\n        match: \"^Contentstack\\\\b\"\n  contentstack-info-contact:\n    description: Info contact information should be present\n    severity: warn\n    given: \"$.info\"\n    then:\n      field: contact\n      function: truthy\n  contentstack-server-defined:\n    description: At least one server URL must be defined\n    severity: error\n    given: \"$.servers\"\n    then:\n      function: length\n      functionOptions:\n        min: 1\n  contentstack-operation-id-camelcase:\n    description: Every operation must define an operationId in camelCase\n    severity: error\n    given: \"$.paths.*[get,put,post,delete,patch].operationId\"\
  \n    then:\n      function: pattern\n      functionOptions:\n        match: \"^[a-z][a-zA-Z0-9]+$\"\n  contentstack-operation-summary-required:\n    description: Every operation must include a non-empty summary\n    severity: error\n    given: \"$.paths.*[get,put,post,delete,patch]\"\n    then:\n      field: summary\n      function: truthy\n  contentstack-tag-defined:\n    description: Operations must reference at least one tag\n    severity: warn\n    given: \"$.paths.*[get,put,post,delete,patch].tags\"\n    then:\n      function: length\n      functionOptions:\n        min: 1\n  contentstack-no-trailing-slash:\n    description: Paths should not end with a trailing slash\n    severity: warn\n    given: \"$.paths\"\n    then:\n      field: \"@key\"\n      function: pattern\n      functionOptions:\n        notMatch: \"/$\"\n  contentstack-success-response-defined:\n    description: Every operation must define a 2xx response\n    severity: error\n    given: \"$.paths.*[get,put,post,delete,patch].responses\"\
  \n    then:\n      function: schema\n      functionOptions:\n        schema:\n          type: object\n          patternProperties:\n            \"^2[0-9]{2}$\": {}\n          minProperties: 1\n"
source_yaml_url: https://raw.githubusercontent.com/api-evangelist/contentstack/refs/heads/main/rules/contentstack-rules.yml
tags:
- Spectral
- Linting
- API Governance
---
