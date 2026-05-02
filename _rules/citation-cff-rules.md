---
categories:
- cff
description: Spectral linting rules defining API design standards and conventions for Citation File Format.
layout: rules
name: Citation File Format API Rules
provider_name: Citation File Format
provider_slug: citation-cff
rule_count: 10
rules:
- description: A CITATION.cff file MUST declare a cff-version field.
  given: '#CitationCff'
  name: cff-version-required
  severity: error
- description: cff-version SHOULD be 1.2.0 to use the current schema.
  given: '#CitationCff.cff-version'
  name: cff-version-current
  severity: warn
- description: A CITATION.cff file MUST contain a message field.
  given: '#CitationCff'
  name: cff-message-required
  severity: error
- description: A CITATION.cff file MUST contain a title field.
  given: '#CitationCff'
  name: cff-title-required
  severity: error
- description: A CITATION.cff file MUST contain at least one author.
  given: '#CitationCff'
  name: cff-authors-required
  severity: error
- description: A CITATION.cff file SHOULD declare a DOI for citable releases.
  given: '#CitationCff'
  name: cff-doi-recommended
  severity: warn
- description: A CITATION.cff file SHOULD declare a software version.
  given: '#CitationCff'
  name: cff-version-recommended
  severity: warn
- description: A CITATION.cff file SHOULD declare a date-released.
  given: '#CitationCff'
  name: cff-date-released-recommended
  severity: warn
- description: A CITATION.cff file SHOULD declare an SPDX license identifier.
  given: '#CitationCff'
  name: cff-license-recommended
  severity: warn
- description: A CITATION.cff file SHOULD declare a repository-code URL.
  given: '#CitationCff'
  name: cff-repository-recommended
  severity: warn
rules_file: rules/citation-cff-rules.yml
rules_url: https://raw.githubusercontent.com/api-evangelist/citation-cff/refs/heads/main/rules/citation-cff-rules.yml
severity_counts:
  error: 4
  hint: 0
  info: 0
  warn: 6
slug: citation-cff-rules
source_filename: citation-cff-rules.yml
source_heading: Spectral Ruleset
source_yaml: "aliases:\n  CitationCff:\n    - \"$\"\nrules:\n  cff-version-required:\n    description: A CITATION.cff file MUST declare a cff-version field.\n    severity: error\n    given: \"#CitationCff\"\n    then:\n      field: cff-version\n      function: truthy\n  cff-version-current:\n    description: cff-version SHOULD be 1.2.0 to use the current schema.\n    severity: warn\n    given: \"#CitationCff.cff-version\"\n    then:\n      function: pattern\n      functionOptions:\n        match: \"^1\\\\.2\\\\.0$\"\n  cff-message-required:\n    description: A CITATION.cff file MUST contain a message field.\n    severity: error\n    given: \"#CitationCff\"\n    then:\n      field: message\n      function: truthy\n  cff-title-required:\n    description: A CITATION.cff file MUST contain a title field.\n    severity: error\n    given: \"#CitationCff\"\n    then:\n      field: title\n      function: truthy\n  cff-authors-required:\n    description: A CITATION.cff file MUST contain at least one\
  \ author.\n    severity: error\n    given: \"#CitationCff\"\n    then:\n      field: authors\n      function: truthy\n  cff-doi-recommended:\n    description: A CITATION.cff file SHOULD declare a DOI for citable releases.\n    severity: warn\n    given: \"#CitationCff\"\n    then:\n      field: doi\n      function: truthy\n  cff-version-recommended:\n    description: A CITATION.cff file SHOULD declare a software version.\n    severity: warn\n    given: \"#CitationCff\"\n    then:\n      field: version\n      function: truthy\n  cff-date-released-recommended:\n    description: A CITATION.cff file SHOULD declare a date-released.\n    severity: warn\n    given: \"#CitationCff\"\n    then:\n      field: date-released\n      function: truthy\n  cff-license-recommended:\n    description: A CITATION.cff file SHOULD declare an SPDX license identifier.\n    severity: warn\n    given: \"#CitationCff\"\n    then:\n      field: license\n      function: truthy\n  cff-repository-recommended:\n    description:\
  \ A CITATION.cff file SHOULD declare a repository-code URL.\n    severity: warn\n    given: \"#CitationCff\"\n    then:\n      field: repository-code\n      function: truthy\n"
source_yaml_url: https://raw.githubusercontent.com/api-evangelist/citation-cff/refs/heads/main/rules/citation-cff-rules.yml
tags:
- Academic
- Citation
- Metadata
- Open Standard
- Repository
- Research
- Software
- YAML
- Spectral
- Linting
- API Governance
---
