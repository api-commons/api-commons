---
name: Security
description: The security of any API is important to producer and consumer, and no consumer should be using any 3rd party API platform that does not clearly communicate and demonstrate an API is secure. API security is a foundational business building block in any API ecosystem when it comes to building trust and keeping consumers integrated with an API.
image: /images/security.png
url: '#'
machineReadable: false
source: concept
tags:
  - Security
  - Trust
aliases:
  - InfoSec
  - Application Security
  - AppSec
  - API Security
yaml_example: |
  - type: Security
    url: https://developers.example.com/security

standards:
  - name: RFC 9116 — A File Format to Aid in Security Vulnerability Disclosure (security.txt)
    url: https://www.rfc-editor.org/rfc/rfc9116
    kind: IETF
  - name: OWASP API Security Top 10 (2023)
    url: https://owasp.org/API-Security/editions/2023/en/0x00-header/
    kind: OWASP
  - name: OWASP Application Security Verification Standard (ASVS)
    url: https://owasp.org/www-project-application-security-verification-standard/
    kind: OWASP
  - name: OWASP Software Assurance Maturity Model (SAMM)
    url: https://owaspsamm.org/
    kind: OWASP
  - name: ISO/IEC 27001 — Information Security Management Systems
    url: https://www.iso.org/standard/27001
    kind: ISO
  - name: ISO/IEC 29147 — Vulnerability Disclosure
    url: https://www.iso.org/standard/72311.html
    kind: ISO
  - name: ISO/IEC 30111 — Vulnerability Handling Processes
    url: https://www.iso.org/standard/69725.html
    kind: ISO
  - name: NIST SP 800-53 — Security and Privacy Controls
    url: https://csrc.nist.gov/pubs/sp/800/53/r5/upd1/final
    kind: NIST
  - name: NIST SP 800-218 — Secure Software Development Framework (SSDF)
    url: https://csrc.nist.gov/pubs/sp/800/218/final
    kind: NIST
  - name: PCI DSS v4.0
    url: https://www.pcisecuritystandards.org/document_library/
    kind: PCI SSC
  - name: SOC 2 — Trust Services Criteria
    url: https://www.aicpa-cima.com/topic/audit-assurance/audit-and-assurance-greater-than-soc-2
    kind: AICPA
  - name: SLSA — Supply-chain Levels for Software Artifacts
    url: https://slsa.dev/
    kind: OpenSSF
  - name: in-toto
    url: https://in-toto.io/
    kind: CNCF
  - name: CVE — Common Vulnerabilities and Exposures
    url: https://www.cve.org/
    kind: MITRE
  - name: CWE — Common Weakness Enumeration
    url: https://cwe.mitre.org/
    kind: MITRE
  - name: CVSS v4.0 — Common Vulnerability Scoring System
    url: https://www.first.org/cvss/v4.0/
    kind: FIRST
  - name: RFC 9325 — Recommendations for Secure Use of TLS and DTLS
    url: https://www.rfc-editor.org/rfc/rfc9325
    kind: IETF
  - name: RFC 6797 — HTTP Strict Transport Security (HSTS)
    url: https://www.rfc-editor.org/rfc/rfc6797
    kind: IETF

headers:
  - name: Strict-Transport-Security
    direction: response
    spec: RFC 6797
    description: Enforces HTTPS for subsequent requests to the host.
  - name: Content-Security-Policy
    direction: response
    spec: W3C CSP Level 3
    description: Restricts which resources a UA may load; applies to API-backed web surfaces.
  - name: X-Content-Type-Options
    direction: response
    spec: WHATWG Fetch (nosniff)
    description: Disables MIME-type sniffing.
  - name: Referrer-Policy
    direction: response
    spec: W3C Referrer Policy
    description: Controls Referer header leakage.
  - name: Cross-Origin-Resource-Policy
    direction: response
    spec: WHATWG Fetch
    description: Restricts cross-origin embedding of API responses.

status_codes:
  - code: '400'
    name: Bad Request
    spec: RFC 9110 §15.5.1
    description: Often returned for malformed/unsafe input rejected by security controls.
  - code: '403'
    name: Forbidden
    spec: RFC 9110 §15.5.4
    description: Request blocked by WAF, IP allowlist, or policy.
  - code: '429'
    name: Too Many Requests
    spec: RFC 6585 §4
    description: Anti-abuse / rate-limiting response.
  - code: '451'
    name: Unavailable For Legal Reasons
    spec: RFC 7725
    description: Resource blocked due to legal or regulatory demand.

well_known:
  - path: /.well-known/security.txt
    spec: RFC 9116
    description: Machine-readable contact and policy for vulnerability disclosure.

openapi_expression:
  - field: components.securitySchemes
    spec: OpenAPI 3.x
    description: Declares schemes that protect operations.
  - field: security
    spec: OpenAPI 3.x
    description: Operation- or document-level security requirement.
  - field: servers[].url
    spec: OpenAPI 3.x
    description: HTTPS base URLs are a baseline security signal.

link_relations:
  - rel: vulnerability-disclosure
    note: Commonly surfaced via security.txt rather than IANA link relation.

governance_rules:
  - id: owasp:api1:2023-no-integer-id
    source: Vacuum / Spectral OWASP ruleset
    description: BOLA — avoid exposing raw integer object IDs without authorization checks.
  - id: owasp:api2:2023-no-http-basic
    source: Vacuum / Spectral OWASP ruleset
    description: Discourages HTTP Basic auth in modern APIs.
  - id: owasp:api3:2023-no-additionalProperties
    source: Vacuum / Spectral OWASP ruleset
    description: Schemas should set additionalProperties=false to prevent mass assignment.
  - id: owasp:api4:2023-rate-limit
    source: Vacuum / Spectral OWASP ruleset
    description: Operations should advertise rate-limit headers.
  - id: owasp:api8:2023-define-error-responses-401
    source: Vacuum / Spectral OWASP ruleset
    description: Define a 401 response for protected operations.

risk:
  owasp:
    - 'OWASP API Security Top 10 (2023): API1 BOLA, API2 Broken Authentication, API3 BOPLA, API4 Unrestricted Resource Consumption, API8 Security Misconfiguration, API9 Improper Inventory Management, API10 Unsafe Consumption of APIs'
    - 'OWASP Top 10 (web)'
  compliance:
    - SOC 2 — Common Criteria (CC6 Logical Access, CC7 System Operations)
    - ISO/IEC 27001 Annex A controls
    - PCI DSS v4 — applicable when handling cardholder data
    - HIPAA Security Rule — 45 CFR §164.308–312
    - GDPR Art. 32 — security of processing
    - NIST SP 800-218 SSDF — secure SDLC practices
  security_implications: Treat the API surface as the security boundary. Combine transport security (TLS 1.2+/1.3, HSTS), strong authN/Z, input validation, output encoding, rate limiting, secret management, dependency/SBOM scanning, signed builds (SLSA), runtime monitoring, and a published vulnerability-disclosure policy (RFC 9116) with a clear SLA for triage and remediation.

tools:
  - name: OWASP ZAP
    url: https://www.zaproxy.org/
    license: Apache-2.0
    category: DAST
  - name: 42Crunch API Security Audit
    url: https://42crunch.com/
    category: API security platform
  - name: Snyk
    url: https://snyk.io/
    category: SCA / SAST
  - name: Trivy
    url: https://trivy.dev/
    license: Apache-2.0
    category: Vulnerability scanner
  - name: Sigstore (cosign)
    url: https://www.sigstore.dev/
    license: Apache-2.0
    category: Supply-chain signing
  - name: securitytxt.org
    url: https://securitytxt.org/
    category: Generator (RFC 9116)

metrics:
  - name: mean_time_to_remediate
    description: Average time from vulnerability report to fix being deployed.
  - name: critical_cvss_open_count
    description: Count of open CVSS 9.0+ findings across the API surface.
  - name: tls_handshake_failure_rate
    description: Rate of TLS handshake failures; signals misconfiguration or deprecated client suites.
  - name: waf_block_rate
    description: Share of traffic blocked by WAF/edge rules.
  - name: secrets_in_repo_findings
    description: Detected leaked credentials in source repos (push-protection / scanning hits).

examples:
  - provider: GitHub
    url: https://providers.apis.io/providers/github/
    note: Publishes security.txt, runs a coordinated VDP, signs releases.
  - provider: Stripe
    url: https://providers.apis.io/providers/stripe/
    note: Detailed security overview, PCI DSS Level 1, public bug bounty.
  - provider: Google
    url: https://providers.apis.io/providers/google/
    note: Google VRP, OSS-Fuzz, SLSA-aligned build provenance.
  - provider: Microsoft Graph
    url: https://providers.apis.io/providers/microsoft-graph/
    note: MSRC disclosure process, SDL, broad compliance attestations.

related_properties:
  - authentication
  - terms-of-service
  - privacy-policy
  - rate-limits
  - error-codes
---
