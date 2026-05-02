---
api_specs:
- filename: apache-jena-fuseki-sparql-api.yaml
  format: yaml
  label: Apache Jena Fuseki SPARQL API
  slug: fuseki-sparql-api
  spec_type: OpenAPI
  url: https://raw.githubusercontent.com/api-evangelist/apache-jena/refs/heads/main/openapi/apache-jena-fuseki-sparql-api.yaml
categories:
- info
- 'no'
- openapi
- operation
- parameter
- paths
- response
- schema
- servers
- sparql
description: Spectral linting rules defining API design standards and conventions for Apache Jena.
layout: rules
name: Apache Jena API Rules
provider_name: Apache Jena
provider_slug: apache-jena
rule_count: 15
rules:
- description: Info title should start with Apache Jena
  given: $.info
  name: info-title-prefix
  severity: warn
- description: Info must have a version
  given: $.info
  name: info-version-required
  severity: error
- description: Must use OpenAPI 3.x
  given: $
  name: openapi-version
  severity: error
- description: Servers must be defined
  given: $
  name: servers-defined
  severity: error
- description: Every operation must have a summary
  given: $.paths[*][get,post,put,patch,delete]
  name: operation-summary-required
  severity: error
- description: Every operation must have an operationId
  given: $.paths[*][get,post,put,patch,delete]
  name: operation-id-required
  severity: error
- description: Every operation must have tags
  given: $.paths[*][get,post,put,patch,delete]
  name: operation-tags-required
  severity: error
- description: Responses must have descriptions
  given: $.paths[*][get,post,put,patch,delete].responses[*]
  name: response-description-required
  severity: error
- description: Every operation must have a 2xx response
  given: $.paths[*][get,post,put,patch,delete].responses
  name: response-2xx-required
  severity: error
- description: SPARQL endpoints should document 400 for invalid queries
  given: $.paths[*].post.responses
  name: response-400-sparql
  severity: warn
- description: SPARQL query endpoints should support sparql-results+json
  given: $.paths[*].get.responses.200.content
  name: sparql-media-types
  severity: info
- description: Descriptions must not be empty
  given: $..description
  name: no-empty-descriptions
  severity: warn
- description: Component schemas should have descriptions
  given: $.components.schemas[*]
  name: schema-description-required
  severity: info
- description: Parameters should have descriptions
  given: $.paths[*][get,post].parameters[*]
  name: parameter-description-required
  severity: warn
- description: Paths must not have trailing slashes
  given: $.paths
  name: paths-no-trailing-slash
  severity: info
rules_file: rules/apache-jena-spectral-rules.yml
rules_url: https://raw.githubusercontent.com/api-evangelist/apache-jena/refs/heads/main/rules/apache-jena-spectral-rules.yml
severity_counts:
  error: 8
  hint: 0
  info: 3
  warn: 4
slug: apache-jena-spectral-rules
source_filename: apache-jena-spectral-rules.yml
source_heading: Spectral Ruleset
source_yaml: "rules:\n  info-title-prefix:\n    description: Info title should start with Apache Jena\n    severity: warn\n    given: \"$.info\"\n    then:\n      field: title\n      function: pattern\n      functionOptions:\n        match: \"^Apache Jena\"\n\n  info-version-required:\n    description: Info must have a version\n    severity: error\n    given: \"$.info\"\n    then:\n      field: version\n      function: truthy\n\n  openapi-version:\n    description: Must use OpenAPI 3.x\n    severity: error\n    given: \"$\"\n    then:\n      field: openapi\n      function: pattern\n      functionOptions:\n        match: \"^3\\\\.\"\n\n  servers-defined:\n    description: Servers must be defined\n    severity: error\n    given: \"$\"\n    then:\n      field: servers\n      function: truthy\n\n  operation-summary-required:\n    description: Every operation must have a summary\n    severity: error\n    given: \"$.paths[*][get,post,put,patch,delete]\"\n    then:\n      field: summary\n     \
  \ function: truthy\n\n  operation-id-required:\n    description: Every operation must have an operationId\n    severity: error\n    given: \"$.paths[*][get,post,put,patch,delete]\"\n    then:\n      field: operationId\n      function: truthy\n\n  operation-tags-required:\n    description: Every operation must have tags\n    severity: error\n    given: \"$.paths[*][get,post,put,patch,delete]\"\n    then:\n      field: tags\n      function: truthy\n\n  response-description-required:\n    description: Responses must have descriptions\n    severity: error\n    given: \"$.paths[*][get,post,put,patch,delete].responses[*]\"\n    then:\n      field: description\n      function: truthy\n\n  response-2xx-required:\n    description: Every operation must have a 2xx response\n    severity: error\n    given: \"$.paths[*][get,post,put,patch,delete].responses\"\n    then:\n      function: schema\n      functionOptions:\n        schema:\n          anyOf:\n            - required: [\"200\"]\n           \
  \ - required: [\"201\"]\n            - required: [\"204\"]\n\n  response-400-sparql:\n    description: SPARQL endpoints should document 400 for invalid queries\n    severity: warn\n    given: \"$.paths[*].post.responses\"\n    then:\n      field: \"400\"\n      function: truthy\n\n  sparql-media-types:\n    description: SPARQL query endpoints should support sparql-results+json\n    severity: info\n    given: \"$.paths[*].get.responses.200.content\"\n    then:\n      field: \"application/sparql-results+json\"\n      function: truthy\n\n  no-empty-descriptions:\n    description: Descriptions must not be empty\n    severity: warn\n    given: \"$..description\"\n    then:\n      function: pattern\n      functionOptions:\n        match: \".+\"\n\n  schema-description-required:\n    description: Component schemas should have descriptions\n    severity: info\n    given: \"$.components.schemas[*]\"\n    then:\n      field: description\n      function: truthy\n\n  parameter-description-required:\n\
  \    description: Parameters should have descriptions\n    severity: warn\n    given: \"$.paths[*][get,post].parameters[*]\"\n    then:\n      field: description\n      function: truthy\n\n  paths-no-trailing-slash:\n    description: Paths must not have trailing slashes\n    severity: info\n    given: \"$.paths\"\n    then:\n      field: \"@key\"\n      function: pattern\n      functionOptions:\n        notMatch: \"\\\\/$\"\n"
source_yaml_url: https://raw.githubusercontent.com/api-evangelist/apache-jena/refs/heads/main/rules/apache-jena-spectral-rules.yml
tags:
- Java
- Linked Data
- OWL
- Ontology
- Open Source
- RDF
- Semantic Web
- SPARQL
- Spectral
- Linting
- API Governance
---
