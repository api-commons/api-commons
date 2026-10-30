---
layout: post
title: "A Standards Map Built Like a Commons"
date: 2026-10-30
tags:
  - API Commons
  - Standards
  - AI Agents
  - Open Data
image: /assets/images/blog/a-standards-map-built-like-a-commons.png
---

Most "landscape" graphics of a technology space are made to be looked at once and shared. They show logos in boxes. Nobody can check them, they go out of date by the next conference, and you can't build anything on top of them. The [Agentic Standards Map](https://frmoretto.github.io/agentic-standards-map/), maintained by Francesco Marinoni Moretto, is a different kind of artifact, and it's worth looking at how it's built as much as at what it says.

It maps who is standardizing agentic commerce: how an AI agent finds a seller, trusts a product, proves who it acts for, and pays. Its 62 entries span W3C, the IETF, GS1, UN/CEFACT, the Linux Foundation, the Agentic AI Foundation and the industry protocols. What makes it a commons, rather than a picture, comes down to a handful of choices.

## What it gets right

| Choice | Why it matters |
| --- | --- |
| **Every statement is dated** | Each entry has its own `status_as_of` date and a read date on every source. You always know how old a claim is. |
| **Every statement is sourced** | Sources are tagged by class (decision, statement and so on), so a press release isn't weighed like a merged pull request. |
| **"Not found" is not "no"** | The map records what it looked for and didn't find, with the date it looked, instead of asserting that something doesn't exist. |
| **No ranking, no predictions** | It records positions with attribution and stated status. It doesn't pick winners. |
| **Open data, open license** | The whole map is [map.json](https://frmoretto.github.io/agentic-standards-map/map.json) plus a calendar feed, under CC BY 4.0, with a DOI so it can be cited. |
| **Corrections in public** | Errors are fixed through issues on [the repository](https://github.com/frmoretto/agentic-standards-map), and new versions ship on Mondays. |

The third row is the one we would point people to. Treating "we didn't find evidence" differently from "the evidence says no" is the discipline that makes shared knowledge trustworthy, and most catalogs get it wrong. They're built on an empty field meaning nothing is there.

## Reuse, with credit

Because the map is open data, we could build on it straight away. Every specification on it now has an entry in the API Evangelist [standards catalog](https://standards.apievangelist.com/agentic-standards-map/). Each entry quotes the map's dated status, links its sources and credits the map. A small script reads `map.json` directly, so the catalog follows the map rather than copying it once and drifting away. It also caught something we had wrong. Francesco got in touch to point out that `/.well-known/ucp` had just been provisionally registered with IANA, while our Well-Known URIs page still said otherwise. Checking the registry corrected it within the hour.

That's what a commons is for. One careful person does the reading, publishes it in a form others can check and reuse, and the knowledge improves as more people use it. The agent standards space is moving too fast for any one organization to track, and a dated, sourced, openly licensed map is how many people can keep up together. If you know something the map doesn't, [open an issue](https://github.com/frmoretto/agentic-standards-map/issues).
