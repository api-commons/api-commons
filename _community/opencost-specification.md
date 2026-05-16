---
name: OpenCost Specification
description: An OpenCostSpecification property references documentation describing how an API or platform's cost reporting conforms to the OpenCost Specification — a CNCF Incubating project that defines a vendor-neutral standard for measuring and allocating Kubernetes and cloud infrastructure costs. OpenCost covers cluster asset costs, workload cost allocation by namespace, deployment, pod, and label, and idle resource cost distribution. Linking an OpenCost conformance document makes Kubernetes cost data interoperable with FinOps tooling.
image: /images/pricing.png
url: '#'
tags:
  - OpenCost
  - FinOps
  - Kubernetes
  - Cost Allocation
aliases:
  - OpenCost Spec
  - OpenCost Conformance
  - Kubernetes Cost Specification
yaml_example: |
  - type: OpenCostSpecification
    url: https://developers.example.com/costs/opencost

standards:
  - name: OpenCost Specification v0.1
    url: https://github.com/opencost/opencost/blob/develop/spec/opencost-specv01.md
    kind: CNCF / OpenCost
  - name: OpenCost project
    url: https://www.opencost.io/
    kind: CNCF (Incubating)
  - name: OpenCost documentation
    url: https://www.opencost.io/docs/
    kind: CNCF / OpenCost
  - name: Kubernetes resource model
    url: https://kubernetes.io/docs/concepts/configuration/manage-resources-containers/
    kind: CNCF / Kubernetes
  - name: Prometheus exposition format
    url: https://prometheus.io/docs/instrumenting/exposition_formats/
    kind: CNCF / Prometheus
  - name: OpenMetrics
    url: https://openmetrics.io/
    kind: CNCF
  - name: FOCUS — FinOps Open Cost and Usage Specification
    url: https://focus.finops.org/
    kind: FinOps Foundation

media_types:
  - type: application/json
    note: Primary response format for OpenCost APIs.
  - type: text/plain
    note: Prometheus metrics exposition for OpenCost-emitted series.

governance_rules:
  - id: asset-coverage
    source: OpenCost Specification
    description: Implementations must enumerate the supported asset categories (Node, Disk, LoadBalancer, ClusterManagement, Network).
  - id: allocation-keys
    source: OpenCost Specification
    description: Allocation must be reportable by namespace, controller, pod, container, service, and label.
  - id: idle-policy-declared
    source: OpenCost Specification
    description: Treatment of idle and unallocated capacity must be documented.
  - id: shared-cost-policy
    source: OpenCost Specification
    description: Shared-cost distribution policy (proportional, even, by-label) must be discoverable.
  - id: currency-iso4217
    source: OpenCost Specification
    description: Reported costs must be denominated in an ISO 4217 currency code.

risk:
  compliance:
    - SOC 2 — cost reporting underpins internal chargeback and showback controls
    - GDPR — workload labels may inadvertently include personal data
  security_implications: OpenCost surfaces detailed workload, label, and capacity data; restrict to operators and finance roles and avoid exposing label values that could leak tenancy.

tools:
  - name: OpenCost
    url: https://www.opencost.io/
    license: Apache-2.0
    category: Reference implementation
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
    category: Dashboards
  - name: CNCF Landscape
    url: https://landscape.cncf.io/
    category: Ecosystem map
  - name: kubectl cost
    url: https://github.com/kubecost/kubectl-cost
    license: Apache-2.0
    category: CLI client

metrics:
  - name: opencost_spec_version
    description: Version of the OpenCost Specification a provider claims conformance to.
  - name: asset_categories_supported
    description: Number of OpenCost asset categories the implementation reports.
  - name: allocation_keys_supported
    description: Number of allocation aggregation keys supported.
  - name: focus_mapping_documented
    description: Boolean — whether the implementation publishes an OpenCost-to-FOCUS column mapping.

examples:
  - provider: OpenCost
    url: https://providers.apis.io/providers/opencost/
    note: Reference implementation maintained by the OpenCost community under CNCF.
  - provider: Kubecost
    url: https://providers.apis.io/providers/kubecost/
    note: Commercial distribution conformant to the OpenCost Specification.

related_properties:
  - opencost-allocation-api
  - focus-billing-export
  - focus-conformance-report
  - focus-contract-commitments
  - finops-framework
  - pricing
---
