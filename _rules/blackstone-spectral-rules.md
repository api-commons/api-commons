---
categories:
- blackstone
description: Spectral linting rules defining API design standards and conventions for Blackstone.
layout: rules
name: Blackstone API Rules
provider_name: Blackstone
provider_slug: blackstone
rule_count: 5
rules:
- description: Fund strategy must be one of the defined values
  given: $.components.schemas.Fund.properties.strategy
  name: blackstone-fund-strategy-enum
  severity: warn
- description: Financial records must include a currency field
  given: $.components.schemas[*].properties
  name: blackstone-currency-required
  severity: warn
- description: Date fields must use ISO 8601 format
  given: $.components.schemas[*].properties[?(@.description =~ /date/i)]
  name: blackstone-date-iso-format
  severity: warn
- description: All API operations should include descriptions
  given: $.paths[*][*]
  name: blackstone-operations-have-descriptions
  severity: warn
- description: All ID fields should be of type string
  given: $.components.schemas[*].properties[?(@.description =~ /identifier|id/i)]
  name: blackstone-ids-are-strings
  severity: warn
rules_file: rules/blackstone-spectral-rules.yml
rules_url: https://raw.githubusercontent.com/api-evangelist/blackstone/refs/heads/main/rules/blackstone-spectral-rules.yml
severity_counts:
  error: 0
  hint: 0
  info: 0
  warn: 5
slug: blackstone-spectral-rules
source_filename: blackstone-spectral-rules.yml
source_heading: Spectral Ruleset
source_yaml: "rules:\n  blackstone-fund-strategy-enum:\n    description: Fund strategy must be one of the defined values\n    message: \"Fund strategy must use a defined enum value\"\n    given: \"$.components.schemas.Fund.properties.strategy\"\n    then:\n      field: enum\n      function: truthy\n\n  blackstone-currency-required:\n    description: Financial records must include a currency field\n    message: \"Currency is required on financial records\"\n    given: \"$.components.schemas[*].properties\"\n    then:\n      field: currency\n      function: defined\n\n  blackstone-date-iso-format:\n    description: Date fields must use ISO 8601 format\n    message: \"Date fields must specify format: date or date-time\"\n    given: \"$.components.schemas[*].properties[?(@.description =~ /date/i)]\"\n    then:\n      field: format\n      function: pattern\n      functionOptions:\n        match: \"^date\"\n\n  blackstone-operations-have-descriptions:\n    description: All API operations should\
  \ include descriptions\n    message: \"Operation is missing a description\"\n    given: \"$.paths[*][*]\"\n    then:\n      field: description\n      function: truthy\n\n  blackstone-ids-are-strings:\n    description: All ID fields should be of type string\n    message: \"ID fields must be of type string\"\n    given: \"$.components.schemas[*].properties[?(@.description =~ /identifier|id/i)]\"\n    then:\n      field: type\n      function: pattern\n      functionOptions:\n        match: \"^string$\"\n"
source_yaml_url: https://raw.githubusercontent.com/api-evangelist/blackstone/refs/heads/main/rules/blackstone-spectral-rules.yml
tags:
- Alternative Assets
- Finance
- Investment Management
- Private Equity
- Real Estate
- Spectral
- Linting
- API Governance
---
