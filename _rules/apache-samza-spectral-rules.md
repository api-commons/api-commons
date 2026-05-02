---
api_specs:
- filename: apache-samza-rest-api.yaml
  format: yaml
  label: Apache Samza
  slug: apache-samza
  spec_type: OpenAPI
  url: https://raw.githubusercontent.com/api-evangelist/apache-samza/refs/heads/main/openapi/apache-samza-rest-api.yaml
categories:
- apache
description: Spectral linting rules defining API design standards and conventions for Apache Samza.
layout: rules
name: Apache Samza API Rules
provider_name: Apache Samza
provider_slug: apache-samza
rule_count: 6
rules:
- description: Info object must have a title
  given: $.info
  name: apache-samza-info-title-required
  severity: error
- description: All operations must have a summary
  given: $.paths[*][*]
  name: apache-samza-operation-summary-required
  severity: error
- description: All operations must have an operationId
  given: $.paths[*][*]
  name: apache-samza-operation-operationId-required
  severity: error
- description: All operations must have tags
  given: $.paths[*][*]
  name: apache-samza-operation-tags-required
  severity: warn
- description: Operation summaries should be prefixed with Apache Samza
  given: $.paths[*][*].summary
  name: apache-samza-operation-summary-apache-prefix
  severity: warn
- description: All operations must have a success response
  given: $.paths[*][*].responses
  name: apache-samza-response-success-required
  severity: error
rules_file: rules/apache-samza-spectral-rules.yml
rules_url: https://raw.githubusercontent.com/api-evangelist/apache-samza/refs/heads/main/rules/apache-samza-spectral-rules.yml
severity_counts:
  error: 4
  hint: 0
  info: 0
  warn: 2
slug: apache-samza-spectral-rules
source_filename: apache-samza-spectral-rules.yml
source_heading: Spectral Ruleset
source_yaml: "rules:\n  apache-samza-info-title-required:\n    description: Info object must have a title\n    message: API must have a title in the info object\n    severity: error\n    given: $.info\n    then:\n      field: title\n      function: truthy\n  apache-samza-operation-summary-required:\n    description: All operations must have a summary\n    message: Operation must have a summary\n    severity: error\n    given: $.paths[*][*]\n    then:\n      field: summary\n      function: truthy\n  apache-samza-operation-operationId-required:\n    description: All operations must have an operationId\n    message: Operation must have an operationId\n    severity: error\n    given: $.paths[*][*]\n    then:\n      field: operationId\n      function: truthy\n  apache-samza-operation-tags-required:\n    description: All operations must have tags\n    message: Operation must have at least one tag\n    severity: warn\n    given: $.paths[*][*]\n    then:\n      field: tags\n      function: truthy\n\
  \  apache-samza-operation-summary-apache-prefix:\n    description: Operation summaries should be prefixed with Apache Samza\n    message: Summary should start with \"Apache Samza\"\n    severity: warn\n    given: $.paths[*][*].summary\n    then:\n      function: pattern\n      functionOptions:\n        match: \"^Apache Samza\"\n  apache-samza-response-success-required:\n    description: All operations must have a success response\n    message: Operation must define a 2xx response\n    severity: error\n    given: $.paths[*][*].responses\n    then:\n      function: schema\n      functionOptions:\n        schema:\n          anyOf:\n            - required: [\"200\"]\n            - required: [\"201\"]\n            - required: [\"204\"]\n"
source_yaml_url: https://raw.githubusercontent.com/api-evangelist/apache-samza/refs/heads/main/rules/apache-samza-spectral-rules.yml
tags:
- Big Data
- Hadoop
- Kafka
- Stream Processing
- Streaming
- Apache
- Open Source
- Spectral
- Linting
- API Governance
---
