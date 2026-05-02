---
categories:
- baxter
description: Spectral linting rules defining API design standards and conventions for Baxter International.
layout: rules
name: Baxter International API Rules
provider_name: Baxter International
provider_slug: baxter-international
rule_count: 5
rules:
- description: All Baxter DeviceBridge API operations must use authentication.
  given: $.paths.*.*.security
  name: baxter-auth-required
  severity: error
- description: All Baxter API operations must have an operationId.
  given: $.paths.*.*
  name: baxter-operation-id-required
  severity: error
- description: Device endpoints should document device identifier parameters.
  given: $.paths[?(@property.match('device'))].*.parameters
  name: baxter-device-id-documented
  severity: warn
- description: Patient data endpoints should require patient identification.
  given: $.paths[?(@property.match('patient'))].*.parameters
  name: baxter-patient-id-required
  severity: error
- description: FHIR endpoints should produce FHIR-compliant content types.
  given: $.paths[?(@property.match('fhir'))].*.responses.200.content
  name: baxter-fhir-content-type
  severity: warn
rules_file: rules/baxter-spectral-rules.yml
rules_url: https://raw.githubusercontent.com/api-evangelist/baxter-international/refs/heads/main/rules/baxter-spectral-rules.yml
severity_counts:
  error: 3
  hint: 0
  info: 0
  warn: 2
slug: baxter-spectral-rules
source_filename: baxter-spectral-rules.yml
source_heading: Spectral Ruleset
source_yaml: "rules:\n  baxter-auth-required:\n    description: All Baxter DeviceBridge API operations must use authentication.\n    message: Operation must include authentication security requirement.\n    severity: error\n    given: $.paths.*.*.security\n    then:\n      function: schema\n      functionOptions:\n        schema:\n          type: array\n          minItems: 1\n\n  baxter-operation-id-required:\n    description: All Baxter API operations must have an operationId.\n    message: Operation is missing operationId.\n    severity: error\n    given: $.paths.*.*\n    then:\n      field: operationId\n      function: truthy\n\n  baxter-device-id-documented:\n    description: Device endpoints should document device identifier parameters.\n    message: Device endpoint should document deviceId path or query parameter.\n    severity: warn\n    given: $.paths[?(@property.match('device'))].*.parameters\n    then:\n      function: schema\n      functionOptions:\n        schema:\n         \
  \ type: array\n          minItems: 1\n\n  baxter-patient-id-required:\n    description: Patient data endpoints should require patient identification.\n    message: Patient data endpoint should document patient identifier parameter.\n    severity: error\n    given: $.paths[?(@property.match('patient'))].*.parameters\n    then:\n      function: schema\n      functionOptions:\n        schema:\n          type: array\n          minItems: 1\n\n  baxter-fhir-content-type:\n    description: FHIR endpoints should produce FHIR-compliant content types.\n    message: FHIR endpoint should produce application/fhir+json content type.\n    severity: warn\n    given: $.paths[?(@property.match('fhir'))].*.responses.200.content\n    then:\n      function: truthy\n"
source_yaml_url: https://raw.githubusercontent.com/api-evangelist/baxter-international/refs/heads/main/rules/baxter-spectral-rules.yml
tags:
- Healthcare
- Medical Devices
- Infusion Pumps
- Patient Monitoring
- Connected Health
- Spectral
- Linting
- API Governance
---
