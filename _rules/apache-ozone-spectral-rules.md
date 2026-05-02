---
api_specs:
- filename: apache-ozone-s3-api.yaml
  format: yaml
  label: Apache Ozone
  slug: apache-ozone
  spec_type: OpenAPI
  url: https://raw.githubusercontent.com/api-evangelist/apache-ozone/refs/heads/main/openapi/apache-ozone-s3-api.yaml
categories:
- info
- operation
- paths
- security
description: Spectral linting rules defining API design standards and conventions for Apache Ozone.
layout: rules
name: Apache Ozone API Rules
provider_name: Apache Ozone
provider_slug: apache-ozone
rule_count: 6
rules:
- description: API must have a title
  given: $.info
  name: info-title-required
  severity: error
- description: ''
  given: $.paths[*][*]
  name: operation-summary-required
  severity: error
- description: ''
  given: $.paths[*][*]
  name: operation-operationId-required
  severity: error
- description: Summaries should start with Apache Ozone
  given: $.paths[*][get,post,put,delete,patch,head].summary
  name: operation-summary-apache-prefix
  severity: info
- description: Paths should follow S3 bucket/key pattern
  given: $.paths[*]~
  name: paths-s3-compatible
  severity: info
- description: S3 API should use AWS Signature authentication
  given: $.info
  name: security-s3-auth
  severity: warn
rules_file: rules/apache-ozone-spectral-rules.yml
rules_url: https://raw.githubusercontent.com/api-evangelist/apache-ozone/refs/heads/main/rules/apache-ozone-spectral-rules.yml
severity_counts:
  error: 3
  hint: 0
  info: 2
  warn: 1
slug: apache-ozone-spectral-rules
source_filename: apache-ozone-spectral-rules.yml
source_heading: Spectral Ruleset
source_yaml: "extends: \"spectral:oas\"\nrules:\n  info-title-required:\n    description: \"API must have a title\"\n    severity: error\n    given: \"$.info\"\n    then:\n      field: title\n      function: truthy\n  operation-summary-required:\n    severity: error\n    given: \"$.paths[*][*]\"\n    then:\n      field: summary\n      function: truthy\n  operation-operationId-required:\n    severity: error\n    given: \"$.paths[*][*]\"\n    then:\n      field: operationId\n      function: truthy\n  operation-summary-apache-prefix:\n    description: \"Summaries should start with Apache Ozone\"\n    severity: info\n    given: \"$.paths[*][get,post,put,delete,patch,head].summary\"\n    then:\n      function: pattern\n      functionOptions:\n        match: \"^Apache Ozone\"\n  paths-s3-compatible:\n    description: \"Paths should follow S3 bucket/key pattern\"\n    severity: info\n    given: \"$.paths[*]~\"\n    then:\n      function: pattern\n      functionOptions:\n        match: \"^/[{a-z]\"\
  \n  security-s3-auth:\n    description: \"S3 API should use AWS Signature authentication\"\n    severity: warn\n    given: \"$.info\"\n    then:\n      field: description\n      function: truthy\n"
source_yaml_url: https://raw.githubusercontent.com/api-evangelist/apache-ozone/refs/heads/main/rules/apache-ozone-spectral-rules.yml
tags:
- Distributed Storage
- Hadoop
- Object Storage
- S3-Compatible
- Apache
- Open Source
- Spectral
- Linting
- API Governance
---
