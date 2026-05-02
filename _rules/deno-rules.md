---
api_specs:
- filename: deno-deploy-rest-api-openapi.yml
  format: yaml
  label: Deno Deploy REST API
  slug: deploy-rest-api
  spec_type: OpenAPI
  url: https://raw.githubusercontent.com/api-evangelist/deno/refs/heads/main/openapi/deno-deploy-rest-api-openapi.yml
- filename: deno-deploy-v2-api-openapi.yml
  format: yaml
  label: Deno Deploy API V2
  slug: deploy-v2-api
  spec_type: OpenAPI
  url: https://raw.githubusercontent.com/api-evangelist/deno/refs/heads/main/openapi/deno-deploy-v2-api-openapi.yml
- filename: deno-subhosting-api-openapi.yml
  format: yaml
  label: Deno Subhosting API
  slug: subhosting-api
  spec_type: OpenAPI
  url: https://raw.githubusercontent.com/api-evangelist/deno/refs/heads/main/openapi/deno-subhosting-api-openapi.yml
categories:
- deno
description: Spectral linting rules defining API design standards and conventions for Deno.
layout: rules
name: Deno API Rules
provider_name: Deno
provider_slug: deno
rule_count: 5
rules:
- description: Info object should contain Deno Deploy support contact details.
  given: $.info.contact
  name: deno-info-contact-email
  severity: warn
- description: Servers should be HTTPS only for Deno Deploy APIs.
  given: $.servers[*].url
  name: deno-server-https
  severity: error
- description: Deno Deploy APIs use Bearer token authentication.
  given: $.components.securitySchemes
  name: deno-bearer-auth-required
  severity: error
- description: Tags should match the documented Deno Deploy resource categories.
  given: $.tags[*].name
  name: deno-tag-allowed
  severity: warn
- description: Operation IDs should be camelCase.
  given: $.paths.*[get,post,put,patch,delete].operationId
  name: deno-operation-id-camel
  severity: warn
rules_file: rules/deno-rules.yml
rules_url: https://raw.githubusercontent.com/api-evangelist/deno/refs/heads/main/rules/deno-rules.yml
severity_counts:
  error: 2
  hint: 0
  info: 0
  warn: 3
slug: deno-rules
source_filename: deno-rules.yml
source_heading: Spectral Ruleset
source_yaml: "extends:\n  - spectral:oas\nrules:\n  deno-info-contact-email:\n    description: Info object should contain Deno Deploy support contact details.\n    given: $.info.contact\n    severity: warn\n    then:\n      field: name\n      function: truthy\n  deno-server-https:\n    description: Servers should be HTTPS only for Deno Deploy APIs.\n    given: $.servers[*].url\n    severity: error\n    then:\n      function: pattern\n      functionOptions:\n        match: \"^https://\"\n  deno-bearer-auth-required:\n    description: Deno Deploy APIs use Bearer token authentication.\n    given: $.components.securitySchemes\n    severity: error\n    then:\n      field: bearerAuth\n      function: truthy\n  deno-tag-allowed:\n    description: Tags should match the documented Deno Deploy resource categories.\n    given: $.tags[*].name\n    severity: warn\n    then:\n      function: enumeration\n      functionOptions:\n        values:\n          - Deployments\n          - Domains\n          -\
  \ KV Databases\n          - Organizations\n          - Projects\n          - Apps\n          - Revisions\n          - Layers\n          - Analytics\n          - Subhosting\n  deno-operation-id-camel:\n    description: Operation IDs should be camelCase.\n    given: $.paths.*[get,post,put,patch,delete].operationId\n    severity: warn\n    then:\n      function: pattern\n      functionOptions:\n        match: \"^[a-z][a-zA-Z0-9]+$\"\n"
source_yaml_url: https://raw.githubusercontent.com/api-evangelist/deno/refs/heads/main/rules/deno-rules.yml
tags:
- Deployment
- Edge
- JavaScript
- Runtime
- Serverless
- TypeScript
- Spectral
- Linting
- API Governance
---
