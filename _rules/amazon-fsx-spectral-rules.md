---
api_specs:
- filename: amazon-fsx-openapi.yml
  format: yaml
  label: Amazon FSx API
  slug: amazon-fsx-api
  spec_type: OpenAPI
  url: https://raw.githubusercontent.com/api-evangelist/amazon-fsx/refs/heads/main/openapi/amazon-fsx-openapi.yml
categories:
- fsx
description: Spectral linting rules defining API design standards and conventions for Amazon FSx.
layout: rules
name: Amazon FSx API Rules
provider_name: Amazon FSx
provider_slug: amazon-fsx
rule_count: 26
rules:
- description: API must include contact information
  given: $.info
  name: fsx-info-contact
  severity: warn
- description: API must have a description
  given: $.info
  name: fsx-info-description
  severity: error
- description: Server URLs must use HTTPS
  given: $.servers[*].url
  name: fsx-server-https
  severity: error
- description: Operations must have a summary
  given: $.paths[*][get,post,put,patch,delete]
  name: fsx-operation-summary
  severity: error
- description: Operations should have a description
  given: $.paths[*][get,post,put,patch,delete]
  name: fsx-operation-description
  severity: warn
- description: Operations must have at least one tag
  given: $.paths[*][get,post,put,patch,delete]
  name: fsx-operation-tags
  severity: error
- description: Operations must have operationId
  given: $.paths[*][get,post,put,patch,delete]
  name: fsx-operation-id
  severity: error
- description: operationId should use camelCase
  given: $.paths[*][get,post,put,patch,delete].operationId
  name: fsx-operation-id-camel-case
  severity: warn
- description: POST operations should define 200 response
  given: $.paths[*][post]
  name: fsx-response-200
  severity: warn
- description: Operations should define 400 response
  given: $.paths[*][get,post,put,patch,delete]
  name: fsx-response-400
  severity: warn
- description: Operations should define 500 response
  given: $.paths[*][get,post,put,patch,delete]
  name: fsx-response-500
  severity: warn
- description: Schema components should have descriptions
  given: $.components.schemas[*]
  name: fsx-schema-description
  severity: warn
- description: Operation tags should use Title Case
  given: $.paths[*][*].tags[*]
  name: fsx-tags-title-case
  severity: warn
- description: FileSystem schema should define FileSystemType field
  given: $.components.schemas.FileSystem.properties
  name: fsx-filesystem-type-documented
  severity: warn
- description: FileSystem lifecycle should define enum values
  given: $.components.schemas.FileSystem.properties.Lifecycle
  name: fsx-lifecycle-enum
  severity: info
- description: Backup type should define enum values
  given: $.components.schemas.Backup.properties.Type
  name: fsx-backup-type-enum
  severity: info
- description: Parameters must have descriptions
  given: $.paths[*][get,post,put,patch,delete].parameters[*]
  name: fsx-parameter-description
  severity: error
- description: Path parameters must be required
  given: $.paths[*][get,post,put,patch,delete].parameters[?(@.in=='path')]
  name: fsx-path-param-required
  severity: error
- description: Object schemas should define properties
  given: $.components.schemas[?(@.type=='object')]
  name: fsx-schema-properties
  severity: warn
- description: POST request bodies should define application/json content
  given: $.paths[*].post.requestBody.content
  name: fsx-request-body-json
  severity: warn
- description: POST creation operationIds should start with 'create'
  given: $.paths[*].post.operationId
  name: fsx-create-prefix
  severity: warn
- description: DELETE operations should have a description
  given: $.paths[*].delete
  name: fsx-delete-operation
  severity: warn
- description: FileSystem schema should document StorageCapacity
  given: $.components.schemas.FileSystem.properties
  name: fsx-storage-capacity-documented
  severity: warn
- description: Resource ARN field should be named ResourceARN
  given: $.components.schemas[*].properties.ResourceARN
  name: fsx-resource-arn-consistent
  severity: info
- description: Tag schema must require Key field
  given: $.components.schemas.Tag.required
  name: fsx-tag-schema-required
  severity: warn
- description: StorageVirtualMachine must reference FileSystemId
  given: $.components.schemas.StorageVirtualMachine.required
  name: fsx-svm-filesystem-required
  severity: warn
rules_file: rules/amazon-fsx-spectral-rules.yml
rules_url: https://raw.githubusercontent.com/api-evangelist/amazon-fsx/refs/heads/main/rules/amazon-fsx-spectral-rules.yml
severity_counts:
  error: 7
  hint: 0
  info: 3
  warn: 16
slug: amazon-fsx-spectral-rules
source_filename: amazon-fsx-spectral-rules.yml
source_heading: Spectral Ruleset
source_yaml: "# Amazon FSx Spectral Rules\nextends: spectral:oas\nrules:\n  fsx-info-contact:\n    description: API must include contact information\n    severity: warn\n    given: \"$.info\"\n    then:\n      field: contact\n      function: truthy\n  fsx-info-description:\n    description: API must have a description\n    severity: error\n    given: \"$.info\"\n    then:\n      field: description\n      function: truthy\n  fsx-server-https:\n    description: Server URLs must use HTTPS\n    severity: error\n    given: \"$.servers[*].url\"\n    then:\n      function: pattern\n      functionOptions:\n        match: \"^https://\"\n  fsx-operation-summary:\n    description: Operations must have a summary\n    severity: error\n    given: \"$.paths[*][get,post,put,patch,delete]\"\n    then:\n      field: summary\n      function: truthy\n  fsx-operation-description:\n    description: Operations should have a description\n    severity: warn\n    given: \"$.paths[*][get,post,put,patch,delete]\"\n\
  \    then:\n      field: description\n      function: truthy\n  fsx-operation-tags:\n    description: Operations must have at least one tag\n    severity: error\n    given: \"$.paths[*][get,post,put,patch,delete]\"\n    then:\n      field: tags\n      function: truthy\n  fsx-operation-id:\n    description: Operations must have operationId\n    severity: error\n    given: \"$.paths[*][get,post,put,patch,delete]\"\n    then:\n      field: operationId\n      function: truthy\n  fsx-operation-id-camel-case:\n    description: operationId should use camelCase\n    severity: warn\n    given: \"$.paths[*][get,post,put,patch,delete].operationId\"\n    then:\n      function: pattern\n      functionOptions:\n        match: \"^[a-z][a-zA-Z0-9]*$\"\n  fsx-response-200:\n    description: POST operations should define 200 response\n    severity: warn\n    given: \"$.paths[*][post]\"\n    then:\n      field: responses.200\n      function: truthy\n  fsx-response-400:\n    description: Operations should\
  \ define 400 response\n    severity: warn\n    given: \"$.paths[*][get,post,put,patch,delete]\"\n    then:\n      field: responses.400\n      function: truthy\n  fsx-response-500:\n    description: Operations should define 500 response\n    severity: warn\n    given: \"$.paths[*][get,post,put,patch,delete]\"\n    then:\n      field: responses.500\n      function: truthy\n  fsx-schema-description:\n    description: Schema components should have descriptions\n    severity: warn\n    given: \"$.components.schemas[*]\"\n    then:\n      field: description\n      function: truthy\n  fsx-tags-title-case:\n    description: Operation tags should use Title Case\n    severity: warn\n    given: \"$.paths[*][*].tags[*]\"\n    then:\n      function: pattern\n      functionOptions:\n        match: \"^[A-Z][a-zA-Z0-9 ]*$\"\n  fsx-filesystem-type-documented:\n    description: FileSystem schema should define FileSystemType field\n    severity: warn\n    given: \"$.components.schemas.FileSystem.properties\"\
  \n    then:\n      field: FileSystemType\n      function: truthy\n  fsx-lifecycle-enum:\n    description: FileSystem lifecycle should define enum values\n    severity: info\n    given: \"$.components.schemas.FileSystem.properties.Lifecycle\"\n    then:\n      field: enum\n      function: truthy\n  fsx-backup-type-enum:\n    description: Backup type should define enum values\n    severity: info\n    given: \"$.components.schemas.Backup.properties.Type\"\n    then:\n      field: enum\n      function: truthy\n  fsx-parameter-description:\n    description: Parameters must have descriptions\n    severity: error\n    given: \"$.paths[*][get,post,put,patch,delete].parameters[*]\"\n    then:\n      field: description\n      function: truthy\n  fsx-path-param-required:\n    description: Path parameters must be required\n    severity: error\n    given: \"$.paths[*][get,post,put,patch,delete].parameters[?(@.in=='path')]\"\n    then:\n      field: required\n      function: truthy\n  fsx-schema-properties:\n\
  \    description: Object schemas should define properties\n    severity: warn\n    given: \"$.components.schemas[?(@.type=='object')]\"\n    then:\n      field: properties\n      function: truthy\n  fsx-request-body-json:\n    description: POST request bodies should define application/json content\n    severity: warn\n    given: \"$.paths[*].post.requestBody.content\"\n    then:\n      function: schema\n      functionOptions:\n        schema:\n          type: object\n          required: [\"application/json\"]\n  fsx-create-prefix:\n    description: POST creation operationIds should start with 'create'\n    severity: warn\n    given: \"$.paths[*].post.operationId\"\n    then:\n      function: pattern\n      functionOptions:\n        match: \"^(create|describe|list|tag|associate)\"\n  fsx-delete-operation:\n    description: DELETE operations should have a description\n    severity: warn\n    given: \"$.paths[*].delete\"\n    then:\n      field: description\n      function: truthy\n  fsx-storage-capacity-documented:\n\
  \    description: FileSystem schema should document StorageCapacity\n    severity: warn\n    given: \"$.components.schemas.FileSystem.properties\"\n    then:\n      field: StorageCapacity\n      function: truthy\n  fsx-resource-arn-consistent:\n    description: Resource ARN field should be named ResourceARN\n    severity: info\n    given: \"$.components.schemas[*].properties.ResourceARN\"\n    then:\n      field: type\n      function: truthy\n  fsx-tag-schema-required:\n    description: Tag schema must require Key field\n    severity: warn\n    given: \"$.components.schemas.Tag.required\"\n    then:\n      function: schema\n      functionOptions:\n        schema:\n          type: array\n          contains:\n            const: Key\n  fsx-svm-filesystem-required:\n    description: StorageVirtualMachine must reference FileSystemId\n    severity: warn\n    given: \"$.components.schemas.StorageVirtualMachine.required\"\n    then:\n      function: schema\n      functionOptions:\n        schema:\n\
  \          type: array\n          contains:\n            const: FileSystemId\n"
source_yaml_url: https://raw.githubusercontent.com/api-evangelist/amazon-fsx/refs/heads/main/rules/amazon-fsx-spectral-rules.yml
tags:
- File Systems
- Lustre
- NetApp
- OpenZFS
- Storage
- Windows
- Spectral
- Linting
- API Governance
---
