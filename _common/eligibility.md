---
name: Eligibility
description: >-
  Who may use an API and where: the countries served and excluded, the kinds of entity that may sign up, restricted uses, whether KYC, KYB or manual approval is required, and a minimum age. The first question an automated onboarding flow has to answer, read verbatim from the provider's own terms.
image: /images/terms-of-service.png
url: '#'
machineReadable: true
source: legal
tags:
  - Legal
  - Onboarding
  - Availability
aliases:
  - Availability
  - Supported Countries
  - Who Can Use This API
yaml_example: |
  - name: Eligibility
    type: Eligibility
    description: The eligibility of the Example Weather API, harvested from its own page.
    url: eligibility/example-weather-api-eligibility.yml
    source_date: '2026-11-09'
    data:
      eligibility: 0.1.0
      provider: Example Weather API
      aid: example-weather-api
      url: https://weather.example.com/legal/api-terms
      source_date: '2026-11-09'
      x-apis-io-derivation:
        synthetic: false
        method: harvested
        read: '2026-11-09'
        tool: engine/business/harvest-business.py
        model: claude-haiku-4-5
      countries:
        served: []
        excluded:
        - KP
        - IR
        text: The API is not available to users located in North Korea or Iran.
      entity_types:
      - type: business
        text: The API is offered to businesses and individual developers.
      - type: developer
        text: The API is offered to businesses and individual developers.
      restricted_uses:
      - summary: Aviation safety decisions
        text: The API must not be used as the sole source of information for aviation safety decisions.
      verification:
        kyc: null
        kyb: false
        approval_required: true
        text: Commercial plans require approval by our team before production keys are issued.
      minimum_age:
        value: 18
        text: You must be at least 18 years old to create an account.

standards:
  - name: API Commons Eligibility schema
    url: https://github.com/api-commons/eligibility
    kind: API Commons (CC BY-NC-SA 4.0 artifacts, Apache-2.0 code)
  - name: ISO 3166-1 alpha-2 country codes
    url: https://www.iso.org/iso-3166-country-codes.html
    kind: ISO

tools:
  - name: API Commons Eligibility schema + validator
    url: https://github.com/api-commons/eligibility
    license: Apache-2.0
    category: Machine-readable schema

related_properties:
  - terms-of-service
  - privacy-policy
  - compliance
  - signup
  - plans
---
