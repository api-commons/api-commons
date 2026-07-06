---
layout: post
title: "Agent Rule Export: Rulesets as Agent-Native Guidance"
date: 2026-07-22
tags:
  - API Commons
  - API Governance
  - Agents
  - MCP
image: /assets/images/blog/agent-rule-export-rulesets-as-agent-native-guidance.png
---

A Spectral ruleset is built to be executed — it runs against a finished document and reports what is wrong. But more and more APIs are being authored by agents, and the way we govern generated work is still to lint it after the fact and hand back a list of failures. That is the wrong moment. An agent that could read the rules before it acts would write to them. So we built [**Agent Rule Export**](https://agents.apicommons.org): it turns a governance ruleset into artifacts an agent can follow while authoring, not just fail after linting.

[**Try it → agents.apicommons.org**](https://agents.apicommons.org)

## Four Agent-Native Artifacts

Point it at a ruleset and it exports the same governance in four shapes, each aimed at a different part of an agent's workflow:

| Artifact | What it is |
| --- | --- |
| **AGENTS.md governance block** | Imperative MUST / SHOULD / MAY rules grouped by section, for the emerging `AGENTS.md` repo convention a coding agent reads while it works. |
| **System-prompt instruction set** | A compact, token-efficient priming block that steers an LLM, rules ordered by strength. |
| **Remediation prompt pack** | Per-rule AI-remediation prompts as a JSON map keyed by rule id — an agent looks up the exact fix for a violation. |
| **Compact rule digest** | A machine-readable checklist (id, requirement, where, severity, tags) stripped of Spectral execution detail, for an agent to self-check. |

The bridge between the two worlds is a single mapping: severity becomes strength. An `error` rule becomes a **MUST**, `warn` and `info` become **SHOULD**, a `hint` becomes **MAY**. The rules a linter would enforce after the fact become guidance the agent carries into the work.

## Bring Your Own Rules, and It Runs in the Browser

Pick a format — OpenAPI, AsyncAPI, Arazzo — and optionally filter by consumer experience or a search term, then copy or download any of the four artifacts. Or switch the source to **Paste your own** and drop in a Spectral `rules:` map to export *your* governance. Everything runs client-side; anything you paste never leaves the page, because there is no server.

It pairs with the [**Validator**](https://validator.apicommons.org), which enforces the rules, and the [**Governance MCP**](https://github.com/api-commons/api-governance-mcp), which lets an agent lint on demand: export the guidance here so the agent writes it right the first time, and enforce with the others when you want to be sure.

Agent Rule Export is one of the [API Commons tools](https://apicommons.org/tools/), and like the rest of them it is open, portable, and Spectral underneath — because the rules that decide whether an API is any good should not be locked inside a vendor, and neither should the guidance an agent needs to get it right. This is another in the series introducing the tools one at a time.
