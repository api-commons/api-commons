---
layout: post
title: "Spectral Ruleset Studio: Turn Style Guides Into Rulesets"
date: 2026-07-12
tags:
  - API Commons
  - Spectral
  - API Governance
  - Rulesets
image: /assets/images/blog/spectral-ruleset-studio-style-guides-into-rulesets.png
---

In a census of 1,005 public GitHub pipelines running [Spectral](https://github.com/stoplightio/spectral), 63% ran the tool on its defaults with no rules of their own. The default ruleset is a config file that ships with the software — a hodgepodge of atomic checks with no naming convention, no categories, and no owner. Running it is not adopting a standard; it is leaving the settings where you found them. Teams do this because authoring and owning rules is hard, so we built a tool that makes the hard part cheap.

[**Try it → studio.apicommons.org**](https://studio.apicommons.org)

## Distilling Prose Is the Point

Paste a line from your style guide — *"operations should have meaningful descriptions"* — and the act of turning it into a rule immediately exposes how vague the prose was. Meaningful how? Longer than what? On which operations? The studio flags the vague words and makes you answer them, and answering **is** governance happening. A ruleset you did not write is a ruleset nobody had to think through, which means it is a ruleset nobody owns. The identical YAML is a governance artifact in one repository and an empty gesture in another; the difference is entirely whether human work exists behind it. Spectral Ruleset Studio forces that work, and makes it fast — three ways to add a rule (distill prose, drop in a grounded starter, or start blank), a target from a JSONPath library, one of the 9 core Spectral functions with guided arguments and **no custom JavaScript**, and live, valid `.spectral.yaml` that updates as you type. Nothing leaves your browser.

## Owned, Named, and Grounded

Every rule gets a convention-following id — the canonical API Commons **Spec / Version / Property / Semantics / Severity** pattern (`oas-3-info-title-length-warn`) — and a named owner, so there is no anonymous copied YAML. And nothing ships without grounding: a description, a rationale for *why*, and a docs or policy link, carried both in the rule `description` and mirrored as an `x-grounding` extension for tooling that wants it structured. New rules default to `warning`, not `error`, because the build-failing severity is a deliberate choice you make sparingly — credibility comes from a small blocking set. You can also write the rule that flags what is wrong, or its twin that recognizes what is right, so you can report progress (*"82% already comply"*) and not only deficits.

## Swagger 2.0 and OpenAPI 3.x, With Parity

A **Target** toggle chooses which dialect(s) to govern, and both are treated at full parity:

| Target | What it emits |
| --- | --- |
| Both (default) | one ruleset governing 2.0 and 3.x — multipath `given` when the check is identical, format-tagged twins when it differs |
| OpenAPI 3.x | only the 3.x form of each rule, with a matching top-level `formats` |
| Swagger 2.0 | only the 2.0 form; one-spec-only rules are dropped when they don't apply |

There is also a tiny companion CLI (`@api-common/spectral-ruleset-studio`) that scaffolds the same grounded starter ruleset from the terminal, so the YAML you copy from the page is byte-for-byte what CI writes.

Spectral Ruleset Studio is one of the [API Commons tools](https://apicommons.org/tools/), and like the rest it is open, portable, and Spectral underneath — because the rules that decide whether an API is any good should not be locked inside a vendor. This is part of a series introducing the tools one at a time.
