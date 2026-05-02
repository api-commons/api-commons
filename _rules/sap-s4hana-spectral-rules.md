---
api_specs:
- filename: overview
  format: yaml
  label: SAP S/4HANA Business Partner API
  slug: ''
  spec_type: OpenAPI
  url: https://api.sap.com/api/API_BUSINESS_PARTNER/overview
- filename: sap-s4hana-sales-order-openapi.yml
  format: yaml
  label: SAP S/4HANA Sales Order API
  slug: ''
  spec_type: OpenAPI
  url: https://raw.githubusercontent.com/api-evangelist/sap-s4hana/refs/heads/main/openapi/sap-s4hana-sales-order-openapi.yml
- filename: overview
  format: yaml
  label: SAP S/4HANA Purchase Order API
  slug: ''
  spec_type: OpenAPI
  url: https://api.sap.com/api/API_PURCHASEORDER_PROCESS_SRV/overview
- filename: overview
  format: yaml
  label: SAP S/4HANA Material Document API
  slug: ''
  spec_type: OpenAPI
  url: https://api.sap.com/api/API_MATERIAL_DOCUMENT_SRV/overview
- filename: overview
  format: yaml
  label: SAP S/4HANA Product Master API
  slug: ''
  spec_type: OpenAPI
  url: https://api.sap.com/api/API_PRODUCT_SRV/overview
- filename: overview
  format: yaml
  label: SAP S/4HANA Journal Entry API
  slug: ''
  spec_type: OpenAPI
  url: https://api.sap.com/api/API_JOURNALENTRY_SRV/overview
- filename: overview
  format: yaml
  label: SAP S/4HANA Billing Document API
  slug: ''
  spec_type: OpenAPI
  url: https://api.sap.com/api/API_BILLING_DOCUMENT_SRV/overview
- filename: overview
  format: yaml
  label: SAP S/4HANA Supplier Invoice API
  slug: ''
  spec_type: OpenAPI
  url: https://api.sap.com/api/API_SUPPLIERINVOICE_PROCESS_SRV/overview
- filename: overview
  format: yaml
  label: SAP S/4HANA Customer Return API
  slug: ''
  spec_type: OpenAPI
  url: https://api.sap.com/api/API_CUSTOMER_RETURN_SRV/overview
- filename: overview
  format: yaml
  label: SAP S/4HANA Purchase Requisition API
  slug: ''
  spec_type: OpenAPI
  url: https://api.sap.com/api/API_PURCHASEREQ_PROCESS_SRV/overview
- filename: overview
  format: yaml
  label: SAP S/4HANA Outbound Delivery API
  slug: ''
  spec_type: OpenAPI
  url: https://api.sap.com/api/API_OUTBOUND_DELIVERY_SRV_0002/overview
- filename: overview
  format: yaml
  label: SAP S/4HANA Inbound Delivery API
  slug: ''
  spec_type: OpenAPI
  url: https://api.sap.com/api/API_INBOUND_DELIVERY_SRV_0002/overview
- filename: overview
  format: yaml
  label: SAP S/4HANA Cost Center API
  slug: ''
  spec_type: OpenAPI
  url: https://api.sap.com/api/API_COSTCENTER_SRV/overview
- filename: overview
  format: yaml
  label: SAP S/4HANA GL Account API
  slug: ''
  spec_type: OpenAPI
  url: https://api.sap.com/api/API_GLACCOUNTINCHARTOFACCOUNTS_SRV/overview
- filename: overview
  format: yaml
  label: SAP S/4HANA Bank Master API
  slug: ''
  spec_type: OpenAPI
  url: https://api.sap.com/api/API_BANKDETAIL_SRV/overview
- filename: overview
  format: yaml
  label: SAP S/4HANA Production Order API
  slug: ''
  spec_type: OpenAPI
  url: https://api.sap.com/api/API_PRODUCTION_ORDER_2_SRV/overview
- filename: overview
  format: yaml
  label: SAP S/4HANA Maintenance Order API
  slug: ''
  spec_type: OpenAPI
  url: https://api.sap.com/api/API_MAINTENANCEORDER/overview
- filename: overview
  format: yaml
  label: SAP S/4HANA Workforce Timesheet API
  slug: ''
  spec_type: OpenAPI
  url: https://api.sap.com/api/API_MANAGE_WORKFORCE_TIMESHEET/overview
categories:
- info
- 'no'
- operation
- response
description: Spectral linting rules defining API design standards and conventions for SAP S/4HANA.
layout: rules
name: SAP S/4HANA API Rules
provider_name: SAP S/4HANA
provider_slug: sap-s4hana
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
rules_file: rules/sap-s4hana-spectral-rules.yml
rules_url: https://raw.githubusercontent.com/api-evangelist/sap-s4hana/refs/heads/main/rules/sap-s4hana-spectral-rules.yml
severity_counts:
  error: 7
  hint: 0
  info: 0
  warn: 0
slug: sap-s4hana-spectral-rules
source_filename: sap-s4hana-spectral-rules.yml
source_heading: Spectral Ruleset
source_yaml: "rules:\n  info-title-required:\n    description: Info title must be present\n    severity: error\n    given: $.info\n    then: {field: title, function: truthy}\n  info-description-required:\n    description: Info description must be present\n    severity: error\n    given: $.info\n    then: {field: description, function: truthy}\n  operation-operationid-required:\n    description: Every operation must have an operationId\n    severity: error\n    given: $.paths[*][get,post,put,patch,delete]\n    then: {field: operationId, function: truthy}\n  operation-summary-required:\n    description: Every operation must have a summary\n    severity: error\n    given: $.paths[*][get,post,put,patch,delete]\n    then: {field: summary, function: truthy}\n  operation-tags-required:\n    description: Every operation must have tags\n    severity: error\n    given: $.paths[*][get,post,put,patch,delete]\n    then: {field: tags, function: truthy}\n  response-description-required:\n    description:\
  \ Every response must have a description\n    severity: error\n    given: $.paths[*][get,post,put,patch,delete].responses[*]\n    then: {field: description, function: truthy}\n  no-empty-descriptions:\n    description: Descriptions must not be empty\n    severity: error\n    given: $..description\n    then: {function: truthy}\n"
source_yaml_url: https://raw.githubusercontent.com/api-evangelist/sap-s4hana/refs/heads/main/rules/sap-s4hana-spectral-rules.yml
tags:
- Business Applications
- Cloud
- Enterprise Resource Planning
- ERP
- Finance
- Human Resources
- Inventory
- Logistics
- Manufacturing
- Plant Maintenance
- Procurement
- S/4HANA
- Sales
- SAP
- Spectral
- Linting
- API Governance
---
