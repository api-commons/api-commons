---
name: Performance
description: Defining the benchmark for performance of an API, providing an overview of how performance is approached and what it means, while also providing actual tests, results, and other evidence that demonstrates that performance is taken seriously.
image: /images/performance.png
url: '#'
machineReadable: true
source: commons
tags:
  - Performance
  - Load Testing
  - Latency 
aliases:
  - Latency
  - Throughput
  - SLO
  - Benchmarks
yaml_example: |
  - type: X-Performance
    url: https://developers.example.com/performance

standards:
  - name: Server-Timing header (W3C)
    url: https://www.w3.org/TR/server-timing/
    kind: W3C
  - name: OpenTelemetry — HTTP semantic conventions
    url: https://opentelemetry.io/docs/specs/semconv/http/
    kind: OpenTelemetry / CNCF
  - name: OpenTelemetry Metrics specification
    url: https://opentelemetry.io/docs/specs/otel/metrics/
    kind: OpenTelemetry / CNCF
  - name: Prometheus exposition format
    url: https://prometheus.io/docs/instrumenting/exposition_formats/
    kind: Prometheus / CNCF
  - name: Apdex
    url: https://www.apdex.org/
    kind: Apdex Alliance
  - name: Core Web Vitals
    url: https://web.dev/articles/vitals
    kind: Google (web measurement)

headers:
  - name: Server-Timing
    direction: response
    spec: W3C Server-Timing
    description: Communicates server-side timing metrics to clients.
  - name: Timing-Allow-Origin
    direction: response
    spec: W3C Resource Timing Level 2
    description: Permits cross-origin readers to access detailed timing values.

media_types:
  - type: application/json
    note: Benchmark result documents and SLO definitions.
  - type: text/plain
    note: Prometheus exposition format for scraping performance metrics.

openapi_expression:
  - field: x-performance
    spec: Vendor extension
    description: Points to benchmark reports, SLOs, or load-test artifacts for the API.
  - field: info.x-sla
    spec: Vendor extension
    description: Custom marker linking the description to a published SLA/SLO document.

governance_rules:
  - id: oas-tag-description
    source: Spectral built-in
    description: Tags should describe performance-relevant grouping (read-heavy vs. write-heavy).
  - id: operation-operationId
    source: Spectral built-in
    description: Stable operationIds are required to correlate benchmarks with the spec over time.

risk:
  security_implications: Performance instrumentation can leak internal topology via Server-Timing or trace identifiers; scrub upstream service names before exposing externally. Unbounded request shapes (large page sizes, deep filters) are both a performance and DoS risk.
  governance: Without published SLOs and benchmark methodology, consumers cannot capacity-plan; without error budgets, performance regressions are not actionable.

tools:
  - name: k6
    url: https://k6.io/
    license: AGPL-3.0
    category: Load testing
  - name: Locust
    url: https://locust.io/
    license: MIT
    category: Load testing
  - name: Apache JMeter
    url: https://jmeter.apache.org/
    license: Apache-2.0
    category: Load testing
  - name: Artillery
    url: https://www.artillery.io/
    category: Load testing
  - name: Prometheus
    url: https://prometheus.io/
    license: Apache-2.0
    category: Metrics / monitoring
  - name: Grafana
    url: https://grafana.com/oss/grafana/
    license: AGPL-3.0
    category: Observability dashboards

metrics:
  - name: request_latency_p50_ms
    description: Median end-to-end request latency.
  - name: request_latency_p95_ms
    description: 95th-percentile latency; common SLO anchor.
  - name: request_latency_p99_ms
    description: 99th-percentile latency; captures tail behavior.
  - name: request_rate
    description: Requests per second per operation (RED — Rate).
  - name: error_rate
    description: Share of responses with 5xx (RED — Errors).
  - name: saturation
    description: Utilization of bottleneck resources — CPU, queue depth, connections (USE — Saturation).
  - name: apdex_score
    description: Apdex score against a defined target latency T.

examples:
  - provider: Cloudflare
    url: https://providers.apis.io/providers/cloudflare/
    note: Publishes Server-Timing values and network performance dashboards.
  - provider: Fastly
    url: https://providers.apis.io/providers/fastly/
    note: Real-time stats API exposing edge performance metrics.
  - provider: Stripe
    url: https://providers.apis.io/providers/stripe/
    note: Public status and historical latency reporting for API operations.
  - provider: GitHub
    url: https://providers.apis.io/providers/github/
    note: Published REST and GraphQL rate limits and status incident history.

related_properties:
  - rate-limits
  - status
  - sla
  - monitoring
  - tests
  - openapi
---
