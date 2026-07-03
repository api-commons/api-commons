---
layout: post
title: "An MCP Server for API Governance"
date: 2026-07-06
tags:
  - API Commons
  - MCP
  - Model Context Protocol
  - Spectral
  - API Governance
  - agents
image: /assets/images/blog/an-mcp-server-for-api-governance.png
---

Every governance tool we've shipped so far assumes a human opens a tab. [API Validator](https://validator.apicommons.org) is a browser app. Discovery is a browser app. That's the right default when a person is doing the work, but it's the wrong shape for the thing increasingly doing the work alongside them: an agent, drafting an OpenAPI document, wiring up an Arazzo workflow, or reviewing someone else's PR, with no browser tab to open and no reason to know one exists.

So we built [**API Governance MCP**](https://github.com/api-commons/api-governance-mcp) — the same governance ruleset as the Validator, exposed as a [Model Context Protocol](https://modelcontextprotocol.io) server any agent can call directly.

[**Install → `npx @api-common/api-governance-mcp`**](https://github.com/api-commons/api-governance-mcp#use-it)

## Same Engine, Same Ruleset, Different Surface

This isn't a new governance product. It's the Validator's engine — [Spectral](https://github.com/stoplightio/spectral) — and its compiled, best-of-breed ruleset, running server-side over stdio instead of in a browser tab. **733 rules across 12 artifact formats** — OpenAPI, AsyncAPI, Arazzo, APIs.json, JSON Schema, MCP, agent skills, rate limits, FinOps, and more — compiled from public Spectral rulesets and the [API Evangelist](https://apievangelist.com) governance rules. Every rule ships at `info` to educate rather than block; you raise the ones you want to enforce.

We built the MCP server as a thin, faithful port: the same rule catalog, the same custom functions, the same severity policy. Anything you'd catch pasting a document into the Validator, an agent now catches on its own, mid-task.

## The Tools

| Tool | What it does |
| --- | --- |
| `lint_artifact` | Lint an artifact (`content`, optional `format`, optional custom `ruleset`) → findings (code, message, severity, path) + counts |
| `list_rulesets` | The artifact formats it governs and, per format, the rules it applies |
| `list_formats` | The artifact formats the ruleset can lint |
| `describe_rule` | Look a finding's `code` up → title, description, severity, tags, target path, and a remediation prompt |
| `validate_ruleset` | Structurally validate a custom Spectral ruleset before you lint with it |
| `request_review` | Get a ready-to-send email to engage [API Evangelist](https://apievangelist.com/services/) for expert governance services |

`describe_rule` is the one that didn't exist in the browser tool. In a UI you hover a rule and read a tooltip; an agent needs that same context as a callable lookup, so it can read the remediation guidance for a finding and act on it without a human relaying the explanation back and forth.

## Why This Changes How Teams Engage With Governance

A browser validator is something a person has to remember exists and choose to visit. That's the whole friction model of governance tooling up to now — it works exactly as well as everyone's discipline about opening the tab. An MCP server flips that: governance stops being a destination and becomes a **capability the agent already has**, the same way it already knows how to run a test suite or check that code compiles. The artifact gets linted as a normal step in producing it, not as a separate errand someone has to initiate.

That matters most for the work nobody was checking anyway — the OpenAPI an agent drafts inline in a chat, the Arazzo workflow it wires up on request, the MCP server definition it scaffolds for you. None of that touched a validator before, because there was no natural moment for a human to paste it in. Now there's a tool call sitting right next to whatever the agent is already doing, so it can check its own output before handing it back — and tell you what it found, in the same conversation, instead of leaving governance for a CI run three steps later.

And when a finding isn't something an agent should just fix on its own — a judgment call, a custom ruleset for your org, a real review — `request_review` hands it a ready-to-send email instead of a shrug. The tool knows the difference between "lint this and fix it" and "this needs a person," and routes to [API Evangelist](https://apievangelist.com/services/) for the latter rather than pretending automation is the whole answer.

## Try It

```json
{
  "mcpServers": {
    "api-governance": {
      "command": "npx",
      "args": ["-y", "@api-common/api-governance-mcp"]
    }
  }
}
```

Drop that into Claude, Cursor, or any MCP client, then ask it to lint an OpenAPI document and tell you what to fix. It's [open source](https://github.com/api-commons/api-governance-mcp), Apache-2.0, and free to run yourself — the expert services around it come from [API Evangelist](https://apievangelist.com/services/).

[**On GitHub →**](https://github.com/api-commons/api-governance-mcp) | [**On npm →**](https://www.npmjs.com/package/@api-common/api-governance-mcp) | [**API Validator →**](https://validator.apicommons.org)
