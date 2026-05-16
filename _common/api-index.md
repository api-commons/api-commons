---
name: Index
description: A discoverable catalog of APIs, packages, or related resources published by a provider — a single document that lists what exists and where to find it. The index is the entry point for both humans browsing an offering and machines crawling an ecosystem; it is what makes an API portfolio (rather than a single API) navigable.
image: /images/api-index.png
url: '#'
machineReadable: true
source: commons
tags:
  - Discovery
  - Catalog
  - Inventory
aliases:
  - API Index
  - APIIndex
  - Catalog
  - API Catalog
  - PackageIndex
  - Package Index
yaml_example: |
  - type: Index
    url: https://developers.example.com/apis.json

standards:
  - name: RFC 9727 — api-catalog Well-Known URI
    url: https://www.rfc-editor.org/rfc/rfc9727
    kind: IETF
  - name: APIs.json
    url: https://apisjson.org/
    kind: Community
  - name: Linkset (RFC 9264)
    url: https://www.rfc-editor.org/rfc/rfc9264
    kind: IETF
  - name: schema.org DataCatalog
    url: https://schema.org/DataCatalog
    kind: Schema.org
  - name: schema.org ItemList
    url: https://schema.org/ItemList
    kind: Schema.org

well_known:
  - path: /.well-known/api-catalog
    spec: RFC 9727
    description: Discoverable catalog of an organization's APIs and supporting resources.

media_types:
  - type: application/linkset+json
    spec: RFC 9264
    note: Default response shape for /.well-known/api-catalog.
  - type: application/json
    note: Used by APIs.json and ad-hoc catalogs.
  - type: application/yaml
    note: Common alternate serialization for APIs.json.

link_relations:
  - rel: index
    spec: IANA Link Relations
    description: Refers to a resource serving as an index of the available resources.
  - rel: collection
    spec: RFC 6573
    description: Identifies a target resource that contains a collection of items.
  - rel: service-desc
    spec: RFC 8631
    description: Used per-entry inside catalogs to link out to machine-readable descriptions.

risk:
  security_implications: An index is an attacker's first stop — it enumerates surface area for free. Publish only intentionally public entries; never include staging, internal, or partner-only APIs in a public catalog. Treat the index as a publication boundary and validate it in CI.

tools:
  - name: APIs.io
    url: https://apis.io/
    category: Public API search built on APIs.json catalogs
  - name: Backstage Software Catalog
    url: https://backstage.io/docs/features/software-catalog/
    license: Apache-2.0
    category: Internal catalog
  - name: api-catalog-cli
    url: https://github.com/api-catalog/api-catalog-cli
    category: RFC 9727 tooling

metrics:
  - name: catalog_freshness_days
    description: Days since the index was last regenerated against the live API inventory.
  - name: catalog_drift
    description: Count of deployed APIs missing from the index, or indexed APIs no longer deployed.
  - name: catalog_crawl_hits
    description: Requests against /.well-known/api-catalog from known directories or aggregators.

examples:
  - provider: U.S. General Services Administration
    url: https://api.data.gov/
    note: Federated catalog spanning multiple federal agencies.
  - provider: APIs.io
    url: https://apis.io/
    note: Public APIs.json-based catalog of API providers.
  - provider: AWS
    url: https://docs.aws.amazon.com/general/latest/gr/aws-service-information.html
    note: Service-level index pointing into per-service documentation.

related_properties:
  - documentation
  - portal
  - openapi
---
