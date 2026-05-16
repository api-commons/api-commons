---
name: Policies
description: Providing the machine-readable policies that define the business aspects of API operations and how it is governed, breaking down the business and technical details of API operations in terms that help organize and make the governance of APIs approachable by business stakeholders and leadership.
image: /images/policies.png
url: '#'
machineReadable: false
source: concept
tags:
  - Policies 
  - Governance
  - Business
  - Leadership
aliases:
  - Policy
  - Governance Policies
  - Business Policies
yaml_example: |
  - type: X-Policies
    url: https://developers.example.com/policies

standards:
  - name: Open Policy Agent (OPA)
    url: https://www.openpolicyagent.org/
    kind: CNCF (graduated)
  - name: Rego policy language
    url: https://www.openpolicyagent.org/docs/latest/policy-language/
    kind: CNCF
  - name: Cedar policy language
    url: https://www.cedarpolicy.com/
    kind: AWS / open source
  - name: JSON Schema 2020-12
    url: https://json-schema.org/specification-links#2020-12
    kind: JSON Schema
  - name: XACML 3.0
    url: https://docs.oasis-open.org/xacml/3.0/xacml-3.0-core-spec-os-en.html
    kind: OASIS
  - name: RFC 6749 — OAuth 2.0 (scopes as policy attributes)
    url: https://www.rfc-editor.org/rfc/rfc6749
    kind: IETF
  - name: NIST SP 800-162 — Attribute Based Access Control
    url: https://csrc.nist.gov/publications/detail/sp/800-162/final
    kind: NIST

media_types:
  - type: application/json
    note: Policy data documents and decision logs (OPA input/result envelopes).
  - type: application/yaml
    note: Common authoring format for policy bundles and config.
  - type: text/x-rego
    note: Rego source files (de facto; .rego extension).

openapi_expression:
  - field: components.securitySchemes / security
    spec: OpenAPI 3.x
    description: OAuth 2.0 scopes act as coarse policy attributes that downstream PDPs can refine.
  - field: x-policy
    spec: Vendor extension
    description: Custom marker referencing a Rego/Cedar bundle that governs the operation.

governance_rules:
  - id: oas-security-defined
    source: Spectral built-in
    description: Operations must reference a defined security scheme so policy enforcement can hook in.
  - id: operation-tag-defined
    source: Spectral built-in
    description: Tags often drive policy scope (e.g., by domain or sensitivity).

risk:
  compliance:
    - SOC 2 CC6.x — logical access controls implemented as auditable policy
    - ISO/IEC 27001 A.9 — access control policy and procedures
    - GDPR Art. 5 — purpose limitation and data minimisation as policy constraints
    - HIPAA 45 CFR §164.308 — administrative safeguards
  security_implications: Without machine-readable policy, authorization logic is scattered through application code and gateways and cannot be audited or replayed. Centralize decisions in a PDP (OPA, Cedar) and emit decision logs for compliance evidence.
  governance: Policy code must be versioned, reviewed, and tested like any other code; uncontrolled policy edits become a privilege-escalation path.

tools:
  - name: Open Policy Agent
    url: https://www.openpolicyagent.org/
    license: Apache-2.0
    category: Policy engine
  - name: Conftest
    url: https://www.conftest.dev/
    license: Apache-2.0
    category: Config / spec policy testing
  - name: Cedar
    url: https://www.cedarpolicy.com/
    license: Apache-2.0
    category: Policy engine
  - name: Styra DAS
    url: https://www.styra.com/
    category: OPA control plane
  - name: AWS Verified Permissions
    url: https://aws.amazon.com/verified-permissions/
    category: Managed Cedar service
  - name: Permit.io
    url: https://www.permit.io/
    category: Policy-as-a-service

metrics:
  - name: policy_decision_count
    description: Number of allow/deny decisions emitted by the PDP per unit time.
  - name: policy_deny_rate
    description: Share of decisions that result in a deny; sudden swings indicate policy regression.
  - name: policy_evaluation_p95_ms
    description: 95th-percentile latency of policy decisions; in-band policy must stay well below request budget.
  - name: policy_bundle_version_drift
    description: Number of enforcement points running an outdated policy bundle.

examples:
  - provider: AWS
    url: https://providers.apis.io/providers/aws/
    note: IAM policy documents and Verified Permissions (Cedar) for application-level authz.
  - provider: GitHub
    url: https://providers.apis.io/providers/github/
    note: Fine-grained PAT permissions and organization policies governing API access.
  - provider: Styra
    url: https://providers.apis.io/providers/styra/
    note: Commercial control plane for Open Policy Agent and Rego policy distribution.

related_properties:
  - rules
  - authentication
  - authorization
  - terms-of-service
  - governance
  - security
---
