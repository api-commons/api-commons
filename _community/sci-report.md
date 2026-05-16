---
name: SCI Report
description: An SCIReport property references a published carbon intensity report for an API or service calculated using the Software Carbon Intensity (SCI) specification — an ISO-ratified standard from the Green Software Foundation. An SCI report documents the measured or estimated carbon intensity for a specific version or deployment of the API, including the methodology, data sources, energy and embodied carbon inputs, the chosen functional unit, and the resulting score. Regular SCI reports enable tracking of carbon efficiency improvements over time.
image: /images/reports.png
url: '#'
tags:
  - Carbon
  - Sustainability
  - SCI Report
  - Green Software
aliases:
  - Software Carbon Intensity Report
  - SCI Disclosure
yaml_example: |
  - type: SCIReport
    url: https://developers.example.com/sustainability/sci-report

standards:
  - name: Software Carbon Intensity (SCI) Specification
    url: https://sci.greensoftware.foundation/
    kind: Green Software Foundation
  - name: SCI Specification source
    url: https://github.com/Green-Software-Foundation/sci
    kind: Green Software Foundation
  - name: ISO/IEC 21031:2024 — Software Carbon Intensity (SCI) specification
    url: https://www.iso.org/standard/86612.html
    kind: ISO/IEC
  - name: GHG Protocol Product Life Cycle Standard
    url: https://ghgprotocol.org/product-standard
    kind: GHG Protocol / WRI / WBCSD
  - name: GHG Protocol Corporate Value Chain (Scope 3) Standard
    url: https://ghgprotocol.org/corporate-value-chain-scope-3-standard
    kind: GHG Protocol / WRI / WBCSD

media_types:
  - type: application/pdf
    note: Formal SCI reports are typically published as PDFs.
  - type: text/markdown
    note: Many open-source projects publish SCI calculations as Markdown in their repos.
  - type: application/json
    note: Machine-readable SCI score artifacts.

governance_rules:
  - id: sci-boundary-documented
    source: SCI Specification
    description: Report must state the software boundary (which components are included).
  - id: sci-functional-unit-declared
    source: SCI Specification
    description: The R (functional unit) — for example per API call or per user — must be explicit.
  - id: sci-methodology-disclosed
    source: SCI Specification
    description: Energy (E), carbon intensity (I), and embodied carbon (M) data sources must be cited.

risk:
  compliance:
    - EU CSRD / ESRS E1 supports software-level disclosures from suppliers
    - California SB 253 disclosure may incorporate product-level carbon claims
  security_implications: Unsubstantiated SCI scores risk greenwashing claims; cite emission factor providers, electricity-mix sources, and embodied carbon datasets so the score is reproducible.

tools:
  - name: Green Software Foundation Impact Framework
    url: https://if.greensoftware.foundation/
    license: MIT
    category: SCI calculation framework
  - name: Impact Framework source
    url: https://github.com/Green-Software-Foundation/if
    license: MIT
    category: SCI calculation framework
  - name: Cloud Carbon Footprint
    url: https://www.cloudcarbonfootprint.org/
    license: Apache-2.0
    category: Cloud energy and emissions estimator
  - name: Kepler
    url: https://sustainable-computing.io/
    license: Apache-2.0
    category: Kubernetes energy metering
  - name: Scaphandre
    url: https://github.com/hubblo-org/scaphandre
    license: Apache-2.0
    category: Power-consumption metrology
  - name: Electricity Maps API
    url: https://www.electricitymaps.com/
    category: Marginal carbon-intensity data (I in SCI)

metrics:
  - name: sci_score
    description: Computed as ((E * I) + M) / R for the declared boundary and functional unit.
  - name: energy_kwh
    description: E — operational energy consumed by the software boundary.
  - name: marginal_carbon_intensity_g_per_kwh
    description: I — region-specific marginal carbon intensity of electricity.
  - name: embodied_carbon_gco2e
    description: M — amortized embodied emissions of hardware over its useful life.
  - name: functional_unit_count
    description: R — denominator such as API requests served, users, or transactions.

examples:
  - provider: Green Software Foundation
    url: https://github.com/Green-Software-Foundation/sci
    note: Canonical SCI specification, examples, and case studies.
  - provider: GitHub
    url: https://providers.apis.io/providers/github/
    note: GitHub published carbon and sustainability work referencing GSF tooling.

related_properties:
  - software-carbon-intensity
  - ghg-protocol-report
  - sustainability
---
