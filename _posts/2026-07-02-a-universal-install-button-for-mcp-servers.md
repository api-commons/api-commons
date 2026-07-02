---
layout: post
title: "A Universal Install Button for MCP Servers"
date: 2026-07-02
tags:
  - API Commons
  - MCP
  - Model Context Protocol
  - install
  - registry
  - agents
image: /assets/images/blog/a-universal-install-button-for-mcp-servers.png
---

Every MCP server today ships its own install instructions, and every one of them is different. A README that tells you to paste a JSON blob into `claude_desktop_config.json`. A different README that gives you a `claude mcp add` command. A third that assumes you're in Cursor and links a deep link. Multiply that by the couple dozen MCP clients now in the wild — Claude Desktop, Cursor, VS Code, Visual Studio, Windsurf, Zed, Cline, Continue, LM Studio, Goose, Warp, Kiro, the CLIs, the web connectors — and every server author is on the hook for writing and maintaining install instructions they can never keep current.

We think there's a commons artifact hiding in that mess. So we built [**MCP Install**](https://install.apicommons.org) — the "Run in Postman" button, but for MCP servers. One button, every client.

[**Try it → install.apicommons.org**](https://install.apicommons.org)

A provider configures their server once and gets a single button that installs it in every major and niche MCP client: one-click deep links where clients support them, ready-to-run CLI commands where they don't, per-OS config snippets where that's all a client offers, and web-connector walkthroughs for the ones that install over the network. The visitor lands on the chooser, it detects their OS, and it renders the exact install path for whichever client they use.

## The Commons Artifact Is the Registry, Not the Button

The button is the visible part. The part that belongs in the commons is underneath it: [**`clients.json`**](https://install.apicommons.org/clients.json), an open, machine-readable registry of *how every MCP client installs a server*.

For each client it records the mechanism — deep-link builder, CLI command template, config-file format and per-OS paths, or connector steps — along with which transports the client speaks (`stdio`, `http`, `sse`) and the shape of the snippet it expects. It's validated by a published [JSON Schema](https://install.apicommons.org/clients.schema.json). That's the load-bearing knowledge that every server author currently has to rediscover by hand, written down once, in the open, under an Apache-2.0 license.

This is API Commons' whole argument applied to a new surface. We've made the case for the [contract as a commons artifact](https://apicommons.org/) (OpenAPI), the [catalog as a commons artifact](https://apis.io) (APIs.json), and the [operational properties as a commons artifact](https://apicommons.org/properties/). Install mechanics are the same kind of object: shared knowledge about how software interoperates that is far more valuable when it's one canonical, forkable, machine-readable file than when it's copied into a thousand READMEs and left to rot.

And because it's just data, **adding a client is (almost always) a pure data PR** to [`public/clients.json`](https://github.com/api-commons/mcp-install/blob/main/public/clients.json). No code change unless a client invents a genuinely new install mechanism. Anyone can build on the registry too — badge generators, docs sites, directories, other CLIs. The button we ship is one consumer of it, not the point of it.

## Carry a Pointer, Not a Payload

There are three ways to tell the button which server to install, and the order matters for a reason that is very much a commons concern:

| Parameter | Carries | Use when |
|---|---|---|
| `?name=io.github.acme/acme-mcp` | An official [MCP Registry](https://modelcontextprotocol.io/registry/about) name | You publish `server.json` to the registry — best, because installs stay current |
| `?server=https://…/server.json` | The URL of a self-hosted manifest | You host the manifest yourself |
| `?config=<base64url>` | An inline definition | Quick start, before a manifest exists anywhere |

Whenever possible the button carries a **pointer** — a registry name or a `server.json` URL — not an inline config. The chooser resolves that pointer and shows the user exactly what they're about to install, from a canonical source, at install time. That's the same instinct behind APIs.json and the MCP Registry: the definition lives in one authoritative place, and everything else references it rather than forking a stale copy into a URL.

## Embed It, or Just Link It

Beyond the hosted chooser, the tool is an embeddable web component — self-contained, no framework:

```html
<script src="https://install.apicommons.org/button.js" async></script>
<mcp-install-button name="io.github.acme/acme-mcp"></mcp-install-button>
```

You can limit the client menu, relabel it, switch it to a light theme, or point `registry` at your own fork of `clients.json`. The generator on the home page will also hand you the button as a plain link, Markdown, HTML, the web component, or a row of per-client deep-link badges — whichever fits where you're publishing.

A note on security, because install buttons are a natural place to get this wrong: **never put real secrets in a button.** Use `<PLACEHOLDER>` values for env vars and headers and let the client prompt the user or run OAuth. Nothing executes from the page — every output is either a link the user's own client confirms, or text the user copies deliberately.

## Where This Goes

The registry starts with the clients that matter most today, and it grows the way a commons artifact should: by contribution. If your client installs MCP servers in a way that isn't captured yet, [open a PR](https://github.com/api-commons/mcp-install). If you publish an MCP server, drop a button on your docs and stop maintaining a dozen sets of install instructions by hand.

MCP Install is free, open tooling from [API Commons](https://apicommons.org). The expert services behind it come from [API Evangelist](https://apievangelist.com/services/).

[**Open MCP Install →**](https://install.apicommons.org) | [The client registry →](https://install.apicommons.org/clients.json) | [On GitHub →](https://github.com/api-commons/mcp-install)
