---
layout: post
title: "Toolsmith: Forge MCP Tools and Agent Skills From Your OpenAPI"
date: 2026-07-28
tags:
  - API Commons
  - MCP
  - Agent Skills
  - Agents
  - OpenAPI
image: /assets/images/blog/toolsmith-forge-mcp-tools-and-agent-skills.png
---

An OpenAPI tells developers what your API can do. Agents need more: an MCP tool for each operation with an honest input schema and behavior annotations, the resources and prompts that give it context, sampling guidance where it helps — and Agent Skills that teach an agent to apply each tool competently. So we built [**Toolsmith**](https://toolsmith.apicommons.org), a browser-first workbench for designing that agent layer. No backend, no accounts; it runs in your browser.

[**Try it → toolsmith.apicommons.org**](https://toolsmith.apicommons.org)

## Design the Agent Layer, Operation by Operation

Load an OpenAPI — the [API Evangelist](https://apievangelist.com) and [APIs.io](https://apis.io) APIs are one click away, or point it at any URL, upload, or paste. Then, for every operation, design a real **MCP tool**: an input schema drawn from the parameters and request body, annotations for whether it's read-only, destructive, or idempotent, the **resources** an agent should read for context, **prompt** templates that guide its use, and **sampling** guidance for when the server should reason over a result. On top of each tool you write one or more **Agent Skills** — and an **API-level** slot holds the skills that span the whole surface, like an overview that indexes every tool.

Everything you design is written back into your OpenAPI as `x-mcp` and `x-agent-skills` extensions per operation, with an `x-mcp-server` block at the root. **The enriched OpenAPI is the single artifact of record** — edit the raw document and your designs travel with it. A deterministic "Draft all" seeds a design for every operation from what the contract already knows; no AI calls, nothing leaves the page.

## Checks Against the Actual Specs

A **Checks** pass lints the whole design against the [MCP](https://modelcontextprotocol.io) spec — tool-name rules and uniqueness, input-schema consistency, annotation sanity, resource URIs, and the registry `server.json` shape (reverse-DNS name, semver, https remotes) — and every [Agent Skills](https://agentskills.io) frontmatter constraint (name pattern, description and compatibility caps, body guidance). Each finding jumps you to the operation that needs it.

## Five Exports — and a Runnable Server

| Export | What it is |
| --- | --- |
| **Enriched OpenAPI** | Your contract with the agent layer embedded as `x-mcp` / `x-agent-skills` / `x-mcp-server` extensions. |
| **MCP server design** | Tools, resources, prompts, and sampling in the shapes MCP clients see. |
| **server.json** | A registry-ready manifest (2025-09-29 schema) for the official MCP Registry. |
| **Agent Skills bundle** | One `SKILL.md` per skill, zipped by directory, with an agent-skills-discovery `index.json` ready for `.well-known/agent-skills/`. |
| **APIs.json properties** | Property entries that wire the artifacts to your provider listing. |
| **Runnable MCP server** | A complete TypeScript project on the official `@modelcontextprotocol/sdk` where every tool proxies to its real operation — path/query/header/body mapping and auth from your spec. `npm install && npm run dev` and it serves. |

That last one closes the loop from *designing* the agent layer to *running* it. We generated a server from the API Evangelist OpenAPI, connected a real MCP client, and it listed fifty-one tools and made live calls straight back to the upstream API — no glue code.

## Open, and It Doesn't Stand Alone

Toolsmith is one of the [API Commons tools](https://apicommons.org/tools/) — open, client-side, and built to hand its output to the tools around it. It pairs with [Context Gate](https://contextgate.apicommons.org) for governing what an agent is allowed to consume and the [Validator](https://validator.apicommons.org) for keeping the contract honest. The agent layer is the interface a growing share of your consumers will use; this is the workbench for designing it on purpose.
