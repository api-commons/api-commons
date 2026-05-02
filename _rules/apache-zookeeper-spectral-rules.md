---
api_specs:
- filename: zookeeper-admin-api.yml
  format: yaml
  label: Apache ZooKeeper Admin Server API
  slug: apache-zookeeper-admin-api
  spec_type: OpenAPI
  url: https://raw.githubusercontent.com/api-evangelist/apache-zookeeper/refs/heads/main/openapi/zookeeper-admin-api.yml
categories:
- info
- operation
- paths
- response
- servers
description: Spectral linting rules defining API design standards and conventions for Apache ZooKeeper.
layout: rules
name: Apache ZooKeeper API Rules
provider_name: Apache ZooKeeper
provider_slug: apache-zookeeper
rule_count: 10
rules:
- description: Info title is required
  given: $.info
  name: info-title-required
  severity: error
- description: API version is required
  given: $.info
  name: info-version-required
  severity: error
- description: Servers array must be defined
  given: $
  name: servers-required
  severity: error
- description: All operations must have a summary
  given: $.paths[*][get,post,put,patch,delete]
  name: operation-summary-required
  severity: error
- description: All operations must have an operationId
  given: $.paths[*][get,post,put,patch,delete]
  name: operation-operationid-required
  severity: error
- description: Operation summaries should start with "Apache ZooKeeper"
  given: $.paths[*][get,post,put,patch,delete].summary
  name: operation-summary-prefix
  severity: info
- description: Every operation should have at least one 2xx response
  given: $.paths[*][get,post,put,patch,delete].responses
  name: response-success-required
  severity: error
- description: All responses must have a description
  given: $.paths[*][get,post,put,patch,delete].responses[*]
  name: response-description-required
  severity: error
- description: All operations should have at least one tag
  given: $.paths[*][get,post,put,patch,delete]
  name: operation-tags-required
  severity: warn
- description: Path segments should use kebab-case or be simple command names
  given: $.paths[*]~
  name: paths-kebab-case
  severity: info
rules_file: rules/apache-zookeeper-spectral-rules.yml
rules_url: https://raw.githubusercontent.com/api-evangelist/apache-zookeeper/refs/heads/main/rules/apache-zookeeper-spectral-rules.yml
severity_counts:
  error: 7
  hint: 0
  info: 2
  warn: 1
slug: apache-zookeeper-spectral-rules
source_filename: apache-zookeeper-spectral-rules.yml
source_heading: Spectral Ruleset
source_yaml: "# Apache ZooKeeper API Spectral Rules\nrules:\n\n  info-title-required:\n    description: Info title is required\n    severity: error\n    given: \"$.info\"\n    then:\n      field: title\n      function: truthy\n\n  info-version-required:\n    description: API version is required\n    severity: error\n    given: \"$.info\"\n    then:\n      field: version\n      function: truthy\n\n  servers-required:\n    description: Servers array must be defined\n    severity: error\n    given: \"$\"\n    then:\n      field: servers\n      function: truthy\n\n  operation-summary-required:\n    description: All operations must have a summary\n    severity: error\n    given: \"$.paths[*][get,post,put,patch,delete]\"\n    then:\n      field: summary\n      function: truthy\n\n  operation-operationid-required:\n    description: All operations must have an operationId\n    severity: error\n    given: \"$.paths[*][get,post,put,patch,delete]\"\n    then:\n      field: operationId\n      function:\
  \ truthy\n\n  operation-summary-prefix:\n    description: Operation summaries should start with \"Apache ZooKeeper\"\n    severity: info\n    given: \"$.paths[*][get,post,put,patch,delete].summary\"\n    then:\n      function: pattern\n      functionOptions:\n        match: \"^Apache ZooKeeper\"\n\n  response-success-required:\n    description: Every operation should have at least one 2xx response\n    severity: error\n    given: \"$.paths[*][get,post,put,patch,delete].responses\"\n    then:\n      function: schema\n      functionOptions:\n        schema:\n          anyOf:\n            - required: ['200']\n            - required: ['201']\n            - required: ['204']\n\n  response-description-required:\n    description: All responses must have a description\n    severity: error\n    given: \"$.paths[*][get,post,put,patch,delete].responses[*]\"\n    then:\n      field: description\n      function: truthy\n\n  operation-tags-required:\n    description: All operations should have at least\
  \ one tag\n    severity: warn\n    given: \"$.paths[*][get,post,put,patch,delete]\"\n    then:\n      field: tags\n      function: truthy\n\n  paths-kebab-case:\n    description: Path segments should use kebab-case or be simple command names\n    severity: info\n    given: \"$.paths[*]~\"\n    then:\n      function: pattern\n      functionOptions:\n        match: \"^(/[a-z0-9_-]+)+$\"\n"
source_yaml_url: https://raw.githubusercontent.com/api-evangelist/apache-zookeeper/refs/heads/main/rules/apache-zookeeper-spectral-rules.yml
tags:
- Configuration Management
- Distributed Coordination
- Leader Election
- Service Discovery
- Open Source
- Spectral
- Linting
- API Governance
---
