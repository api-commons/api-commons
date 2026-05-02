---
api_specs:
- filename: dagster-external-assets-rest-api-openapi.yml
  format: yaml
  label: Dagster External Assets REST API
  slug: external-assets-rest-api
  spec_type: OpenAPI
  url: https://raw.githubusercontent.com/api-evangelist/dagster/refs/heads/main/openapi/dagster-external-assets-rest-api-openapi.yml
categories:
- dagster
description: Spectral linting rules defining API design standards and conventions for Dagster.
layout: rules
name: Dagster API Rules
provider_name: Dagster
provider_slug: dagster
rule_count: 5
rules:
- description: API info should provide a contact for the Dagster project.
  given: $.info
  name: dagster-info-contact
  severity: warn
- description: Materialization, check, and observation request bodies must require asset_key.
  given: $.components.schemas[?(@property == 'AssetMaterialization' || @property == 'AssetCheck' || @property == 'AssetObservation')]
  name: dagster-asset-key-required
  severity: error
- description: Asset check severity must be limited to WARN or ERROR.
  given: $.components.schemas.AssetCheck.properties.severity
  name: dagster-check-severity-enum
  severity: error
- description: Every operation should be tagged with Materializations, Checks, or Observations.
  given: $.paths[*][*]
  name: dagster-operation-tags
  severity: warn
- description: API should declare a Dagster-Cloud-Api-Token security scheme.
  given: $.components.securitySchemes
  name: dagster-cloud-token-scheme
  severity: warn
rules_file: rules/dagster-external-assets-rest-api-rules.yml
rules_url: https://raw.githubusercontent.com/api-evangelist/dagster/refs/heads/main/rules/dagster-external-assets-rest-api-rules.yml
severity_counts:
  error: 2
  hint: 0
  info: 0
  warn: 3
slug: dagster-external-assets-rest-api-rules
source_filename: dagster-external-assets-rest-api-rules.yml
source_heading: Spectral Ruleset
source_yaml: "extends:\n  - spectral:oas\nrules:\n  dagster-info-contact:\n    description: API info should provide a contact for the Dagster project.\n    given: $.info\n    severity: warn\n    then:\n      field: contact\n      function: truthy\n  dagster-asset-key-required:\n    description: Materialization, check, and observation request bodies must require asset_key.\n    given: $.components.schemas[?(@property == 'AssetMaterialization' || @property == 'AssetCheck' || @property == 'AssetObservation')]\n    severity: error\n    then:\n      field: required\n      function: truthy\n  dagster-check-severity-enum:\n    description: Asset check severity must be limited to WARN or ERROR.\n    given: $.components.schemas.AssetCheck.properties.severity\n    severity: error\n    then:\n      field: enum\n      function: truthy\n  dagster-operation-tags:\n    description: Every operation should be tagged with Materializations, Checks, or Observations.\n    given: $.paths[*][*]\n    severity:\
  \ warn\n    then:\n      field: tags\n      function: truthy\n  dagster-cloud-token-scheme:\n    description: API should declare a Dagster-Cloud-Api-Token security scheme.\n    given: $.components.securitySchemes\n    severity: warn\n    then:\n      field: DagsterCloudToken\n      function: truthy\n"
source_yaml_url: https://raw.githubusercontent.com/api-evangelist/dagster/refs/heads/main/rules/dagster-external-assets-rest-api-rules.yml
tags:
- Data Engineering
- Data Orchestration
- Data Pipelines
- ETL
- Workflows
- Assets
- GraphQL
- Spectral
- Linting
- API Governance
---
