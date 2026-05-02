---
api_specs:
- filename: arlula-openapi.yaml
  format: yaml
  label: Arlula API
  slug: arlula-api
  spec_type: OpenAPI
  url: https://raw.githubusercontent.com/api-evangelist/arlula/refs/heads/main/openapi/arlula-openapi.yaml
categories:
- arlula
description: Spectral linting rules defining API design standards and conventions for Arlula.
layout: rules
name: Arlula API Rules
provider_name: Arlula
provider_slug: arlula
rule_count: 30
rules:
- description: API must have a title.
  given: $.info
  name: arlula-info-title
  severity: error
- description: API must have a description.
  given: $.info
  name: arlula-info-description
  severity: warn
- description: API must have a version.
  given: $.info
  name: arlula-info-version
  severity: error
- description: API should have contact information.
  given: $.info
  name: arlula-info-contact
  severity: warn
- description: Must use OpenAPI 3.0.x.
  given: $
  name: arlula-openapi-version
  severity: error
- description: API must have servers defined.
  given: $
  name: arlula-servers-present
  severity: error
- description: All server URLs must use HTTPS.
  given: $.servers[*]
  name: arlula-servers-https
  severity: error
- description: API must have paths defined.
  given: $
  name: arlula-paths-present
  severity: error
- description: Path segments should use kebab-case or camelCase consistently.
  given: $.paths[*]~
  name: arlula-path-kebab-case
  severity: warn
- description: Every operation must have a summary.
  given: $.paths[*][get,post,put,patch,delete,options,head]
  name: arlula-operation-summary
  severity: error
- description: Every operation should have a description.
  given: $.paths[*][get,post,put,patch,delete,options,head]
  name: arlula-operation-description
  severity: warn
- description: Every operation must have tags.
  given: $.paths[*][get,post,put,patch,delete,options,head]
  name: arlula-operation-tags
  severity: error
- description: Every operation must have an operationId.
  given: $.paths[*][get,post,put,patch,delete,options,head]
  name: arlula-operation-id
  severity: error
- description: Parameters should have descriptions.
  given: $.paths[*][get,post,put,patch,delete][parameters][*]
  name: arlula-parameter-description
  severity: warn
- description: Parameters must have a schema.
  given: $.paths[*][get,post,put,patch,delete][parameters][*]
  name: arlula-parameter-schema
  severity: error
- description: Request bodies must have content defined.
  given: $.paths[*][post,put,patch].requestBody
  name: arlula-request-body-content
  severity: error
- description: POST/PUT/PATCH operations should accept application/json.
  given: $.paths[*][post,put,patch].requestBody.content
  name: arlula-request-body-json
  severity: warn
- description: GET operations should define a 200 response.
  given: $.paths[*].get.responses
  name: arlula-response-200
  severity: warn
- description: Responses must have descriptions.
  given: $.paths[*][get,post,put,patch,delete].responses[*]
  name: arlula-response-description
  severity: error
- description: Operations should document 401 Unauthorized responses.
  given: $.paths[*][get,post,put,patch,delete].responses
  name: arlula-response-401
  severity: warn
- description: Operations should document 500 error responses.
  given: $.paths[*][get,post,put,patch,delete].responses
  name: arlula-response-500
  severity: warn
- description: Schemas in components should have titles.
  given: $.components.schemas[*]
  name: arlula-schema-title
  severity: warn
- description: Schemas should have descriptions.
  given: $.components.schemas[*]
  name: arlula-schema-description
  severity: warn
- description: Schema properties should have descriptions.
  given: $.components.schemas[*].properties[*]
  name: arlula-property-description
  severity: warn
- description: Schema properties should have examples.
  given: $.components.schemas[*].properties[*]
  name: arlula-property-example
  severity: info
- description: API must define security schemes.
  given: $.components
  name: arlula-security-defined
  severity: error
- description: Arlula API uses HTTP Basic authentication.
  given: $.components.securitySchemes.BasicAuth
  name: arlula-security-basic-auth
  severity: error
- description: Archive search must use POST method.
  given: $.paths['/api/archive/search']
  name: arlula-archive-search-post
  severity: warn
- description: Tasking search must use POST method.
  given: $.paths['/api/tasking/search']
  name: arlula-tasking-search-post
  severity: warn
- description: Resource data download should support binary responses.
  given: $.paths['/api/resource/{resource}/data'].get.responses['200'].content
  name: arlula-resource-data-binary
  severity: info
rules_file: rules/arlula-spectral-rules.yml
rules_url: https://raw.githubusercontent.com/api-evangelist/arlula/refs/heads/main/rules/arlula-spectral-rules.yml
severity_counts:
  error: 14
  hint: 0
  info: 2
  warn: 14
slug: arlula-spectral-rules
source_filename: arlula-spectral-rules.yml
source_heading: Spectral Ruleset
source_yaml: "rules:\n  # Info Rules\n  arlula-info-title:\n    description: API must have a title.\n    message: \"Info object must have a non-empty title.\"\n    severity: error\n    given: \"$.info\"\n    then:\n      field: title\n      function: truthy\n\n  arlula-info-description:\n    description: API must have a description.\n    message: \"Info object must have a non-empty description.\"\n    severity: warn\n    given: \"$.info\"\n    then:\n      field: description\n      function: truthy\n\n  arlula-info-version:\n    description: API must have a version.\n    message: \"Info object must have a version.\"\n    severity: error\n    given: \"$.info\"\n    then:\n      field: version\n      function: truthy\n\n  arlula-info-contact:\n    description: API should have contact information.\n    message: \"Info object should include contact details.\"\n    severity: warn\n    given: \"$.info\"\n    then:\n      field: contact\n      function: truthy\n\n  # OpenAPI Version\n  arlula-openapi-version:\n\
  \    description: Must use OpenAPI 3.0.x.\n    message: \"OpenAPI version must be 3.0.x.\"\n    severity: error\n    given: \"$\"\n    then:\n      field: openapi\n      function: pattern\n      functionOptions:\n        match: \"^3\\\\.0\\\\.\"\n\n  # Servers Rules\n  arlula-servers-present:\n    description: API must have servers defined.\n    message: \"Servers array must be present and non-empty.\"\n    severity: error\n    given: \"$\"\n    then:\n      field: servers\n      function: truthy\n\n  arlula-servers-https:\n    description: All server URLs must use HTTPS.\n    message: \"Server URL must use HTTPS.\"\n    severity: error\n    given: \"$.servers[*]\"\n    then:\n      field: url\n      function: pattern\n      functionOptions:\n        match: \"^https://\"\n\n  # Paths Rules\n  arlula-paths-present:\n    description: API must have paths defined.\n    message: \"Paths object must be present and non-empty.\"\n    severity: error\n    given: \"$\"\n    then:\n      field: paths\n\
  \      function: truthy\n\n  arlula-path-kebab-case:\n    description: Path segments should use kebab-case or camelCase consistently.\n    message: \"Path should follow consistent casing conventions.\"\n    severity: warn\n    given: \"$.paths[*]~\"\n    then:\n      function: pattern\n      functionOptions:\n        match: \"^/[a-zA-Z0-9/{}_-]*$\"\n\n  # Operations Rules\n  arlula-operation-summary:\n    description: Every operation must have a summary.\n    message: \"Operation must have a summary.\"\n    severity: error\n    given: \"$.paths[*][get,post,put,patch,delete,options,head]\"\n    then:\n      field: summary\n      function: truthy\n\n  arlula-operation-description:\n    description: Every operation should have a description.\n    message: \"Operation should have a description.\"\n    severity: warn\n    given: \"$.paths[*][get,post,put,patch,delete,options,head]\"\n    then:\n      field: description\n      function: truthy\n\n  arlula-operation-tags:\n    description: Every\
  \ operation must have tags.\n    message: \"Operation must have at least one tag.\"\n    severity: error\n    given: \"$.paths[*][get,post,put,patch,delete,options,head]\"\n    then:\n      field: tags\n      function: truthy\n\n  arlula-operation-id:\n    description: Every operation must have an operationId.\n    message: \"Operation must have an operationId.\"\n    severity: error\n    given: \"$.paths[*][get,post,put,patch,delete,options,head]\"\n    then:\n      field: operationId\n      function: truthy\n\n  # Parameters Rules\n  arlula-parameter-description:\n    description: Parameters should have descriptions.\n    message: \"Parameter should have a description.\"\n    severity: warn\n    given: \"$.paths[*][get,post,put,patch,delete][parameters][*]\"\n    then:\n      field: description\n      function: truthy\n\n  arlula-parameter-schema:\n    description: Parameters must have a schema.\n    message: \"Parameter must have a schema.\"\n    severity: error\n    given: \"$.paths[*][get,post,put,patch,delete][parameters][*]\"\
  \n    then:\n      field: schema\n      function: truthy\n\n  # Request Body Rules\n  arlula-request-body-content:\n    description: Request bodies must have content defined.\n    message: \"Request body must have content.\"\n    severity: error\n    given: \"$.paths[*][post,put,patch].requestBody\"\n    then:\n      field: content\n      function: truthy\n\n  arlula-request-body-json:\n    description: POST/PUT/PATCH operations should accept application/json.\n    message: \"Request body should support application/json content type.\"\n    severity: warn\n    given: \"$.paths[*][post,put,patch].requestBody.content\"\n    then:\n      function: truthy\n\n  # Response Rules\n  arlula-response-200:\n    description: GET operations should define a 200 response.\n    message: \"GET operation should have a 200 response.\"\n    severity: warn\n    given: \"$.paths[*].get.responses\"\n    then:\n      field: \"200\"\n      function: truthy\n\n  arlula-response-description:\n    description: Responses\
  \ must have descriptions.\n    message: \"Response must have a description.\"\n    severity: error\n    given: \"$.paths[*][get,post,put,patch,delete].responses[*]\"\n    then:\n      field: description\n      function: truthy\n\n  arlula-response-401:\n    description: Operations should document 401 Unauthorized responses.\n    message: \"Operation should define a 401 response.\"\n    severity: warn\n    given: \"$.paths[*][get,post,put,patch,delete].responses\"\n    then:\n      field: \"401\"\n      function: truthy\n\n  arlula-response-500:\n    description: Operations should document 500 error responses.\n    message: \"Operation should define a 500 response.\"\n    severity: warn\n    given: \"$.paths[*][get,post,put,patch,delete].responses\"\n    then:\n      field: \"500\"\n      function: truthy\n\n  # Schema Rules\n  arlula-schema-title:\n    description: Schemas in components should have titles.\n    message: \"Schema must have a title.\"\n    severity: warn\n    given: \"$.components.schemas[*]\"\
  \n    then:\n      field: title\n      function: truthy\n\n  arlula-schema-description:\n    description: Schemas should have descriptions.\n    message: \"Schema should have a description.\"\n    severity: warn\n    given: \"$.components.schemas[*]\"\n    then:\n      field: description\n      function: truthy\n\n  arlula-property-description:\n    description: Schema properties should have descriptions.\n    message: \"Schema property should have a description.\"\n    severity: warn\n    given: \"$.components.schemas[*].properties[*]\"\n    then:\n      field: description\n      function: truthy\n\n  arlula-property-example:\n    description: Schema properties should have examples.\n    message: \"Schema property should have an example value.\"\n    severity: info\n    given: \"$.components.schemas[*].properties[*]\"\n    then:\n      field: example\n      function: truthy\n\n  # Security Rules\n  arlula-security-defined:\n    description: API must define security schemes.\n    message:\
  \ \"Security schemes must be defined in components.\"\n    severity: error\n    given: \"$.components\"\n    then:\n      field: securitySchemes\n      function: truthy\n\n  arlula-security-basic-auth:\n    description: Arlula API uses HTTP Basic authentication.\n    message: \"BasicAuth security scheme must use http type with basic scheme.\"\n    severity: error\n    given: \"$.components.securitySchemes.BasicAuth\"\n    then:\n      field: type\n      function: enumeration\n      functionOptions:\n        values:\n          - http\n\n  # Satellite Imagery Specific Rules\n  arlula-archive-search-post:\n    description: Archive search must use POST method.\n    message: \"Archive search endpoint must use POST.\"\n    severity: warn\n    given: \"$.paths['/api/archive/search']\"\n    then:\n      field: post\n      function: truthy\n\n  arlula-tasking-search-post:\n    description: Tasking search must use POST method.\n    message: \"Tasking search endpoint must use POST.\"\n    severity:\
  \ warn\n    given: \"$.paths['/api/tasking/search']\"\n    then:\n      field: post\n      function: truthy\n\n  arlula-resource-data-binary:\n    description: Resource data download should support binary responses.\n    message: \"Resource data endpoint should return binary content type.\"\n    severity: info\n    given: \"$.paths['/api/resource/{resource}/data'].get.responses['200'].content\"\n    then:\n      function: truthy\n"
source_yaml_url: https://raw.githubusercontent.com/api-evangelist/arlula/refs/heads/main/rules/arlula-spectral-rules.yml
tags:
- Earth Observation
- Geospatial
- Imagery
- Remote Sensing
- Satellites
- Spectral
- Linting
- API Governance
---
