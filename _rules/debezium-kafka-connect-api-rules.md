---
api_specs:
- filename: debezium-connect.yml
  format: yaml
  label: Debezium Kafka Connect REST API
  slug: debezium-kafka-connect-api
  spec_type: OpenAPI
  url: https://raw.githubusercontent.com/api-evangelist/debezium/refs/heads/main/openapi/debezium-connect.yml
categories:
- debezium
description: Spectral linting rules defining API design standards and conventions for Debezium.
layout: rules
name: Debezium API Rules
provider_name: Debezium
provider_slug: debezium
rule_count: 5
rules:
- description: API info should include the Apache 2.0 license used by Debezium.
  given: $.info
  name: debezium-info-license
  severity: warn
- description: Servers should reference a Kafka Connect worker (default port 8083).
  given: $.servers[*].url
  name: debezium-connect-base-url
  severity: warn
- description: API should expose /connectors as a primary resource path.
  given: $.paths
  name: debezium-connectors-resource
  severity: error
- description: Connector resources should expose tasks management.
  given: $.paths
  name: debezium-connector-tasks
  severity: warn
- description: Operations should be tagged Connectors, Tasks, Cluster, or Topics.
  given: $.paths[*][*]
  name: debezium-operation-tags
  severity: warn
rules_file: rules/debezium-kafka-connect-api-rules.yml
rules_url: https://raw.githubusercontent.com/api-evangelist/debezium/refs/heads/main/rules/debezium-kafka-connect-api-rules.yml
severity_counts:
  error: 1
  hint: 0
  info: 0
  warn: 4
slug: debezium-kafka-connect-api-rules
source_filename: debezium-kafka-connect-api-rules.yml
source_heading: Spectral Ruleset
source_yaml: "extends:\n  - spectral:oas\nrules:\n  debezium-info-license:\n    description: API info should include the Apache 2.0 license used by Debezium.\n    given: $.info\n    severity: warn\n    then:\n      field: license\n      function: truthy\n  debezium-connect-base-url:\n    description: Servers should reference a Kafka Connect worker (default port 8083).\n    given: $.servers[*].url\n    severity: warn\n    then:\n      function: pattern\n      functionOptions:\n        match: \"8083\"\n  debezium-connectors-resource:\n    description: API should expose /connectors as a primary resource path.\n    given: $.paths\n    severity: error\n    then:\n      function: pattern\n      functionOptions:\n        match: \"/connectors\"\n  debezium-connector-tasks:\n    description: Connector resources should expose tasks management.\n    given: $.paths\n    severity: warn\n    then:\n      function: pattern\n      functionOptions:\n        match: \"/tasks\"\n  debezium-operation-tags:\n\
  \    description: Operations should be tagged Connectors, Tasks, Cluster, or Topics.\n    given: $.paths[*][*]\n    severity: warn\n    then:\n      field: tags\n      function: truthy\n"
source_yaml_url: https://raw.githubusercontent.com/api-evangelist/debezium/refs/heads/main/rules/debezium-kafka-connect-api-rules.yml
tags:
- Apache Kafka
- CDC
- Change Data Capture
- Databases
- Event Streaming
- Open Source
- Spectral
- Linting
- API Governance
---
