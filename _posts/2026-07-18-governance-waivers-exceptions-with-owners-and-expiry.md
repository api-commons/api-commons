---
layout: post
title: "Governance Waivers: Exceptions With Owners and Expiry"
date: 2026-07-18
tags:
  - API Commons
  - Spectral
  - API Governance
  - Waivers
image: /assets/images/blog/governance-waivers-exceptions-with-owners-and-expiry.png
---

Every real API governance program eventually hits a rule it cannot satisfy yet — a legacy endpoint, a deadline, a deliberate deviation. Without a sanctioned way to record that, teams route *around* governance: they disable the rule globally, delete the CI step, or ignore the report. The rule is gone, and so is the record of why. So we built [**Governance Waivers**](https://waivers.apicommons.org) — a browser-first tool that makes exceptions sanctioned, owned, and expiring instead of ad-hoc.

[**Try it → waivers.apicommons.org**](https://waivers.apicommons.org)

## The Waiver

A waiver is a small, machine-readable record: a rule, an optional scope, and a reason, owner, ticket, and expiry. Scope is optional and precise — a waiver can cover a rule everywhere, only in certain files, or only under a specific path — so waiving `operation-tags` on `/v1/legacy` does **not** hide a new `operation-tags` violation on `/invoices`.

```yaml
version: "0.1"
waivers:
  - id: WVR-001
    rule: operation-tags
    scope:
      files: ["apis/legacy/**"]
      path: "$.paths['/v1/legacy'].*"
    reason: Legacy endpoint predates our tagging standard; tracked in JIRA-482.
    owner: team-billing
    ticket: https://example.atlassian.net/browse/JIRA-482
    granted: "2026-05-01"
    expires: "2026-12-01"
```

## Reconcile, Don't Suppress

Paste your `spectral lint -f json` output and a waivers file, and the tool reconciles them. Violations are classified, waivers are classified, and the headline is the **effective result** — the honest set of failures after sanctioned waivers, which is what your build should actually gate on. Download it as filtered Spectral JSON.

| Violations | Waivers |
|---|---|
| **waived** — active waiver covers it | **active** / **expiring** (within 30 days) |
| **live** — no waiver, fails the gate | **expired** — lapsed, so it resurfaces |
| **expired** — waiver lapsed, resurfaces | **permanent** (a smell) / **stale** (matches nothing — delete it) |

The two states we care most about are **permanent** and **stale**: a waiver with no expiry is a smell, and one that no longer matches anything means the issue was fixed and the record should be deleted. The tool surfaces both instead of letting them accumulate silently. You can author waivers in a small in-tool form or bring an existing file, and everything runs client-side — the lint results and waivers you paste never leave the page.

Governance Waivers is one of the [API Commons tools](https://apicommons.org/tools/), open and portable and Spectral underneath, and part of a series introducing the tools one at a time. The goal is not zero exceptions — it is exceptions that are sanctioned, owned, and expiring, so teams stop routing around governance and start being honest about it.
