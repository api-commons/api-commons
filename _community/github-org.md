---
name: GitHub Organization
description: A GitHub Organization is commonplace for larger more organized API producers, establishing a place where you can find SDKs and other code used for integration, but also machine-readable artifacts, issues, discussions, and other useful outputs from everyday API operations that will help provide nutrients for an API ecosystem.
image: /images/github-org.png
url: '#'
machineReadable: false
source: platform
tags:
  - GitHub
aliases:
  - GitHub Org
  - GH Organization
  - Source Organization

standards:
  - name: GitHub REST API — Organizations
    url: https://docs.github.com/en/rest/orgs/orgs
    kind: GitHub
  - name: GitHub GraphQL API
    url: https://docs.github.com/en/graphql
    kind: GitHub
  - name: schema.org Organization
    url: https://schema.org/Organization
    kind: schema.org
  - name: OpenSSF Scorecard
    url: https://github.com/ossf/scorecard
    kind: OpenSSF
  - name: Backstage Software Catalog
    url: https://backstage.io/docs/features/software-catalog/
    kind: CNCF
  - name: SPDX License List
    url: https://spdx.org/licenses/
    kind: Linux Foundation

headers:
  - name: Authorization
    direction: request
    spec: RFC 9110
    description: Bearer token (PAT, fine-grained PAT, or GitHub App installation token).
  - name: X-RateLimit-Limit
    direction: response
    spec: GitHub REST API
    description: Per-hour request budget for the calling identity.
  - name: X-RateLimit-Remaining
    direction: response
    spec: GitHub REST API
    description: Remaining requests in the current window.
  - name: Link
    direction: response
    spec: RFC 8288
    description: Pagination links (rel="next", rel="prev", rel="last").

media_types:
  - type: application/vnd.github+json
    note: Canonical media type for the GitHub REST API.
  - type: application/json
    note: Returned by the GraphQL endpoint.

well_known:
  - path: /.well-known/security.txt
    spec: RFC 9116
    description: Security contact disclosure for the org's primary domain.

link_relations:
  - rel: next
    spec: RFC 8288 / GitHub Link header pagination
  - rel: prev
    spec: RFC 8288 / GitHub Link header pagination
  - rel: last
    spec: RFC 8288 / GitHub Link header pagination

risk:
  security_implications: Org-level access tokens, especially classic PATs with `admin:org`, can read private repos, manage members, and rotate secrets. Prefer fine-grained PATs or GitHub Apps with least-privilege installation scopes; enable SAML SSO and 2FA enforcement; review OpenSSF Scorecard signals (branch protection, code review) at the org level.

tools:
  - name: GitHub CLI (gh)
    url: https://cli.github.com/
    license: MIT
    category: Org and repo management
  - name: OpenSSF Scorecard
    url: https://github.com/ossf/scorecard
    license: Apache-2.0
    category: Org/repo health scoring
  - name: Backstage
    url: https://backstage.io/
    license: Apache-2.0
    category: Developer portal / catalog
  - name: Octokit
    url: https://github.com/octokit
    license: MIT
    category: Official GitHub SDKs
  - name: GitHub Apps
    url: https://docs.github.com/en/apps
    category: Scoped automation identities
  - name: Dependabot
    url: https://github.com/dependabot
    category: Org-wide dependency hygiene

metrics:
  - name: public_repo_count
    description: Number of public repositories under the organization.
  - name: members_visible_count
    description: Public members of the organization.
  - name: avg_scorecard_score
    description: Mean OpenSSF Scorecard across org repos.
  - name: two_factor_enforced
    description: Whether the org requires 2FA for all members.

examples:
  - provider: Stripe
    url: https://providers.apis.io/providers/stripe/
    note: github.com/stripe — SDKs, OpenAPI, and engineering blog posts.
  - provider: GitHub
    url: https://providers.apis.io/providers/github/
    note: github.com/github and github.com/octokit — first-party tooling.
  - provider: Google
    url: https://providers.apis.io/providers/google/
    note: github.com/google and github.com/googleapis — SDKs and discovery docs.
  - provider: Microsoft
    url: https://providers.apis.io/providers/microsoft/
    note: github.com/microsoft and github.com/Azure — SDKs and platform tooling.

related_properties:
  - github-repo
  - sdks
  - source-code
  - openapi
---
