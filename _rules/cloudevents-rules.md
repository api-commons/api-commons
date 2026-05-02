---
api_specs:
- filename: cloudevents-http-asyncapi.yml
  format: yaml
  label: CloudEvents Specification
  slug: cloudevents-spec
  spec_type: AsyncAPI
  url: https://raw.githubusercontent.com/api-evangelist/cloudevents/refs/heads/main/asyncapi/cloudevents-http-asyncapi.yml
- filename: cloudevents-subscriptions-openapi.yml
  format: yaml
  label: CloudEvents Subscriptions API
  slug: cloudevents-subscriptions
  spec_type: OpenAPI
  url: https://raw.githubusercontent.com/api-evangelist/cloudevents/refs/heads/main/openapi/cloudevents-subscriptions-openapi.yml
categories:
- cloudevents
description: Spectral linting rules defining API design standards and conventions for CloudEvents.
layout: rules
name: CloudEvents API Rules
provider_name: CloudEvents
provider_slug: cloudevents
rule_count: 9
rules:
- description: API contact information must be present.
  given: $.info
  name: cloudevents-info-contact
  severity: error
- description: API license must be declared (CloudEvents publishes under Apache-2.0).
  given: $.info
  name: cloudevents-info-license
  severity: warn
- description: CloudEvents-aligned APIs should declare an Apache-2.0 license.
  given: $.info.license.name
  name: cloudevents-info-license-apache
  severity: warn
- description: All server URLs must use HTTPS.
  given: $.servers[*].url
  name: cloudevents-server-https
  severity: error
- description: Every operation must declare a unique operationId.
  given: $.paths[*][get,post,put,patch,delete]
  name: cloudevents-operation-id
  severity: error
- description: Every operation must declare at least one tag.
  given: $.paths[*][get,post,put,patch,delete]
  name: cloudevents-operation-tags
  severity: warn
- description: Every operation must include a short summary.
  given: $.paths[*][get,post,put,patch,delete]
  name: cloudevents-operation-summary
  severity: warn
- description: Mutating operations should declare 4xx error responses.
  given: $.paths[*][post,put,patch,delete].responses
  name: cloudevents-error-responses
  severity: warn
- description: Subscription schemas must include the CloudEvents-required `id`, `source`, and `sink` attributes.
  given: $.components.schemas.Subscription.properties
  name: cloudevents-subscription-required-attributes
  severity: warn
rules_file: rules/cloudevents-rules.yml
rules_url: https://raw.githubusercontent.com/api-evangelist/cloudevents/refs/heads/main/rules/cloudevents-rules.yml
severity_counts:
  error: 3
  hint: 0
  info: 0
  warn: 6
slug: cloudevents-rules
source_filename: cloudevents-rules.yml
source_heading: Spectral Ruleset
source_yaml: "extends:\n  - spectral:oas\n\n# Spectral linting rules for the CloudEvents Subscriptions API and any\n# OpenAPI describing CloudEvents-compliant endpoints.\nrules:\n  cloudevents-info-contact:\n    description: API contact information must be present.\n    severity: error\n    given: \"$.info\"\n    then:\n      field: contact\n      function: truthy\n\n  cloudevents-info-license:\n    description: API license must be declared (CloudEvents publishes under Apache-2.0).\n    severity: warn\n    given: \"$.info\"\n    then:\n      field: license\n      function: truthy\n\n  cloudevents-info-license-apache:\n    description: CloudEvents-aligned APIs should declare an Apache-2.0 license.\n    severity: warn\n    given: \"$.info.license.name\"\n    then:\n      function: pattern\n      functionOptions:\n        match: \"(?i)apache\"\n\n  cloudevents-server-https:\n    description: All server URLs must use HTTPS.\n    severity: error\n    given: \"$.servers[*].url\"\n    then:\n \
  \     function: pattern\n      functionOptions:\n        match: \"^https://\"\n\n  cloudevents-operation-id:\n    description: Every operation must declare a unique operationId.\n    severity: error\n    given: \"$.paths[*][get,post,put,patch,delete]\"\n    then:\n      field: operationId\n      function: truthy\n\n  cloudevents-operation-tags:\n    description: Every operation must declare at least one tag.\n    severity: warn\n    given: \"$.paths[*][get,post,put,patch,delete]\"\n    then:\n      field: tags\n      function: schema\n      functionOptions:\n        schema:\n          type: array\n          minItems: 1\n\n  cloudevents-operation-summary:\n    description: Every operation must include a short summary.\n    severity: warn\n    given: \"$.paths[*][get,post,put,patch,delete]\"\n    then:\n      field: summary\n      function: truthy\n\n  cloudevents-error-responses:\n    description: Mutating operations should declare 4xx error responses.\n    severity: warn\n    given: \"\
  $.paths[*][post,put,patch,delete].responses\"\n    then:\n      function: schema\n      functionOptions:\n        schema:\n          type: object\n          anyOf:\n            - required: [\"400\"]\n            - required: [\"401\"]\n            - required: [\"403\"]\n            - required: [\"404\"]\n\n  cloudevents-subscription-required-attributes:\n    description: Subscription schemas must include the CloudEvents-required `id`, `source`, and `sink` attributes.\n    severity: warn\n    given: \"$.components.schemas.Subscription.properties\"\n    then:\n      function: schema\n      functionOptions:\n        schema:\n          type: object\n          required: [\"id\", \"source\", \"sink\"]\n"
source_yaml_url: https://raw.githubusercontent.com/api-evangelist/cloudevents/refs/heads/main/rules/cloudevents-rules.yml
tags:
- Cloud Native
- Events
- Graduated
- Interoperability
- Messaging
- Specification
- Spectral
- Linting
- API Governance
---
