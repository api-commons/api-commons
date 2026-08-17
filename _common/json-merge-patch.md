---
name: JSON Merge Patch
description: A standardized way to describe a partial update to a JSON document, defined in RFC 7396 and carried as the application/merge-patch+json media type on an HTTP PATCH. The patch document mirrors the shape of the target — present members are replaced, null members are removed, and absent members are left alone — which makes it the lowest-ceremony option for partial updates when consumers should not have to send a whole resource back to change one field. Declaring merge-patch support explicitly tells consumers and agents that PATCH means RFC 7396 semantics rather than a provider-invented convention.
image: /images/schema.png
url: '#'
machineReadable: false
source: contracts
tags:
  - Patch
  - Partial Update
  - JSON
  - IETF
aliases:
  - Merge Patch
  - RFC 7396
  - merge-patch+json
  - Partial Update
yaml_example: |
  - type: JSONMergePatch
    url: https://developers.example.com/json-merge-patch

standards:
  - name: RFC 7396 — JSON Merge Patch
    url: https://www.rfc-editor.org/rfc/rfc7396
    kind: IETF
  - name: RFC 5789 — PATCH Method for HTTP
    url: https://www.rfc-editor.org/rfc/rfc5789
    kind: IETF
  - name: RFC 6902 — JavaScript Object Notation (JSON) Patch
    url: https://www.rfc-editor.org/rfc/rfc6902
    kind: IETF (the operation-based alternative)
  - name: RFC 9110 — HTTP Semantics
    url: https://www.rfc-editor.org/rfc/rfc9110
    kind: IETF
  - name: RFC 9457 — Problem Details for HTTP APIs
    url: https://www.rfc-editor.org/rfc/rfc9457
    kind: IETF
  - name: OpenAPI Specification (requestBody content media types)
    url: https://spec.openapis.org/oas/latest.html
    kind: OpenAPI Initiative

headers:
  - name: Content-Type
    direction: request
    spec: RFC 7396 §4
    description: Must be application/merge-patch+json for a merge patch request body.
  - name: Accept-Patch
    direction: response
    spec: RFC 5789 §3.1
    description: Advertises which patch media types a resource accepts; the discovery hook most providers skip.
  - name: If-Match
    direction: request
    spec: RFC 9110 §13.1.1
    description: Guards against lost updates by conditioning the patch on the current ETag.
  - name: ETag
    direction: response
    spec: RFC 9110 §8.8.3
    description: Gives clients the validator to send back in If-Match on the next patch.

status_codes:
  - code: '200'
    name: OK
    spec: RFC 9110 §15.3.1
    description: Patch applied and the updated representation returned.
  - code: '204'
    name: No Content
    spec: RFC 9110 §15.3.5
    description: Patch applied with no representation returned.
  - code: '409'
    name: Conflict
    spec: RFC 9110 §15.5.10
    description: Patch cannot be applied against the current state of the resource.
  - code: '412'
    name: Precondition Failed
    spec: RFC 9110 §15.5.13
    description: If-Match validator no longer matches — the resource changed under the client.
  - code: '415'
    name: Unsupported Media Type
    spec: RFC 9110 §15.5.16
    description: Resource does not accept application/merge-patch+json.
  - code: '422'
    name: Unprocessable Content
    spec: RFC 9110 §15.5.21
    description: Patch is well-formed merge-patch but produces an invalid resource.

media_types:
  - type: application/merge-patch+json
    spec: RFC 7396
    note: The merge patch document itself.
  - type: application/json-patch+json
    spec: RFC 6902
    note: The operation-based alternative — use when order, test, move, or array element edits matter.
  - type: application/problem+json
    spec: RFC 9457
    note: Recommended payload for explaining a rejected patch.

openapi_expression:
  - field: paths.{path}.patch.requestBody.content
    spec: OpenAPI 3.x
    description: Key the request body on application/merge-patch+json and give it a schema with no required members.
  - field: components.schemas
    spec: OpenAPI 3.x
    description: The patch schema is usually the resource schema with required dropped and nullable allowed, not the resource schema itself.
  - field: responses.'415'
    spec: OpenAPI 3.x
    description: Document the unsupported-media-type response so clients know patch format negotiation exists.

governance_rules:
  - id: oas-operation-4xx-response
    source: Spectral built-in
    description: PATCH operations should document 409, 412, and 415 alongside the success response.
  - id: oas-request-body-content
    source: Spectral (ruleset-dependent)
    description: Check that a PATCH request body declares an explicit patch media type rather than plain application/json.

risk:
  owasp:
    - 'OWASP API Security Top 10: API3:2023 Broken Object Property Level Authorization'
    - 'OWASP API Security Top 10: API6:2023 Unrestricted Access to Sensitive Business Flows'
  compliance:
    - SOC 2 CC8.1 — change management with traceable partial updates
    - GDPR Art. 16 — right to rectification is frequently implemented as a partial update
  security_implications: >-
    Merge patch is a mass-assignment vector by design — the patch document names the fields to change, so any writable
    field an attacker can guess is reachable unless the server allowlists per-property authorization. Two further traps
    are specific to RFC 7396: a null member means delete, so a client that serializes absent optional fields as null
    will silently erase data; and merge patch cannot address array elements, so array members are always replaced
    wholesale. Reject unknown members, authorize per property rather than per resource, and pair patches with If-Match
    so concurrent writers cannot clobber each other.

tools:
  - name: JSON Merge Patch tool and API
    url: https://www.jsonmergepatch.com/
    category: Browser tool + hosted API for applying and generating merge patches
  - name: json-merge-patch (npm)
    url: https://github.com/pierreinglebert/json-merge-patch
    license: MIT
    category: JavaScript library
  - name: Spectral
    url: https://github.com/stoplightio/spectral
    license: Apache-2.0
    category: Linter

metrics:
  - name: patch_media_type_share
    description: Share of PATCH operations declaring an explicit patch media type versus plain application/json.
  - name: patch_415_rate
    description: Fraction of PATCH requests rejected as unsupported media type; indicates undocumented format expectations.
  - name: patch_412_rate
    description: Fraction of PATCH requests failing a precondition; measures concurrent-write pressure.
  - name: unintended_null_deletes
    description: Count of patches whose null members removed a field the client did not intend to remove.

examples:
  - provider: Kubernetes
    url: https://kubernetes.io/docs/tasks/manage-kubernetes-objects/update-api-object-kubectl-patch/
    note: Supports RFC 7396 merge patch alongside RFC 6902 JSON patch and its own strategic merge patch.

related_properties:
  - openapi
  - json-schema
  - error-codes
  - versioning
  - data-contract
---
