---
categories:
- dab
description: Spectral linting rules defining API design standards and conventions for Databricks Asset Bundles.
layout: rules
name: Databricks Asset Bundles API Rules
provider_name: Databricks Asset Bundles
provider_slug: databricks-asset-bundles
rule_count: 5
rules:
- description: Bundle root must include a bundle block with a name.
  given: $
  name: dab-bundle-required
  severity: error
- description: Target mode must be development or production.
  given: $.targets[*].mode
  name: dab-target-mode-enum
  severity: warn
- description: Workspace root_path should begin with /Workspace or /Volumes.
  given: $.workspace.root_path
  name: dab-workspace-root-path
  severity: warn
- description: Permission levels must be CAN_VIEW, CAN_RUN, CAN_MANAGE, or IS_OWNER.
  given: $.permissions[*].level
  name: dab-permission-level-enum
  severity: error
- description: Only one target may be marked default true.
  given: $.targets
  name: dab-single-default-target
  severity: warn
rules_file: rules/databricks-asset-bundles-rules.yml
rules_url: https://raw.githubusercontent.com/api-evangelist/databricks-asset-bundles/refs/heads/main/rules/databricks-asset-bundles-rules.yml
severity_counts:
  error: 2
  hint: 0
  info: 0
  warn: 3
slug: databricks-asset-bundles-rules
source_filename: databricks-asset-bundles-rules.yml
source_heading: Spectral Ruleset
source_yaml: "extends:\n  - spectral:oas\nrules:\n  dab-bundle-required:\n    description: Bundle root must include a bundle block with a name.\n    given: $\n    severity: error\n    then:\n      field: bundle\n      function: truthy\n  dab-target-mode-enum:\n    description: Target mode must be development or production.\n    given: $.targets[*].mode\n    severity: warn\n    then:\n      function: enumeration\n      functionOptions:\n        values:\n          - development\n          - production\n  dab-workspace-root-path:\n    description: Workspace root_path should begin with /Workspace or /Volumes.\n    given: $.workspace.root_path\n    severity: warn\n    then:\n      function: pattern\n      functionOptions:\n        match: \"^/Workspace|^/Volumes\"\n  dab-permission-level-enum:\n    description: Permission levels must be CAN_VIEW, CAN_RUN, CAN_MANAGE, or IS_OWNER.\n    given: $.permissions[*].level\n    severity: error\n    then:\n      function: enumeration\n      functionOptions:\n\
  \        values:\n          - CAN_VIEW\n          - CAN_RUN\n          - CAN_MANAGE\n          - IS_OWNER\n  dab-single-default-target:\n    description: Only one target may be marked default true.\n    given: $.targets\n    severity: warn\n    then:\n      function: truthy\n"
source_yaml_url: https://raw.githubusercontent.com/api-evangelist/databricks-asset-bundles/refs/heads/main/rules/databricks-asset-bundles-rules.yml
tags:
- CI/CD
- Data Engineering
- Databricks
- Deployment
- Infrastructure as Code
- Jobs
- Machine Learning
- MLOps
- Pipelines
- Workflows
- Spectral
- Linting
- API Governance
---
