---
api_specs:
- filename: cubefs-s3-api-openapi.yml
  format: yaml
  label: CubeFS S3-Compatible API
  slug: cubefs-s3-api
  spec_type: OpenAPI
  url: https://raw.githubusercontent.com/api-evangelist/cubefs/refs/heads/main/openapi/cubefs-s3-api-openapi.yml
- filename: cubefs-master-api-openapi.yml
  format: yaml
  label: CubeFS Master API
  slug: cubefs-master-api
  spec_type: OpenAPI
  url: https://raw.githubusercontent.com/api-evangelist/cubefs/refs/heads/main/openapi/cubefs-master-api-openapi.yml
categories:
- cubefs
description: Spectral linting rules defining API design standards and conventions for CubeFS.
layout: rules
name: CubeFS API Rules
provider_name: CubeFS
provider_slug: cubefs
rule_count: 6
rules:
- description: CubeFS API specs must declare a contact.
  given: $.info
  name: cubefs-info-contact
  severity: warn
- description: CubeFS specs must declare at least one server.
  given: $.servers
  name: cubefs-server-defined
  severity: error
- description: Volume admin endpoints should be under /admin or /vol prefix.
  given: $.paths
  name: cubefs-master-volume-paths
  severity: warn
- description: Operations must declare a tag.
  given: $.paths[*][get,post,put,delete]
  name: cubefs-tag-required
  severity: warn
- description: Operation IDs should be camelCase.
  given: $.paths[*][get,post,put,delete].operationId
  name: cubefs-operation-id-camel
  severity: warn
- description: Volume create/update operations must require a vol name parameter.
  given: $.paths[?(@property.match(/admin\/(createVol|getVol)|vol\/(update|delete|expand)/))][post,get,delete].parameters[*].name
  name: cubefs-cluster-admin-name-required
  severity: warn
rules_file: rules/cubefs-master-rules.yml
rules_url: https://raw.githubusercontent.com/api-evangelist/cubefs/refs/heads/main/rules/cubefs-master-rules.yml
severity_counts:
  error: 1
  hint: 0
  info: 0
  warn: 5
slug: cubefs-master-rules
source_filename: cubefs-master-rules.yml
source_heading: Spectral Ruleset
source_yaml: "extends: [[spectral:oas, all]]\nrules:\n  cubefs-info-contact:\n    description: CubeFS API specs must declare a contact.\n    given: $.info\n    severity: warn\n    then:\n      field: contact\n      function: truthy\n  cubefs-server-defined:\n    description: CubeFS specs must declare at least one server.\n    given: $.servers\n    severity: error\n    then:\n      function: truthy\n  cubefs-master-volume-paths:\n    description: Volume admin endpoints should be under /admin or /vol prefix.\n    given: $.paths\n    severity: warn\n    then:\n      function: schema\n      functionOptions:\n        schema:\n          type: object\n          patternProperties:\n            \"^/(admin|vol|cluster|dataNode|metaNode|user|s3|disk|partition|raft)/\":\n              type: object\n          additionalProperties: false\n  cubefs-tag-required:\n    description: Operations must declare a tag.\n    given: $.paths[*][get,post,put,delete]\n    severity: warn\n    then:\n      field: tags\n\
  \      function: truthy\n  cubefs-operation-id-camel:\n    description: Operation IDs should be camelCase.\n    given: $.paths[*][get,post,put,delete].operationId\n    severity: warn\n    then:\n      function: pattern\n      functionOptions:\n        match: '^[a-z][a-zA-Z0-9]+$'\n  cubefs-cluster-admin-name-required:\n    description: Volume create/update operations must require a vol name parameter.\n    given: $.paths[?(@property.match(/admin\\/(createVol|getVol)|vol\\/(update|delete|expand)/))][post,get,delete].parameters[*].name\n    severity: warn\n    then:\n      function: pattern\n      functionOptions:\n        match: '^(name|authKey|capacity|owner|mpCount|replicaNum|crossZone|enableToken|description)$'\n"
source_yaml_url: https://raw.githubusercontent.com/api-evangelist/cubefs/refs/heads/main/rules/cubefs-master-rules.yml
tags:
- Cloud Native
- CNCF Graduated
- Distributed File System
- Kubernetes
- Object Storage
- POSIX
- S3 Compatible
- Storage
- Spectral
- Linting
- API Governance
---
