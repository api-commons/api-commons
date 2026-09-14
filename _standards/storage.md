---
name: Storage
description: >-
  Nobody ratified S3 as the object-storage standard. It became one because vendor after vendor
  implemented Amazon's interface on their own hardware, and an application written against one
  now runs against dozens by changing an endpoint. This is also the profile with the weakest
  evidence behind its adoption numbers, and it says so rather than presenting a confident
  table.
cohort: reimplementation — independent servers built against a published interface
status: Published — 116 operations graded, 46 adopters recorded, none testable
repository: https://github.com/api-commons/storage
image: /images/api-commons-icon.png

profiles:

  - name: The S3 Interface
    standard_id: s3-2006-03-01
    originator: Amazon Web Services
    description: >-
      8 core operations — the CRUD primitives and nothing else. Multipart upload does
      not reach core, and the deprecated ListObjects outpolls ListObjectsV2 five to one.
    source:
      name: boto/botocore — botocore/data/s3/2006-03-01/service-2.json
      url: https://github.com/boto/botocore
      license: Apache-2.0
      pinned: aeb03fc4ae530e0b3f47d588b6021581db870c8c
      note: >-
        116 operations, 722 shapes, protocol
        rest-xml, API version 2006-03-01. The catalog's
        own S3 spec carried 15 paths against these 116, which is why this was generated fresh.
    measurement: >-
      58 providers claim S3 compatibility and 12 publish a spec
      declaring an S3 operation — the thinnest evidence base of the five standards here, and
      every share should be read as a signal rather than a census. There is no tested grade and
      that was tested rather than assumed: an S3 server validates the signature before it routes
      the operation, so MinIO's public endpoint answers AccessDenied to a supported and an
      unsupported subresource alike, and AWS returns 307 to everything. The vendor compatibility
      matrices that would have been the natural evidence render client-side or mark support in
      no parseable structure, so they are recorded as claims and nothing is synthesised from
      them.
    tiers:
      - name: Core
        count: 8
        description: >-
          ListBuckets and ListObjects at 83.3%, then DeleteBucket, DeleteObject and GetObject at
          75%, CreateBucket at 66.7%, HeadObject and PutObject at 58.3%. ListObjects — the
          version AWS has recommended against for years — outpolls ListObjectsV2 by five to one.
          What an ecosystem implements and what its originator recommends are different things.
      - name: Extended
        count: 8
        description: >-
          Multipart upload (41.7% for CreateMultipartUpload), HeadBucket, CopyObject and
          ListObjectsV2 at 16.7%. The threshold here is a count rather than a percentage: with a
          cohort of 12, one declaration is 8.3% and a single provider is not
          corroboration.
      - name: Vendor
        count: 100
        description: >-
          Declared by at most one provider. Nearly all of the bucket configuration surface —
          ?acl, ?cors, ?lifecycle, ?versioning, ?replication, Storage Lens, Access Grants.
    adopters:
      count: 46
      as_of: '2026-09-13'
      url: https://github.com/api-commons/storage/blob/main/adopters/s3-2006-03-01.yml
      matrix_url: https://github.com/api-commons/storage/blob/main/adopters/s3-2006-03-01-matrix.md
      evidence:
        - grade: declared
          count: 12
          description: Publishes an OpenAPI declaring S3 operations. This is the whole measurement.
        - grade: vendor-matrix
          count: 2
          description: >-
            MinIO and Cloudflare R2 publish compatibility tables, recorded here as their claim
            with a URL and a date. No per-operation support is read from them.
        - grade: prose
          count: 32
          description: Says S3-compatible and nothing a reader can check.
        - grade: tested
          count: 0
          description: >-
            Structurally unavailable. Authorization precedes routing, so an anonymous caller
            learns nothing about which operations exist.
    apis:
      - name: Model
        description: >-
          The artifact of record — tier-stamped, with the query subresources that identify 99 of
          the 116 operations intact.
        properties:
          - type: Model
            url: https://raw.githubusercontent.com/api-commons/storage/main/standard/s3-2006-03-01/s3-model.json
      - name: OpenAPI
        description: >-
          A labelled convenience. The API collapses to 12 method and path
          pairs, so each keeps one operation and lists the rest in x-s3-operations.
        properties:
          - type: OpenAPI
            url: https://raw.githubusercontent.com/api-commons/storage/main/standard/s3-2006-03-01/openapi.yml
      - name: Profile
        description: All 116 operations with tier, evidence and subresource.
        properties:
          - type: Profile
            url: https://raw.githubusercontent.com/api-commons/storage/main/standard/s3-2006-03-01/profile.yml
      - name: Spectral Ruleset
        description: >-
          8 core-operation rules plus one that warns on JSON-only responses, because
          S3 is rest-xml. It matches path shape rather than parameter spelling.
        properties:
          - type: SpectralRules
            url: https://raw.githubusercontent.com/api-commons/storage/main/standard/s3-2006-03-01/spectral/s3-profile.yaml
      - name: Arazzo
        description: >-
          Create, put, get, list, delete, delete. The only conformance flow in this programme
          that cannot be run anonymously.
        properties:
          - type: Arazzo
            url: https://raw.githubusercontent.com/api-commons/storage/main/standard/s3-2006-03-01/arazzo/core-conformance.yml
      - name: MCP Tools
        description: MCP tool definitions for the core tier.
        properties:
          - type: MCP
            url: https://raw.githubusercontent.com/api-commons/storage/main/standard/s3-2006-03-01/mcp/tools.json

licensing: >-
  Derived from botocore's service-2.json under Apache-2.0, with its NOTICE carried in the
  repository. API Commons artifacts are CC BY-NC-SA 4.0 and code is Apache-2.0. Not published
  by, affiliated with, or endorsed by Amazon Web Services; the name S3 appears as a factual
  reference to the interface described.

tags:
  - Object Storage
  - Storage
  - Cloud Storage

further_reading:
  - name: Why OpenAPI cannot describe S3
    url: https://github.com/api-commons/storage/blob/main/standard/s3-2006-03-01/profile.yml
    description: >-
      99 of 116 operations are identified by a query subresource and the API collapses to 12
      method and path pairs. The profile records every collision.
  - name: The adopters building block
    url: https://github.com/api-commons/adopters
    description: The schema behind the registry, and the evidence grades it enforces.
---
