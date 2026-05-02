---
categories:
- ac
description: Spectral linting rules defining API design standards and conventions for Acceptance Criteria.
layout: rules
name: Acceptance Criteria API Rules
provider_name: Acceptance Criteria
provider_slug: acceptance-criteria
rule_count: 27
rules:
- description: APIs managing acceptance criteria must require authentication
  given: $.paths[*][get,post,put,patch,delete]
  name: ac-require-security-scheme
  severity: error
- description: API paths must use kebab-case naming
  given: $.paths[*]~
  name: ac-path-kebab-case
  severity: warn
- description: API paths must not have trailing slashes
  given: $.paths[*]~
  name: ac-no-trailing-slash
  severity: warn
- description: All operations must have a summary
  given: $.paths[*][get,post,put,patch,delete]
  name: ac-operations-require-summary
  severity: error
- description: All operations must have an operationId
  given: $.paths[*][get,post,put,patch,delete]
  name: ac-operations-require-operation-id
  severity: error
- description: OperationIds must use camelCase
  given: $.paths[*][get,post,put,patch,delete].operationId
  name: ac-operation-id-camel-case
  severity: warn
- description: All operations must have at least one tag
  given: $.paths[*][get,post,put,patch,delete]
  name: ac-operations-require-tags
  severity: warn
- description: All operations should have a description
  given: $.paths[*][get,post,put,patch,delete]
  name: ac-operations-require-description
  severity: info
- description: GET operations must define a 200 response
  given: $.paths[*].get.responses
  name: ac-require-200-response
  severity: error
- description: POST operations should define a 201 created response
  given: $.paths[*].post.responses
  name: ac-require-201-on-post
  severity: warn
- description: Operations must define a 401 unauthorized response
  given: $.paths[*][get,post,put,patch,delete].responses
  name: ac-require-401-response
  severity: warn
- description: Operations on parameterized paths must define a 404 response
  given: $.paths[?(@~.match(/\{.*\}/))][get,put,patch,delete].responses
  name: ac-require-404-on-parameterized-paths
  severity: warn
- description: All operations must define a 500 server error response
  given: $.paths[*][get,post,put,patch,delete].responses
  name: ac-require-500-response
  severity: warn
- description: All schema components must have a description
  given: $.components.schemas[*]
  name: ac-schema-require-description
  severity: warn
- description: Schema properties should have descriptions for self-documenting APIs
  given: $.components.schemas[*].properties[*]
  name: ac-schema-properties-require-description
  severity: info
- description: Resource schemas must include an id property
  given: $.components.schemas[?(!@.title =~ /(List|Request)$/)]
  name: ac-require-id-property
  severity: warn
- description: Timestamp fields must use date-time format
  given: $.components.schemas[*].properties[?(@.description =~ /[Tt]imestamp|At$|[Dd]ate/)]
  name: ac-timestamp-format
  severity: error
- description: Gherkin-format acceptance criteria must include given, when, and then fields
  given: $.components.schemas.AcceptanceCriterion.properties
  name: ac-gherkin-given-when-then
  severity: info
- description: Status fields must use defined enum values
  given: $.components.schemas[*].properties.status
  name: ac-status-enum-values
  severity: warn
- description: Priority fields must use defined enum values
  given: $.components.schemas[*].properties.priority
  name: ac-priority-enum-values
  severity: warn
- description: Request bodies must use application/json content type
  given: $.paths[*][post,put,patch].requestBody.content
  name: ac-require-json-request-body
  severity: error
- description: Success responses must return application/json
  given: $.paths[*][get,post,put,patch].responses[200,201].content
  name: ac-require-json-response
  severity: error
- description: List schema responses must include a total count
  given: $.components.schemas[?(@.title =~ /List$/)]
  name: ac-list-responses-require-total
  severity: warn
- description: List schema responses must include page for pagination
  given: $.components.schemas[?(@.title =~ /List$/)]
  name: ac-list-responses-require-page
  severity: warn
- description: API spec must include a version
  given: $.info
  name: ac-info-require-version
  severity: error
- description: API spec must include a description
  given: $.info
  name: ac-info-require-description
  severity: error
- description: API spec should include contact information
  given: $.info
  name: ac-info-require-contact
  severity: info
rules_file: rules/acceptance-criteria-spectral-rules.yml
rules_url: https://raw.githubusercontent.com/api-evangelist/acceptance-criteria/refs/heads/main/rules/acceptance-criteria-spectral-rules.yml
severity_counts:
  error: 9
  hint: 0
  info: 4
  warn: 14
slug: acceptance-criteria-spectral-rules
source_filename: acceptance-criteria-spectral-rules.yml
source_heading: Spectral Ruleset
source_yaml: "extends: spectral:oas\nrules:\n  # Authentication Rules\n  ac-require-security-scheme:\n    description: APIs managing acceptance criteria must require authentication\n    message: \"Operation '{{path}}' must define security requirements\"\n    severity: error\n    given: \"$.paths[*][get,post,put,patch,delete]\"\n    then:\n      field: security\n      function: truthy\n\n  # Path Naming Rules\n  ac-path-kebab-case:\n    description: API paths must use kebab-case naming\n    message: \"Path '{{value}}' must use kebab-case\"\n    severity: warn\n    given: \"$.paths[*]~\"\n    then:\n      function: pattern\n      functionOptions:\n        match: \"^(/[a-z0-9-]+({[a-zA-Z]+})?)*$\"\n\n  ac-no-trailing-slash:\n    description: API paths must not have trailing slashes\n    message: \"Path '{{value}}' must not have a trailing slash\"\n    severity: warn\n    given: \"$.paths[*]~\"\n    then:\n      function: pattern\n      functionOptions:\n        notMatch: \"/$\"\n\n  # Operation\
  \ Rules\n  ac-operations-require-summary:\n    description: All operations must have a summary\n    message: \"Operation at '{{path}}' must have a summary\"\n    severity: error\n    given: \"$.paths[*][get,post,put,patch,delete]\"\n    then:\n      field: summary\n      function: truthy\n\n  ac-operations-require-operation-id:\n    description: All operations must have an operationId\n    message: \"Operation at '{{path}}' must have an operationId\"\n    severity: error\n    given: \"$.paths[*][get,post,put,patch,delete]\"\n    then:\n      field: operationId\n      function: truthy\n\n  ac-operation-id-camel-case:\n    description: OperationIds must use camelCase\n    message: \"OperationId '{{value}}' must use camelCase\"\n    severity: warn\n    given: \"$.paths[*][get,post,put,patch,delete].operationId\"\n    then:\n      function: pattern\n      functionOptions:\n        match: \"^[a-z][a-zA-Z0-9]*$\"\n\n  ac-operations-require-tags:\n    description: All operations must have at\
  \ least one tag\n    message: \"Operation at '{{path}}' must have at least one tag\"\n    severity: warn\n    given: \"$.paths[*][get,post,put,patch,delete]\"\n    then:\n      field: tags\n      function: truthy\n\n  ac-operations-require-description:\n    description: All operations should have a description\n    message: \"Operation at '{{path}}' should have a description\"\n    severity: info\n    given: \"$.paths[*][get,post,put,patch,delete]\"\n    then:\n      field: description\n      function: truthy\n\n  # Response Rules\n  ac-require-200-response:\n    description: GET operations must define a 200 response\n    message: \"GET operation at '{{path}}' must define a 200 response\"\n    severity: error\n    given: \"$.paths[*].get.responses\"\n    then:\n      field: \"200\"\n      function: truthy\n\n  ac-require-201-on-post:\n    description: POST operations should define a 201 created response\n    message: \"POST operation at '{{path}}' should define a 201 response\"\n    severity:\
  \ warn\n    given: \"$.paths[*].post.responses\"\n    then:\n      field: \"201\"\n      function: truthy\n\n  ac-require-401-response:\n    description: Operations must define a 401 unauthorized response\n    message: \"Operation at '{{path}}' must define a 401 response\"\n    severity: warn\n    given: \"$.paths[*][get,post,put,patch,delete].responses\"\n    then:\n      field: \"401\"\n      function: truthy\n\n  ac-require-404-on-parameterized-paths:\n    description: Operations on parameterized paths must define a 404 response\n    message: \"Operation at '{{path}}' must define a 404 response\"\n    severity: warn\n    given: \"$.paths[?(@~.match(/\\\\{.*\\\\}/))][get,put,patch,delete].responses\"\n    then:\n      field: \"404\"\n      function: truthy\n\n  ac-require-500-response:\n    description: All operations must define a 500 server error response\n    message: \"Operation at '{{path}}' must define a 500 response\"\n    severity: warn\n    given: \"$.paths[*][get,post,put,patch,delete].responses\"\
  \n    then:\n      field: \"500\"\n      function: truthy\n\n  # Schema Rules\n  ac-schema-require-description:\n    description: All schema components must have a description\n    message: \"Schema '{{path}}' must have a description\"\n    severity: warn\n    given: \"$.components.schemas[*]\"\n    then:\n      field: description\n      function: truthy\n\n  ac-schema-properties-require-description:\n    description: Schema properties should have descriptions for self-documenting APIs\n    message: \"Property at '{{path}}' should have a description\"\n    severity: info\n    given: \"$.components.schemas[*].properties[*]\"\n    then:\n      field: description\n      function: truthy\n\n  ac-require-id-property:\n    description: Resource schemas must include an id property\n    message: \"Schema '{{path}}' must include an 'id' property\"\n    severity: warn\n    given: \"$.components.schemas[?(!@.title =~ /(List|Request)$/)]\"\n    then:\n      field: properties.id\n      function: truthy\n\
  \n  ac-timestamp-format:\n    description: Timestamp fields must use date-time format\n    message: \"Timestamp property at '{{path}}' must use format: date-time\"\n    severity: error\n    given: \"$.components.schemas[*].properties[?(@.description =~ /[Tt]imestamp|At$|[Dd]ate/)]\"\n    then:\n      field: format\n      function: enumeration\n      functionOptions:\n        values:\n          - date-time\n          - date\n\n  # Acceptance Criteria Specific Rules\n  ac-gherkin-given-when-then:\n    description: Gherkin-format acceptance criteria must include given, when, and then fields\n    message: \"Gherkin acceptance criterion at '{{path}}' should include 'given', 'when', and 'then' properties\"\n    severity: info\n    given: \"$.components.schemas.AcceptanceCriterion.properties\"\n    then:\n      function: schema\n      functionOptions:\n        schema:\n          required: [given, when, then]\n\n  ac-status-enum-values:\n    description: Status fields must use defined enum values\n\
  \    message: \"Status property at '{{path}}' must define enum values\"\n    severity: warn\n    given: \"$.components.schemas[*].properties.status\"\n    then:\n      field: enum\n      function: truthy\n\n  ac-priority-enum-values:\n    description: Priority fields must use defined enum values\n    message: \"Priority property at '{{path}}' must define enum values\"\n    severity: warn\n    given: \"$.components.schemas[*].properties.priority\"\n    then:\n      field: enum\n      function: truthy\n\n  # Content Type Rules\n  ac-require-json-request-body:\n    description: Request bodies must use application/json content type\n    message: \"Request body at '{{path}}' must use application/json\"\n    severity: error\n    given: \"$.paths[*][post,put,patch].requestBody.content\"\n    then:\n      field: application/json\n      function: truthy\n\n  ac-require-json-response:\n    description: Success responses must return application/json\n    message: \"Response at '{{path}}' must return\
  \ application/json\"\n    severity: error\n    given: \"$.paths[*][get,post,put,patch].responses[200,201].content\"\n    then:\n      field: application/json\n      function: truthy\n\n  # Pagination Rules\n  ac-list-responses-require-total:\n    description: List schema responses must include a total count\n    message: \"List schema '{{path}}' must include a 'total' property\"\n    severity: warn\n    given: \"$.components.schemas[?(@.title =~ /List$/)]\"\n    then:\n      field: properties.total\n      function: truthy\n\n  ac-list-responses-require-page:\n    description: List schema responses must include page for pagination\n    message: \"List schema '{{path}}' must include a 'page' property\"\n    severity: warn\n    given: \"$.components.schemas[?(@.title =~ /List$/)]\"\n    then:\n      field: properties.page\n      function: truthy\n\n  # Info Rules\n  ac-info-require-version:\n    description: API spec must include a version\n    message: \"API info must include a version\"\
  \n    severity: error\n    given: \"$.info\"\n    then:\n      field: version\n      function: truthy\n\n  ac-info-require-description:\n    description: API spec must include a description\n    message: \"API info must include a description\"\n    severity: error\n    given: \"$.info\"\n    then:\n      field: description\n      function: truthy\n\n  ac-info-require-contact:\n    description: API spec should include contact information\n    message: \"API info should include a contact object\"\n    severity: info\n    given: \"$.info\"\n    then:\n      field: contact\n      function: truthy\n"
source_yaml_url: https://raw.githubusercontent.com/api-evangelist/acceptance-criteria/refs/heads/main/rules/acceptance-criteria-spectral-rules.yml
tags:
- Agile
- Behavior Driven Development
- Gherkin
- Quality Assurance
- Requirements
- Testing
- User Stories
- Spectral
- Linting
- API Governance
---
