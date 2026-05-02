---
categories:
- dbos
description: Spectral linting rules defining API design standards and conventions for DBOS.
layout: rules
name: DBOS API Rules
provider_name: DBOS
provider_slug: dbos
rule_count: 5
rules:
- description: Workflow decorators should always carry an explicit name.
  given: $.components.schemas.Workflow.properties.name
  name: dbos-workflow-decorator-named
  severity: warn
- description: Step retries must have max_attempts and backoff_rate.
  given: $.components.schemas.Step
  name: dbos-step-retry-bounds
  severity: warn
- description: Transaction isolation level must be SERIALIZABLE, REPEATABLE READ, or READ COMMITTED.
  given: $.components.schemas.Transaction.properties.isolation_level
  name: dbos-transaction-isolation-enum
  severity: error
- description: Scheduled workflows must define a cron expression.
  given: $.components.schemas.Scheduled.properties.cron
  name: dbos-scheduled-cron
  severity: error
- description: API info should include a contact for the DBOS project.
  given: $.info
  name: dbos-info-contact
  severity: warn
rules_file: rules/dbos-rules.yml
rules_url: https://raw.githubusercontent.com/api-evangelist/dbos/refs/heads/main/rules/dbos-rules.yml
severity_counts:
  error: 2
  hint: 0
  info: 0
  warn: 3
slug: dbos-rules
source_filename: dbos-rules.yml
source_heading: Spectral Ruleset
source_yaml: "extends:\n  - spectral:oas\nrules:\n  dbos-workflow-decorator-named:\n    description: Workflow decorators should always carry an explicit name.\n    given: $.components.schemas.Workflow.properties.name\n    severity: warn\n    then:\n      function: truthy\n  dbos-step-retry-bounds:\n    description: Step retries must have max_attempts and backoff_rate.\n    given: $.components.schemas.Step\n    severity: warn\n    then:\n      field: properties\n      function: truthy\n  dbos-transaction-isolation-enum:\n    description: Transaction isolation level must be SERIALIZABLE, REPEATABLE READ, or READ COMMITTED.\n    given: $.components.schemas.Transaction.properties.isolation_level\n    severity: error\n    then:\n      field: enum\n      function: truthy\n  dbos-scheduled-cron:\n    description: Scheduled workflows must define a cron expression.\n    given: $.components.schemas.Scheduled.properties.cron\n    severity: error\n    then:\n      function: truthy\n  dbos-info-contact:\n\
  \    description: API info should include a contact for the DBOS project.\n    given: $.info\n    severity: warn\n    then:\n      field: contact\n      function: truthy\n"
source_yaml_url: https://raw.githubusercontent.com/api-evangelist/dbos/refs/heads/main/rules/dbos-rules.yml
tags:
- API Composition
- Durable Execution
- Postgres
- Queues
- Scheduled Jobs
- Workflow
- Spectral
- Linting
- API Governance
---
