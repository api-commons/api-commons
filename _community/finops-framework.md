---
name: FinOps Framework
description: A FinOpsFramework property references a document describing how an API provider or platform aligns to the FinOps Framework — the operational framework published by the FinOps Foundation for managing cloud, SaaS, and AI financial operations. The 2025 Framework revision expanded coverage to four scopes — public cloud, SaaS, data center, and AI. A FinOps Framework alignment document describes which capabilities the provider supports, at what maturity level, and how they enable customer FinOps practices such as cost allocation, budgeting, forecasting, and unit economics.
image: /images/guidance.png
url: '#'
tags:
  - FinOps
  - Framework
  - Cloud Financial Management
  - Governance
aliases:
  - FinOps Foundation Framework
  - Cloud Financial Management Framework
  - FOCUS Framework Alignment
yaml_example: |
  - type: FinOpsFramework
    url: https://developers.example.com/finops

standards:
  - name: FinOps Framework (2025)
    url: https://www.finops.org/framework/
    kind: FinOps Foundation
  - name: FinOps Capabilities
    url: https://www.finops.org/framework/capabilities/
    kind: FinOps Foundation
  - name: FinOps Domains
    url: https://www.finops.org/framework/domains/
    kind: FinOps Foundation
  - name: FinOps Personas
    url: https://www.finops.org/framework/personas/
    kind: FinOps Foundation
  - name: FinOps Maturity Model
    url: https://www.finops.org/framework/maturity-model/
    kind: FinOps Foundation
  - name: FinOps Principles
    url: https://www.finops.org/framework/principles/
    kind: FinOps Foundation
  - name: FOCUS — FinOps Open Cost and Usage Specification
    url: https://focus.finops.org/
    kind: FinOps Foundation
  - name: FinOps Open Cost Quantity Specification (FOCUS)
    url: https://focus.finops.org/focus-specification/
    kind: FinOps Foundation

governance_rules:
  - id: framework-scope-declared
    source: FinOps Foundation
    description: Alignment document should declare which Framework scopes (Cloud, SaaS, Data Center, AI) it covers.
  - id: capability-mapping-listed
    source: FinOps Foundation
    description: Should enumerate which FinOps Capabilities the provider enables for customers.
  - id: maturity-stated
    source: FinOps Foundation
    description: Capabilities should be tagged Crawl / Walk / Run per the FinOps Maturity Model.

risk:
  compliance:
    - SOC 2 — financial-operations evidence often referenced in cost governance
    - ISO/IEC 27001 — asset and supplier management overlap with FinOps inventory
  security_implications: FinOps alignment documents typically disclose billing data flows and discount structures; treat as commercially sensitive but not as a security boundary.

tools:
  - name: FinOps Foundation
    url: https://www.finops.org/
    category: Standards body
  - name: FOCUS Specification
    url: https://focus.finops.org/
    category: Specification
  - name: OpenCost
    url: https://www.opencost.io/
    license: Apache-2.0
    category: Open-source FinOps tooling
  - name: Kubecost
    url: https://www.kubecost.com/
    category: FinOps tooling
  - name: CloudZero
    url: https://www.cloudzero.com/
    category: FinOps platform
  - name: Vantage
    url: https://www.vantage.sh/
    category: FinOps platform

metrics:
  - name: capabilities_supported
    description: Count of FinOps Framework Capabilities the provider can demonstrate.
  - name: framework_scopes_covered
    description: Number of the four Framework scopes (Cloud, SaaS, Data Center, AI) addressed.
  - name: maturity_score
    description: Average Crawl/Walk/Run rating across declared capabilities.

examples:
  - provider: AWS
    url: https://providers.apis.io/providers/aws/
    note: AWS Cloud Financial Management practice areas align to several FinOps Capabilities.
  - provider: Google Cloud
    url: https://providers.apis.io/providers/google-cloud/
    note: Google Cloud FinOps Hub maps native tooling to FinOps Framework capabilities.
  - provider: Microsoft Azure
    url: https://providers.apis.io/providers/azure/
    note: Microsoft Cost Management materials reference FinOps Framework alignment.

related_properties:
  - focus-billing-export
  - focus-conformance-report
  - focus-contract-commitments
  - invoice-reconciliation
  - opencost-specification
  - pricing
---
