---
layout: post
title: "API Certification: Verifiable Governance Trust Stamps"
date: 2026-07-20
tags:
  - API Commons
  - API Governance
  - Certification
  - Trust
image: /assets/images/blog/api-certification-verifiable-trust-stamps.png
---

Almost every governance tool faces the producer — it helps the team publishing an API check their own work. But the most important question about an API is usually asked by someone else entirely: the consumer standing in front of an API they did not build, wondering whether they should trust it. A claim on a marketing page is a poor answer. A portable, verifiable artifact is a better one. So we built [**API Certification**](https://certification.apicommons.org) — a browser-first tool that issues and verifies tamper-evident API governance certificates.

[**Try it → certification.apicommons.org**](https://certification.apicommons.org)

## What a Certificate Attests

A certificate states that a specific API description passed a named ruleset at a profile threshold, on a date. Its power is the **SHA-256 fingerprint** computed over the canonical API description plus the ruleset identity and profile. Because that fingerprint is recomputable, verification is trustless: if the API has drifted by even one character, or the certificate was forged, the recomputed fingerprint will not match and the certificate fails. This is **integrity, not identity** — it proves *what* was certified, not *who* signed it. Key management and signing are a deliberate follow-up; the honest, recomputable core comes first.

The profile is the pass threshold the certificate attests to:

| Profile | Requires |
| --- | --- |
| **Baseline** | 0 errors (warnings and info permitted) |
| **Standard** | 0 errors and 0 warnings |
| **Strict** | fully clean — 0 errors, warnings, or info |

## Two Modes: Issue and Verify

In **Issue** mode you paste your API description plus the `spectral lint -f json` result, name the ruleset, and pick a profile. If the result meets the profile, the tool mints a certificate you can download, copy, or reference as an `apis.json` property. In **Verify** mode you paste a certificate plus the API description you hold; the tool recomputes the fingerprint and reports **valid**, **tampered / mismatch**, **expired**, or **not a passing certificate**. Everything runs client-side — the descriptions, results, and certificates you paste never leave the page, because there is no server.

## Composes With the Stack

Certification is not a silo. Run the [Validator](https://validator.apicommons.org) to produce the Spectral result, certify that result here, then reference the certificate from your `apis.json` so consumers can verify it before they integrate. Governance stops being a private ritual and becomes a public signal a person or a machine can independently confirm in seconds.

API Certification is one of the [API Commons tools](https://apicommons.org/tools/), and like the rest it is open, portable, and free to fork — because the trust that decides whether an API is worth integrating should not be locked inside a vendor. This is one more in a series introducing the tools one at a time.
