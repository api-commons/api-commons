---
categories:
- blobr
description: Spectral linting rules defining API design standards and conventions for Blobr.
layout: rules
name: Blobr API Rules
provider_name: Blobr
provider_slug: blobr
rule_count: 5
rules:
- description: Campaign status must use Google Ads enum values
  given: $.components.schemas.Campaign.properties.status
  name: blobr-campaign-status-enum
  severity: warn
- description: Recommendation priority must be high, medium, or low
  given: $.components.schemas.Recommendation.properties.priority
  name: blobr-recommendation-priority-enum
  severity: warn
- description: Recommendation status must use defined workflow states
  given: $.components.schemas.Recommendation.properties.status
  name: blobr-recommendation-status-enum
  severity: warn
- description: Budget amounts should use Google Ads micros format
  given: $.components.schemas.Campaign.properties.budget.properties.amountMicros
  name: blobr-budget-micros
  severity: warn
- description: Timestamp fields must use ISO 8601 date-time format
  given: $.components.schemas[*].properties[?(@.description =~ /timestamp|created|applied/i)]
  name: blobr-dates-iso8601
  severity: warn
rules_file: rules/blobr-spectral-rules.yml
rules_url: https://raw.githubusercontent.com/api-evangelist/blobr/refs/heads/main/rules/blobr-spectral-rules.yml
severity_counts:
  error: 0
  hint: 0
  info: 0
  warn: 5
slug: blobr-spectral-rules
source_filename: blobr-spectral-rules.yml
source_heading: Spectral Ruleset
source_yaml: "rules:\n  blobr-campaign-status-enum:\n    description: Campaign status must use Google Ads enum values\n    message: \"Campaign status must be ENABLED, PAUSED, or REMOVED\"\n    given: \"$.components.schemas.Campaign.properties.status\"\n    then:\n      field: enum\n      function: truthy\n\n  blobr-recommendation-priority-enum:\n    description: Recommendation priority must be high, medium, or low\n    message: \"Recommendation priority must use defined enum values\"\n    given: \"$.components.schemas.Recommendation.properties.priority\"\n    then:\n      field: enum\n      function: truthy\n\n  blobr-recommendation-status-enum:\n    description: Recommendation status must use defined workflow states\n    message: \"Status must be pending, approved, rejected, or applied\"\n    given: \"$.components.schemas.Recommendation.properties.status\"\n    then:\n      field: enum\n      function: truthy\n\n  blobr-budget-micros:\n    description: Budget amounts should use Google Ads\
  \ micros format\n    message: \"Budget amountMicros should be of type integer\"\n    given: \"$.components.schemas.Campaign.properties.budget.properties.amountMicros\"\n    then:\n      field: type\n      function: pattern\n      functionOptions:\n        match: \"^integer$\"\n\n  blobr-dates-iso8601:\n    description: Timestamp fields must use ISO 8601 date-time format\n    message: \"Date-time fields must specify format: date-time\"\n    given: \"$.components.schemas[*].properties[?(@.description =~ /timestamp|created|applied/i)]\"\n    then:\n      field: format\n      function: pattern\n      functionOptions:\n        match: \"^date-time$\"\n"
source_yaml_url: https://raw.githubusercontent.com/api-evangelist/blobr/refs/heads/main/rules/blobr-spectral-rules.yml
tags:
- Advertising
- AI Agents
- Google Ads
- Marketing Automation
- PPC
- Spectral
- Linting
- API Governance
---
