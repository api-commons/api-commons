---
api_specs:
- filename: apache-shiro-rest-api.yaml
  format: yaml
  label: Apache Shiro
  slug: apache-shiro
  spec_type: OpenAPI
  url: https://raw.githubusercontent.com/api-evangelist/apache-shiro/refs/heads/main/openapi/apache-shiro-rest-api.yaml
categories:
- apache
description: Spectral linting rules defining API design standards and conventions for Apache Shiro.
layout: rules
name: Apache Shiro API Rules
provider_name: Apache Shiro
provider_slug: apache-shiro
rule_count: 6
rules:
- description: Info object must have a title
  given: $.info
  name: apache-shiro-info-title-required
  severity: error
- description: All operations must have a summary
  given: $.paths[*][*]
  name: apache-shiro-operation-summary-required
  severity: error
- description: All operations must have an operationId
  given: $.paths[*][*]
  name: apache-shiro-operation-operationId-required
  severity: error
- description: All operations must have tags
  given: $.paths[*][*]
  name: apache-shiro-operation-tags-required
  severity: warn
- description: Operation summaries should be prefixed with Apache Shiro
  given: $.paths[*][*].summary
  name: apache-shiro-operation-summary-apache-prefix
  severity: warn
- description: All operations must have a success response
  given: $.paths[*][*].responses
  name: apache-shiro-response-success-required
  severity: error
rules_file: rules/apache-shiro-spectral-rules.yml
rules_url: https://raw.githubusercontent.com/api-evangelist/apache-shiro/refs/heads/main/rules/apache-shiro-spectral-rules.yml
severity_counts:
  error: 4
  hint: 0
  info: 0
  warn: 2
slug: apache-shiro-spectral-rules
source_filename: apache-shiro-spectral-rules.yml
source_heading: Spectral Ruleset
source_yaml: "rules:\n  apache-shiro-info-title-required:\n    description: Info object must have a title\n    message: API must have a title in the info object\n    severity: error\n    given: $.info\n    then:\n      field: title\n      function: truthy\n  apache-shiro-operation-summary-required:\n    description: All operations must have a summary\n    message: Operation must have a summary\n    severity: error\n    given: $.paths[*][*]\n    then:\n      field: summary\n      function: truthy\n  apache-shiro-operation-operationId-required:\n    description: All operations must have an operationId\n    message: Operation must have an operationId\n    severity: error\n    given: $.paths[*][*]\n    then:\n      field: operationId\n      function: truthy\n  apache-shiro-operation-tags-required:\n    description: All operations must have tags\n    message: Operation must have at least one tag\n    severity: warn\n    given: $.paths[*][*]\n    then:\n      field: tags\n      function: truthy\n\
  \  apache-shiro-operation-summary-apache-prefix:\n    description: Operation summaries should be prefixed with Apache Shiro\n    message: Summary should start with \"Apache Shiro\"\n    severity: warn\n    given: $.paths[*][*].summary\n    then:\n      function: pattern\n      functionOptions:\n        match: \"^Apache Shiro\"\n  apache-shiro-response-success-required:\n    description: All operations must have a success response\n    message: Operation must define a 2xx response\n    severity: error\n    given: $.paths[*][*].responses\n    then:\n      function: schema\n      functionOptions:\n        schema:\n          anyOf:\n            - required: [\"200\"]\n            - required: [\"201\"]\n            - required: [\"204\"]\n"
source_yaml_url: https://raw.githubusercontent.com/api-evangelist/apache-shiro/refs/heads/main/rules/apache-shiro-spectral-rules.yml
tags:
- Authentication
- Authorization
- Cryptography
- Java
- Security
- Apache
- Open Source
- Spectral
- Linting
- API Governance
---
