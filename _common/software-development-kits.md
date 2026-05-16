---
name: Software Development Kits (SDKs)
description: Providing code snippets, libraries, and full software development kits, or simply SDKs is considered standard operating procedure for APIs. Generating SDKs from OpenAPI has become common, and providing all of the top programming languages is expected by developers, making SDKs one of the essential API building block for any API operations.
image: /images/software-development-kits.png
url: '#'
machineReadable: false
source: concept
tags:
  - SDKs
  - Code
  - Programming Languages
  - Integration
aliases:
  - SDK
  - Client Library
  - Client
  - Bindings
yaml_example: |
  - type: SDKs
    url: https://developers.example.com/sdks

standards:
  - name: OpenAPI Specification 3.1
    url: https://spec.openapis.org/oas/v3.1.0
    kind: OpenAPI Initiative
  - name: OpenAPI Generator
    url: https://openapi-generator.tech/
    kind: Project
  - name: Semantic Versioning 2.0.0
    url: https://semver.org/spec/v2.0.0.html
    kind: SemVer
  - name: SPDX License List
    url: https://spdx.org/licenses/
    kind: Linux Foundation
  - name: SPDX Specification
    url: https://spdx.github.io/spdx-spec/
    kind: ISO/IEC 5962
  - name: npm package.json
    url: https://docs.npmjs.com/cli/v10/configuring-npm/package-json
    kind: Package registry
  - name: PyPI Core Metadata 2.3
    url: https://packaging.python.org/en/latest/specifications/core-metadata/
    kind: PyPA
  - name: Maven POM Reference
    url: https://maven.apache.org/pom.html
    kind: Apache Maven
  - name: NuGet .nuspec
    url: https://learn.microsoft.com/nuget/reference/nuspec
    kind: NuGet
  - name: Go Modules Reference
    url: https://go.dev/ref/mod
    kind: Go Project

openapi_expression:
  - field: info.contact
    spec: OpenAPI 3.x
    description: Often points to the SDK repository or maintainer.
  - field: externalDocs
    spec: OpenAPI 3.x
    description: Frequently used to link to the SDK index page.
  - field: info.license
    spec: OpenAPI 3.x
    description: License of the API description; SDKs typically carry their own SPDX identifier in package metadata.
  - field: x-codeSamples
    spec: Redoc / Redocly vendor extension
    description: Per-operation code samples in target SDK languages.

link_relations:
  - rel: service-desc
    spec: IANA Link Relations
    description: Pointer to the machine-readable description SDKs are generated from.

governance_rules:
  - id: info-contact
    source: Spectral built-in
    description: "`info.contact` must be present so SDK consumers can reach maintainers."
  - id: info-license
    source: Spectral built-in
    description: "`info.license` must be defined."
  - id: operation-operationId
    source: Spectral built-in
    description: Every operation needs a unique operationId — SDK generators map these to method names.
  - id: operation-operationId-unique
    source: Spectral built-in
  - id: operation-tag-defined
    source: Spectral built-in
    description: Operations must be tagged consistently; many generators group methods by tag into namespaces or files.

risk:
  security_implications: SDKs are a software-supply-chain surface. Signed packages, reproducible builds, SBOMs (SPDX/CycloneDX), and pinned transitive dependencies reduce typosquatting and dependency-confusion risk. SDKs that bundle credentials, telemetry, or auto-update behavior need explicit user disclosure.
  compliance:
    - Export controls — SDKs that include or call cryptography may be subject to EAR/Wassenaar review
    - Open-source license compatibility — SDK license must be compatible with bundled transitive dependencies

tools:
  - name: OpenAPI Generator
    url: https://openapi-generator.tech/
    license: Apache-2.0
    category: SDK generator
  - name: Speakeasy
    url: https://www.speakeasy.com/
    category: SDK generator
  - name: Fern
    url: https://www.buildwithfern.com/
    category: SDK generator
  - name: Stainless
    url: https://www.stainless.com/
    category: SDK generator
  - name: Kiota
    url: https://learn.microsoft.com/openapi/kiota/overview
    license: MIT
    category: SDK generator
  - name: liblab
    url: https://liblab.com/
    category: SDK generator

metrics:
  - name: sdk_language_coverage
    description: Number of officially supported SDK languages.
  - name: sdk_release_lag_days
    description: Days between an API release and matching SDK release across languages.
  - name: sdk_weekly_downloads
    description: Package-manager download counts per language.
  - name: sdk_open_issues
    description: Open issues and median time-to-close across SDK repos.
  - name: sdk_breaking_change_rate
    description: Major-version bumps per quarter; high values erode integrator trust.

examples:
  - provider: Stripe
    url: https://providers.apis.io/providers/stripe/
    note: Eight+ official SDKs (Ruby, Node, Python, PHP, Java, Go, .NET, iOS, Android) maintained in-house.
  - provider: Twilio
    url: https://providers.apis.io/providers/twilio/
    note: Multi-language helper libraries generated from internal API definitions.
  - provider: AWS
    url: https://providers.apis.io/providers/aws/
    note: SDKs across 10+ languages with consistent service/client patterns and SBOMs.
  - provider: GitHub
    url: https://providers.apis.io/providers/github/
    note: Octokit family of SDKs covering REST and GraphQL surfaces.

related_properties:
  - documentation
  - openapi
  - getting-started
  - code-samples
  - github
---
