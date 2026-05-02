---
api_specs:
- filename: amazon-firewall-manager-openapi.yml
  format: yaml
  label: AWS Firewall Manager API
  slug: aws-firewall-manager-api
  spec_type: OpenAPI
  url: https://raw.githubusercontent.com/api-evangelist/amazon-firewall-manager/refs/heads/main/openapi/amazon-firewall-manager-openapi.yml
categories:
- fms
description: Spectral linting rules defining API design standards and conventions for Amazon Firewall Manager.
layout: rules
name: Amazon Firewall Manager API Rules
provider_name: Amazon Firewall Manager
provider_slug: amazon-firewall-manager
rule_count: 25
rules:
- description: API must include contact information
  given: $.info
  name: fms-info-contact
  severity: warn
- description: API must have a description
  given: $.info
  name: fms-info-description
  severity: error
- description: All server URLs must use HTTPS
  given: $.servers[*].url
  name: fms-server-https
  severity: error
- description: Operations must have a summary
  given: $.paths[*][get,post,put,patch,delete]
  name: fms-operation-summary
  severity: error
- description: Operations should have a description
  given: $.paths[*][get,post,put,patch,delete]
  name: fms-operation-description
  severity: warn
- description: Operations must have at least one tag
  given: $.paths[*][get,post,put,patch,delete]
  name: fms-operation-tags
  severity: error
- description: Operations must have operationId
  given: $.paths[*][get,post,put,patch,delete]
  name: fms-operation-id
  severity: error
- description: operationId should use camelCase
  given: $.paths[*][get,post,put,patch,delete].operationId
  name: fms-operation-id-camel-case
  severity: warn
- description: GET and POST operations should define 200 response
  given: $.paths[*][get,post]
  name: fms-response-200
  severity: warn
- description: Operations should define 400 response
  given: $.paths[*][get,post,put,patch,delete]
  name: fms-response-400
  severity: warn
- description: Operations should define 500 response
  given: $.paths[*][get,post,put,patch,delete]
  name: fms-response-500
  severity: warn
- description: Operations accessing resources by ID should define 404
  given: $.paths[*~'\{[^}]+\}'][get,put,patch,delete].responses
  name: fms-response-404
  severity: warn
- description: Parameters must have descriptions
  given: $.paths[*][get,post,put,patch,delete].parameters[*]
  name: fms-parameter-description
  severity: error
- description: Path parameters must be marked as required
  given: $.paths[*][get,post,put,patch,delete].parameters[?(@.in=='path')]
  name: fms-path-param-required
  severity: error
- description: Schema components should have descriptions
  given: $.components.schemas[*]
  name: fms-schema-description
  severity: warn
- description: Operation tags should use Title Case
  given: $.paths[*][*].tags[*]
  name: fms-tags-title-case
  severity: warn
- description: Collection GET operationIds should start with 'list'
  given: $.paths[*~'[^}]$'].get.operationId
  name: fms-list-operation-prefix
  severity: warn
- description: PUT policy requests should define a request body
  given: $.paths[*].post.requestBody
  name: fms-put-policy-request
  severity: error
- description: Policies should document RemediationEnabled field in schema
  given: $.components.schemas.Policy.properties
  name: fms-policy-remediation-documented
  severity: warn
- description: SecurityServicePolicyData Type should define allowed enum values
  given: $.components.schemas.SecurityServicePolicyData.properties.Type
  name: fms-security-service-type-enum
  severity: warn
- description: DELETE operations should have a description
  given: $.paths[*].delete
  name: fms-delete-operation
  severity: warn
- description: Admin account endpoint should be documented
  given: $.paths
  name: fms-admin-account-documented
  severity: info
- description: Compliance endpoint should be documented
  given: $.paths
  name: fms-compliance-endpoint-documented
  severity: info
- description: Resource set endpoint should be documented
  given: $.paths
  name: fms-resource-set-documented
  severity: info
- description: Object schemas should define properties
  given: $.components.schemas[?(@.type=='object')]
  name: fms-schema-properties-defined
  severity: warn
rules_file: rules/amazon-firewall-manager-spectral-rules.yml
rules_url: https://raw.githubusercontent.com/api-evangelist/amazon-firewall-manager/refs/heads/main/rules/amazon-firewall-manager-spectral-rules.yml
severity_counts:
  error: 8
  hint: 0
  info: 3
  warn: 14
slug: amazon-firewall-manager-spectral-rules
source_filename: amazon-firewall-manager-spectral-rules.yml
source_heading: Spectral Ruleset
source_yaml: "# Amazon Firewall Manager Spectral Rules\nextends: spectral:oas\nrules:\n  fms-info-contact:\n    description: API must include contact information\n    severity: warn\n    given: \"$.info\"\n    then:\n      field: contact\n      function: truthy\n  fms-info-description:\n    description: API must have a description\n    severity: error\n    given: \"$.info\"\n    then:\n      field: description\n      function: truthy\n  fms-server-https:\n    description: All server URLs must use HTTPS\n    severity: error\n    given: \"$.servers[*].url\"\n    then:\n      function: pattern\n      functionOptions:\n        match: \"^https://\"\n  fms-operation-summary:\n    description: Operations must have a summary\n    severity: error\n    given: \"$.paths[*][get,post,put,patch,delete]\"\n    then:\n      field: summary\n      function: truthy\n  fms-operation-description:\n    description: Operations should have a description\n    severity: warn\n    given: \"$.paths[*][get,post,put,patch,delete]\"\
  \n    then:\n      field: description\n      function: truthy\n  fms-operation-tags:\n    description: Operations must have at least one tag\n    severity: error\n    given: \"$.paths[*][get,post,put,patch,delete]\"\n    then:\n      field: tags\n      function: truthy\n  fms-operation-id:\n    description: Operations must have operationId\n    severity: error\n    given: \"$.paths[*][get,post,put,patch,delete]\"\n    then:\n      field: operationId\n      function: truthy\n  fms-operation-id-camel-case:\n    description: operationId should use camelCase\n    severity: warn\n    given: \"$.paths[*][get,post,put,patch,delete].operationId\"\n    then:\n      function: pattern\n      functionOptions:\n        match: \"^[a-z][a-zA-Z0-9]*$\"\n  fms-response-200:\n    description: GET and POST operations should define 200 response\n    severity: warn\n    given: \"$.paths[*][get,post]\"\n    then:\n      field: responses.200\n      function: truthy\n  fms-response-400:\n    description: Operations\
  \ should define 400 response\n    severity: warn\n    given: \"$.paths[*][get,post,put,patch,delete]\"\n    then:\n      field: responses.400\n      function: truthy\n  fms-response-500:\n    description: Operations should define 500 response\n    severity: warn\n    given: \"$.paths[*][get,post,put,patch,delete]\"\n    then:\n      field: responses.500\n      function: truthy\n  fms-response-404:\n    description: Operations accessing resources by ID should define 404\n    severity: warn\n    given: \"$.paths[*~'\\\\{[^}]+\\\\}'][get,put,patch,delete].responses\"\n    then:\n      field: \"404\"\n      function: truthy\n  fms-parameter-description:\n    description: Parameters must have descriptions\n    severity: error\n    given: \"$.paths[*][get,post,put,patch,delete].parameters[*]\"\n    then:\n      field: description\n      function: truthy\n  fms-path-param-required:\n    description: Path parameters must be marked as required\n    severity: error\n    given: \"$.paths[*][get,post,put,patch,delete].parameters[?(@.in=='path')]\"\
  \n    then:\n      field: required\n      function: truthy\n  fms-schema-description:\n    description: Schema components should have descriptions\n    severity: warn\n    given: \"$.components.schemas[*]\"\n    then:\n      field: description\n      function: truthy\n  fms-tags-title-case:\n    description: Operation tags should use Title Case\n    severity: warn\n    given: \"$.paths[*][*].tags[*]\"\n    then:\n      function: pattern\n      functionOptions:\n        match: \"^[A-Z][a-zA-Z0-9 ]*$\"\n  fms-list-operation-prefix:\n    description: Collection GET operationIds should start with 'list'\n    severity: warn\n    given: \"$.paths[*~'[^}]$'].get.operationId\"\n    then:\n      function: pattern\n      functionOptions:\n        match: \"^list\"\n  fms-put-policy-request:\n    description: PUT policy requests should define a request body\n    severity: error\n    given: \"$.paths[*].post.requestBody\"\n    then:\n      field: content\n      function: truthy\n  fms-policy-remediation-documented:\n\
  \    description: Policies should document RemediationEnabled field in schema\n    message: \"Policy schema should include RemediationEnabled property\"\n    severity: warn\n    given: \"$.components.schemas.Policy.properties\"\n    then:\n      field: RemediationEnabled\n      function: truthy\n  fms-security-service-type-enum:\n    description: SecurityServicePolicyData Type should define allowed enum values\n    severity: warn\n    given: \"$.components.schemas.SecurityServicePolicyData.properties.Type\"\n    then:\n      field: enum\n      function: truthy\n  fms-delete-operation:\n    description: DELETE operations should have a description\n    severity: warn\n    given: \"$.paths[*].delete\"\n    then:\n      field: description\n      function: truthy\n  fms-admin-account-documented:\n    description: Admin account endpoint should be documented\n    severity: info\n    given: \"$.paths\"\n    then:\n      field: \"/fms/2018-01-01/admin-account\"\n      function: truthy\n  fms-compliance-endpoint-documented:\n\
  \    description: Compliance endpoint should be documented\n    severity: info\n    given: \"$.paths\"\n    then:\n      field: \"/fms/2018-01-01/compliance/{policyId}/detail/{memberAccountId}\"\n      function: truthy\n  fms-resource-set-documented:\n    description: Resource set endpoint should be documented\n    severity: info\n    given: \"$.paths\"\n    then:\n      field: \"/fms/2018-01-01/resource-set\"\n      function: truthy\n  fms-schema-properties-defined:\n    description: Object schemas should define properties\n    severity: warn\n    given: \"$.components.schemas[?(@.type=='object')]\"\n    then:\n      field: properties\n      function: truthy\n"
source_yaml_url: https://raw.githubusercontent.com/api-evangelist/amazon-firewall-manager/refs/heads/main/rules/amazon-firewall-manager-spectral-rules.yml
tags:
- Compliance
- Firewall
- Network Security
- Security
- Spectral
- Linting
- API Governance
---
