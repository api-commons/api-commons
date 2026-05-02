---
api_specs:
- filename: axon-server-api.yml
  format: yaml
  label: Axon Framework
  slug: axon-framework
  spec_type: OpenAPI
  url: https://raw.githubusercontent.com/api-evangelist/axon-framework/refs/heads/main/openapi/axon-server-api.yml
categories:
- axon
description: Spectral linting rules defining API design standards and conventions for Axon Framework.
layout: rules
name: Axon Framework API Rules
provider_name: Axon Framework
provider_slug: axon-framework
rule_count: 5
rules:
- description: All operations must have a summary starting with "Axon Framework"
  given: $.paths[*][get,post,put,delete,patch]
  name: axon-operation-summary
  severity: warn
- description: All operations must have an operationId
  given: $.paths[*][get,post,put,delete,patch]
  name: axon-operation-id
  severity: error
- description: Info object must have a title
  given: $.info
  name: axon-info-title
  severity: error
- description: All responses must have a description
  given: $.paths[*][*].responses[*]
  name: axon-response-description
  severity: error
- description: Operations should have x-microcks-operation annotation
  given: $.paths[*][get,post,put,delete,patch]
  name: axon-microcks-annotation
  severity: info
rules_file: rules/axon-framework-spectral-rules.yml
rules_url: https://raw.githubusercontent.com/api-evangelist/axon-framework/refs/heads/main/rules/axon-framework-spectral-rules.yml
severity_counts:
  error: 3
  hint: 0
  info: 1
  warn: 1
slug: axon-framework-spectral-rules
source_filename: axon-framework-spectral-rules.yml
source_heading: Spectral Ruleset
source_yaml: "rules:\n  axon-operation-summary:\n    description: All operations must have a summary starting with \"Axon Framework\"\n    severity: warn\n    given: \"$.paths[*][get,post,put,delete,patch]\"\n    then:\n      field: summary\n      function: pattern\n      functionOptions:\n        match: \"^Axon Framework\"\n  axon-operation-id:\n    description: All operations must have an operationId\n    severity: error\n    given: \"$.paths[*][get,post,put,delete,patch]\"\n    then:\n      field: operationId\n      function: truthy\n  axon-info-title:\n    description: Info object must have a title\n    severity: error\n    given: \"$.info\"\n    then:\n      field: title\n      function: truthy\n  axon-response-description:\n    description: All responses must have a description\n    severity: error\n    given: \"$.paths[*][*].responses[*]\"\n    then:\n      field: description\n      function: truthy\n  axon-microcks-annotation:\n    description: Operations should have x-microcks-operation\
  \ annotation\n    severity: info\n    given: \"$.paths[*][get,post,put,delete,patch]\"\n    then:\n      field: x-microcks-operation\n      function: truthy\n"
source_yaml_url: https://raw.githubusercontent.com/api-evangelist/axon-framework/refs/heads/main/rules/axon-framework-spectral-rules.yml
tags:
- CQRS
- Event Sourcing
- Event-Driven
- Java
- Messaging
- Microservices
- Spectral
- Linting
- API Governance
---
