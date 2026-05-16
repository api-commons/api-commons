---
name: OpenCost Allocation API
description: An OpenCostAllocationAPI property references an API endpoint that exposes Kubernetes and cloud infrastructure cost allocation data in a format compatible with the OpenCost Allocation API specification. The OpenCost API returns workload cost data aggregated by namespace, deployment, pod, service, or label, and supports time-window queries and shared cost distribution. Indexing an OpenCost-compatible allocation endpoint makes container cost data programmatically accessible to FinOps dashboards, chargeback tools, and engineering teams.
image: /images/pricing.png
url: '#'
tags:
  - OpenCost
  - FinOps
  - Kubernetes
  - Cost Allocation
  - API
aliases:
  - OpenCost API
  - Kubernetes Cost Allocation API
  - Allocation Endpoint
yaml_example: |
  - type: OpenCostAllocationAPI
    url: https://developers.example.com/costs/allocation

standards:
  - name: OpenCost Specification
    url: https://github.com/opencost/opencost/blob/develop/spec/opencost-specv01.md
    kind: CNCF / OpenCost
  - name: OpenCost project
    url: https://www.opencost.io/
    kind: CNCF (Incubating)
  - name: OpenCost API documentation
    url: https://www.opencost.io/docs/integrations/api
    kind: CNCF / OpenCost
  - name: Prometheus exposition format
    url: https://prometheus.io/docs/instrumenting/exposition_formats/
    kind: CNCF / Prometheus
  - name: OpenMetrics
    url: https://openmetrics.io/
    kind: CNCF
  - name: Kubernetes API
    url: https://kubernetes.io/docs/reference/using-api/
    kind: CNCF / Kubernetes

media_types:
  - type: application/json
    note: Primary response media type for OpenCost allocation queries.
  - type: text/plain
    note: Used for Prometheus metrics scraping (text exposition format).

openapi_expression:
  - field: paths./allocation
    spec: OpenCost API
    description: Allocation endpoint accepts window, aggregate, and accumulate query parameters.
  - field: paths./allocation/compute
    spec: OpenCost API
    description: On-demand allocation computation endpoint.
  - field: paths./assets
    spec: OpenCost API
    description: Returns cluster-level asset cost data.

governance_rules:
  - id: window-required
    source: OpenCost API
    description: Allocation queries must specify a time window (e.g., '7d', '2024-01-01,2024-01-31').
  - id: aggregate-known-keys
    source: OpenCost API
    description: aggregate parameter must use supported keys (namespace, deployment, pod, controller, service, label:<name>, etc.).
  - id: idle-handling-declared
    source: OpenCost Specification
    description: Responses should declare whether idle costs are included, shared, or excluded.
  - id: shared-cost-explicit
    source: OpenCost Specification
    description: Any shared-cost distribution policy applied to the response must be discoverable.

risk:
  compliance:
    - SOC 2 — cost allocation data informs chargeback and internal financial controls
    - GDPR — allocation labels may carry tenant or user identifiers
  security_implications: Allocation APIs disclose workload-level spend, label values, and capacity posture; require authentication and consider scoping by namespace or RBAC role.

tools:
  - name: OpenCost
    url: https://www.opencost.io/
    license: Apache-2.0
    category: Cost allocation engine
  - name: Kubecost
    url: https://www.kubecost.com/
    category: Commercial OpenCost distribution
  - name: Prometheus
    url: https://prometheus.io/
    license: Apache-2.0
    category: Metrics backend
  - name: Grafana
    url: https://grafana.com/
    license: AGPL-3.0
    category: Dashboards for OpenCost
  - name: Thanos
    url: https://thanos.io/
    license: Apache-2.0
    category: Long-term metrics storage
  - name: kubectl cost
    url: https://github.com/kubecost/kubectl-cost
    license: Apache-2.0
    category: CLI client

metrics:
  - name: allocation_query_latency_p95_ms
    description: 95th-percentile latency of /allocation requests.
  - name: allocation_rows_returned
    description: Number of aggregated allocation rows in a response.
  - name: idle_cost_share
    description: Fraction of total cost attributed to idle resources in the window.
  - name: shared_cost_share
    description: Fraction of total cost distributed via shared-cost rules.
  - name: cluster_cost_total
    description: Total cluster cost over the queried window.

examples:
  - provider: OpenCost
    url: https://providers.apis.io/providers/opencost/
    note: Reference implementation of the OpenCost Allocation API.
  - provider: Kubecost
    url: https://providers.apis.io/providers/kubecost/
    note: Commercial distribution that implements the OpenCost API.

related_properties:
  - opencost-specification
  - focus-billing-export
  - focus-conformance-report
  - finops-framework
  - pricing
---
