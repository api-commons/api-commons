---
api_specs:
- filename: crossref-openapi.yml
  format: yaml
  label: Crossref REST API
  slug: crossref-rest-api
  spec_type: OpenAPI
  url: https://raw.githubusercontent.com/api-evangelist/crossref/refs/heads/main/openapi/crossref-openapi.yml
categories:
- crossref
description: Spectral linting rules defining API design standards and conventions for Crossref.
layout: rules
name: Crossref API Rules
provider_name: Crossref
provider_slug: crossref
rule_count: 6
rules:
- description: API info object should reference Crossref contact.
  given: $.info.contact
  name: crossref-info-contact
  severity: error
- description: API must define core entity collections used across the platform.
  given: $.paths
  name: crossref-required-paths
  severity: error
- description: API must define lookup paths for individual DOIs and agency.
  given: $.paths
  name: crossref-doi-paths
  severity: error
- description: All operations must define an operationId.
  given: $.paths.*.*
  name: crossref-operation-id
  severity: error
- description: All operations must define tags.
  given: $.paths.*.*
  name: crossref-tags
  severity: error
- description: Works endpoints should be tagged with Works.
  given: $.paths['/works','/works/{doi}'].get.tags
  name: crossref-works-tag
  severity: warn
rules_file: rules/crossref-rules.yml
rules_url: https://raw.githubusercontent.com/api-evangelist/crossref/refs/heads/main/rules/crossref-rules.yml
severity_counts:
  error: 5
  hint: 0
  info: 0
  warn: 1
slug: crossref-rules
source_filename: crossref-rules.yml
source_heading: Spectral Ruleset
source_yaml: "extends: [\"spectral:oas\"]\ndocumentationUrl: https://www.crossref.org/documentation/retrieve-metadata/rest-api/\nrules:\n  crossref-info-contact:\n    description: API info object should reference Crossref contact.\n    given: \"$.info.contact\"\n    severity: error\n    then:\n      field: url\n      function: pattern\n      functionOptions:\n        match: \"crossref\"\n  crossref-required-paths:\n    description: API must define core entity collections used across the platform.\n    given: \"$.paths\"\n    severity: error\n    then:\n      function: schema\n      functionOptions:\n        schema:\n          type: object\n          required:\n            - /works\n            - /journals\n            - /members\n            - /funders\n            - /types\n            - /licenses\n            - /prefixes\n  crossref-doi-paths:\n    description: API must define lookup paths for individual DOIs and agency.\n    given: \"$.paths\"\n    severity: error\n    then:\n      function:\
  \ schema\n      functionOptions:\n        schema:\n          type: object\n          required:\n            - /works/{doi}\n            - /works/{doi}/agency\n  crossref-operation-id:\n    description: All operations must define an operationId.\n    given: \"$.paths.*.*\"\n    severity: error\n    then:\n      field: operationId\n      function: truthy\n  crossref-tags:\n    description: All operations must define tags.\n    given: \"$.paths.*.*\"\n    severity: error\n    then:\n      field: tags\n      function: truthy\n  crossref-works-tag:\n    description: Works endpoints should be tagged with Works.\n    given: \"$.paths['/works','/works/{doi}'].get.tags\"\n    severity: warn\n    then:\n      function: schema\n      functionOptions:\n        schema:\n          type: array\n          contains:\n            const: Works\n"
source_yaml_url: https://raw.githubusercontent.com/api-evangelist/crossref/refs/heads/main/rules/crossref-rules.yml
tags:
- Citations
- DOI
- Funders
- Identifiers
- Journals
- Licenses
- Members
- Metadata
- Open Access
- ORCID
- Prefixes
- Publishers
- Reference Linking
- ROR
- Scholarly
- Spectral
- Linting
- API Governance
---
