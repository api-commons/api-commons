---
api_specs:
- filename: datahub-openapi-openapi.yml
  format: yaml
  label: DataHub OpenAPI
  slug: datahub-openapi
  spec_type: OpenAPI
  url: https://raw.githubusercontent.com/api-evangelist/datahub/refs/heads/main/openapi/datahub-openapi-openapi.yml
- filename: datahub-actions-asyncapi.yml
  format: yaml
  label: DataHub Actions Framework
  slug: datahub-actions-framework
  spec_type: AsyncAPI
  url: https://raw.githubusercontent.com/api-evangelist/datahub/refs/heads/main/asyncapi/datahub-actions-asyncapi.yml
categories:
- datahub
description: Spectral linting rules defining API design standards and conventions for DataHub.
layout: rules
name: DataHub API Rules
provider_name: DataHub
provider_slug: datahub
rule_count: 5
rules:
- description: API info should provide a contact for the DataHub project.
  given: $.info
  name: datahub-info-contact
  severity: warn
- description: OpenAPI paths should be served under /openapi.
  given: $.paths
  name: datahub-openapi-prefix
  severity: warn
- description: URN parameters must follow the urn:li:<entityType>:<id> pattern.
  given: $.paths.*.*.parameters[?(@.name=='urn')].schema
  name: datahub-urn-pattern
  severity: warn
- description: Every operation must declare at least one tag.
  given: $.paths[*][*]
  name: datahub-operation-tags
  severity: error
- description: Aspect schemas should include a version field for timeline history.
  given: $.components.schemas[?(@.title && @.title.match(/Aspect/))]
  name: datahub-aspect-versioned
  severity: warn
rules_file: rules/datahub-rules.yml
rules_url: https://raw.githubusercontent.com/api-evangelist/datahub/refs/heads/main/rules/datahub-rules.yml
severity_counts:
  error: 1
  hint: 0
  info: 0
  warn: 4
slug: datahub-rules
source_filename: datahub-rules.yml
source_heading: Spectral Ruleset
source_yaml: "extends:\n  - spectral:oas\nrules:\n  datahub-info-contact:\n    description: API info should provide a contact for the DataHub project.\n    given: $.info\n    severity: warn\n    then:\n      field: contact\n      function: truthy\n  datahub-openapi-prefix:\n    description: OpenAPI paths should be served under /openapi.\n    given: $.paths\n    severity: warn\n    then:\n      function: pattern\n      functionOptions:\n        match: \"^/openapi\"\n  datahub-urn-pattern:\n    description: URN parameters must follow the urn:li:<entityType>:<id> pattern.\n    given: $.paths.*.*.parameters[?(@.name=='urn')].schema\n    severity: warn\n    then:\n      field: pattern\n      function: truthy\n  datahub-operation-tags:\n    description: Every operation must declare at least one tag.\n    given: $.paths[*][*]\n    severity: error\n    then:\n      field: tags\n      function: truthy\n  datahub-aspect-versioned:\n    description: Aspect schemas should include a version field for\
  \ timeline history.\n    given: $.components.schemas[?(@.title && @.title.match(/Aspect/))]\n    severity: warn\n    then:\n      field: properties.version\n      function: truthy\n"
source_yaml_url: https://raw.githubusercontent.com/api-evangelist/datahub/refs/heads/main/rules/datahub-rules.yml
tags:
- Data Catalog
- Data Discovery
- Data Governance
- Data Lineage
- Metadata
- Spectral
- Linting
- API Governance
---
