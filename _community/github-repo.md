---
name: GitHub Repository
description: GitHub repositories are great for making SDK and other artifacts developers will need to put an API to work, but you can also publish OpenAPI, examples, and even run your entire API portal using GitHub pages. A GitHub repository has proven itself to be an essential building block of any public API program, and powers API Commons.
image: /images/github-repo.png
url: '#'
machineReadable: false
source: platform
tags:
  - GitHub
aliases:
  - GitHub Repo
  - Source Repository
  - Git Repository

standards:
  - name: GitHub REST API — Repositories
    url: https://docs.github.com/en/rest/repos/repos
    kind: GitHub
  - name: GitHub GraphQL API
    url: https://docs.github.com/en/graphql
    kind: GitHub
  - name: schema.org SoftwareSourceCode
    url: https://schema.org/SoftwareSourceCode
    kind: schema.org
  - name: OpenSSF Scorecard
    url: https://github.com/ossf/scorecard
    kind: OpenSSF
  - name: SPDX License List
    url: https://spdx.org/licenses/
    kind: Linux Foundation
  - name: RFC 9116 — security.txt
    url: https://www.rfc-editor.org/rfc/rfc9116
    kind: IETF
  - name: Contributor Covenant Code of Conduct
    url: https://www.contributor-covenant.org/
    kind: Community standard

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
  - name: ETag
    direction: response
    spec: RFC 9110 §8.8.3
    description: Conditional-GET caching support on repository endpoints.
  - name: Link
    direction: response
    spec: RFC 8288
    description: Pagination links for list endpoints.

media_types:
  - type: application/vnd.github+json
    note: Canonical media type for the GitHub REST API.
  - type: application/vnd.github.raw
    note: Raw file contents from the Contents API.
  - type: application/vnd.github.html
    note: HTML-rendered Markdown content.

well_known:
  - path: /.well-known/security.txt
    spec: RFC 9116
    description: Security contact disclosure; commonly mirrored from a SECURITY.md.
  - path: /.well-known/funding-manifest-urls
    spec: GitHub Sponsors (de facto)
    description: Funding sources discovery; relates to FUNDING.yml in repos.

link_relations:
  - rel: next
    spec: RFC 8288 / GitHub Link header pagination
  - rel: prev
    spec: RFC 8288 / GitHub Link header pagination

governance_rules:
  - id: repo-has-readme
    source: Community convention
    description: README.md present at repo root.
  - id: repo-has-license
    source: SPDX / OpenSSF Scorecard "License" check
    description: LICENSE file detected and SPDX-identifiable.
  - id: repo-has-security-md
    source: GitHub Community Standards
    description: SECURITY.md present advertising disclosure policy.
  - id: repo-has-contributing
    source: GitHub Community Standards
    description: CONTRIBUTING.md describes contribution flow.
  - id: repo-has-code-of-conduct
    source: GitHub Community Standards
    description: CODE_OF_CONDUCT.md present.
  - id: repo-has-codeowners
    source: GitHub
    description: CODEOWNERS file routes reviews to the right maintainers.
  - id: repo-branch-protected
    source: OpenSSF Scorecard "Branch-Protection"
    description: Default branch requires reviews and status checks.

risk:
  security_implications: Public repos can leak secrets, tokens, and internal URLs in code or git history. Enforce secret scanning, push protection, branch protection on the default branch, signed commits where possible, and Dependabot/SCA alerts. OpenSSF Scorecard surfaces these signals.

tools:
  - name: GitHub CLI (gh)
    url: https://cli.github.com/
    license: MIT
    category: Repo management
  - name: OpenSSF Scorecard
    url: https://github.com/ossf/scorecard
    license: Apache-2.0
    category: Repo health scoring
  - name: gitleaks
    url: https://github.com/gitleaks/gitleaks
    license: MIT
    category: Secret scanning
  - name: trufflehog
    url: https://github.com/trufflesecurity/trufflehog
    license: AGPL-3.0
    category: Secret scanning
  - name: GitHub Actions
    url: https://docs.github.com/en/actions
    category: CI/CD
  - name: Dependabot
    url: https://github.com/dependabot
    category: Dependency updates

metrics:
  - name: stars_count
    description: Repository stargazers.
  - name: forks_count
    description: Forks of the repository.
  - name: open_issues_count
    description: Open issues including pull requests in the REST API count.
  - name: scorecard_score
    description: Aggregate OpenSSF Scorecard score (0–10).
  - name: time_to_first_review_p50
    description: Median time from PR open to first human review.

examples:
  - provider: Stripe
    url: https://providers.apis.io/providers/stripe/
    note: github.com/stripe/stripe-node and openapi specs in github.com/stripe/openapi.
  - provider: Twilio
    url: https://providers.apis.io/providers/twilio/
    note: github.com/twilio repos host SDKs and OpenAPI.
  - provider: GitHub
    url: https://providers.apis.io/providers/github/
    note: github.com/github/rest-api-description ships the official OpenAPI for the GitHub API.
  - provider: Kubernetes
    url: https://providers.apis.io/providers/kubernetes/
    note: github.com/kubernetes/kubernetes is the canonical source repo.

related_properties:
  - github-org
  - source-code
  - openapi
  - sdks
  - license
  - security
---
