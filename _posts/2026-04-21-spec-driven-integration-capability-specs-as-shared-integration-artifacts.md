---
layout: post
title: 'Spec-Driven Integration: Capability Specs as Shared Integration Artifacts'
image: /assets/images/blog/spec-driven-integration-capability-specs-as-shared-integration-artifacts.png
---
The API Commons principle has always been that specifications are shareable artifacts. An OpenAPI document published to the commons can be consumed, implemented, forked, and composed by anyone. The specification exists independently of any particular implementation.

[Spec-Driven Integration](https://github.com/naftiko/framework/wiki/Spec%E2%80%90Driven-Integration) extends this principle into the integration layer. When the specification IS the integration — not documentation about it, but the executable definition itself — then sharing a spec means sharing a running integration. Fork it, modify it, deploy it. The spec is the artifact and the implementation simultaneously.

## Integration Artifacts in the Commons

A Naftiko capability spec is a YAML file that declares what an integration consumes and what it exposes. It is self-contained: authentication, data shaping, protocol mapping, and multi-surface exposure all live in the same document. It is executable: the Naftiko engine reads it at runtime and serves live integrations without code generation.

This makes capability specs ideal commons artifacts:

- **Shareable** — publish a spec and any team can run it
- **Composable** — import shared definitions and compose new capabilities from them
- **Forkable** — derive a variant optimized for a different consumer or context
- **Versioned** — track evolution in git like any other specification

When the spec is the integration, the commons becomes an integration marketplace. Not a catalog of documentation — a catalog of executable integration artifacts.

## SDI and the Commons Philosophy

SDI's core principle — specifications as the lingua franca — is the commons philosophy applied to integrations. The spec is the shared contract. It is human-readable for review. It is machine-readable for execution. It is portable across any runtime that implements the specification format.

Open-source capability specs, published under open licenses, composed from shared building blocks, executing on an open-source engine — this is the commons vision realized for the integration layer.

[Read the SDI methodology](https://github.com/naftiko/framework/wiki/Spec%E2%80%90Driven-Integration) | [Explore the Naftiko Fleet](https://github.com/naftiko/fleet?utm_source=api-commons&utm_medium=blog&utm_campaign=methodology-spec-driven-integration&utm_content=sdi-shared-artifacts-commons)
