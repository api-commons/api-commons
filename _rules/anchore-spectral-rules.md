---
api_specs:
- filename: anchore-enterprise-api.yaml
  format: yaml
  label: Anchore Enterprise API
  slug: anchore-enterprise-api
  spec_type: OpenAPI
  url: https://raw.githubusercontent.com/api-evangelist/anchore/refs/heads/main/openapi/anchore-enterprise-api.yaml
categories:
- anchore
description: Spectral linting rules defining API design standards and conventions for Anchore.
layout: rules
name: Anchore API Rules
provider_name: Anchore
provider_slug: anchore
rule_count: 9
rules:
- description: OpenAPI info object must have a description
  given: $.info
  name: anchore-openapi-info-description
  severity: error
- description: OpenAPI info object must have a version
  given: $.info
  name: anchore-openapi-info-version
  severity: error
- description: Every operation must have an operationId
  given: $.paths[*][get,post,put,patch,delete]
  name: anchore-operation-operationId
  severity: error
- description: Every operation must have a summary
  given: $.paths[*][get,post,put,patch,delete]
  name: anchore-operation-summary
  severity: warn
- description: Every GET operation must have a 200 response
  given: $.paths[*].get.responses
  name: anchore-response-200
  severity: warn
- description: API must define security requirements
  given: $
  name: anchore-security-defined
  severity: error
- description: Schema properties must have a type
  given: $.components.schemas[*].properties[*]
  name: anchore-schema-type
  severity: warn
- description: Vulnerability severity must use standard values
  given: $.components.schemas.Vulnerability.properties.severity
  name: anchore-severity-enum
  severity: warn
- description: Image digest fields should follow SHA256 format
  given: $.components.schemas[*].properties.imageDigest
  name: anchore-digest-format
  severity: hint
rules_file: rules/anchore-spectral-rules.yml
rules_url: https://raw.githubusercontent.com/api-evangelist/anchore/refs/heads/main/rules/anchore-spectral-rules.yml
severity_counts:
  error: 4
  hint: 1
  info: 0
  warn: 4
slug: anchore-spectral-rules
source_filename: anchore-spectral-rules.yml
source_heading: Spectral Ruleset
source_yaml: "rules:\n  anchore-openapi-info-description:\n    description: OpenAPI info object must have a description\n    message: 'Info object must have a description'\n    given: '$.info'\n    severity: error\n    then:\n      field: description\n      function: truthy\n\n  anchore-openapi-info-version:\n    description: OpenAPI info object must have a version\n    message: 'Info object must have a version'\n    given: '$.info'\n    severity: error\n    then:\n      field: version\n      function: truthy\n\n  anchore-operation-operationId:\n    description: Every operation must have an operationId\n    message: 'Operation must have an operationId'\n    given: '$.paths[*][get,post,put,patch,delete]'\n    severity: error\n    then:\n      field: operationId\n      function: truthy\n\n  anchore-operation-summary:\n    description: Every operation must have a summary\n    message: 'Operation must have a summary'\n    given: '$.paths[*][get,post,put,patch,delete]'\n    severity: warn\n \
  \   then:\n      field: summary\n      function: truthy\n\n  anchore-response-200:\n    description: Every GET operation must have a 200 response\n    message: 'GET operations must define a 200 response'\n    given: '$.paths[*].get.responses'\n    severity: warn\n    then:\n      field: '200'\n      function: truthy\n\n  anchore-security-defined:\n    description: API must define security requirements\n    message: 'API must define global security'\n    given: '$'\n    severity: error\n    then:\n      field: security\n      function: truthy\n\n  anchore-schema-type:\n    description: Schema properties must have a type\n    message: 'Schema property must have a type'\n    given: '$.components.schemas[*].properties[*]'\n    severity: warn\n    then:\n      field: type\n      function: truthy\n\n  anchore-severity-enum:\n    description: Vulnerability severity must use standard values\n    message: 'Severity must be one of Critical, High, Medium, Low, Negligible, Unknown'\n    given: \"\
  $.components.schemas.Vulnerability.properties.severity\"\n    severity: warn\n    then:\n      function: truthy\n\n  anchore-digest-format:\n    description: Image digest fields should follow SHA256 format\n    message: 'imageDigest should be a string type'\n    given: \"$.components.schemas[*].properties.imageDigest\"\n    severity: hint\n    then:\n      field: type\n      function: truthy\n"
source_yaml_url: https://raw.githubusercontent.com/api-evangelist/anchore/refs/heads/main/rules/anchore-spectral-rules.yml
tags:
- Container Security
- Containers
- SBOM
- Software Supply Chain
- Vulnerability Scanning
- Spectral
- Linting
- API Governance
---
