---
name: GHG Protocol Report
description: A GHGProtocolReport property references a published greenhouse gas emissions report for an API provider or platform, structured according to the GHG Protocol — the global standard for measuring Scope 1, 2, and 3 greenhouse gas emissions. Cloud provider carbon APIs from AWS, Azure, and GCP all align their calculations to GHG Protocol categories. Linking a GHG Protocol report from an APIs.json index makes the provider's emissions posture discoverable by enterprise customers with Scope 3 supply chain reporting requirements.
image: /images/reports.png
url: '#'
tags:
  - GHG Protocol
  - Emissions
  - Sustainability
  - Carbon
aliases:
  - Greenhouse Gas Report
  - GHG Inventory
  - Carbon Disclosure Report
yaml_example: |
  - type: GHGProtocolReport
    url: https://developers.example.com/sustainability/ghg-report

standards:
  - name: GHG Protocol Corporate Accounting and Reporting Standard
    url: https://ghgprotocol.org/corporate-standard
    kind: GHG Protocol / WRI / WBCSD
  - name: GHG Protocol Corporate Value Chain (Scope 3) Standard
    url: https://ghgprotocol.org/corporate-value-chain-scope-3-standard
    kind: GHG Protocol / WRI / WBCSD
  - name: GHG Protocol Scope 2 Guidance
    url: https://ghgprotocol.org/scope-2-guidance
    kind: GHG Protocol / WRI / WBCSD
  - name: GHG Protocol Product Life Cycle Accounting and Reporting Standard
    url: https://ghgprotocol.org/product-standard
    kind: GHG Protocol / WRI / WBCSD
  - name: ISO 14064-1 — Quantification and reporting of GHG emissions and removals at organization level
    url: https://www.iso.org/standard/66453.html
    kind: ISO
  - name: ISO 14064-2 — Quantification, monitoring and reporting of GHG emission reductions or removal enhancements at project level
    url: https://www.iso.org/standard/66454.html
    kind: ISO
  - name: ISO 14064-3 — Verification and validation of GHG statements
    url: https://www.iso.org/standard/66455.html
    kind: ISO
  - name: CDP Climate Change Disclosure
    url: https://www.cdp.net/en/climate
    kind: Disclosure framework

media_types:
  - type: application/pdf
    note: Most published GHG/sustainability reports are PDFs.
  - type: text/html
    note: Web-rendered sustainability microsites.
  - type: application/json
    note: Programmatic emissions APIs (AWS CCFT, Azure Sustainability, Google Cloud Carbon Footprint).

risk:
  compliance:
    - EU Corporate Sustainability Reporting Directive (CSRD) and ESRS E1 climate disclosure
    - SEC climate disclosure rule (USA)
    - UK Streamlined Energy and Carbon Reporting (SECR)
    - California SB 253 — Climate Corporate Data Accountability Act
  security_implications: Emissions claims that cannot be substantiated invite regulatory action and accusations of greenwashing; ensure boundaries, base year, and methodology are stated explicitly and that third-party assurance is referenced when available.

tools:
  - name: AWS Customer Carbon Footprint Tool
    url: https://aws.amazon.com/aws-cost-management/aws-customer-carbon-footprint-tool/
    category: Cloud emissions reporting
  - name: Google Cloud Carbon Footprint
    url: https://cloud.google.com/carbon-footprint
    category: Cloud emissions reporting
  - name: Microsoft Sustainability Manager / Emissions Impact Dashboard
    url: https://www.microsoft.com/en-us/sustainability/emissions-impact-dashboard
    category: Cloud emissions reporting
  - name: Cloud Carbon Footprint
    url: https://www.cloudcarbonfootprint.org/
    license: Apache-2.0
    category: Open-source multi-cloud estimator
  - name: Watershed
    url: https://watershed.com/
    category: Enterprise carbon accounting
  - name: Persefoni
    url: https://www.persefoni.com/
    category: Enterprise carbon accounting

metrics:
  - name: scope_1_tco2e
    description: Direct emissions from owned or controlled sources, in tonnes of CO2 equivalent.
  - name: scope_2_tco2e_location_based
    description: Indirect emissions from purchased electricity using grid-average emission factors.
  - name: scope_2_tco2e_market_based
    description: Indirect emissions reflecting contractual instruments (PPAs, RECs, guarantees of origin).
  - name: scope_3_tco2e
    description: Value chain emissions across the 15 Scope 3 categories (purchased goods, use of sold products, etc.).
  - name: emissions_intensity_per_request
    description: tCO2e normalized per API call, transaction, or user.

examples:
  - provider: AWS
    url: https://providers.apis.io/providers/aws/
    note: Customer Carbon Footprint Tool reports Scope 1/2/3 aligned to GHG Protocol and ISO 14064.
  - provider: Google
    url: https://providers.apis.io/providers/google/
    note: Google Cloud Carbon Footprint exposes per-project emissions following GHG Protocol categorization.
  - provider: Microsoft Azure
    url: https://providers.apis.io/providers/microsoft-azure/
    note: Emissions Impact Dashboard / Sustainability Manager aligned to GHG Protocol.
  - provider: Salesforce
    url: https://providers.apis.io/providers/salesforce/
    note: Net Zero Cloud product and corporate sustainability report published against GHG Protocol.

related_properties:
  - sci-report
  - software-carbon-intensity
  - sustainability
  - esg
---
