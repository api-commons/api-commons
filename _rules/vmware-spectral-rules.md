---
api_specs:
- filename: vmware-vsphere-api-openapi.yml
  format: yaml
  label: vSphere API
  slug: vsphere-api
  spec_type: OpenAPI
  url: https://raw.githubusercontent.com/api-evangelist/vmware/refs/heads/main/openapi/vmware-vsphere-api-openapi.yml
- filename: openapi.yaml
  format: yaml
  label: vCloud Director API
  slug: vcloud-director-api
  spec_type: OpenAPI
  url: https://developer.vmware.com/apis/vmware-cloud-director/latest/openapi/
- filename: openapi.yaml
  format: yaml
  label: NSX-T Data Center API
  slug: nsx-t-data-center-api
  spec_type: OpenAPI
  url: https://developer.vmware.com/apis/nsx-t/latest/openapi/
- filename: openapi.yaml
  format: yaml
  label: vRealize Automation API
  slug: vrealize-automation-api
  spec_type: OpenAPI
  url: https://developer.vmware.com/apis/vrealize-automation/latest/openapi/
- filename: openapi.yaml
  format: yaml
  label: VMware Cloud on AWS API
  slug: vmware-cloud-on-aws-api
  spec_type: OpenAPI
  url: https://developer.vmware.com/apis/vmc/latest/openapi/
- filename: openapi.yaml
  format: yaml
  label: vRealize Operations API
  slug: vrealize-operations-api
  spec_type: OpenAPI
  url: https://developer.vmware.com/apis/vrealize-operations/latest/openapi/
categories:
- info
- 'no'
- operation
- response
description: Spectral linting rules defining API design standards and conventions for VMware.
layout: rules
name: VMware API Rules
provider_name: VMware
provider_slug: vmware
rule_count: 7
rules:
- description: Info title must be present
  given: $.info
  name: info-title-required
  severity: error
- description: Info description must be present
  given: $.info
  name: info-description-required
  severity: error
- description: Every operation must have an operationId
  given: $.paths[*][get,post,put,patch,delete]
  name: operation-operationid-required
  severity: error
- description: Every operation must have a summary
  given: $.paths[*][get,post,put,patch,delete]
  name: operation-summary-required
  severity: error
- description: Every operation must have tags
  given: $.paths[*][get,post,put,patch,delete]
  name: operation-tags-required
  severity: error
- description: Every response must have a description
  given: $.paths[*][get,post,put,patch,delete].responses[*]
  name: response-description-required
  severity: error
- description: Descriptions must not be empty
  given: $..description
  name: no-empty-descriptions
  severity: error
rules_file: rules/vmware-spectral-rules.yml
rules_url: https://raw.githubusercontent.com/api-evangelist/vmware/refs/heads/main/rules/vmware-spectral-rules.yml
severity_counts:
  error: 7
  hint: 0
  info: 0
  warn: 0
slug: vmware-spectral-rules
source_filename: vmware-spectral-rules.yml
source_heading: Spectral Ruleset
source_yaml: "rules:\n  info-title-required:\n    description: Info title must be present\n    severity: error\n    given: $.info\n    then: {field: title, function: truthy}\n  info-description-required:\n    description: Info description must be present\n    severity: error\n    given: $.info\n    then: {field: description, function: truthy}\n  operation-operationid-required:\n    description: Every operation must have an operationId\n    severity: error\n    given: $.paths[*][get,post,put,patch,delete]\n    then: {field: operationId, function: truthy}\n  operation-summary-required:\n    description: Every operation must have a summary\n    severity: error\n    given: $.paths[*][get,post,put,patch,delete]\n    then: {field: summary, function: truthy}\n  operation-tags-required:\n    description: Every operation must have tags\n    severity: error\n    given: $.paths[*][get,post,put,patch,delete]\n    then: {field: tags, function: truthy}\n  response-description-required:\n    description:\
  \ Every response must have a description\n    severity: error\n    given: $.paths[*][get,post,put,patch,delete].responses[*]\n    then: {field: description, function: truthy}\n  no-empty-descriptions:\n    description: Descriptions must not be empty\n    severity: error\n    given: $..description\n    then: {function: truthy}\n"
source_yaml_url: https://raw.githubusercontent.com/api-evangelist/vmware/refs/heads/main/rules/vmware-spectral-rules.yml
tags:
- Cloud Computing
- Container Management
- Hybrid Cloud
- Infrastructure
- Virtualization
- Spectral
- Linting
- API Governance
---
