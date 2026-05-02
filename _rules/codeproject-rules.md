---
api_specs:
- filename: codeproject-rest-api-openapi.yml
  format: yaml
  label: CodeProject REST API
  slug: codeproject-api
  spec_type: OpenAPI
  url: https://raw.githubusercontent.com/api-evangelist/codeproject/refs/heads/main/openapi/codeproject-rest-api-openapi.yml
- filename: codeproject-ai-server-openapi.yml
  format: yaml
  label: CodeProject.AI Server API
  slug: codeproject-ai-server
  spec_type: OpenAPI
  url: https://raw.githubusercontent.com/api-evangelist/codeproject/refs/heads/main/openapi/codeproject-ai-server-openapi.yml
categories:
- codeproject
description: Spectral linting rules defining API design standards and conventions for CodeProject.
layout: rules
name: CodeProject API Rules
provider_name: CodeProject
provider_slug: codeproject
rule_count: 9
rules:
- description: API contact information must be present.
  given: $.info
  name: codeproject-info-contact
  severity: error
- description: Public CodeProject API servers must use HTTPS.
  given: $.servers[?(@.url && @.url.indexOf('codeproject.com') > -1)].url
  name: codeproject-public-server-https
  severity: error
- description: CodeProject.AI Server example server URL should reference localhost.
  given: $.servers[?(@.url && @.url.indexOf('localhost') > -1)].url
  name: codeproject-ai-server-localhost
  severity: info
- description: Every operation must declare a unique operationId.
  given: $.paths[*][get,post,put,patch,delete]
  name: codeproject-operation-id
  severity: error
- description: Operations must declare at least one tag.
  given: $.paths[*][get,post,put,patch,delete]
  name: codeproject-operation-tags
  severity: warn
- description: All paths must be versioned under /v1/.
  given: $.paths
  name: codeproject-version-prefix
  severity: warn
- description: My/* operations must require oauth2 with at least one scope.
  given: $.paths['/v1/My/Profile','/v1/My/Reputation','/v1/My/Articles','/v1/My/Answers','/v1/My/Blog','/v1/My/Bookmarks','/v1/My/Notifications','/v1/My/Tips'][get].security
  name: codeproject-oauth2-on-my
  severity: error
- description: Operations should declare 4xx error responses.
  given: $.paths[*][get,post,put,patch,delete].responses
  name: codeproject-error-responses
  severity: warn
- description: CodeProject.AI Server upload endpoints should accept multipart/form-data.
  given: $.paths[?(@property && @property.indexOf('/v1/vision/') > -1)].post.requestBody.content
  name: codeproject-ai-multipart
  severity: info
rules_file: rules/codeproject-rules.yml
rules_url: https://raw.githubusercontent.com/api-evangelist/codeproject/refs/heads/main/rules/codeproject-rules.yml
severity_counts:
  error: 4
  hint: 0
  info: 2
  warn: 3
slug: codeproject-rules
source_filename: codeproject-rules.yml
source_heading: Spectral Ruleset
source_yaml: "extends:\n  - spectral:oas\n\n# Spectral linting rules for CodeProject APIs.\n# Covers both the public REST API at api.codeproject.com (OAuth 2.0 protected,\n# read-mostly resources) and the locally hosted CodeProject.AI Server REST API\n# (no auth by default, multipart uploads, /v1/* paths).\nrules:\n  codeproject-info-contact:\n    description: API contact information must be present.\n    severity: error\n    given: \"$.info\"\n    then:\n      field: contact\n      function: truthy\n\n  codeproject-public-server-https:\n    description: Public CodeProject API servers must use HTTPS.\n    severity: error\n    given: \"$.servers[?(@.url && @.url.indexOf('codeproject.com') > -1)].url\"\n    then:\n      function: pattern\n      functionOptions:\n        match: \"^https://\"\n\n  codeproject-ai-server-localhost:\n    description: CodeProject.AI Server example server URL should reference localhost.\n    severity: info\n    given: \"$.servers[?(@.url && @.url.indexOf('localhost')\
  \ > -1)].url\"\n    then:\n      function: pattern\n      functionOptions:\n        match: \"localhost\"\n\n  codeproject-operation-id:\n    description: Every operation must declare a unique operationId.\n    severity: error\n    given: \"$.paths[*][get,post,put,patch,delete]\"\n    then:\n      field: operationId\n      function: truthy\n\n  codeproject-operation-tags:\n    description: Operations must declare at least one tag.\n    severity: warn\n    given: \"$.paths[*][get,post,put,patch,delete]\"\n    then:\n      field: tags\n      function: schema\n      functionOptions:\n        schema:\n          type: array\n          minItems: 1\n\n  codeproject-version-prefix:\n    description: All paths must be versioned under /v1/.\n    severity: warn\n    given: \"$.paths\"\n    then:\n      function: schema\n      functionOptions:\n        schema:\n          type: object\n          patternProperties:\n            \"^/v1/\": {}\n\n  codeproject-oauth2-on-my:\n    description: My/* operations\
  \ must require oauth2 with at least one scope.\n    severity: error\n    given: \"$.paths['/v1/My/Profile','/v1/My/Reputation','/v1/My/Articles','/v1/My/Answers','/v1/My/Blog','/v1/My/Bookmarks','/v1/My/Notifications','/v1/My/Tips'][get].security\"\n    then:\n      function: schema\n      functionOptions:\n        schema:\n          type: array\n          minItems: 1\n\n  codeproject-error-responses:\n    description: Operations should declare 4xx error responses.\n    severity: warn\n    given: \"$.paths[*][get,post,put,patch,delete].responses\"\n    then:\n      function: schema\n      functionOptions:\n        schema:\n          type: object\n          anyOf:\n            - required: [\"400\"]\n            - required: [\"401\"]\n            - required: [\"403\"]\n            - required: [\"404\"]\n\n  codeproject-ai-multipart:\n    description: CodeProject.AI Server upload endpoints should accept multipart/form-data.\n    severity: info\n    given: \"$.paths[?(@property && @property.indexOf('/v1/vision/')\
  \ > -1)].post.requestBody.content\"\n    then:\n      function: schema\n      functionOptions:\n        schema:\n          type: object\n          required: [\"multipart/form-data\"]\n"
source_yaml_url: https://raw.githubusercontent.com/api-evangelist/codeproject/refs/heads/main/rules/codeproject-rules.yml
tags:
- AI
- Articles
- Community
- Computer Vision
- Developer Community
- Face Recognition
- Forum
- Knowledge Base
- License Plate Recognition
- Object Detection
- Q&A
- Software Development
- Tutorials
- Spectral
- Linting
- API Governance
---
