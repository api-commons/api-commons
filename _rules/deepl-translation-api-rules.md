---
api_specs:
- filename: deepl-translation-api-openapi.yml
  format: yaml
  label: DeepL Translation API
  slug: deepl-translation-api
  spec_type: OpenAPI
  url: https://raw.githubusercontent.com/api-evangelist/deepl/refs/heads/main/openapi/deepl-translation-api-openapi.yml
categories:
- deepl
description: Spectral linting rules defining API design standards and conventions for DeepL.
layout: rules
name: DeepL API Rules
provider_name: DeepL
provider_slug: deepl
rule_count: 5
rules:
- description: API info should include the DeepL developer contact.
  given: $.info
  name: deepl-info-contact
  severity: warn
- description: Servers should reference api.deepl.com or api-free.deepl.com.
  given: $.servers[*].url
  name: deepl-base-url
  severity: warn
- description: API should declare the DeepL-Auth-Key authentication scheme.
  given: $.components.securitySchemes
  name: deepl-auth-key
  severity: error
- description: API should expose a /translate endpoint.
  given: $.paths
  name: deepl-translate-resource
  severity: error
- description: Operations should be tagged Translate, Documents, Glossaries, Languages, Usage, or Write.
  given: $.paths[*][*]
  name: deepl-operation-tags
  severity: warn
rules_file: rules/deepl-translation-api-rules.yml
rules_url: https://raw.githubusercontent.com/api-evangelist/deepl/refs/heads/main/rules/deepl-translation-api-rules.yml
severity_counts:
  error: 2
  hint: 0
  info: 0
  warn: 3
slug: deepl-translation-api-rules
source_filename: deepl-translation-api-rules.yml
source_heading: Spectral Ruleset
source_yaml: "extends:\n  - spectral:oas\nrules:\n  deepl-info-contact:\n    description: API info should include the DeepL developer contact.\n    given: $.info\n    severity: warn\n    then:\n      field: contact\n      function: truthy\n  deepl-base-url:\n    description: Servers should reference api.deepl.com or api-free.deepl.com.\n    given: $.servers[*].url\n    severity: warn\n    then:\n      function: pattern\n      functionOptions:\n        match: \"deepl\\\\.com\"\n  deepl-auth-key:\n    description: API should declare the DeepL-Auth-Key authentication scheme.\n    given: $.components.securitySchemes\n    severity: error\n    then:\n      field: authKey\n      function: truthy\n  deepl-translate-resource:\n    description: API should expose a /translate endpoint.\n    given: $.paths\n    severity: error\n    then:\n      function: pattern\n      functionOptions:\n        match: \"/translate\"\n  deepl-operation-tags:\n    description: Operations should be tagged Translate, Documents,\
  \ Glossaries, Languages, Usage, or Write.\n    given: $.paths[*][*]\n    severity: warn\n    then:\n      field: tags\n      function: truthy\n"
source_yaml_url: https://raw.githubusercontent.com/api-evangelist/deepl/refs/heads/main/rules/deepl-translation-api-rules.yml
tags:
- Artificial Intelligence
- Deep Learning
- Glossaries
- Localization
- Machine Learning
- Machine Translation
- Translation
- Spectral
- Linting
- API Governance
---
