---
name: Invoice Reconciliation
description: An InvoiceReconciliation property references documentation explaining how an API provider's billing data maps to issued invoices — including how to match billing export rows to invoice line items using invoice identifiers. FOCUS 1.2 introduced dedicated Invoice ID columns specifically to enable this reconciliation. For enterprise API consumers, the ability to tie API usage records to financial invoices is a compliance and audit requirement. Linking reconciliation documentation makes this mapping discoverable alongside the API.
image: /images/invoices.png
url: '#'
tags:
  - Invoice
  - FinOps
  - Billing
  - Reconciliation
aliases:
  - Invoice Mapping
  - Billing-to-Invoice Reconciliation
  - Invoice Line Item Matching
yaml_example: |
  - type: InvoiceReconciliation
    url: https://developers.example.com/billing/reconciliation

standards:
  - name: FOCUS — FinOps Open Cost and Usage Specification
    url: https://focus.finops.org/
    kind: FinOps Foundation
  - name: FOCUS Specification (latest, Invoice ID columns)
    url: https://focus.finops.org/focus-specification/
    kind: FinOps Foundation
  - name: ISO 20022 — Financial Services Universal Message Scheme
    url: https://www.iso20022.org/
    kind: ISO
  - name: ASC X12 EDI 810 — Invoice
    url: https://x12.org/
    kind: ASC X12
  - name: EN 16931 — European e-invoicing semantic data model
    url: https://www.cencenelec.eu/areas-of-work/cen-cenelec-topics/digital-society/einvoicing/
    kind: CEN
  - name: Peppol BIS Billing 3.0
    url: https://docs.peppol.eu/poacc/billing/3.0/
    kind: OpenPeppol
  - name: UBL 2.1 — Universal Business Language
    url: https://docs.oasis-open.org/ubl/UBL-2.1.html
    kind: OASIS
  - name: schema.org Invoice
    url: https://schema.org/Invoice
    kind: schema.org

media_types:
  - type: application/xml
    note: Common for UBL, Peppol BIS, and EN 16931 invoice payloads.
  - type: application/json
    note: Used by API-delivered invoice and reconciliation endpoints.
  - type: application/pdf
    note: Human-readable invoice delivery; reconciliation typically requires a structured companion file.
  - type: text/csv
    spec: RFC 4180
    note: Common for FOCUS billing export rows that join to invoices by InvoiceId.

governance_rules:
  - id: invoice-id-present
    source: FOCUS Specification
    description: Billing rows must include the InvoiceId field to enable reconciliation to a specific invoice document.
  - id: invoice-issuer-identified
    source: FOCUS Specification
    description: The InvoiceIssuer should be identifiable so resellers and marketplace flows are unambiguous.
  - id: billing-period-aligned
    source: FOCUS Specification
    description: BillingPeriodStart / BillingPeriodEnd must align with the invoice period for one-to-one reconciliation.
  - id: currency-matches-invoice
    source: FOCUS Specification
    description: BillingCurrency on the row must match the currency of the issued invoice.

risk:
  compliance:
    - SOX — invoice reconciliation is a financial control surface
    - SOC 2 — billing accuracy assertions rely on reconciliation evidence
    - EU VAT Directive — e-invoicing mandates apply to many cross-border flows
    - GDPR — invoices typically contain controller-identifiable data
  security_implications: Invoice documents disclose negotiated pricing, account identifiers, and sometimes contract terms; restrict access to billing administrators.

tools:
  - name: FOCUS Specification
    url: https://focus.finops.org/
    category: Specification
  - name: Peppol
    url: https://peppol.org/
    category: e-invoicing network
  - name: UBL
    url: https://www.oasis-open.org/committees/ubl/
    category: Document standard
  - name: GoBD-compliant archivers
    url: https://www.bundesfinanzministerium.de/
    category: Regional archive tooling
  - name: FOCUS Validator
    url: https://github.com/finopsfoundation/focus_validator
    license: Apache-2.0
    category: Conformance validator

metrics:
  - name: reconciled_rows_pct
    description: Percentage of billing-export rows successfully matched to invoice line items.
  - name: invoice_variance_value
    description: Aggregate monetary variance between summed billing rows and invoice totals.
  - name: unmatched_invoice_lines
    description: Count of invoice line items with no corresponding billing-export rows.
  - name: reconciliation_lag_days
    description: Days between invoice issuance and availability of fully reconciled detail rows.

examples:
  - provider: AWS
    url: https://providers.apis.io/providers/aws/
    note: AWS Cost and Usage Report includes invoice_id and bill_invoicing_entity for reconciliation.
  - provider: Microsoft Azure
    url: https://providers.apis.io/providers/azure/
    note: Azure billing exports expose invoice number on each charge row.
  - provider: Google Cloud
    url: https://providers.apis.io/providers/google-cloud/
    note: Cloud Billing BigQuery export includes invoice.month and invoice metadata.
  - provider: Stripe
    url: https://providers.apis.io/providers/stripe/
    note: Stripe Invoicing exposes invoice IDs and line items via the Invoices API.

related_properties:
  - focus-billing-export
  - focus-conformance-report
  - focus-contract-commitments
  - finops-framework
  - billing
  - pricing
---
