---
api_specs:
- filename: eventmesh-admin.yml
  format: yaml
  label: Apache EventMesh Admin API
  slug: eventmesh-admin-api
  spec_type: OpenAPI
  url: https://raw.githubusercontent.com/api-evangelist/apache-event-mesh/refs/heads/main/openapi/eventmesh-admin.yml
- filename: eventmesh-messaging.yml
  format: yaml
  label: Apache EventMesh Messaging API
  slug: eventmesh-messaging-api
  spec_type: AsyncAPI
  url: https://raw.githubusercontent.com/api-evangelist/apache-event-mesh/refs/heads/main/asyncapi/eventmesh-messaging.yml
categories:
- info
- operation
- parameter
- paths
- response
- schema
description: Spectral linting rules defining API design standards and conventions for Apache EventMesh.
layout: rules
name: Apache EventMesh API Rules
provider_name: Apache EventMesh
provider_slug: apache-event-mesh
rule_count: 10
rules:
- description: Info title must be defined
  given: $.info
  name: info-title-required
  severity: error
- description: API version must be specified
  given: $.info
  name: info-version-required
  severity: error
- description: All operations must have a summary
  given: $.paths[*][get,post,put,delete,patch]
  name: operation-summary-required
  severity: error
- description: Operation summaries should start with Apache EventMesh
  given: $.paths[*][get,post,put,delete,patch].summary
  name: operation-summary-apache-eventmesh-prefix
  severity: warn
- description: All operations must have an operationId
  given: $.paths[*][get,post,put,delete,patch]
  name: operation-operationId-required
  severity: error
- description: All operations must have at least one tag
  given: $.paths[*][get,post,put,delete,patch]
  name: operation-tags-required
  severity: warn
- description: Path segments should use kebab-case
  given: $.paths
  name: paths-kebab-case
  severity: warn
- description: All parameters must have descriptions
  given: $.paths[*][get,post,put,delete,patch].parameters[*]
  name: parameter-description-required
  severity: warn
- description: All responses must have descriptions
  given: $.paths[*][get,post,put,delete,patch].responses[*]
  name: response-description-required
  severity: warn
- description: Schema properties should have descriptions
  given: $.components.schemas[*].properties[*]
  name: schema-property-description
  severity: info
rules_file: rules/apache-event-mesh-spectral-rules.yml
rules_url: https://raw.githubusercontent.com/api-evangelist/apache-event-mesh/refs/heads/main/rules/apache-event-mesh-spectral-rules.yml
severity_counts:
  error: 4
  hint: 0
  info: 1
  warn: 5
slug: apache-event-mesh-spectral-rules
source_filename: apache-event-mesh-spectral-rules.yml
source_heading: Spectral Ruleset
source_yaml: "# Apache EventMesh Spectral Ruleset\nrules:\n  info-title-required:\n    description: Info title must be defined\n    severity: error\n    given: $.info\n    then:\n      field: title\n      function: truthy\n  info-version-required:\n    description: API version must be specified\n    severity: error\n    given: $.info\n    then:\n      field: version\n      function: truthy\n  operation-summary-required:\n    description: All operations must have a summary\n    severity: error\n    given: $.paths[*][get,post,put,delete,patch]\n    then:\n      field: summary\n      function: truthy\n  operation-summary-apache-eventmesh-prefix:\n    description: Operation summaries should start with Apache EventMesh\n    severity: warn\n    given: $.paths[*][get,post,put,delete,patch].summary\n    then:\n      function: pattern\n      functionOptions:\n        match: \"^Apache EventMesh\"\n  operation-operationId-required:\n    description: All operations must have an operationId\n    severity:\
  \ error\n    given: $.paths[*][get,post,put,delete,patch]\n    then:\n      field: operationId\n      function: truthy\n  operation-tags-required:\n    description: All operations must have at least one tag\n    severity: warn\n    given: $.paths[*][get,post,put,delete,patch]\n    then:\n      field: tags\n      function: truthy\n  paths-kebab-case:\n    description: Path segments should use kebab-case\n    severity: warn\n    given: $.paths\n    then:\n      field: \"@key\"\n      function: pattern\n      functionOptions:\n        match: \"^(/[a-z0-9{}_-]+)+$\"\n  parameter-description-required:\n    description: All parameters must have descriptions\n    severity: warn\n    given: $.paths[*][get,post,put,delete,patch].parameters[*]\n    then:\n      field: description\n      function: truthy\n  response-description-required:\n    description: All responses must have descriptions\n    severity: warn\n    given: $.paths[*][get,post,put,delete,patch].responses[*]\n    then:\n      field:\
  \ description\n      function: truthy\n  schema-property-description:\n    description: Schema properties should have descriptions\n    severity: info\n    given: $.components.schemas[*].properties[*]\n    then:\n      field: description\n      function: truthy\n"
source_yaml_url: https://raw.githubusercontent.com/api-evangelist/apache-event-mesh/refs/heads/main/rules/apache-event-mesh-spectral-rules.yml
tags:
- Apache
- CloudEvents
- Event-Driven
- Messaging
- Open Source
- Pub-Sub
- Serverless
- Spectral
- Linting
- API Governance
---
