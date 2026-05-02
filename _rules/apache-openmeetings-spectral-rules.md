---
api_specs:
- filename: apache-openmeetings-rest-api.json
  format: json
  label: Apache OpenMeetings REST API
  slug: apache-openmeetings-rest-api
  spec_type: OpenAPI
  url: https://raw.githubusercontent.com/api-evangelist/apache-openmeetings/refs/heads/main/openapi/apache-openmeetings-rest-api.json
categories:
- info
- operation
- paths
- response
- schema
- servers
description: Spectral linting rules defining API design standards and conventions for Apache OpenMeetings.
layout: rules
name: Apache OpenMeetings API Rules
provider_name: Apache OpenMeetings
provider_slug: apache-openmeetings
rule_count: 10
rules:
- description: API must have a title
  given: $.info
  name: info-title-required
  severity: error
- description: API must have a description
  given: $.info
  name: info-description-required
  severity: warn
- description: Operations must have summaries
  given: $.paths[*][*]
  name: operation-summary-required
  severity: error
- description: Operations must have operationIds
  given: $.paths[*][*]
  name: operation-operationId-required
  severity: error
- description: Operations must have tags
  given: $.paths[*][*]
  name: operation-tags-required
  severity: warn
- description: Path segments should use kebab-case
  given: $.paths[*]~
  name: paths-kebab-case
  severity: warn
- description: Operation summaries should start with Apache OpenMeetings
  given: $.paths[*][get,post,put,delete,patch].summary
  name: operation-summary-apache-prefix
  severity: info
- description: Servers should use HTTPS
  given: $.servers[*].url
  name: servers-https
  severity: warn
- description: Operations must have a success response
  given: $.paths[*][*].responses
  name: response-success-required
  severity: error
- description: Schema properties should have descriptions
  given: $.components.schemas[*].properties[*]
  name: schema-properties-described
  severity: info
rules_file: rules/apache-openmeetings-spectral-rules.yml
rules_url: https://raw.githubusercontent.com/api-evangelist/apache-openmeetings/refs/heads/main/rules/apache-openmeetings-spectral-rules.yml
severity_counts:
  error: 4
  hint: 0
  info: 2
  warn: 4
slug: apache-openmeetings-spectral-rules
source_filename: apache-openmeetings-spectral-rules.yml
source_heading: Spectral Ruleset
source_yaml: "extends: \"spectral:oas\"\nrules:\n  info-title-required:\n    description: \"API must have a title\"\n    severity: error\n    given: \"$.info\"\n    then:\n      field: title\n      function: truthy\n  info-description-required:\n    description: \"API must have a description\"\n    severity: warn\n    given: \"$.info\"\n    then:\n      field: description\n      function: truthy\n  operation-summary-required:\n    description: \"Operations must have summaries\"\n    severity: error\n    given: \"$.paths[*][*]\"\n    then:\n      field: summary\n      function: truthy\n  operation-operationId-required:\n    description: \"Operations must have operationIds\"\n    severity: error\n    given: \"$.paths[*][*]\"\n    then:\n      field: operationId\n      function: truthy\n  operation-tags-required:\n    description: \"Operations must have tags\"\n    severity: warn\n    given: \"$.paths[*][*]\"\n    then:\n      field: tags\n      function: truthy\n  paths-kebab-case:\n    description:\
  \ \"Path segments should use kebab-case\"\n    severity: warn\n    given: \"$.paths[*]~\"\n    then:\n      function: pattern\n      functionOptions:\n        match: \"^(/[a-z0-9{}-]+)+$\"\n  operation-summary-apache-prefix:\n    description: \"Operation summaries should start with Apache OpenMeetings\"\n    severity: info\n    given: \"$.paths[*][get,post,put,delete,patch].summary\"\n    then:\n      function: pattern\n      functionOptions:\n        match: \"^Apache OpenMeetings\"\n  servers-https:\n    description: \"Servers should use HTTPS\"\n    severity: warn\n    given: \"$.servers[*].url\"\n    then:\n      function: pattern\n      functionOptions:\n        match: \"^https://\"\n  response-success-required:\n    description: \"Operations must have a success response\"\n    severity: error\n    given: \"$.paths[*][*].responses\"\n    then:\n      function: schema\n      functionOptions:\n        schema:\n          anyOf:\n            - required: [\"200\"]\n            - required:\
  \ [\"201\"]\n            - required: [\"204\"]\n  schema-properties-described:\n    description: \"Schema properties should have descriptions\"\n    severity: info\n    given: \"$.components.schemas[*].properties[*]\"\n    then:\n      field: description\n      function: truthy\n"
source_yaml_url: https://raw.githubusercontent.com/api-evangelist/apache-openmeetings/refs/heads/main/rules/apache-openmeetings-spectral-rules.yml
tags:
- Collaboration
- Video Conferencing
- Web Conferencing
- Whiteboard
- Apache
- Open Source
- Conferencing
- Spectral
- Linting
- API Governance
---
