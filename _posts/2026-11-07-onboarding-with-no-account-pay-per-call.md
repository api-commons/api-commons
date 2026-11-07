---
layout: post
title: "Onboarding With No Account: Pay Per Call Comes to the API Onboarding Descriptor"
date: 2026-11-07
tags:
  - API Commons
  - API Onboarding
  - Agents
  - Payments
  - HTTP 402
image: /assets/images/blog/onboarding-with-no-account-pay-per-call.png
---

The [API Onboarding Descriptor](https://github.com/api-commons/api-onboarding) describes what it takes to get from "I found your API" to "I have working credentials" — the account, the plan, the terms, the verification queue, the console clicks — in a form an agent can read and a generic engine can run. Until this week it assumed one thing about every provider: that somewhere along the way, you create an account.

That is no longer true everywhere. Some APIs now answer an unpaid request with `402 Payment Required` and a price, and the caller retries with payment attached — over [x402](https://www.x402.org) or the Machine Payments Protocol. No signup, no key, no secret to store. The payment is the credential.

## Where the Idea Came From

[Issue #2](https://github.com/api-commons/api-onboarding/issues/2) proposes a set of 0.2 additions drawn from Telnyx's agent-signup file, one of which is letting an agent fund an account by API. A comment on that issue pointed out the case it doesn't cover: the agent that never has an account to fund. The commenter runs a pay-per-call service and offered an appendix built around it. We took the idea and left the appendix — a spec's example should not be one vendor's product — but the gap was real.

We checked it against what the descriptor could already say. `open` means no registration, but it also means free, so an agent would read the cost wrong. `aauth` means no registration too, but it identifies the caller by a signing key, not by payment. Nothing fit.

## What We Added

- **A `pay-per-call` registration mechanism**, with a `payment` object: the `protocols` (`x402`, `mpp`), a `discoveryUrl` where prices are published, the settlement `network` and `asset`, whether a free `preview` exists and how to ask for it, and any `spendControls`.
- **A `payment` credential type**, so the credentials section can say "nothing is issued" without saying "none" — which reads as free.
- **One shared list of payment protocols**, so when account funding lands in 0.2 it spells them the same way.
- **The engine** now handles it: given a pay-per-call descriptor with nothing to register, it prints the payment terms and succeeds, instead of failing for lack of a flow.

Two things we deliberately did not do. `discoveryUrl` is any URL — we did not pin it to `/.well-known/x402`, because that is not a registered well-known URI. And the example in the repo is an invented provider.

While we were in there, we also fixed a quiet bug: the GitHub descriptor used a `private-key` credential type — correctly, since GitHub Apps issue a PEM key — that the schema had never listed. It now validates, and so does every other descriptor.

## Three Ways In

The README now sets the three paths side by side: sign up and get credentials, try a sandbox first, or pay per call. Each fits a different kind of use. Steady, high-volume work wants an account and negotiated terms. Occasional or exploratory agent work — one lookup today, maybe none tomorrow — is exactly where the signup costs more than the calls. A provider can offer more than one, and the descriptor lists each as its own mechanism, so an agent can pick before it makes its first request.

That is the point of the descriptor. Not to pick a winner among these models, but to make sure the agent knows which ones are on the table. The schema, engine, and example are at [github.com/api-commons/api-onboarding](https://github.com/api-commons/api-onboarding), and the rest of the 0.2 discussion is still open on [issue #2](https://github.com/api-commons/api-onboarding/issues/2).
