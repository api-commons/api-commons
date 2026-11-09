---
name: Privacy Policy
description: |
  Breaking up the privacy policy into machine-readable, schema defined properties that allow for the legal side of an API to be understood programmatically. A privacy policy sets the stage when it comes to consumption, helping consumers with what they can expect when it comes to how their data and usage of digital resources will be shared or sold. 
image: /images/privacy-policy.png
url: '#'
machineReadable: true
source: concept
tags:
  - Legal
aliases:
  - Privacy Notice
  - Privacy Statement
  - Data Protection Notice
yaml_example: |
  - name: Privacy Policy
    type: PrivacyPolicy
    description: The privacy policy of the Example Weather API, harvested from its own page.
    url: privacy/example-weather-api-privacy-policy.yml
    source_date: '2026-11-09'
    data:
      privacy_policy: 0.1.0
      provider: Example Weather API
      aid: example-weather-api
      url: https://weather.example.com/legal/privacy
      source_date: '2026-11-09'
      x-apis-io-derivation:
        synthetic: false
        method: harvested
        read: '2026-11-09'
        tool: engine/business/harvest-business.py
        model: claude-haiku-4-5
      role:
        value: processor
        text: When we process personal data on behalf of our API customers, we act as a data processor.
      data_categories:
      - category: contact
        text: We collect your name and email address when you create a developer account.
      - category: location
        text: API requests may include latitude and longitude coordinates.
      purposes:
      - purpose: Service delivery
        text: We use request data only to return the forecast you asked for.
      retention:
      - scope: API request logs
        period: 90 days
        text: API request logs are retained for 90 days.
      residency:
      - region: United States
        text: Customer data is stored in data centers located in the United States.
      transfers:
      - mechanism: SCC
        text: Transfers from the EEA rely on the Standard Contractual Clauses.
      subprocessors:
        url: https://weather.example.com/legal/subprocessors
        text: A current list of subprocessors is available on our subprocessors page.
      dpa:
        available: true
        url: https://weather.example.com/legal/dpa
        text: Our Data Processing Addendum is available to all customers.
      deletion:
        route: privacy@weather.example.com
        text: To request deletion of your data, email privacy@weather.example.com.
      rights:
      - right: access
        text: You have the right to access the personal data we hold about you.
      sale_or_sharing:
        stance: prohibited
        text: We do not sell your personal information.

standards:
  - name: API Commons Privacy Policy schema
    url: https://github.com/api-commons/privacy-policy
    kind: API Commons (CC BY-NC-SA 4.0 artifacts, Apache-2.0 code)
  - name: W3C Data Privacy Vocabulary (DPV)
    url: https://w3c.github.io/dpv/
    kind: W3C Community Group
  - name: GDPR — Regulation (EU) 2016/679
    url: https://eur-lex.europa.eu/eli/reg/2016/679/oj
    kind: EU
  - name: GDPR Articles 12–14 — Information to be provided to the data subject
    url: https://gdpr-info.eu/chapter-3/
    kind: EU
  - name: California Consumer Privacy Act (CCPA) / CPRA
    url: https://oag.ca.gov/privacy/ccpa
    kind: US-CA
  - name: ISO/IEC 27701 — Privacy Information Management
    url: https://www.iso.org/standard/71670.html
    kind: ISO
  - name: ISO/IEC 29100 — Privacy Framework
    url: https://www.iso.org/standard/45123.html
    kind: ISO
  - name: NIST Privacy Framework
    url: https://www.nist.gov/privacy-framework
    kind: NIST
  - name: schema.org PrivacyPolicy (WebPage subtype)
    url: https://schema.org/PrivacyPolicy
    kind: schema.org
  - name: IANA Link Relation — privacy-policy
    url: https://www.iana.org/assignments/link-relations/link-relations.xhtml
    kind: IANA
  - name: Global Privacy Control
    url: https://globalprivacycontrol.org/
    kind: Community / W3C CG
  - name: HIPAA Privacy Rule — 45 CFR Part 164 Subpart E
    url: https://www.hhs.gov/hipaa/for-professionals/privacy/index.html
    kind: US-HHS
  - name: Children's Online Privacy Protection Act (COPPA)
    url: https://www.ftc.gov/legal-library/browse/rules/childrens-online-privacy-protection-rule-coppa
    kind: US-FTC
  - name: LGPD — Lei Geral de Proteção de Dados (Brazil)
    url: https://www.gov.br/anpd/pt-br
    kind: BR

headers:
  - name: Link
    direction: response
    spec: RFC 8288
    description: May advertise rel="privacy-policy" pointing at the policy URL.
  - name: Sec-GPC
    direction: request
    spec: Global Privacy Control (W3C CG draft)
    description: Signals the user's opt-out of sale/sharing under CCPA/CPRA.
  - name: DNT
    direction: request
    spec: W3C Tracking Preference Expression (Note)
    description: Legacy Do Not Track signal; largely superseded by Sec-GPC.

status_codes:
  - code: '451'
    name: Unavailable For Legal Reasons
    spec: RFC 7725
    description: Resource withheld due to privacy/legal demand (e.g., jurisdictional block).

openapi_expression:
  - field: info.termsOfService
    spec: OpenAPI 3.x §4.8.2 Info Object
    description: Privacy policy is frequently linked alongside or from the ToS URL.
  - field: info.contact
    spec: OpenAPI 3.x §4.8.2 / Contact Object
    description: Contact for privacy / data-protection inquiries (e.g., DPO).

link_relations:
  - rel: privacy-policy
    spec: IANA Link Relations registry
    note: Used in Link headers, Atom, HAL, JSON:API, and HTML <link>.

governance_rules:
  - id: info-contact
    source: Spectral built-in
    description: Info contact should be present — useful for privacy/DPO routing.
  - id: info-license
    source: Spectral built-in
    description: License is required; complements (but does not replace) a privacy policy.

risk:
  compliance:
    - GDPR Art. 12 — transparent information, communication
    - GDPR Art. 13 — information collected from the data subject
    - GDPR Art. 14 — information collected from third parties
    - GDPR Art. 30 — records of processing activities
    - GDPR Art. 32 — security of processing
    - CCPA/CPRA — notice at collection, right to know / delete / opt-out of sale
    - HIPAA Privacy Rule — Notice of Privacy Practices
    - COPPA — parental consent for children under 13
    - LGPD — analogous transparency and rights obligations (Brazil)
    - PIPEDA — Canadian federal private-sector law
  security_implications: A privacy policy is the consumer-facing surface of the data-protection program. It must accurately describe data collected, purposes, lawful bases (GDPR), retention, sub-processors, international transfers (SCCs/adequacy), security measures (Art. 32), and individual rights with response SLAs. Misalignment between the policy and actual API data flows is itself a regulatory and reputational risk. Version the policy, surface effective_date, and notify users of material changes before they take effect.

tools:
  - name: API Commons Privacy Policy schema + validator
    url: https://github.com/api-commons/privacy-policy
    license: Apache-2.0
    category: Machine-readable schema
  - name: OneTrust
    url: https://www.onetrust.com/
    category: Privacy management platform
  - name: TrustArc
    url: https://trustarc.com/
    category: Privacy management platform
  - name: Osano
    url: https://www.osano.com/
    category: Consent and privacy management
  - name: Iubenda
    url: https://www.iubenda.com/
    category: Policy generator
  - name: Termly
    url: https://termly.io/
    category: Policy generator
  - name: Global Privacy Control reference site
    url: https://globalprivacycontrol.org/
    category: Standards reference

metrics:
  - name: dsar_response_time_days
    description: Mean time to respond to data subject access requests (GDPR Art. 12 §3 — one month).
  - name: privacy_policy_version_count
    description: Number of distinct published privacy policy versions over time.
  - name: consent_rate
    description: Share of users that grant a given consent category.
  - name: third_party_processor_count
    description: Number of sub-processors disclosed in the policy.
  - name: gpc_honor_rate
    description: Share of inbound requests carrying Sec-GPC that result in opt-out being applied.

examples:
  - provider: Stripe
    url: https://providers.apis.io/providers/stripe/
    note: Detailed global privacy center with regional notices and sub-processor list.
  - provider: GitHub
    url: https://providers.apis.io/providers/github/
    note: Versioned Privacy Statement with change history on docs.github.com.
  - provider: Google
    url: https://providers.apis.io/providers/google/
    note: Cross-product privacy policy plus per-product supplements.
  - provider: Microsoft Graph
    url: https://providers.apis.io/providers/microsoft-graph/
    note: Microsoft Privacy Statement with detailed product sections and DSR portal.

related_properties:
  - terms-of-service
  - security
  - signup
  - authentication
  - service-level-agreement
---
