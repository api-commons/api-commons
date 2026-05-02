---
api_specs:
- filename: microsoft-azure-api-management-rest-api-openapi.yaml
  format: yaml
  label: Azure API Management REST API
  slug: azure-api-management-rest-api
  spec_type: OpenAPI
  url: https://raw.githubusercontent.com/api-evangelist/microsoft-azure-api-management/refs/heads/main/openapi/microsoft-azure-api-management-rest-api-openapi.yaml
- filename: microsoft-azure-api-management-gateway-openapi.yaml
  format: yaml
  label: Azure API Management Gateway
  slug: azure-api-management-gateway
  spec_type: OpenAPI
  url: https://raw.githubusercontent.com/api-evangelist/microsoft-azure-api-management/refs/heads/main/openapi/microsoft-azure-api-management-gateway-openapi.yaml
- filename: microsoft-azure-api-management-self-hosted-gateway-openapi.yaml
  format: yaml
  label: Azure API Management Self-Hosted Gateway
  slug: azure-api-management-self-hosted-gateway
  spec_type: OpenAPI
  url: https://raw.githubusercontent.com/api-evangelist/microsoft-azure-api-management/refs/heads/main/openapi/microsoft-azure-api-management-self-hosted-gateway-openapi.yaml
- filename: microsoft-azure-api-management-ai-gateway-openapi.yaml
  format: yaml
  label: Azure API Management AI Gateway
  slug: azure-api-management-ai-gateway
  spec_type: OpenAPI
  url: https://raw.githubusercontent.com/api-evangelist/microsoft-azure-api-management/refs/heads/main/openapi/microsoft-azure-api-management-ai-gateway-openapi.yaml
- filename: microsoft-azure-api-management-developer-portal-openapi.yaml
  format: yaml
  label: Azure API Management Developer Portal
  slug: azure-api-management-developer-portal
  spec_type: OpenAPI
  url: https://raw.githubusercontent.com/api-evangelist/microsoft-azure-api-management/refs/heads/main/openapi/microsoft-azure-api-management-developer-portal-openapi.yaml
categories:
- azure
description: Spectral linting rules defining API design standards and conventions for Microsoft Azure API Management.
layout: rules
name: Microsoft Azure API Management API Rules
provider_name: Microsoft Azure API Management
provider_slug: microsoft-azure-api-management
rule_count: 15
rules:
- description: Operation IDs must follow the {Resource}_{Action} pattern (e.g., Api_Get, ApiManagementService_CreateOrUpdate).
  given: $.paths[*][get,put,post,patch,delete,head].operationId
  name: azure-operation-id-format
  severity: warn
- description: Every operation must have a description.
  given: $.paths[*][get,put,post,patch,delete,head]
  name: azure-operation-description
  severity: warn
- description: Every operation must have a summary.
  given: $.paths[*][get,put,post,patch,delete,head]
  name: azure-operation-summary
  severity: warn
- description: Every operation must have at least one tag.
  given: $.paths[*][get,put,post,patch,delete,head]
  name: azure-operation-tags
  severity: warn
- description: Paths should follow Azure Resource Manager conventions, starting with /subscriptions or /providers.
  given: $.paths
  name: azure-arm-path-pattern
  severity: info
- description: Resource provider paths must use a Microsoft.* namespace (e.g., Microsoft.ApiManagement).
  given: $.paths
  name: azure-provider-namespace
  severity: warn
- description: The API should define an azure_auth OAuth2 security scheme.
  given: $.components.securitySchemes
  name: azure-auth-scheme-defined
  severity: info
- description: The API should have global security referencing azure_auth.
  given: $
  name: azure-global-security
  severity: info
- description: Operations should include a default error response for consistent error handling.
  given: $.paths[*][get,put,post,patch,delete,head].responses
  name: azure-error-response
  severity: info
- description: Success responses must have a description.
  given: $.paths[*][get,put,post,patch,delete,head].responses.200
  name: azure-response-description
  severity: warn
- description: The API info object must specify a version.
  given: $.info
  name: azure-api-version-info
  severity: error
- description: ARM APIs should use https://management.azure.com as the server URL.
  given: $.servers[*].url
  name: azure-management-server
  severity: info
- description: The operation ID prefix (before underscore) should align with the operation tag for consistency.
  given: $.paths[*][get,put,post,patch,delete,head]
  name: azure-operationid-tag-consistency
  severity: info
- description: API info should include contact information.
  given: $.info
  name: azure-contact-info
  severity: info
- description: API info should include license information.
  given: $.info
  name: azure-license-info
  severity: info
rules_file: rules/microsoft-azure-api-management-rules.yaml
rules_url: https://raw.githubusercontent.com/api-evangelist/microsoft-azure-api-management/refs/heads/main/rules/microsoft-azure-api-management-rules.yaml
severity_counts:
  error: 1
  hint: 0
  info: 8
  warn: 6
slug: microsoft-azure-api-management-rules
source_filename: microsoft-azure-api-management-rules.yaml
source_heading: Spectral Ruleset
source_yaml: "extends:\n  - spectral:oas\n\nrules:\n\n  # ---------------------------------------------------------------------------\n  # Operation ID naming convention: {Resource}_{Action}\n  # ---------------------------------------------------------------------------\n  azure-operation-id-format:\n    description: Operation IDs must follow the {Resource}_{Action} pattern (e.g., Api_Get, ApiManagementService_CreateOrUpdate).\n    severity: warn\n    given: \"$.paths[*][get,put,post,patch,delete,head].operationId\"\n    then:\n      function: pattern\n      functionOptions:\n        match: \"^[A-Z][a-zA-Z0-9]*(_[A-Z][a-zA-Z0-9]*)+$\"\n\n  # ---------------------------------------------------------------------------\n  # Every operation must have a description\n  # ---------------------------------------------------------------------------\n  azure-operation-description:\n    description: Every operation must have a description.\n    severity: warn\n    given: \"$.paths[*][get,put,post,patch,delete,head]\"\
  \n    then:\n      field: description\n      function: truthy\n\n  # ---------------------------------------------------------------------------\n  # Every operation must have a summary\n  # ---------------------------------------------------------------------------\n  azure-operation-summary:\n    description: Every operation must have a summary.\n    severity: warn\n    given: \"$.paths[*][get,put,post,patch,delete,head]\"\n    then:\n      field: summary\n      function: truthy\n\n  # ---------------------------------------------------------------------------\n  # Every operation must have tags\n  # ---------------------------------------------------------------------------\n  azure-operation-tags:\n    description: Every operation must have at least one tag.\n    severity: warn\n    given: \"$.paths[*][get,put,post,patch,delete,head]\"\n    then:\n      field: tags\n      function: truthy\n\n  # ---------------------------------------------------------------------------\n  # ARM paths\
  \ should start with /subscriptions or /providers\n  # ---------------------------------------------------------------------------\n  azure-arm-path-pattern:\n    description: Paths should follow Azure Resource Manager conventions, starting with /subscriptions or /providers.\n    severity: info\n    given: \"$.paths\"\n    then:\n      function: pattern\n      functionOptions:\n        match: \"^/(subscriptions|providers)/.*$\"\n    # NOTE: This rule is expressed at the path-key level via the custom function below.\n    # Spectral cannot iterate object keys natively, so we use oas-path-param instead.\n\n  # ---------------------------------------------------------------------------\n  # Paths containing /providers/ must use Microsoft.* namespace\n  # ---------------------------------------------------------------------------\n  azure-provider-namespace:\n    description: Resource provider paths must use a Microsoft.* namespace (e.g., Microsoft.ApiManagement).\n    severity: warn\n    given:\
  \ \"$.paths\"\n    then:\n      function: schema\n      functionOptions:\n        schema:\n          type: object\n          patternProperties:\n            \".*providers.*\":\n              description: Provider paths are present\n          additionalProperties: true\n\n  # ---------------------------------------------------------------------------\n  # Security scheme should define OAuth2 (azure_auth)\n  # ---------------------------------------------------------------------------\n  azure-auth-scheme-defined:\n    description: The API should define an azure_auth OAuth2 security scheme.\n    severity: info\n    given: \"$.components.securitySchemes\"\n    then:\n      field: azure_auth\n      function: truthy\n\n  # ---------------------------------------------------------------------------\n  # Global security should reference azure_auth\n  # ---------------------------------------------------------------------------\n  azure-global-security:\n    description: The API should have global\
  \ security referencing azure_auth.\n    severity: info\n    given: \"$\"\n    then:\n      field: security\n      function: truthy\n\n  # ---------------------------------------------------------------------------\n  # Responses should include a default or error response\n  # ---------------------------------------------------------------------------\n  azure-error-response:\n    description: Operations should include a default error response for consistent error handling.\n    severity: info\n    given: \"$.paths[*][get,put,post,patch,delete,head].responses\"\n    then:\n      function: schema\n      functionOptions:\n        schema:\n          type: object\n          anyOf:\n            - required: [\"default\"]\n            - required: [\"4XX\"]\n            - required: [\"400\"]\n            - required: [\"404\"]\n\n  # ---------------------------------------------------------------------------\n  # 200 response should have a description\n  # ---------------------------------------------------------------------------\n\
  \  azure-response-description:\n    description: Success responses must have a description.\n    severity: warn\n    given: \"$.paths[*][get,put,post,patch,delete,head].responses.200\"\n    then:\n      field: description\n      function: truthy\n\n  # ---------------------------------------------------------------------------\n  # Info must have a version\n  # ---------------------------------------------------------------------------\n  azure-api-version-info:\n    description: The API info object must specify a version.\n    severity: error\n    given: \"$.info\"\n    then:\n      field: version\n      function: truthy\n\n  # ---------------------------------------------------------------------------\n  # Server URL should use management.azure.com for ARM APIs\n  # ---------------------------------------------------------------------------\n  azure-management-server:\n    description: ARM APIs should use https://management.azure.com as the server URL.\n    severity: info\n    given:\
  \ \"$.servers[*].url\"\n    then:\n      function: pattern\n      functionOptions:\n        match: \"^https://\"\n\n  # ---------------------------------------------------------------------------\n  # Operation ID should match the tag prefix\n  # ---------------------------------------------------------------------------\n  azure-operationid-tag-consistency:\n    description: The operation ID prefix (before underscore) should align with the operation tag for consistency.\n    severity: info\n    given: \"$.paths[*][get,put,post,patch,delete,head]\"\n    then:\n      function: schema\n      functionOptions:\n        schema:\n          type: object\n          required:\n            - operationId\n            - tags\n\n  # ---------------------------------------------------------------------------\n  # Contact info should be present\n  # ---------------------------------------------------------------------------\n  azure-contact-info:\n    description: API info should include contact information.\n\
  \    severity: info\n    given: \"$.info\"\n    then:\n      field: contact\n      function: truthy\n\n  # ---------------------------------------------------------------------------\n  # License should be present\n  # ---------------------------------------------------------------------------\n  azure-license-info:\n    description: API info should include license information.\n    severity: info\n    given: \"$.info\"\n    then:\n      field: license\n      function: truthy\n"
source_yaml_url: https://raw.githubusercontent.com/api-evangelist/microsoft-azure-api-management/refs/heads/main/rules/microsoft-azure-api-management-rules.yaml
tags:
- AI Gateway
- API Gateway
- API Management
- Enterprise
- Microsoft Azure
- Spectral
- Linting
- API Governance
---
