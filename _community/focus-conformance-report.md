---
name: FOCUS Conformance Report
description: A FocusConformanceReport property references a published document describing how a provider's billing data maps to the FOCUS schema — including any gaps between native fields and the FOCUS column definitions. The FinOps Foundation's certified conformance program requires providers to publish a native-to-FOCUS column mapping and a conformance gap report. Linking this document makes verifiable billing data compatibility discoverable by FinOps tools and enterprise procurement teams.
image: /images/compliance.png
url: '#'
tags:
  - FOCUS
  - FinOps
  - Conformance
  - Billing
aliases:
  - FOCUS Conformance Summary
  - FOCUS Mapping Report
  - FOCUS Gap Analysis
yaml_example: |
  - type: FocusConformanceReport
    url: https://developers.example.com/billing/focus-conformance

standards:
  - name: FOCUS Conformance Program
    url: https://focus.finops.org/conformance/
    kind: FinOps Foundation
  - name: FOCUS — FinOps Open Cost and Usage Specification
    url: https://focus.finops.org/
    kind: FinOps Foundation
  - name: FOCUS Specification (latest)
    url: https://focus.finops.org/focus-specification/
    kind: FinOps Foundation
  - name: FOCUS Conformance Summary template
    url: https://focus.finops.org/conformance/
    kind: FinOps Foundation

governance_rules:
  - id: conformance-version-declared
    source: FOCUS Conformance Program
    description: Report must state the FOCUS specification version it was assessed against.
  - id: native-to-focus-mapping
    source: FOCUS Conformance Program
    description: Report must include a native-column to FOCUS-column mapping table.
  - id: gap-disclosure
    source: FOCUS Conformance Program
    description: Any unsupported or partially supported FOCUS columns must be enumerated with rationale.
  - id: optional-columns-listed
    source: FOCUS Conformance Program
    description: Optional columns supported by the provider should be explicitly listed.

risk:
  compliance:
    - SOX — conformance evidence supports auditability of billing transformations
    - SOC 2 — supplier-management evidence for FinOps tooling vendors
  security_implications: Conformance reports are typically public and reveal billing schema structure; they do not themselves expose customer data but may reveal which discount mechanics a provider supports.

tools:
  - name: FOCUS Validator
    url: https://github.com/finopsfoundation/focus_validator
    license: Apache-2.0
    category: Conformance validator
  - name: FOCUS Specification
    url: https://focus.finops.org/
    category: Specification
  - name: FOCUS Conformance Program
    url: https://focus.finops.org/conformance/
    category: Certification program
  - name: FinOps Foundation
    url: https://www.finops.org/
    category: Standards body

metrics:
  - name: focus_columns_conformant
    description: Number of FOCUS columns the export fully satisfies.
  - name: focus_columns_partial
    description: Number of columns with partial support documented in the gap report.
  - name: focus_columns_unsupported
    description: Number of mandatory FOCUS columns the provider does not yet produce.
  - name: conformance_assessed_version
    description: FOCUS specification version against which the report was assessed.

examples:
  - provider: AWS
    url: https://providers.apis.io/providers/aws/
    note: AWS publishes FOCUS 1.0 conformance documentation for its Data Exports.
  - provider: Microsoft Azure
    url: https://providers.apis.io/providers/azure/
    note: Microsoft Cost Management publishes a FOCUS conformance summary.
  - provider: Google Cloud
    url: https://providers.apis.io/providers/google-cloud/
    note: Google Cloud Billing publishes its FOCUS-aligned mapping documentation.
  - provider: Oracle Cloud
    url: https://providers.apis.io/providers/oracle-cloud/
    note: OCI publishes a FOCUS conformance summary for its billing export.

related_properties:
  - focus-billing-export
  - focus-contract-commitments
  - invoice-reconciliation
  - finops-framework
  - opencost-specification
  - compliance
---
