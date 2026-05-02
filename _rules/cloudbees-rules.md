---
categories:
- cloudbees
description: Spectral linting rules defining API design standards and conventions for CloudBees.
layout: rules
name: CloudBees API Rules
provider_name: CloudBees
provider_slug: cloudbees
rule_count: 12
rules:
- description: API contact information must be present.
  given: $.info
  name: cloudbees-info-contact
  severity: error
- description: API license must be declared.
  given: $.info
  name: cloudbees-info-license
  severity: warn
- description: All server URLs must use HTTPS.
  given: $.servers[*].url
  name: cloudbees-server-https
  severity: error
- description: CloudBees Feature Management server URLs must point at x-api.rollout.io.
  given: $.servers[?(@.url && @.url.indexOf('rollout.io') > -1)].url
  name: cloudbees-feature-mgmt-base
  severity: warn
- description: CloudBees CD/RO server URLs must include /rest/v1.0.
  given: $.servers[?(@.url && @.url.indexOf('cloudbees') > -1 && @.url.indexOf('cd') > -1)].url
  name: cloudbees-cd-versioned
  severity: warn
- description: A bearer or basic security scheme must be declared.
  given: $.components.securitySchemes
  name: cloudbees-bearer-or-basic
  severity: error
- description: Every operation must declare at least one tag.
  given: $.paths[*][get,post,put,patch,delete]
  name: cloudbees-operation-tags
  severity: warn
- description: Every operation must include a short summary.
  given: $.paths[*][get,post,put,patch,delete]
  name: cloudbees-operation-summary
  severity: warn
- description: Every operation must declare a unique operationId.
  given: $.paths[*][get,post,put,patch,delete]
  name: cloudbees-operation-id
  severity: error
- description: Mutating operations should declare 4xx error responses.
  given: $.paths[*][post,put,patch,delete].responses
  name: cloudbees-error-responses
  severity: warn
- description: Feature Management endpoints should document the 555 rate-limit response.
  given: $.paths[?(@property.match(/applications|environments|flags|experiments/))][*].responses
  name: cloudbees-rate-limit-555
  severity: info
- description: List endpoints should support page/limit pagination params.
  given: $.paths[?(@property.match(/applications$|environments$|flags$|experiments$|audit$/))].get.parameters[*].name
  name: cloudbees-pagination
  severity: info
rules_file: rules/cloudbees-rules.yml
rules_url: https://raw.githubusercontent.com/api-evangelist/cloudbees/refs/heads/main/rules/cloudbees-rules.yml
severity_counts:
  error: 4
  hint: 0
  info: 2
  warn: 6
slug: cloudbees-rules
source_filename: cloudbees-rules.yml
source_heading: Spectral Ruleset
source_yaml: "extends:\n  - spectral:oas\n\n# Spectral linting rules tuned for the CloudBees API surface.\n# Validates conventions across CloudBees CI (Jenkins-derived), CloudBees\n# CD/RO, and CloudBees Feature Management (Rollout) — JSON responses,\n# token-based auth, and resource-oriented paths.\nrules:\n  cloudbees-info-contact:\n    description: API contact information must be present.\n    severity: error\n    given: \"$.info\"\n    then:\n      field: contact\n      function: truthy\n\n  cloudbees-info-license:\n    description: API license must be declared.\n    severity: warn\n    given: \"$.info\"\n    then:\n      field: license\n      function: truthy\n\n  cloudbees-server-https:\n    description: All server URLs must use HTTPS.\n    severity: error\n    given: \"$.servers[*].url\"\n    then:\n      function: pattern\n      functionOptions:\n        match: \"^https://\"\n\n  cloudbees-feature-mgmt-base:\n    description: CloudBees Feature Management server URLs must point at\
  \ x-api.rollout.io.\n    severity: warn\n    given: \"$.servers[?(@.url && @.url.indexOf('rollout.io') > -1)].url\"\n    then:\n      function: pattern\n      functionOptions:\n        match: \"/public-api(/|$)\"\n\n  cloudbees-cd-versioned:\n    description: CloudBees CD/RO server URLs must include /rest/v1.0.\n    severity: warn\n    given: \"$.servers[?(@.url && @.url.indexOf('cloudbees') > -1 && @.url.indexOf('cd') > -1)].url\"\n    then:\n      function: pattern\n      functionOptions:\n        match: \"/rest/v1\\\\.0(/|$)\"\n\n  cloudbees-bearer-or-basic:\n    description: A bearer or basic security scheme must be declared.\n    severity: error\n    given: \"$.components.securitySchemes\"\n    then:\n      function: truthy\n\n  cloudbees-operation-tags:\n    description: Every operation must declare at least one tag.\n    severity: warn\n    given: \"$.paths[*][get,post,put,patch,delete]\"\n    then:\n      field: tags\n      function: schema\n      functionOptions:\n        schema:\n\
  \          type: array\n          minItems: 1\n\n  cloudbees-operation-summary:\n    description: Every operation must include a short summary.\n    severity: warn\n    given: \"$.paths[*][get,post,put,patch,delete]\"\n    then:\n      field: summary\n      function: truthy\n\n  cloudbees-operation-id:\n    description: Every operation must declare a unique operationId.\n    severity: error\n    given: \"$.paths[*][get,post,put,patch,delete]\"\n    then:\n      field: operationId\n      function: truthy\n\n  cloudbees-error-responses:\n    description: Mutating operations should declare 4xx error responses.\n    severity: warn\n    given: \"$.paths[*][post,put,patch,delete].responses\"\n    then:\n      function: schema\n      functionOptions:\n        schema:\n          type: object\n          anyOf:\n            - required: [\"400\"]\n            - required: [\"401\"]\n            - required: [\"403\"]\n            - required: [\"404\"]\n            - required: [\"422\"]\n\n  cloudbees-rate-limit-555:\n\
  \    description: Feature Management endpoints should document the 555 rate-limit response.\n    severity: info\n    given: \"$.paths[?(@property.match(/applications|environments|flags|experiments/))][*].responses\"\n    then:\n      function: schema\n      functionOptions:\n        schema:\n          type: object\n          anyOf:\n            - required: [\"555\"]\n            - required: [\"429\"]\n\n  cloudbees-pagination:\n    description: List endpoints should support page/limit pagination params.\n    severity: info\n    given: \"$.paths[?(@property.match(/applications$|environments$|flags$|experiments$|audit$/))].get.parameters[*].name\"\n    then:\n      function: enumeration\n      functionOptions:\n        values:\n          - page\n          - limit\n          - offset\n          - per_page\n          - cursor\n          - sort\n"
source_yaml_url: https://raw.githubusercontent.com/api-evangelist/cloudbees/refs/heads/main/rules/cloudbees-rules.yml
tags:
- CI/CD
- Continuous Delivery
- Continuous Integration
- DevOps
- Feature Flags
- Feature Management
- Jenkins
- Release Orchestration
- Software Delivery
- Spectral
- Linting
- API Governance
---
