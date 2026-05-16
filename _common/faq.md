---
name: FAQ
description: A curated set of questions consumers actually ask, with concise authoritative answers. A good FAQ short-circuits the common-question slice of support load, makes the API feel approachable, and surfaces issues the rest of the documentation does not address head-on. FAQs work best when they are sourced from real support conversations and revised on a cadence rather than written once and abandoned.
image: /images/faq.png
url: '#'
machineReadable: false
source: commons
tags:
  - Onboarding
  - Support
  - Documentation
aliases:
  - Frequently Asked Questions
  - Q&A
  - Help
yaml_example: |
  - type: FAQ
    url: https://developers.example.com/faq

standards:
  - name: schema.org FAQPage
    url: https://schema.org/FAQPage
    kind: Schema.org
  - name: schema.org Question
    url: https://schema.org/Question
    kind: Schema.org
  - name: schema.org Answer
    url: https://schema.org/Answer
    kind: Schema.org
  - name: CommonMark 0.31
    url: https://spec.commonmark.org/0.31.2/
    kind: CommonMark

link_relations:
  - rel: help
    spec: IANA Link Relations
    description: Refers to context-sensitive help — FAQs are a common target.

risk:
  security_implications: FAQ entries about authentication and key handling routinely become quoted in support tickets — incorrect or out-of-date guidance there propagates widely. Review the auth/security FAQ entries every spec revision and on every credential-handling change.

tools:
  - name: Algolia DocSearch
    url: https://docsearch.algolia.com/
    category: Search across FAQ and docs
  - name: Discourse
    url: https://www.discourse.org/
    license: GPL-2.0
    category: Community FAQ surfacing
  - name: Mintlify
    url: https://mintlify.com/
    category: Docs platform with FAQ components

metrics:
  - name: faq_search_hit_rate
    description: Share of in-docs search queries that match an FAQ entry — measures coverage.
  - name: ticket_deflection_rate
    description: Drop in support tickets after publishing or updating an FAQ entry.
  - name: faq_freshness_days
    description: Days since each FAQ entry was last reviewed against current product behavior.

examples:
  - provider: Stripe
    url: https://support.stripe.com/
    note: Searchable help center with FAQ-style entries linked from product surfaces.
  - provider: Plaid
    url: https://plaid.com/docs/faq/
    note: Dedicated developer FAQ alongside reference docs.
  - provider: SendGrid
    url: https://docs.sendgrid.com/
    note: FAQ entries surfaced inline with deliverability and onboarding topics.

related_properties:
  - documentation
  - support
  - getting-started
  - forums
---
