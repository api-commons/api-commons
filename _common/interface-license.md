---
name: Interface License
description: Using the API Commons interface license to provide a legal position of the naming, ordering, and overall design of your API, not just the code or other parts. An interface license will help define the legal tone you take with how your API paths are able to be put to work within other applications and integrations.
image: /images/interface-license.png
url: https://github.com/api-commons/interface-license
machineReadable: true
source: commons
tags:
  - Legal
  - Licensing
  - Client
  - Server
  - Data
aliases:
  - API License
  - Specification License
  - Interface Copyright
gist: https://gist.github.com/kinlane/d4965f2d9a39135f2bfd33f0e9cbc42d.js
yaml_example: |
  - type: InterfaceLicense
    url: https://developers.example.com/license

standards:
  - name: SPDX License List
    url: https://spdx.org/licenses/
    kind: Linux Foundation
  - name: SPDX Specification
    url: https://spdx.dev/specifications/
    kind: ISO/IEC 5962
  - name: OpenAPI Specification — info.license
    url: https://spec.openapis.org/oas/latest.html#license-object
    kind: OpenAPI Initiative
  - name: OpenAPI Specification (Apache-2.0)
    url: https://www.apache.org/licenses/LICENSE-2.0
    kind: ASF
  - name: Open Source Initiative — approved licenses
    url: https://opensource.org/licenses/
    kind: OSI
  - name: Creative Commons licenses
    url: https://creativecommons.org/licenses/
    kind: Creative Commons
  - name: FRAND licensing principles
    url: https://www.etsi.org/intellectual-property-rights
    kind: ETSI
  - name: API Commons interface license
    url: https://github.com/api-commons/interface-license
    kind: Community

media_types:
  - type: text/html
    note: License texts and summaries are typically served as HTML.
  - type: text/plain
    note: LICENSE files are conventionally plain text.
  - type: application/json
    note: Machine-readable license declarations including SPDX identifiers.

openapi_expression:
  - field: info.license.name
    spec: OpenAPI 3.x
    description: Human-readable license name (e.g. "Apache 2.0").
  - field: info.license.url
    spec: OpenAPI 3.x
    description: URL to the full license text.
  - field: info.license.identifier
    spec: OpenAPI 3.1
    description: SPDX license identifier (e.g. "Apache-2.0", "MIT"); mutually exclusive with url.

link_relations:
  - rel: license
    spec: RFC 4946 / IANA Link Relations
    description: Refers to a license associated with the context.

governance_rules:
  - id: info-license
    source: Spectral built-in
    description: API metadata must declare a license.
  - id: license-url
    source: Spectral built-in
    description: License must resolve to a URL or SPDX identifier.

risk:
  compliance:
    - SPDX — license identification for software bill of materials
    - ISO/IEC 5962 — SPDX standardization
    - DMCA — derivative-work claims around API surface copying
    - EU Copyright Directive — software interface protections (Art. 5)
  security_implications: Ambiguous or missing interface licenses block enterprise adoption and create ammunition for clone / fork disputes. Re-licensing without versioning the spec breaks SBOM tooling that pins on SPDX identifiers.

tools:
  - name: SPDX License List
    url: https://spdx.org/licenses/
    license: CC0-1.0
    category: License registry
  - name: ScanCode Toolkit
    url: https://github.com/nexB/scancode-toolkit
    license: Apache-2.0
    category: License scanner
  - name: FOSSA
    url: https://fossa.com/
    category: License compliance
  - name: Black Duck
    url: https://www.blackduck.com/
    category: License compliance
  - name: REUSE
    url: https://reuse.software/
    license: CC0-1.0
    category: Licensing compliance
  - name: ClearlyDefined
    url: https://clearlydefined.io/
    category: License metadata

metrics:
  - name: license_declared
    description: Whether the API specification declares an info.license.
  - name: spdx_identifier_present
    description: Whether the declared license carries a valid SPDX identifier.
  - name: osi_approved
    description: Whether the declared license is OSI-approved.
  - name: license_change_count
    description: Number of license changes across published API versions.

examples:
  - provider: OpenAPI Initiative
    url: https://providers.apis.io/providers/openapi/
    note: The OpenAPI Specification itself is licensed Apache-2.0.
  - provider: Stripe
    url: https://providers.apis.io/providers/stripe/
    note: Stripe publishes OpenAPI definitions with an MIT license.
  - provider: GitHub
    url: https://providers.apis.io/providers/github/
    note: GitHub OpenAPI description is licensed under a permissive (MIT) license.
  - provider: Kubernetes
    url: https://providers.apis.io/providers/kubernetes/
    note: Kubernetes OpenAPI spec is distributed under Apache-2.0.

related_properties:
  - terms-of-service
  - privacy-policy
  - code-of-conduct
  - openapi
  - pricing
---
