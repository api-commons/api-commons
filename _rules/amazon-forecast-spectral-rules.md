---
api_specs:
- filename: amazon-forecast-openapi.yml
  format: yaml
  label: Amazon Forecast API
  slug: amazon-forecast-api
  spec_type: OpenAPI
  url: https://raw.githubusercontent.com/api-evangelist/amazon-forecast/refs/heads/main/openapi/amazon-forecast-openapi.yml
categories:
- forecast
description: Spectral linting rules defining API design standards and conventions for Amazon Forecast.
layout: rules
name: Amazon Forecast API Rules
provider_name: Amazon Forecast
provider_slug: amazon-forecast
rule_count: 25
rules:
- description: API must include contact information
  given: $.info
  name: forecast-info-contact
  severity: warn
- description: API must have a description
  given: $.info
  name: forecast-info-description
  severity: error
- description: Server URLs must use HTTPS
  given: $.servers[*].url
  name: forecast-server-https
  severity: error
- description: Operations must have a summary
  given: $.paths[*][get,post,put,patch,delete]
  name: forecast-operation-summary
  severity: error
- description: Operations should have a description
  given: $.paths[*][get,post,put,patch,delete]
  name: forecast-operation-description
  severity: warn
- description: Operations must have at least one tag
  given: $.paths[*][get,post,put,patch,delete]
  name: forecast-operation-tags
  severity: error
- description: Operations must have operationId
  given: $.paths[*][get,post,put,patch,delete]
  name: forecast-operation-id
  severity: error
- description: operationId should use camelCase
  given: $.paths[*][get,post,put,patch,delete].operationId
  name: forecast-operation-id-camel-case
  severity: warn
- description: POST operations should define 200 response
  given: $.paths[*][post]
  name: forecast-response-200
  severity: warn
- description: Operations should define 400 response
  given: $.paths[*][get,post,put,patch,delete]
  name: forecast-response-400
  severity: warn
- description: Operations should define 500 response
  given: $.paths[*][get,post,put,patch,delete]
  name: forecast-response-500
  severity: warn
- description: Parameters must have descriptions
  given: $.paths[*][get,post,put,patch,delete].parameters[*]
  name: forecast-parameter-description
  severity: error
- description: Schema components should have descriptions
  given: $.components.schemas[*]
  name: forecast-schema-description
  severity: warn
- description: Operation tags should use Title Case
  given: $.paths[*][*].tags[*]
  name: forecast-tags-title-case
  severity: warn
- description: Collection GET operationIds should start with 'list'
  given: $.paths[*~'[^}]$'].get.operationId
  name: forecast-list-operation-prefix
  severity: warn
- description: POST operationIds should start with 'create'
  given: $.paths[*].post.operationId
  name: forecast-create-post-prefix
  severity: warn
- description: Dataset schema should define Domain enum values
  given: $.components.schemas.Dataset.properties.Domain
  name: forecast-dataset-domain-documented
  severity: warn
- description: Predictor schema should include ForecastHorizon
  given: $.components.schemas.Predictor.properties
  name: forecast-predictor-horizon-documented
  severity: warn
- description: Object schemas should define properties
  given: $.components.schemas[?(@.type=='object')]
  name: forecast-schema-properties-defined
  severity: warn
- description: POST request bodies must define content
  given: $.paths[*].post.requestBody
  name: forecast-request-body-content
  severity: error
- description: ARN fields should follow consistent naming (ResourceArn pattern)
  given: $.components.schemas[*].properties[*~'Arn$']
  name: forecast-arn-fields-consistent
  severity: info
- description: ForecastTypes should be an array of quantile strings
  given: $.components.schemas.Forecast.properties.ForecastTypes
  name: forecast-forecast-types-array
  severity: info
- description: Resources should document Status field
  given: $.components.schemas[*].properties.Status
  name: forecast-status-field-documented
  severity: info
- description: Tag schema should be defined
  given: $.components.schemas
  name: forecast-tag-schema-documented
  severity: warn
- description: Export job request should require Destination
  given: $.components.schemas.CreateForecastExportJobRequest.required
  name: forecast-export-job-destination
  severity: warn
rules_file: rules/amazon-forecast-spectral-rules.yml
rules_url: https://raw.githubusercontent.com/api-evangelist/amazon-forecast/refs/heads/main/rules/amazon-forecast-spectral-rules.yml
severity_counts:
  error: 7
  hint: 0
  info: 3
  warn: 15
slug: amazon-forecast-spectral-rules
source_filename: amazon-forecast-spectral-rules.yml
source_heading: Spectral Ruleset
source_yaml: "# Amazon Forecast Spectral Rules\nextends: spectral:oas\nrules:\n  forecast-info-contact:\n    description: API must include contact information\n    severity: warn\n    given: \"$.info\"\n    then:\n      field: contact\n      function: truthy\n  forecast-info-description:\n    description: API must have a description\n    severity: error\n    given: \"$.info\"\n    then:\n      field: description\n      function: truthy\n  forecast-server-https:\n    description: Server URLs must use HTTPS\n    severity: error\n    given: \"$.servers[*].url\"\n    then:\n      function: pattern\n      functionOptions:\n        match: \"^https://\"\n  forecast-operation-summary:\n    description: Operations must have a summary\n    severity: error\n    given: \"$.paths[*][get,post,put,patch,delete]\"\n    then:\n      field: summary\n      function: truthy\n  forecast-operation-description:\n    description: Operations should have a description\n    severity: warn\n    given: \"$.paths[*][get,post,put,patch,delete]\"\
  \n    then:\n      field: description\n      function: truthy\n  forecast-operation-tags:\n    description: Operations must have at least one tag\n    severity: error\n    given: \"$.paths[*][get,post,put,patch,delete]\"\n    then:\n      field: tags\n      function: truthy\n  forecast-operation-id:\n    description: Operations must have operationId\n    severity: error\n    given: \"$.paths[*][get,post,put,patch,delete]\"\n    then:\n      field: operationId\n      function: truthy\n  forecast-operation-id-camel-case:\n    description: operationId should use camelCase\n    severity: warn\n    given: \"$.paths[*][get,post,put,patch,delete].operationId\"\n    then:\n      function: pattern\n      functionOptions:\n        match: \"^[a-z][a-zA-Z0-9]*$\"\n  forecast-response-200:\n    description: POST operations should define 200 response\n    severity: warn\n    given: \"$.paths[*][post]\"\n    then:\n      field: responses.200\n      function: truthy\n  forecast-response-400:\n    description:\
  \ Operations should define 400 response\n    severity: warn\n    given: \"$.paths[*][get,post,put,patch,delete]\"\n    then:\n      field: responses.400\n      function: truthy\n  forecast-response-500:\n    description: Operations should define 500 response\n    severity: warn\n    given: \"$.paths[*][get,post,put,patch,delete]\"\n    then:\n      field: responses.500\n      function: truthy\n  forecast-parameter-description:\n    description: Parameters must have descriptions\n    severity: error\n    given: \"$.paths[*][get,post,put,patch,delete].parameters[*]\"\n    then:\n      field: description\n      function: truthy\n  forecast-schema-description:\n    description: Schema components should have descriptions\n    severity: warn\n    given: \"$.components.schemas[*]\"\n    then:\n      field: description\n      function: truthy\n  forecast-tags-title-case:\n    description: Operation tags should use Title Case\n    severity: warn\n    given: \"$.paths[*][*].tags[*]\"\n    then:\n\
  \      function: pattern\n      functionOptions:\n        match: \"^[A-Z][a-zA-Z0-9 ]*$\"\n  forecast-list-operation-prefix:\n    description: Collection GET operationIds should start with 'list'\n    severity: warn\n    given: \"$.paths[*~'[^}]$'].get.operationId\"\n    then:\n      function: pattern\n      functionOptions:\n        match: \"^list\"\n  forecast-create-post-prefix:\n    description: POST operationIds should start with 'create'\n    severity: warn\n    given: \"$.paths[*].post.operationId\"\n    then:\n      function: pattern\n      functionOptions:\n        match: \"^(create|tag)\"\n  forecast-dataset-domain-documented:\n    description: Dataset schema should define Domain enum values\n    severity: warn\n    given: \"$.components.schemas.Dataset.properties.Domain\"\n    then:\n      field: enum\n      function: truthy\n  forecast-predictor-horizon-documented:\n    description: Predictor schema should include ForecastHorizon\n    severity: warn\n    given: \"$.components.schemas.Predictor.properties\"\
  \n    then:\n      field: ForecastHorizon\n      function: truthy\n  forecast-schema-properties-defined:\n    description: Object schemas should define properties\n    severity: warn\n    given: \"$.components.schemas[?(@.type=='object')]\"\n    then:\n      field: properties\n      function: truthy\n  forecast-request-body-content:\n    description: POST request bodies must define content\n    severity: error\n    given: \"$.paths[*].post.requestBody\"\n    then:\n      field: content\n      function: truthy\n  forecast-arn-fields-consistent:\n    description: ARN fields should follow consistent naming (ResourceArn pattern)\n    message: \"ARN field '{{value}}' should end with 'Arn'\"\n    severity: info\n    given: \"$.components.schemas[*].properties[*~'Arn$']\"\n    then:\n      field: type\n      function: truthy\n  forecast-forecast-types-array:\n    description: ForecastTypes should be an array of quantile strings\n    severity: info\n    given: \"$.components.schemas.Forecast.properties.ForecastTypes\"\
  \n    then:\n      field: type\n      function: pattern\n      functionOptions:\n        match: \"^array$\"\n  forecast-status-field-documented:\n    description: Resources should document Status field\n    severity: info\n    given: \"$.components.schemas[*].properties.Status\"\n    then:\n      field: type\n      function: truthy\n  forecast-tag-schema-documented:\n    description: Tag schema should be defined\n    severity: warn\n    given: \"$.components.schemas\"\n    then:\n      field: Tag\n      function: truthy\n  forecast-export-job-destination:\n    description: Export job request should require Destination\n    severity: warn\n    given: \"$.components.schemas.CreateForecastExportJobRequest.required\"\n    then:\n      function: schema\n      functionOptions:\n        schema:\n          type: array\n          contains:\n            const: Destination\n"
source_yaml_url: https://raw.githubusercontent.com/api-evangelist/amazon-forecast/refs/heads/main/rules/amazon-forecast-spectral-rules.yml
tags:
- Forecasting
- Machine Learning
- Predictive Analytics
- Time Series
- Spectral
- Linting
- API Governance
---
