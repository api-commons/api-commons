---
api_specs:
- filename: cfpb-ccdb-openapi.yml
  format: yaml
  label: Consumer Complaint Database API
  slug: ccdb
  spec_type: OpenAPI
  url: https://raw.githubusercontent.com/api-evangelist/consumer-financial-protection-bureau/refs/heads/main/openapi/cfpb-ccdb-openapi.yml
- filename: cfpb-hmda-data-browser-openapi.yml
  format: yaml
  label: HMDA Data Browser API
  slug: hmda-data-browser
  spec_type: OpenAPI
  url: https://raw.githubusercontent.com/api-evangelist/consumer-financial-protection-bureau/refs/heads/main/openapi/cfpb-hmda-data-browser-openapi.yml
- filename: cfpb-hmda-institutions-openapi.yml
  format: yaml
  label: HMDA Institutions API
  slug: hmda-institutions
  spec_type: OpenAPI
  url: https://raw.githubusercontent.com/api-evangelist/consumer-financial-protection-bureau/refs/heads/main/openapi/cfpb-hmda-institutions-openapi.yml
categories:
- cfpb
description: Spectral linting rules defining API design standards and conventions for Consumer Financial Protection Bureau.
layout: rules
name: Consumer Financial Protection Bureau API Rules
provider_name: Consumer Financial Protection Bureau
provider_slug: consumer-financial-protection-bureau
rule_count: 8
rules:
- description: API contact information must be present.
  given: $.info
  name: cfpb-info-contact
  severity: error
- description: All server URLs must use HTTPS.
  given: $.servers[*].url
  name: cfpb-server-https
  severity: error
- description: Server URLs must point to a *.cfpb.gov or consumerfinance.gov host.
  given: $.servers[*].url
  name: cfpb-server-cfpb-host
  severity: warn
- description: Every operation must declare a unique operationId.
  given: $.paths[*][get,post,put,patch,delete]
  name: cfpb-operation-id
  severity: error
- description: Operations must declare at least one tag.
  given: $.paths[*][get,post,put,patch,delete]
  name: cfpb-operation-tags
  severity: warn
- description: Public-data APIs should declare a CC0 or other public-domain license.
  given: $.info.license
  name: cfpb-public-license
  severity: info
- description: Responses should declare application/json or text/csv content types.
  given: $.paths[*].get.responses['200'].content
  name: cfpb-csv-or-json-content
  severity: info
- description: Lookups and detail endpoints should declare 404 responses.
  given: $.paths[?(@property.match(/\{.*\}/))][get].responses
  name: cfpb-error-responses
  severity: info
rules_file: rules/consumer-financial-protection-bureau-rules.yml
rules_url: https://raw.githubusercontent.com/api-evangelist/consumer-financial-protection-bureau/refs/heads/main/rules/consumer-financial-protection-bureau-rules.yml
severity_counts:
  error: 3
  hint: 0
  info: 3
  warn: 2
slug: consumer-financial-protection-bureau-rules
source_filename: consumer-financial-protection-bureau-rules.yml
source_heading: Spectral Ruleset
source_yaml: "extends:\n  - spectral:oas\n\n# Spectral linting rules for CFPB public data APIs.\n# Tuned to consumerfinance.gov and ffiec.cfpb.gov conventions: HTTPS,\n# unauthenticated public access (no security scheme required), JSON +\n# CSV outputs, and explicit year/date filters.\nrules:\n  cfpb-info-contact:\n    description: API contact information must be present.\n    severity: error\n    given: \"$.info\"\n    then:\n      field: contact\n      function: truthy\n\n  cfpb-server-https:\n    description: All server URLs must use HTTPS.\n    severity: error\n    given: \"$.servers[*].url\"\n    then:\n      function: pattern\n      functionOptions:\n        match: \"^https://\"\n\n  cfpb-server-cfpb-host:\n    description: Server URLs must point to a *.cfpb.gov or consumerfinance.gov host.\n    severity: warn\n    given: \"$.servers[*].url\"\n    then:\n      function: pattern\n      functionOptions:\n        match: \"(cfpb\\\\.gov|consumerfinance\\\\.gov)\"\n\n  cfpb-operation-id:\n\
  \    description: Every operation must declare a unique operationId.\n    severity: error\n    given: \"$.paths[*][get,post,put,patch,delete]\"\n    then:\n      field: operationId\n      function: truthy\n\n  cfpb-operation-tags:\n    description: Operations must declare at least one tag.\n    severity: warn\n    given: \"$.paths[*][get,post,put,patch,delete]\"\n    then:\n      field: tags\n      function: schema\n      functionOptions:\n        schema:\n          type: array\n          minItems: 1\n\n  cfpb-public-license:\n    description: Public-data APIs should declare a CC0 or other public-domain license.\n    severity: info\n    given: \"$.info.license\"\n    then:\n      field: name\n      function: pattern\n      functionOptions:\n        match: \"(CC0|Public Domain|Creative Commons)\"\n\n  cfpb-csv-or-json-content:\n    description: Responses should declare application/json or text/csv content types.\n    severity: info\n    given: \"$.paths[*].get.responses['200'].content\"\
  \n    then:\n      function: schema\n      functionOptions:\n        schema:\n          type: object\n          anyOf:\n            - required: [\"application/json\"]\n            - required: [\"text/csv\"]\n\n  cfpb-error-responses:\n    description: Lookups and detail endpoints should declare 404 responses.\n    severity: info\n    given: \"$.paths[?(@property.match(/\\\\{.*\\\\}/))][get].responses\"\n    then:\n      function: schema\n      functionOptions:\n        schema:\n          type: object\n          required: [\"404\"]\n"
source_yaml_url: https://raw.githubusercontent.com/api-evangelist/consumer-financial-protection-bureau/refs/heads/main/rules/consumer-financial-protection-bureau-rules.yml
tags:
- Banking
- Complaints
- Consumer Protection
- Federal Government
- Financial Services
- HMDA
- Mortgages
- Open Data
- Spectral
- Linting
- API Governance
---
