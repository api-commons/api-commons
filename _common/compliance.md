---
name: Compliance
description: Compliance attestations and certifications (SOC 2, ISO, HIPAA, GDPR) relevant to the API.
image: /images/compliance.png
url: '#'
machineReadable: true
source: legal
tags:
  - Compliance
  - Certifications
  - Trust
yaml_example: |
  - name: Compliance
    type: Compliance
    description: The compliance of the Example Weather API, harvested from its own page.
    url: compliance/example-weather-api-compliance.yml
    source_date: '2026-11-09'
    data:
      compliance: 0.1.0
      provider: Example Weather API
      aid: example-weather-api
      url: https://trust.weather.example.com/
      source_date: '2026-11-09'
      x-apis-io-derivation:
        synthetic: false
        method: harvested
        read: '2026-11-09'
        tool: engine/business/harvest-business.py
        model: claude-haiku-4-5
      trust_center:
        url: https://trust.weather.example.com/
      attestations:
      - framework: SOC2
        type: Type II
        scope: Forecast API and developer portal
        period: 12 months
        issuer: An independent third-party auditor
        report_access: nda
        text: Example Weather API has completed a SOC 2 Type II audit. The report is available under
          NDA.
      - framework: ISO27001
        type: certified
        scope: null
        period: null
        issuer: null
        report_access: on_request
        text: We are ISO/IEC 27001 certified. Certificates are available on request.

standards:
  - name: API Commons Compliance schema
    url: https://github.com/api-commons/compliance
    kind: API Commons (CC BY-NC-SA 4.0 artifacts, Apache-2.0 code)
  - name: NIST OSCAL
    url: https://pages.nist.gov/OSCAL/
    kind: NIST
  - name: CSA STAR Registry
    url: https://cloudsecurityalliance.org/star/registry
    kind: Cloud Security Alliance

tools:
  - name: API Commons Compliance schema + validator
    url: https://github.com/api-commons/compliance
    license: Apache-2.0
    category: Machine-readable schema
---
