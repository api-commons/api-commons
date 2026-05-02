---
api_specs:
- filename: copper-developer-api-openapi.yml
  format: yaml
  label: Copper Developer API
  slug: developer-api
  spec_type: OpenAPI
  url: https://raw.githubusercontent.com/api-evangelist/copper/refs/heads/main/openapi/copper-developer-api-openapi.yml
categories:
- copper
description: Spectral linting rules defining API design standards and conventions for Copper.
layout: rules
name: Copper API Rules
provider_name: Copper
provider_slug: copper
rule_count: 14
rules:
- description: API info object should include contact information.
  given: $.info
  name: copper-info-contact
  severity: error
- description: API info object should include license information.
  given: $.info
  name: copper-info-license
  severity: warn
- description: All servers must use HTTPS.
  given: $.servers[*].url
  name: copper-server-https
  severity: error
- description: Servers should reference the Copper Developer API host.
  given: $.servers[*].url
  name: copper-base-url
  severity: warn
- description: Operations should be protected by Copper auth headers.
  given: $.security
  name: copper-required-auth-headers
  severity: error
- description: Every operation must have at least one tag.
  given: $.paths.*[get,post,put,delete,patch]
  name: copper-operation-tags
  severity: error
- description: Every operation must have a summary.
  given: $.paths.*[get,post,put,delete,patch]
  name: copper-operation-summary
  severity: error
- description: Operations should include a description.
  given: $.paths.*[get,post,put,delete,patch]
  name: copper-operation-description
  severity: warn
- description: Every operation must have an operationId in camelCase.
  given: $.paths.*[get,post,put,delete,patch]
  name: copper-operation-id
  severity: error
- description: Search endpoints should support page_number and page_size parameters.
  given: $.paths['/people/search','/companies/search','/leads/search','/opportunities/search','/tasks/search','/activities/search'].post.requestBody.content.application/json.schema
  name: copper-pagination-params
  severity: warn
- description: Tags should use PascalCase plural resource names.
  given: $.tags[*].name
  name: copper-tag-pascal-case
  severity: warn
- description: API description should mention rate limits.
  given: $.info.description
  name: copper-rate-limit-documented
  severity: info
- description: Error responses should reference an Error schema.
  given: $.components.schemas
  name: copper-error-schema
  severity: warn
- description: Resource id fields should be int64 integers.
  given: $.components.schemas.*.properties.id
  name: copper-resource-id-integer
  severity: warn
rules_file: rules/copper-developer-api-rules.yml
rules_url: https://raw.githubusercontent.com/api-evangelist/copper/refs/heads/main/rules/copper-developer-api-rules.yml
severity_counts:
  error: 6
  hint: 0
  info: 1
  warn: 7
slug: copper-developer-api-rules
source_filename: copper-developer-api-rules.yml
source_heading: Spectral Ruleset
source_yaml: "extends: [\"spectral:oas\"]\ndocumentationUrl: https://developer.copper.com/\nrules:\n  copper-info-contact:\n    description: API info object should include contact information.\n    message: \"{{description}}: info.contact is required.\"\n    given: \"$.info\"\n    severity: error\n    then:\n      field: contact\n      function: truthy\n  copper-info-license:\n    description: API info object should include license information.\n    given: \"$.info\"\n    severity: warn\n    then:\n      field: license\n      function: truthy\n  copper-server-https:\n    description: All servers must use HTTPS.\n    given: \"$.servers[*].url\"\n    severity: error\n    then:\n      function: pattern\n      functionOptions:\n        match: \"^https://\"\n  copper-base-url:\n    description: Servers should reference the Copper Developer API host.\n    given: \"$.servers[*].url\"\n    severity: warn\n    then:\n      function: pattern\n      functionOptions:\n        match: \"api.copper.com/developer_api\"\
  \n  copper-required-auth-headers:\n    description: Operations should be protected by Copper auth headers.\n    given: \"$.security\"\n    severity: error\n    then:\n      function: truthy\n  copper-operation-tags:\n    description: Every operation must have at least one tag.\n    given: \"$.paths.*[get,post,put,delete,patch]\"\n    severity: error\n    then:\n      field: tags\n      function: truthy\n  copper-operation-summary:\n    description: Every operation must have a summary.\n    given: \"$.paths.*[get,post,put,delete,patch]\"\n    severity: error\n    then:\n      field: summary\n      function: truthy\n  copper-operation-description:\n    description: Operations should include a description.\n    given: \"$.paths.*[get,post,put,delete,patch]\"\n    severity: warn\n    then:\n      field: description\n      function: truthy\n  copper-operation-id:\n    description: Every operation must have an operationId in camelCase.\n    given: \"$.paths.*[get,post,put,delete,patch]\"\n \
  \   severity: error\n    then:\n      field: operationId\n      function: pattern\n      functionOptions:\n        match: \"^[a-z][a-zA-Z0-9]+$\"\n  copper-pagination-params:\n    description: Search endpoints should support page_number and page_size parameters.\n    given: \"$.paths['/people/search','/companies/search','/leads/search','/opportunities/search','/tasks/search','/activities/search'].post.requestBody.content.application/json.schema\"\n    severity: warn\n    then:\n      function: truthy\n  copper-tag-pascal-case:\n    description: Tags should use PascalCase plural resource names.\n    given: \"$.tags[*].name\"\n    severity: warn\n    then:\n      function: pattern\n      functionOptions:\n        match: \"^[A-Z][a-zA-Z]+s?$\"\n  copper-rate-limit-documented:\n    description: API description should mention rate limits.\n    given: \"$.info.description\"\n    severity: info\n    then:\n      function: pattern\n      functionOptions:\n        match: \"rate|limit|180|3 requests\"\
  \n  copper-error-schema:\n    description: Error responses should reference an Error schema.\n    given: \"$.components.schemas\"\n    severity: warn\n    then:\n      field: Error\n      function: truthy\n  copper-resource-id-integer:\n    description: Resource id fields should be int64 integers.\n    given: \"$.components.schemas.*.properties.id\"\n    severity: warn\n    then:\n      field: type\n      function: enumeration\n      functionOptions:\n        values:\n          - integer\n"
source_yaml_url: https://raw.githubusercontent.com/api-evangelist/copper/refs/heads/main/rules/copper-developer-api-rules.yml
tags:
- Activities
- Companies
- Contact Relationship Management
- Contacts
- CRM
- Customer Relationship Management
- Google Workspace
- Leads
- Opportunities
- People
- Projects
- Sales
- Tasks
- Spectral
- Linting
- API Governance
---
