---
api_specs:
- filename: apache-pdfbox-api.yaml
  format: yaml
  label: Apache PDFBox
  slug: apache-pdfbox
  spec_type: OpenAPI
  url: https://raw.githubusercontent.com/api-evangelist/apache-pdfbox/refs/heads/main/openapi/apache-pdfbox-api.yaml
categories:
- info
- operation
- paths
- response
description: Spectral linting rules defining API design standards and conventions for Apache PDFBox.
layout: rules
name: Apache PDFBox API Rules
provider_name: Apache PDFBox
provider_slug: apache-pdfbox
rule_count: 6
rules:
- description: ''
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
- description: Summaries should start with Apache PDFBox
  given: $.paths[*][get,post,put,delete,patch].summary
  name: operation-summary-apache-prefix
  severity: info
- description: Document paths should follow /documents pattern
  given: $.paths[*]~
  name: paths-document-resource
  severity: info
- description: ''
  given: $.paths[*][get,post,put].responses
  name: response-success-required
  severity: error
rules_file: rules/apache-pdfbox-spectral-rules.yml
rules_url: https://raw.githubusercontent.com/api-evangelist/apache-pdfbox/refs/heads/main/rules/apache-pdfbox-spectral-rules.yml
severity_counts:
  error: 4
  hint: 0
  info: 2
  warn: 0
slug: apache-pdfbox-spectral-rules
source_filename: apache-pdfbox-spectral-rules.yml
source_heading: Spectral Ruleset
source_yaml: "extends: \"spectral:oas\"\nrules:\n  info-title-required:\n    severity: error\n    given: \"$.info\"\n    then:\n      field: title\n      function: truthy\n  operation-summary-required:\n    severity: error\n    given: \"$.paths[*][*]\"\n    then:\n      field: summary\n      function: truthy\n  operation-operationId-required:\n    severity: error\n    given: \"$.paths[*][*]\"\n    then:\n      field: operationId\n      function: truthy\n  operation-summary-apache-prefix:\n    description: \"Summaries should start with Apache PDFBox\"\n    severity: info\n    given: \"$.paths[*][get,post,put,delete,patch].summary\"\n    then:\n      function: pattern\n      functionOptions:\n        match: \"^Apache PDFBox\"\n  paths-document-resource:\n    description: \"Document paths should follow /documents pattern\"\n    severity: info\n    given: \"$.paths[*]~\"\n    then:\n      function: pattern\n      functionOptions:\n        match: \"^/documents\"\n  response-success-required:\n\
  \    severity: error\n    given: \"$.paths[*][get,post,put].responses\"\n    then:\n      function: schema\n      functionOptions:\n        schema:\n          required: [\"200\"]\n"
source_yaml_url: https://raw.githubusercontent.com/api-evangelist/apache-pdfbox/refs/heads/main/rules/apache-pdfbox-spectral-rules.yml
tags:
- Document Processing
- Java
- PDF
- Text Extraction
- Apache
- Open Source
- Spectral
- Linting
- API Governance
---
