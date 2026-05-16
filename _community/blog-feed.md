---
name: Blog Feed
description: An Atom or RSS feed for a blog or is still an essential item, and despise the demise of Google Reader, it is still a fundamental aspect of any blog. While blogging is not as popular as it once was, it is still a useful way to keep API consumers up to date with what is happening with change across each API they are depending on.
image: /images/blog-feed.png
url: '#'
machineReadable: true
source: community
tags:
  - Blog
  - Feed
  - RSS
  - Atom
aliases:
  - RSS Feed
  - Atom Feed
  - Syndication Feed
  - JSON Feed

standards:
  - name: RSS 2.0 Specification
    url: https://www.rssboard.org/rss-specification
    kind: RSS Advisory Board
  - name: RFC 4287 — The Atom Syndication Format
    url: https://www.rfc-editor.org/rfc/rfc4287
    kind: IETF
  - name: RFC 5023 — The Atom Publishing Protocol
    url: https://www.rfc-editor.org/rfc/rfc5023
    kind: IETF
  - name: JSON Feed 1.1
    url: https://www.jsonfeed.org/version/1.1/
    kind: Community
  - name: WebSub
    url: https://www.w3.org/TR/websub/
    kind: W3C
  - name: schema.org BlogPosting
    url: https://schema.org/BlogPosting
    kind: schema.org

headers:
  - name: Content-Type
    direction: response
    spec: RFC 9110
    description: Identifies the feed media type.
  - name: ETag
    direction: response
    spec: RFC 9110 §8.8.3
    description: Conditional-GET support so aggregators can skip unchanged feeds.
  - name: Last-Modified
    direction: response
    spec: RFC 9110 §8.8.2
    description: Conditional-GET timestamp; widely used with If-Modified-Since.
  - name: If-None-Match
    direction: request
    spec: RFC 9110 §13.1.2
    description: Sent by polite aggregators to avoid re-downloading unchanged feeds.

media_types:
  - type: application/rss+xml
    note: De facto media type for RSS 2.0.
  - type: application/atom+xml
    spec: RFC 4287
  - type: application/feed+json
    note: JSON Feed 1.1 advertised media type.
  - type: application/xml
    note: Sometimes used as a fallback for RSS/Atom.

link_relations:
  - rel: alternate
    spec: HTML LINK element / IANA Link Relations
    description: <link rel="alternate" type="application/rss+xml" ...> autodiscovery from an HTML page.
  - rel: self
    spec: RFC 4287 §4.2.7.2 (Atom)
    description: Canonical URL of the feed document.
  - rel: hub
    spec: WebSub
    description: WebSub hub for push subscriptions.
  - rel: next
    spec: RFC 5005 — Feed Paging and Archiving
    description: Pagination across archived feed documents.
  - rel: prev-archive
    spec: RFC 5005
    description: Previous archive document in a paged feed.

governance_rules:
  - id: feed-discoverable-from-homepage
    source: Community convention
    description: HTML pages link to the feed via <link rel="alternate">.
  - id: feed-supports-conditional-get
    source: RFC 9110
    description: Server honors ETag / If-Modified-Since to reduce aggregator load.
  - id: feed-items-have-stable-guid
    source: RSS 2.0 / Atom id
    description: Each item has a unique, stable identifier so dedup works.

risk:
  security_implications: Feeds embedding raw HTML must be sanitized by consumers (XSS into reader UIs). Server-side, parsers historically suffered XXE in XML processing — disable external entity resolution. Avoid leaking unpublished drafts via cached feeds.

tools:
  - name: Feed Validator (W3C)
    url: https://validator.w3.org/feed/
    category: Validation
  - name: feedparser (Python)
    url: https://github.com/kurtmckee/feedparser
    license: BSD-2-Clause
    category: Parser
  - name: rome (Java)
    url: https://github.com/rometools/rome
    license: Apache-2.0
    category: Parser
  - name: Feedly
    url: https://feedly.com/
    category: Aggregator / reader
  - name: Inoreader
    url: https://www.inoreader.com/
    category: Aggregator / reader
  - name: NetNewsWire
    url: https://netnewswire.com/
    license: MIT
    category: Desktop / mobile reader

metrics:
  - name: feed_freshness_hours
    description: Hours since the most recent item's publish date.
  - name: item_count
    description: Number of items currently returned by the feed.
  - name: conditional_get_hit_rate
    description: Share of polls answered with 304 Not Modified.
  - name: subscriber_count
    description: Reported subscribers (from WebSub or aggregator user-agents).

examples:
  - provider: Stripe
    url: https://providers.apis.io/providers/stripe/
    note: Stripe engineering and changelog feeds.
  - provider: GitHub
    url: https://providers.apis.io/providers/github/
    note: GitHub Blog and Changelog publish RSS/Atom feeds.
  - provider: AWS
    url: https://providers.apis.io/providers/aws/
    note: AWS What's New, Security Bulletins, and service blogs offer RSS.
  - provider: Cloudflare
    url: https://providers.apis.io/providers/cloudflare/
    note: Cloudflare Blog and changelog publish RSS feeds.

related_properties:
  - blog
  - changelog
  - news
  - press
---
