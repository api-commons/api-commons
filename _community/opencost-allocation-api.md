---
name: OpenCost Allocation API
description: An OpenCostAllocationAPI property references an API endpoint that exposes Kubernetes and cloud infrastructure cost allocation data in a format compatible with the OpenCost Allocation API specification. The OpenCost API returns workload cost data aggregated by namespace, deployment, pod, service, or label, and supports time-window queries and shared cost distribution. Indexing an OpenCost-compatible allocation endpoint makes container cost data programmatically accessible to FinOps dashboards, chargeback tools, and engineering teams.
image: /images/pricing.png
url: #
tags:
  - OpenCost
  - FinOps
  - Kubernetes
  - Cost Allocation
  - API
yaml_example: |
  - type: OpenCostAllocationAPI
    url: https://developers.example.com/costs/allocation
---
