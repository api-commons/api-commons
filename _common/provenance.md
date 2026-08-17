---
name: Provenance
description: Where the data, the artifact, or the API description actually came from — who or what produced it, from which source, through which activity, and when. Provenance is the difference between an artifact being present and an artifact being trustworthy, and it is the property most often missing when an API description, a dataset, or a generated answer is reused downstream. Two distinct families are in play, and an API program usually needs both — data provenance, described by the W3C PROV family, and build or supply-chain provenance, described by in-toto, SLSA, and SPDX.
image: /images/provenance.png
url: '#'
machineReadable: false
source: contracts
tags:
  - Provenance
  - Trust
  - Lineage
  - Attestation
aliases:
  - Lineage
  - Data Provenance
  - Attestation
  - PROV
  - Chain of Custody
yaml_example: |
  - type: Provenance
    url: https://developers.example.com/provenance

standards:
  - name: PROV-DM — The PROV Data Model
    url: https://www.w3.org/TR/prov-dm/
    kind: W3C Recommendation
  - name: PROV-O — The PROV Ontology
    url: https://www.w3.org/TR/prov-o/
    kind: W3C Recommendation
  - name: PROV-N — The Provenance Notation
    url: https://www.w3.org/TR/prov-n/
    kind: W3C Recommendation
  - name: PROV Model Primer / Overview
    url: https://www.w3.org/TR/prov-overview/
    kind: W3C Note
  - name: PROV-JSONLD — A JSON-LD Representation for the PROV Data Model
    url: https://www.w3.org/submissions/prov-jsonld/
    kind: W3C Member Submission (not a Recommendation)
  - name: PROV-JSON — A JSON Representation for PROV
    url: https://www.w3.org/submissions/prov-json/
    kind: W3C Member Submission (not a Recommendation)
  - name: JSON-LD 1.1
    url: https://www.w3.org/TR/json-ld11/
    kind: W3C Recommendation
  - name: in-toto — supply chain attestation framework
    url: https://in-toto.io/
    kind: CNCF / Linux Foundation
  - name: SLSA — Supply-chain Levels for Software Artifacts
    url: https://slsa.dev/
    kind: OpenSSF
  - name: SPDX — Software Package Data Exchange
    url: https://spdx.dev/
    kind: Linux Foundation / ISO 5962
  - name: Sigstore
    url: https://www.sigstore.dev/
    kind: OpenSSF
  - name: C2PA — Content Credentials
    url: https://c2pa.org/
    kind: C2PA / Linux Foundation

media_types:
  - type: application/ld+json
    spec: JSON-LD 1.1
    note: The serialization PROV-JSONLD rides on, so provenance can be processed as linked data.
  - type: application/json
    spec: PROV-JSON
    note: Plain-JSON PROV encoding for consumers that do not process linked data.
  - type: text/provenance-notation
    spec: PROV-N
    note: Human-readable PROV notation.

openapi_expression:
  - field: info.x-provenance
    spec: Vendor extension
    description: No standard OpenAPI field carries provenance; providers commonly declare source and generator as an extension.
  - field: info.description
    spec: OpenAPI 3.x
    description: Where hand-authored descriptions usually state whether the document was generated from code or written by hand.
  - field: externalDocs
    spec: OpenAPI 3.x
    description: Can point at the provenance record or attestation for the description itself.

link_relations:
  - rel: via
    spec: RFC 8288 / IANA Link Relations
    description: Identifies a resource that is the source of the information in the context resource.
  - rel: describedby
    spec: IANA Link Relations
    description: Points from an artifact to the document describing it, including a provenance record.
  - rel: canonical
    spec: RFC 6596
    description: Names the authoritative location, the first question any provenance check asks.

governance_rules:
  - id: oas-info-contact
    source: Spectral built-in
    description: An artifact with no accountable owner cannot carry credible provenance.
  - id: oas-info-license
    source: Spectral built-in
    description: License is the minimum provenance claim on a reusable description.
  - id: oas3-server-not-example.com
    source: Spectral built-in
    description: Placeholder servers are the clearest signal a description was scaffolded rather than derived from a running API.

risk:
  compliance:
    - EU AI Act Art. 10 — data governance and traceability of training data
    - GDPR Art. 30 — records of processing activities
    - US EO 14028 / NIST SP 800-218 (SSDF) — provenance and SBOM for software supply chains
    - FDA / 21 CFR Part 11 — audit trails for regulated records
    - SOC 2 CC7.2 — evidence that monitored artifacts are what they claim to be
  security_implications: >-
    Provenance is what makes an artifact checkable rather than merely present. Without it, a scaffolded or fabricated
    OpenAPI is indistinguishable from one derived from a running API, an SBOM cannot be tied to the build that produced
    it, and a dataset cannot be traced to a source with a compatible license. Provenance records are also a disclosure
    surface in their own right — build hosts, internal repository paths, and contributor identities routinely leak
    through attestations. Publish provenance signed and scoped, verify signatures rather than trusting the presence of
    a record, and treat an unsigned attestation as an unverified claim.

tools:
  - name: Sigstore cosign
    url: https://www.sigstore.dev/
    license: Apache-2.0
    category: Signing and verification
  - name: in-toto attestation framework
    url: https://in-toto.io/
    license: Apache-2.0
    category: Supply-chain attestation
  - name: SLSA verifier
    url: https://slsa.dev/
    category: Build provenance verification
  - name: SPDX tools
    url: https://spdx.dev/
    license: Apache-2.0
    category: SBOM

metrics:
  - name: artifacts_with_provenance
    description: Share of published artifacts (descriptions, datasets, packages) carrying a provenance record.
  - name: provenance_verification_rate
    description: Fraction of provenance records that verify against a signature rather than merely existing.
  - name: source_traceable_fields
    description: Share of fields in a published dataset traceable to a named originating source.
  - name: unattested_dependency_count
    description: Dependencies in the estate with no build attestation.

examples:
  - provider: GitHub
    url: https://docs.github.com/en/actions/how-tos/secure-your-work/use-artifact-attestations/use-artifact-attestations
    note: Artifact attestations bind a build to its source and workflow, verifiable with the GitHub CLI.
  - provider: npm
    url: https://docs.npmjs.com/generating-provenance-statements
    note: Publishes signed provenance statements linking a package version to the repository and CI run that built it.

related_properties:
  - json-ld
  - json-ld-context
  - interface-license
  - governance-rules
  - lifecycle
  - change-log
---
