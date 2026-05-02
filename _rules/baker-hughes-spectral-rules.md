---
categories:
- baker
description: Spectral linting rules defining API design standards and conventions for Baker Hughes.
layout: rules
name: Baker Hughes API Rules
provider_name: Baker Hughes
provider_slug: baker-hughes
rule_count: 15
rules:
- description: Baker Hughes APIs must include contact information.
  given: $.info
  name: baker-hughes-info-contact-required
  severity: warn
- description: API version must follow semantic versioning.
  given: $.info.version
  name: baker-hughes-info-version-semver
  severity: warn
- description: Path segments must use kebab-case.
  given: $.paths[*]~
  name: baker-hughes-path-kebab-case
  severity: warn
- description: Asset resource paths should use assetId as the path parameter.
  given: $.paths[*]~
  name: baker-hughes-path-asset-id-param
  severity: info
- description: All operations must have an operationId.
  given: $.paths[*][get,post,put,patch,delete,options,head]
  name: baker-hughes-operation-id-required
  severity: error
- description: All operations must have a summary.
  given: $.paths[*][get,post,put,patch,delete]
  name: baker-hughes-operation-summary-required
  severity: warn
- description: All operations must have at least one tag.
  given: $.paths[*][get,post,put,patch,delete]
  name: baker-hughes-operation-tags-required
  severity: warn
- description: All Baker Hughes APIs must define security schemes.
  given: $
  name: baker-hughes-security-required
  severity: error
- description: Baker Hughes APIs should use OAuth2 for authentication.
  given: $.components.securitySchemes[*]
  name: baker-hughes-oauth2-required
  severity: warn
- description: GET operations must define a 200 response.
  given: $.paths[*].get.responses
  name: baker-hughes-response-200-required
  severity: error
- description: Error responses must reference a schema.
  given: $.paths[*][*].responses[4XX,5XX].content[*]
  name: baker-hughes-response-error-schemas
  severity: warn
- description: All named schemas must have a description.
  given: $.components.schemas[*]
  name: baker-hughes-schema-description-required
  severity: warn
- description: Schema properties should have descriptions.
  given: $.components.schemas[*].properties[*]
  name: baker-hughes-schema-properties-descriptions
  severity: info
- description: All parameters must have descriptions.
  given: $.paths[*][*].parameters[*]
  name: baker-hughes-parameter-description-required
  severity: warn
- description: Global tags must have descriptions.
  given: $.tags[*]
  name: baker-hughes-tags-description-required
  severity: warn
rules_file: rules/baker-hughes-spectral-rules.yml
rules_url: https://raw.githubusercontent.com/api-evangelist/baker-hughes/refs/heads/main/rules/baker-hughes-spectral-rules.yml
severity_counts:
  error: 3
  hint: 0
  info: 2
  warn: 10
slug: baker-hughes-spectral-rules
source_filename: baker-hughes-spectral-rules.yml
source_heading: Spectral Ruleset
source_yaml: "rules:\n  # Info Object Rules\n  baker-hughes-info-contact-required:\n    description: Baker Hughes APIs must include contact information.\n    message: \"API info must include a contact object with name and email.\"\n    severity: warn\n    given: \"$.info\"\n    then:\n      field: contact\n      function: truthy\n\n  baker-hughes-info-version-semver:\n    description: API version must follow semantic versioning.\n    message: \"API version must be in semver format (e.g. 1.0.0).\"\n    severity: warn\n    given: \"$.info.version\"\n    then:\n      function: pattern\n      functionOptions:\n        match: \"^[0-9]+\\\\.[0-9]+\\\\.[0-9]+\"\n\n  # Path Rules\n  baker-hughes-path-kebab-case:\n    description: Path segments must use kebab-case.\n    message: \"Path segments must be kebab-case (lowercase with hyphens, no underscores).\"\n    severity: warn\n    given: \"$.paths[*]~\"\n    then:\n      function: pattern\n      functionOptions:\n        notMatch: \"_\"\n\n  baker-hughes-path-asset-id-param:\n\
  \    description: Asset resource paths should use assetId as the path parameter.\n    message: \"Asset paths should use {assetId} as the identifier parameter.\"\n    severity: info\n    given: \"$.paths[*]~\"\n    then:\n      function: pattern\n      functionOptions:\n        notMatch: \"\\\\{asset[^I]\"\n\n  # Operation Rules\n  baker-hughes-operation-id-required:\n    description: All operations must have an operationId.\n    message: \"Operation must have an operationId.\"\n    severity: error\n    given: \"$.paths[*][get,post,put,patch,delete,options,head]\"\n    then:\n      field: operationId\n      function: truthy\n\n  baker-hughes-operation-summary-required:\n    description: All operations must have a summary.\n    message: \"Operation must have a summary.\"\n    severity: warn\n    given: \"$.paths[*][get,post,put,patch,delete]\"\n    then:\n      field: summary\n      function: truthy\n\n  baker-hughes-operation-tags-required:\n    description: All operations must have at\
  \ least one tag.\n    message: \"Operation must have at least one tag for categorization.\"\n    severity: warn\n    given: \"$.paths[*][get,post,put,patch,delete]\"\n    then:\n      field: tags\n      function: truthy\n\n  # Security Rules\n  baker-hughes-security-required:\n    description: All Baker Hughes APIs must define security schemes.\n    message: \"API must define security requirements.\"\n    severity: error\n    given: \"$\"\n    then:\n      field: security\n      function: truthy\n\n  baker-hughes-oauth2-required:\n    description: Baker Hughes APIs should use OAuth2 for authentication.\n    message: \"Security schemes should include OAuth2.\"\n    severity: warn\n    given: \"$.components.securitySchemes[*]\"\n    then:\n      field: type\n      function: enumeration\n      functionOptions:\n        values: [oauth2, http, apiKey]\n\n  # Response Rules\n  baker-hughes-response-200-required:\n    description: GET operations must define a 200 response.\n    message: \"GET\
  \ operations must define a 200 success response.\"\n    severity: error\n    given: \"$.paths[*].get.responses\"\n    then:\n      field: \"200\"\n      function: truthy\n\n  baker-hughes-response-error-schemas:\n    description: Error responses must reference a schema.\n    message: \"4xx and 5xx responses should include a schema.\"\n    severity: warn\n    given: \"$.paths[*][*].responses[4XX,5XX].content[*]\"\n    then:\n      field: schema\n      function: truthy\n\n  # Schema Rules\n  baker-hughes-schema-description-required:\n    description: All named schemas must have a description.\n    message: \"Schema components must have a description.\"\n    severity: warn\n    given: \"$.components.schemas[*]\"\n    then:\n      field: description\n      function: truthy\n\n  baker-hughes-schema-properties-descriptions:\n    description: Schema properties should have descriptions.\n    message: \"Schema properties should include descriptions.\"\n    severity: info\n    given: \"$.components.schemas[*].properties[*]\"\
  \n    then:\n      field: description\n      function: truthy\n\n  # Parameter Rules\n  baker-hughes-parameter-description-required:\n    description: All parameters must have descriptions.\n    message: \"Parameters must include a description.\"\n    severity: warn\n    given: \"$.paths[*][*].parameters[*]\"\n    then:\n      field: description\n      function: truthy\n\n  # Tag Rules\n  baker-hughes-tags-description-required:\n    description: Global tags must have descriptions.\n    message: \"Tags defined in the info section must have descriptions.\"\n    severity: warn\n    given: \"$.tags[*]\"\n    then:\n      field: description\n      function: truthy\n"
source_yaml_url: https://raw.githubusercontent.com/api-evangelist/baker-hughes/refs/heads/main/rules/baker-hughes-spectral-rules.yml
tags:
- Energy Technology
- Industrial IoT
- Oil And Gas
- Asset Performance Management
- Digital Energy
- Spectral
- Linting
- API Governance
---
