---
api_specs:
- filename: atandt-wireless-apis.yaml
  format: yaml
  label: AT&T Wireless APIs
  slug: att-wireless-apis
  spec_type: OpenAPI
  url: https://raw.githubusercontent.com/api-evangelist/atandt/refs/heads/main/openapi/atandt-wireless-apis.yaml
- filename: atandt-network-apis.yaml
  format: yaml
  label: AT&T 5G Network APIs
  slug: att-network-apis
  spec_type: OpenAPI
  url: https://raw.githubusercontent.com/api-evangelist/atandt/refs/heads/main/openapi/atandt-network-apis.yaml
- filename: atandt-enterprise-connectivity-apis.yaml
  format: yaml
  label: AT&T Enterprise Connectivity APIs
  slug: att-enterprise-connectivity-apis
  spec_type: OpenAPI
  url: https://raw.githubusercontent.com/api-evangelist/atandt/refs/heads/main/openapi/atandt-enterprise-connectivity-apis.yaml
categories:
- atandt
description: Spectral linting rules defining API design standards and conventions for AT&T.
layout: rules
name: AT&T API Rules
provider_name: AT&T
provider_slug: atandt
rule_count: 27
rules:
- description: AT&T APIs must have a title in the info object
  given: $.info
  name: atandt-info-title-required
  severity: error
- description: AT&T APIs must include a description
  given: $.info
  name: atandt-info-description-required
  severity: error
- description: AT&T APIs must specify a version
  given: $.info
  name: atandt-info-version-required
  severity: error
- description: AT&T APIs must include contact information
  given: $.info
  name: atandt-info-contact-required
  severity: warn
- description: AT&T APIs must include terms of service
  given: $.info
  name: atandt-info-terms-required
  severity: warn
- description: AT&T APIs must use OpenAPI 3.0.x
  given: $
  name: atandt-openapi-version
  severity: error
- description: AT&T APIs must define at least one server
  given: $
  name: atandt-servers-required
  severity: error
- description: AT&T API servers must use HTTPS
  given: $.servers[*]
  name: atandt-server-url-https
  severity: error
- description: AT&T API servers should use att.com domains
  given: $.servers[*]
  name: atandt-server-att-domain
  severity: warn
- description: All AT&T API operations must have an operationId
  given: $.paths[*][get,post,put,patch,delete,options,head]
  name: atandt-operation-id-required
  severity: error
- description: All AT&T API operations must have a summary
  given: $.paths[*][get,post,put,patch,delete,options,head]
  name: atandt-operation-summary-required
  severity: error
- description: All AT&T API operations must have a description
  given: $.paths[*][get,post,put,patch,delete,options,head]
  name: atandt-operation-description-required
  severity: warn
- description: All AT&T API operations must have tags
  given: $.paths[*][get,post,put,patch,delete,options,head]
  name: atandt-operation-tags-required
  severity: warn
- description: All AT&T API parameters must have a description
  given: $.paths[*][*].parameters[*]
  name: atandt-parameter-description-required
  severity: warn
- description: Path parameters must be marked as required
  given: $.paths[*][*].parameters[?(@.in == 'path')]
  name: atandt-path-parameter-required
  severity: error
- description: AT&T API request bodies must define content
  given: $.paths[*][*].requestBody
  name: atandt-request-body-content-required
  severity: error
- description: AT&T API request bodies should support application/json
  given: $.paths[*][*].requestBody.content
  name: atandt-request-body-json
  severity: warn
- description: All AT&T API responses must have a description
  given: $.paths[*][*].responses[*]
  name: atandt-response-description-required
  severity: error
- description: AT&T API operations must define at least one success response
  given: $.paths[*][get,post,put,patch,delete]
  name: atandt-success-response-required
  severity: error
- description: AT&T POST/PUT/PATCH operations should define 400 response
  given: $.paths[*][post,put,patch].responses
  name: atandt-error-400-defined
  severity: warn
- description: AT&T API operations should define 401 response
  given: $.paths[*][get,post,put,patch,delete].responses
  name: atandt-error-401-defined
  severity: warn
- description: AT&T API component schemas must have a type
  given: $.components.schemas[*]
  name: atandt-schema-type-required
  severity: warn
- description: AT&T API component schemas must have a description
  given: $.components.schemas[*]
  name: atandt-schema-description-required
  severity: warn
- description: AT&T APIs must define security schemes
  given: $.components
  name: atandt-security-schemes-required
  severity: error
- description: AT&T APIs should use OAuth 2.0
  given: $.components.securitySchemes[*]
  name: atandt-security-oauth2
  severity: warn
- description: AT&T CAMARA APIs must use E.164 format for phone numbers
  given: $.components.schemas[*].properties.phoneNumber
  name: atandt-phone-number-e164
  severity: warn
- description: AT&T APIs must define top-level tags
  given: $
  name: atandt-tags-defined
  severity: warn
rules_file: rules/atandt-spectral-rules.yml
rules_url: https://raw.githubusercontent.com/api-evangelist/atandt/refs/heads/main/rules/atandt-spectral-rules.yml
severity_counts:
  error: 13
  hint: 0
  info: 0
  warn: 14
slug: atandt-spectral-rules
source_filename: atandt-spectral-rules.yml
source_heading: Spectral Ruleset
source_yaml: "rules:\n  # Info / Metadata Rules\n  atandt-info-title-required:\n    description: AT&T APIs must have a title in the info object\n    message: info.title is required for AT&T APIs\n    severity: error\n    given: $.info\n    then:\n      field: title\n      function: truthy\n\n  atandt-info-description-required:\n    description: AT&T APIs must include a description\n    message: info.description is required for AT&T APIs\n    severity: error\n    given: $.info\n    then:\n      field: description\n      function: truthy\n\n  atandt-info-version-required:\n    description: AT&T APIs must specify a version\n    message: info.version is required for AT&T APIs\n    severity: error\n    given: $.info\n    then:\n      field: version\n      function: truthy\n\n  atandt-info-contact-required:\n    description: AT&T APIs must include contact information\n    message: info.contact is required for AT&T APIs\n    severity: warn\n    given: $.info\n    then:\n      field: contact\n \
  \     function: truthy\n\n  atandt-info-terms-required:\n    description: AT&T APIs must include terms of service\n    message: info.termsOfService is required for AT&T APIs\n    severity: warn\n    given: $.info\n    then:\n      field: termsOfService\n      function: truthy\n\n  # OpenAPI Version\n  atandt-openapi-version:\n    description: AT&T APIs must use OpenAPI 3.0.x\n    message: openapi must be 3.0.x\n    severity: error\n    given: $\n    then:\n      field: openapi\n      function: pattern\n      functionOptions:\n        match: '^3\\.0\\.\\d+$'\n\n  # Servers\n  atandt-servers-required:\n    description: AT&T APIs must define at least one server\n    message: servers array is required\n    severity: error\n    given: $\n    then:\n      field: servers\n      function: truthy\n\n  atandt-server-url-https:\n    description: AT&T API servers must use HTTPS\n    message: Server URL must use HTTPS\n    severity: error\n    given: $.servers[*]\n    then:\n      field: url\n    \
  \  function: pattern\n      functionOptions:\n        match: '^https://'\n\n  atandt-server-att-domain:\n    description: AT&T API servers should use att.com domains\n    message: Server URL should use att.com domain\n    severity: warn\n    given: $.servers[*]\n    then:\n      field: url\n      function: pattern\n      functionOptions:\n        match: '\\.att\\.com'\n\n  # Operations\n  atandt-operation-id-required:\n    description: All AT&T API operations must have an operationId\n    message: operationId is required for all operations\n    severity: error\n    given: $.paths[*][get,post,put,patch,delete,options,head]\n    then:\n      field: operationId\n      function: truthy\n\n  atandt-operation-summary-required:\n    description: All AT&T API operations must have a summary\n    message: summary is required for all operations\n    severity: error\n    given: $.paths[*][get,post,put,patch,delete,options,head]\n    then:\n      field: summary\n      function: truthy\n\n  atandt-operation-description-required:\n\
  \    description: All AT&T API operations must have a description\n    message: description is required for all operations\n    severity: warn\n    given: $.paths[*][get,post,put,patch,delete,options,head]\n    then:\n      field: description\n      function: truthy\n\n  atandt-operation-tags-required:\n    description: All AT&T API operations must have tags\n    message: tags array is required for all operations\n    severity: warn\n    given: $.paths[*][get,post,put,patch,delete,options,head]\n    then:\n      field: tags\n      function: truthy\n\n  # Parameters\n  atandt-parameter-description-required:\n    description: All AT&T API parameters must have a description\n    message: description is required for all parameters\n    severity: warn\n    given: $.paths[*][*].parameters[*]\n    then:\n      field: description\n      function: truthy\n\n  atandt-path-parameter-required:\n    description: Path parameters must be marked as required\n    message: Path parameters must have required=true\n\
  \    severity: error\n    given: $.paths[*][*].parameters[?(@.in == 'path')]\n    then:\n      field: required\n      function: truthy\n\n  # Request Bodies\n  atandt-request-body-content-required:\n    description: AT&T API request bodies must define content\n    message: requestBody.content is required\n    severity: error\n    given: $.paths[*][*].requestBody\n    then:\n      field: content\n      function: truthy\n\n  atandt-request-body-json:\n    description: AT&T API request bodies should support application/json\n    message: requestBody should include application/json content type\n    severity: warn\n    given: $.paths[*][*].requestBody.content\n    then:\n      function: schema\n      functionOptions:\n        schema:\n          type: object\n          required:\n            - application/json\n\n  # Responses\n  atandt-response-description-required:\n    description: All AT&T API responses must have a description\n    message: Response description is required\n    severity:\
  \ error\n    given: $.paths[*][*].responses[*]\n    then:\n      field: description\n      function: truthy\n\n  atandt-success-response-required:\n    description: AT&T API operations must define at least one success response\n    message: At least one 2xx response is required\n    severity: error\n    given: $.paths[*][get,post,put,patch,delete]\n    then:\n      function: schema\n      functionOptions:\n        schema:\n          type: object\n          properties:\n            responses:\n              type: object\n          required:\n            - responses\n\n  atandt-error-400-defined:\n    description: AT&T POST/PUT/PATCH operations should define 400 response\n    message: 400 Bad Request response should be defined for mutating operations\n    severity: warn\n    given: $.paths[*][post,put,patch].responses\n    then:\n      function: schema\n      functionOptions:\n        schema:\n          type: object\n          required:\n            - '400'\n\n  atandt-error-401-defined:\n\
  \    description: AT&T API operations should define 401 response\n    message: 401 Unauthorized response should be defined for secured operations\n    severity: warn\n    given: $.paths[*][get,post,put,patch,delete].responses\n    then:\n      function: schema\n      functionOptions:\n        schema:\n          type: object\n          required:\n            - '401'\n\n  # Schemas\n  atandt-schema-type-required:\n    description: AT&T API component schemas must have a type\n    message: Schema type is required\n    severity: warn\n    given: $.components.schemas[*]\n    then:\n      field: type\n      function: truthy\n\n  atandt-schema-description-required:\n    description: AT&T API component schemas must have a description\n    message: Schema description is required\n    severity: warn\n    given: $.components.schemas[*]\n    then:\n      field: description\n      function: truthy\n\n  # Security\n  atandt-security-schemes-required:\n    description: AT&T APIs must define security schemes\n\
  \    message: components.securitySchemes is required\n    severity: error\n    given: $.components\n    then:\n      field: securitySchemes\n      function: truthy\n\n  atandt-security-oauth2:\n    description: AT&T APIs should use OAuth 2.0\n    message: OAuth 2.0 security scheme should be defined\n    severity: warn\n    given: $.components.securitySchemes[*]\n    then:\n      field: type\n      function: enumeration\n      functionOptions:\n        values:\n          - oauth2\n\n  # Phone Number Format (CAMARA / AT&T specific)\n  atandt-phone-number-e164:\n    description: AT&T CAMARA APIs must use E.164 format for phone numbers\n    message: Phone number properties should use E.164 pattern\n    severity: warn\n    given: $.components.schemas[*].properties.phoneNumber\n    then:\n      field: pattern\n      function: truthy\n\n  # Tags\n  atandt-tags-defined:\n    description: AT&T APIs must define top-level tags\n    message: Top-level tags array is required\n    severity: warn\n \
  \   given: $\n    then:\n      field: tags\n      function: truthy\n"
source_yaml_url: https://raw.githubusercontent.com/api-evangelist/atandt/refs/heads/main/rules/atandt-spectral-rules.yml
tags:
- Telecommunications
- Fortune 100
- Wireless
- Wireline
- Broadband
- Enterprise
- 5G
- Network
- Spectral
- Linting
- API Governance
---
