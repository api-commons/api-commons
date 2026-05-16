---
name: Forums
description: Forums are a common way for developers to engage in a self-service way within a community. The forum may or may not be owned and managed by a platform, but almost always thrive when they are user supported, providing an opportunity for more advanced API consumers to answer questions and support the needs of newer API consumers.
image: /images/forums.png
url: '#'
machineReadable: false
source: concept
tags:
  - SDKs
aliases:
  - Community
  - Discussions
  - Message Board
yaml_example: |
  - type: Forums
    url: https://forum.example.com/

standards:
  - name: schema.org DiscussionForumPosting
    url: https://schema.org/DiscussionForumPosting
    kind: schema.org
  - name: schema.org Comment
    url: https://schema.org/Comment
    kind: schema.org
  - name: ActivityPub
    url: https://www.w3.org/TR/activitypub/
    kind: W3C
  - name: Atom Syndication Format (RFC 4287)
    url: https://www.rfc-editor.org/rfc/rfc4287
    kind: IETF
  - name: Atom Threading Extensions (RFC 4685)
    url: https://www.rfc-editor.org/rfc/rfc4685
    kind: IETF
  - name: WebSub
    url: https://www.w3.org/TR/websub/
    kind: W3C

link_relations:
  - rel: replies
    spec: RFC 4685 (Atom Threading)
  - rel: alternate
    spec: RFC 8288 (Web Linking)

governance_rules:
  - id: info-contact-url
    source: Spectral (oas-info-contact)
    description: A forum URL is a common value for info.contact.url when a provider prefers community channels over direct email.

risk:
  security_implications: Public forums can leak internal details (stack traces, tokens pasted by users, customer identifiers). Moderation policy and a posted code of conduct reduce abuse; PII redaction in support transcripts is essential.

tools:
  - name: Discourse
    url: https://www.discourse.org/
    license: GPL-2.0
    category: Self-hosted forum
  - name: GitHub Discussions
    url: https://docs.github.com/en/discussions
    category: Hosted Q&A / forum
  - name: Stack Exchange API
    url: https://api.stackexchange.com/
    category: Q&A platform API
  - name: Discord
    url: https://discord.com/developers/docs
    category: Real-time community
  - name: Slack
    url: https://api.slack.com/
    category: Real-time community
  - name: Vanilla Forums
    url: https://success.vanillaforums.com/kb/dev
    category: Hosted forum

metrics:
  - name: active_posters_30d
    description: Distinct users posting within a 30-day window.
  - name: answered_question_rate
    description: Share of questions marked answered or accepted.
  - name: first_response_p50_hours
    description: Median time from question post to first human reply.
  - name: staff_reply_ratio
    description: Fraction of threads with at least one provider-side response — signals investment in the community.

examples:
  - provider: Stripe
    url: https://providers.apis.io/providers/stripe/
    note: Discord-based developer community linked from the docs.
  - provider: GitHub
    url: https://providers.apis.io/providers/github/
    note: GitHub Community Discussions across topical categories.
  - provider: Twilio
    url: https://providers.apis.io/providers/twilio/
    note: Stack Overflow tag plus a Discord server for SIGNAL community.

related_properties:
  - support
  - contact
  - community
  - portal
---
