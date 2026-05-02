---
api_specs:
- filename: amazon-fraud-detector-openapi.yml
  format: yaml
  label: Amazon Fraud Detector API
  slug: amazon-fraud-detector-api
  spec_type: OpenAPI
  url: https://raw.githubusercontent.com/api-evangelist/amazon-fraud-detector/refs/heads/main/openapi/amazon-fraud-detector-openapi.yml
categories:
- fraud
description: Spectral linting rules defining API design standards and conventions for Amazon Fraud Detector.
layout: rules
name: Amazon Fraud Detector API Rules
provider_name: Amazon Fraud Detector
provider_slug: amazon-fraud-detector
rule_count: 25
rules:
- description: API must include contact information
  given: $.info
  name: fraud-detector-info-contact
  severity: warn
- description: API must have a description
  given: $.info
  name: fraud-detector-info-description
  severity: error
- description: Server URLs must use HTTPS
  given: $.servers[*].url
  name: fraud-detector-server-https
  severity: error
- description: Operations must have a summary
  given: $.paths[*][get,post,put,patch,delete]
  name: fraud-detector-operation-summary
  severity: error
- description: Operations should have a description
  given: $.paths[*][get,post,put,patch,delete]
  name: fraud-detector-operation-description
  severity: warn
- description: Operations must have at least one tag
  given: $.paths[*][get,post,put,patch,delete]
  name: fraud-detector-operation-tags
  severity: error
- description: Operations must have operationId
  given: $.paths[*][get,post,put,patch,delete]
  name: fraud-detector-operation-id
  severity: error
- description: POST operations should define 200 response
  given: $.paths[*][post]
  name: fraud-detector-response-200
  severity: warn
- description: Operations should define 400 response
  given: $.paths[*][get,post,put,patch,delete]
  name: fraud-detector-response-400
  severity: warn
- description: Operations should define 500 response
  given: $.paths[*][get,post,put,patch,delete]
  name: fraud-detector-response-500
  severity: warn
- description: Schema components should have descriptions
  given: $.components.schemas[*]
  name: fraud-detector-schema-description
  severity: warn
- description: Operation tags should use Title Case
  given: $.paths[*][*].tags[*]
  name: fraud-detector-tags-title-case
  severity: warn
- description: Detector schema must reference eventTypeName
  given: $.components.schemas.Detector.required
  name: fraud-detector-detector-event-type
  severity: warn
- description: Model type should define allowed enum values
  given: $.components.schemas.Model.properties.modelType
  name: fraud-detector-model-type-enum
  severity: warn
- description: Rule schema must include outcomes
  given: $.components.schemas.Rule.required
  name: fraud-detector-rule-outcomes
  severity: warn
- description: Event prediction request must include entities
  given: $.components.schemas.GetEventPredictionRequest.required
  name: fraud-detector-prediction-entities
  severity: warn
- description: Parameters must have descriptions
  given: $.paths[*][get,post,put,patch,delete].parameters[*]
  name: fraud-detector-parameter-description
  severity: error
- description: Path parameters must be required
  given: $.paths[*][get,post,put,patch,delete].parameters[?(@.in=='path')]
  name: fraud-detector-path-param-required
  severity: error
- description: Object schemas should define properties
  given: $.components.schemas[?(@.type=='object')]
  name: fraud-detector-schema-properties
  severity: warn
- description: ARN fields should be consistently named 'arn'
  given: $.components.schemas[*].properties.arn
  name: fraud-detector-arn-fields
  severity: info
- description: Event type schema must include labels field
  given: $.components.schemas.EventType.required
  name: fraud-detector-event-type-labels
  severity: warn
- description: Rule language should define DETECTORPL enum
  given: $.components.schemas.Rule.properties.language
  name: fraud-detector-rule-language-enum
  severity: info
- description: Request bodies should define application/json content
  given: $.paths[*][put,post].requestBody.content
  name: fraud-detector-request-body-json
  severity: warn
- description: Tag schema must require key field
  given: $.components.schemas.Tag.required
  name: fraud-detector-tag-key-required
  severity: warn
- description: DELETE operations should define 404 response
  given: $.paths[*].delete.responses
  name: fraud-detector-delete-not-found
  severity: warn
rules_file: rules/amazon-fraud-detector-spectral-rules.yml
rules_url: https://raw.githubusercontent.com/api-evangelist/amazon-fraud-detector/refs/heads/main/rules/amazon-fraud-detector-spectral-rules.yml
severity_counts:
  error: 7
  hint: 0
  info: 2
  warn: 16
slug: amazon-fraud-detector-spectral-rules
source_filename: amazon-fraud-detector-spectral-rules.yml
source_heading: Spectral Ruleset
source_yaml: "# Amazon Fraud Detector Spectral Rules\nextends: spectral:oas\nrules:\n  fraud-detector-info-contact:\n    description: API must include contact information\n    severity: warn\n    given: \"$.info\"\n    then:\n      field: contact\n      function: truthy\n  fraud-detector-info-description:\n    description: API must have a description\n    severity: error\n    given: \"$.info\"\n    then:\n      field: description\n      function: truthy\n  fraud-detector-server-https:\n    description: Server URLs must use HTTPS\n    severity: error\n    given: \"$.servers[*].url\"\n    then:\n      function: pattern\n      functionOptions:\n        match: \"^https://\"\n  fraud-detector-operation-summary:\n    description: Operations must have a summary\n    severity: error\n    given: \"$.paths[*][get,post,put,patch,delete]\"\n    then:\n      field: summary\n      function: truthy\n  fraud-detector-operation-description:\n    description: Operations should have a description\n    severity:\
  \ warn\n    given: \"$.paths[*][get,post,put,patch,delete]\"\n    then:\n      field: description\n      function: truthy\n  fraud-detector-operation-tags:\n    description: Operations must have at least one tag\n    severity: error\n    given: \"$.paths[*][get,post,put,patch,delete]\"\n    then:\n      field: tags\n      function: truthy\n  fraud-detector-operation-id:\n    description: Operations must have operationId\n    severity: error\n    given: \"$.paths[*][get,post,put,patch,delete]\"\n    then:\n      field: operationId\n      function: truthy\n  fraud-detector-response-200:\n    description: POST operations should define 200 response\n    severity: warn\n    given: \"$.paths[*][post]\"\n    then:\n      field: responses.200\n      function: truthy\n  fraud-detector-response-400:\n    description: Operations should define 400 response\n    severity: warn\n    given: \"$.paths[*][get,post,put,patch,delete]\"\n    then:\n      field: responses.400\n      function: truthy\n  fraud-detector-response-500:\n\
  \    description: Operations should define 500 response\n    severity: warn\n    given: \"$.paths[*][get,post,put,patch,delete]\"\n    then:\n      field: responses.500\n      function: truthy\n  fraud-detector-schema-description:\n    description: Schema components should have descriptions\n    severity: warn\n    given: \"$.components.schemas[*]\"\n    then:\n      field: description\n      function: truthy\n  fraud-detector-tags-title-case:\n    description: Operation tags should use Title Case\n    severity: warn\n    given: \"$.paths[*][*].tags[*]\"\n    then:\n      function: pattern\n      functionOptions:\n        match: \"^[A-Z][a-zA-Z0-9 ]*$\"\n  fraud-detector-detector-event-type:\n    description: Detector schema must reference eventTypeName\n    severity: warn\n    given: \"$.components.schemas.Detector.required\"\n    then:\n      function: schema\n      functionOptions:\n        schema:\n          type: array\n          contains:\n            const: eventTypeName\n  fraud-detector-model-type-enum:\n\
  \    description: Model type should define allowed enum values\n    severity: warn\n    given: \"$.components.schemas.Model.properties.modelType\"\n    then:\n      field: enum\n      function: truthy\n  fraud-detector-rule-outcomes:\n    description: Rule schema must include outcomes\n    severity: warn\n    given: \"$.components.schemas.Rule.required\"\n    then:\n      function: schema\n      functionOptions:\n        schema:\n          type: array\n          contains:\n            const: outcomes\n  fraud-detector-prediction-entities:\n    description: Event prediction request must include entities\n    severity: warn\n    given: \"$.components.schemas.GetEventPredictionRequest.required\"\n    then:\n      function: schema\n      functionOptions:\n        schema:\n          type: array\n          contains:\n            const: entities\n  fraud-detector-parameter-description:\n    description: Parameters must have descriptions\n    severity: error\n    given: \"$.paths[*][get,post,put,patch,delete].parameters[*]\"\
  \n    then:\n      field: description\n      function: truthy\n  fraud-detector-path-param-required:\n    description: Path parameters must be required\n    severity: error\n    given: \"$.paths[*][get,post,put,patch,delete].parameters[?(@.in=='path')]\"\n    then:\n      field: required\n      function: truthy\n  fraud-detector-schema-properties:\n    description: Object schemas should define properties\n    severity: warn\n    given: \"$.components.schemas[?(@.type=='object')]\"\n    then:\n      field: properties\n      function: truthy\n  fraud-detector-arn-fields:\n    description: ARN fields should be consistently named 'arn'\n    severity: info\n    given: \"$.components.schemas[*].properties.arn\"\n    then:\n      field: type\n      function: truthy\n  fraud-detector-event-type-labels:\n    description: Event type schema must include labels field\n    severity: warn\n    given: \"$.components.schemas.EventType.required\"\n    then:\n      function: schema\n      functionOptions:\n\
  \        schema:\n          type: array\n          contains:\n            const: labels\n  fraud-detector-rule-language-enum:\n    description: Rule language should define DETECTORPL enum\n    severity: info\n    given: \"$.components.schemas.Rule.properties.language\"\n    then:\n      field: enum\n      function: truthy\n  fraud-detector-request-body-json:\n    description: Request bodies should define application/json content\n    severity: warn\n    given: \"$.paths[*][put,post].requestBody.content\"\n    then:\n      function: schema\n      functionOptions:\n        schema:\n          type: object\n          required: [\"application/json\"]\n  fraud-detector-tag-key-required:\n    description: Tag schema must require key field\n    severity: warn\n    given: \"$.components.schemas.Tag.required\"\n    then:\n      function: schema\n      functionOptions:\n        schema:\n          type: array\n          contains:\n            const: key\n  fraud-detector-delete-not-found:\n    description:\
  \ DELETE operations should define 404 response\n    severity: warn\n    given: \"$.paths[*].delete.responses\"\n    then:\n      field: \"404\"\n      function: truthy\n"
source_yaml_url: https://raw.githubusercontent.com/api-evangelist/amazon-fraud-detector/refs/heads/main/rules/amazon-fraud-detector-spectral-rules.yml
tags:
- Financial Services
- Fraud Detection
- Machine Learning
- Security
- Spectral
- Linting
- API Governance
---
