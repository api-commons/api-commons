---
name: Service Level Agreement
description: A service level agreement, or simply SLA, defines the level of service you expect from a vendor, laying out the metrics by which service is measured, as well as remedies or penalties should agreed-on service levels not be achieved. A SLA sets the tone between an API producer and consumer and can be communicated as part of API change management practices.
image: /images/service-level-agreement.png
url: '#'
machineReadable: false
source: concept
tags:
  - Change
  - Legal
  - Agreements
aliases:
  - SLA
  - SLO
  - SLI
  - Service Level Objective
  - Service Level Indicator
yaml_example: |
  - type: ServiceLevelAgreement
    url: https://developers.example.com/sla

standards:
  - name: ISO/IEC 19086-1 — Cloud SLA Framework and Terminology
    url: https://www.iso.org/standard/67545.html
    kind: ISO/IEC
  - name: ISO/IEC 19086-2 — Metric Model
    url: https://www.iso.org/standard/67546.html
    kind: ISO/IEC
  - name: ISO/IEC 19086-3 — Core Requirements
    url: https://www.iso.org/standard/67547.html
    kind: ISO/IEC
  - name: ISO/IEC 19086-4 — Security and PII Protection
    url: https://www.iso.org/standard/68241.html
    kind: ISO/IEC
  - name: OpenSLO
    url: https://openslo.com/
    kind: Community
  - name: RFC 9457 — Problem Details for HTTP APIs
    url: https://www.rfc-editor.org/rfc/rfc9457
    kind: IETF
  - name: Google SRE — SLI / SLO / SLA terminology
    url: https://sre.google/sre-book/service-level-objectives/
    kind: SRE
  - name: schema.org serviceArea
    url: https://schema.org/serviceArea
    kind: schema.org

headers:
  - name: Retry-After
    direction: response
    spec: RFC 9110 §10.2.3
    description: Hint to the client when service is expected to recover after a degradation.
  - name: Content-Type
    direction: response
    spec: RFC 9457
    description: 'application/problem+json for SLA-breach error responses.'

status_codes:
  - code: '503'
    name: Service Unavailable
    spec: RFC 9110 §15.6.4
    description: Service temporarily unavailable; typically counted against availability SLOs.
  - code: '504'
    name: Gateway Timeout
    spec: RFC 9110 §15.6.5
    description: Upstream timeout; commonly part of latency SLO measurement.
  - code: '429'
    name: Too Many Requests
    spec: RFC 6585 §4
    description: May indicate the consumer exceeded the tier covered by their SLA.

media_types:
  - type: text/html
    note: SLA documents are typically published as HTML.
  - type: application/yaml
    note: OpenSLO uses YAML manifests.
  - type: application/problem+json
    spec: RFC 9457
    note: Used for structured SLA-breach error responses.

openapi_expression:
  - field: info.termsOfService
    spec: OpenAPI 3.x
    description: Frequently points to the SLA or links to it from the terms page.
  - field: info.x-sla
    spec: OpenAPI extension (vendor)
    description: No standard OpenAPI field for SLAs; commonly carried as an extension.

governance_rules:
  - id: info-contact
    source: Spectral built-in
    description: Customers need an owner to escalate SLA breaches to.
  - id: info-license
    source: Spectral built-in
    description: License and SLA are commonly cross-referenced in API metadata.

risk:
  compliance:
    - ISO/IEC 27001 A.15 — supplier relationships and service delivery
    - SOC 2 A1.1 — availability commitments
    - HIPAA Business Associate Agreements — often reference uptime SLAs
    - GDPR Art. 28 — processor agreements typically include service-level terms
    - FedRAMP / NIST SP 800-53 SA-9 — external information system services
  security_implications: SLA documents publicly disclose architectural commitments (regions, failover, RTO/RPO). Avoid leaking internal incident-response playbooks; keep credits and remedies precise to avoid ambiguity during incidents.

tools:
  - name: Nobl9
    url: https://www.nobl9.com/
    category: SLO platform
  - name: Sloth
    url: https://sloth.dev/
    license: Apache-2.0
    category: Prometheus SLO generator
  - name: Pyrra
    url: https://github.com/pyrra-dev/pyrra
    license: Apache-2.0
    category: Open-source SLO
  - name: Datadog SLOs
    url: https://docs.datadoghq.com/service_management/service_level_objectives/
    category: Observability SLO
  - name: Grafana SLO
    url: https://grafana.com/docs/grafana-cloud/alerting-and-irm/slo/
    category: Observability SLO
  - name: PagerDuty
    url: https://www.pagerduty.com/
    category: Incident response

metrics:
  - name: availability
    description: Fraction of time the service is up versus the SLA target (e.g. 99.9%).
  - name: latency_p95_ms
    description: 95th-percentile request latency over the measurement window.
  - name: latency_p99_ms
    description: 99th-percentile request latency over the measurement window.
  - name: error_budget_burn_rate
    description: Rate of consumption of the allowed error budget for an SLO.
  - name: mttr_minutes
    description: Mean time to recover from incidents counted against the SLA.
  - name: sla_credit_issued
    description: Dollar value of service credits issued for breaches in the period.

examples:
  - provider: AWS
    url: https://providers.apis.io/providers/aws/
    note: Per-service SLAs with tiered credit percentages by monthly availability.
  - provider: Google Cloud
    url: https://providers.apis.io/providers/google-cloud/
    note: Service-specific SLAs published per product with credit schedules.
  - provider: Microsoft Azure
    url: https://providers.apis.io/providers/microsoft-azure/
    note: Per-service SLAs aggregated into a single SLA portal.
  - provider: Stripe
    url: https://providers.apis.io/providers/stripe/
    note: API uptime SLA published for enterprise customers.

related_properties:
  - status
  - rate-limits
  - terms-of-service
  - support
  - error-codes
---
