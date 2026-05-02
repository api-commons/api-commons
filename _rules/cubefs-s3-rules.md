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
rule_count: 3
rules:
- description: CubeFS S3 spec must declare a server.
  given: $.servers
  name: cubefs-s3-server-defined
  severity: error
- description: S3 bucket-scoped operations must include {Bucket} path parameter.
  given: $.paths
  name: cubefs-s3-bucket-path
  severity: warn
- description: S3 operations must declare a tag (Buckets, Objects, Multipart, Acl).
  given: $.paths[*][get,post,put,delete,head]
  name: cubefs-s3-tag-required
  severity: warn
rules_file: rules/cubefs-s3-rules.yml
rules_url: https://raw.githubusercontent.com/api-evangelist/cubefs/refs/heads/main/rules/cubefs-s3-rules.yml
severity_counts:
  error: 1
  hint: 0
  info: 0
  warn: 2
slug: cubefs-s3-rules
source_filename: cubefs-s3-rules.yml
source_heading: Spectral Ruleset
source_yaml: "extends: [[spectral:oas, all]]\nrules:\n  cubefs-s3-server-defined:\n    description: CubeFS S3 spec must declare a server.\n    given: $.servers\n    severity: error\n    then:\n      function: truthy\n  cubefs-s3-bucket-path:\n    description: S3 bucket-scoped operations must include {Bucket} path parameter.\n    given: $.paths\n    severity: warn\n    then:\n      function: schema\n      functionOptions:\n        schema:\n          type: object\n          patternProperties:\n            \"^/(\\\\{Bucket\\\\}|)\":\n              type: object\n  cubefs-s3-tag-required:\n    description: S3 operations must declare a tag (Buckets, Objects, Multipart, Acl).\n    given: $.paths[*][get,post,put,delete,head]\n    severity: warn\n    then:\n      field: tags\n      function: truthy\n"
source_yaml_url: https://raw.githubusercontent.com/api-evangelist/cubefs/refs/heads/main/rules/cubefs-s3-rules.yml
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
