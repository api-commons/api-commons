---
name: Software Carbon Intensity
description: A SoftwareCarbonIntensity property references a published Software Carbon Intensity (SCI) score or methodology document for an API or service. SCI is an ISO-ratified standard from the Green Software Foundation quantifying carbon intensity using the formula SCI = ((E * I) + M) per R — where E is energy consumed, I is the marginal carbon intensity of electricity, M is embodied carbon, and R is a functional unit such as per API call or per user. Publishing an SCI score makes carbon efficiency measurable and comparable across API providers.
image: /images/climate.png
url: '#'
tags:
  - Carbon
  - Sustainability
  - SCI
  - Green Software
aliases:
  - SCI
  - SCI Score
yaml_example: |
  - type: SoftwareCarbonIntensity
    url: https://developers.example.com/sustainability/sci

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
  - name: Green Software Foundation Principles of Green Software Engineering
    url: https://learn.greensoftware.foundation/
    kind: Green Software Foundation
  - name: GHG Protocol Product Life Cycle Standard
    url: https://ghgprotocol.org/product-standard
    kind: GHG Protocol / WRI / WBCSD

media_types:
  - type: application/json
    note: Machine-readable SCI score and component breakdown.
  - type: application/yaml
    note: Impact Framework manifests describing SCI pipelines.
  - type: text/markdown
    note: Methodology and reasoning published alongside the score.

governance_rules:
  - id: sci-formula-disclosed
    source: SCI Specification
    description: The SCI score must be derived from ((E * I) + M) / R, not arbitrary aggregation.
  - id: sci-marginal-not-average
    source: SCI Specification
    description: I should reflect marginal carbon intensity where data is available, not annual averages.
  - id: sci-embodied-amortized
    source: SCI Specification
    description: M (embodied carbon) is amortized across the hardware's useful life and reservation share.

risk:
  compliance:
    - CSRD / ESRS E1 — product carbon footprint disclosures
    - Customer Scope 3 Category 1 (purchased goods and services) reporting on SaaS usage
  security_implications: An SCI score without disclosed inputs is unverifiable; cite electricity-mix data provider, hardware embodied-carbon dataset, and the measurement boundary so the number is reproducible and defensible.

tools:
  - name: Green Software Foundation Impact Framework
    url: https://if.greensoftware.foundation/
    license: MIT
    category: SCI calculation
  - name: Impact Framework source
    url: https://github.com/Green-Software-Foundation/if
    license: MIT
    category: SCI calculation
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
    category: Marginal carbon-intensity data feed

metrics:
  - name: sci_score
    description: ((E * I) + M) / R — the core SCI number.
  - name: energy_per_request_wh
    description: E component normalized to a single API request.
  - name: carbon_intensity_g_per_kwh
    description: I — marginal grid intensity for the region serving the workload.
  - name: embodied_gco2e_amortized
    description: M — amortized share of hardware embodied emissions attributable to the workload.
  - name: requests_per_score_window
    description: R — functional-unit count over the measurement window.

examples:
  - provider: Green Software Foundation
    url: https://github.com/Green-Software-Foundation/sci
    note: Specification, formula derivation, and reference case studies.
  - provider: GitHub
    url: https://providers.apis.io/providers/github/
    note: Green Software Foundation work and tooling discussions hosted publicly on GitHub.

related_properties:
  - sci-report
  - ghg-protocol-report
  - sustainability
---
