---
name: Problem Details for HTTP APIs
description: >-
  A base OpenAPI for Problem Details for HTTP APIs, as defined by RFC 9457 — a way to
  carry machine-readable details of errors in an HTTP response, so nobody has to define
  a new error response format per API. RFC 9457 obsoleted RFC 7807 in July 2023, and the
  `urn:ietf:rfc:7807` XML namespace in the base is retained deliberately, per RFC 9457
  Appendix B. Originally developed by Bump.sh as part of their
  [Train Travel API template](https://bump.sh/bump-examples/doc/train-travel-api),
  reduced here to a base just for showcasing Problem Details. Conformance is checked by
  the API Commons Problem Details Spectral ruleset, listed below.
image: /images/problems.png
url: https://www.rfc-editor.org/rfc/rfc9457
tags:
  - Problems
  - Errors
  - IETF
  - RFC 9457

apis:

  - name: OpenAPI
    description: The OpenAPI base for Problem Details for HTTP APIs.
    properties:
      - type: GitHubGist
        url: https://gist.github.com/kinlane/1d72cbfd4abce1a13e5c489c950486b2.js

  - name: Repository
    description: The repository for the base.
    properties:
      - type: GitHubRepository
        url: https://github.com/api-commons/problem-details-for-http-apis

  - name: Spectral Ruleset
    description: >-
      Sixteen grounded rules checking an OpenAPI's error responses against RFC 9457 —
      the media type, the five members and their JSON types, extension members, and the
      headers that belong with 401 and 429. Adopt it by `extends` or from npm.
    properties:
      - type: GitHubRepository
        url: https://github.com/api-commons/spectral-problem-details-ruleset
      - type: Rules
        url: https://rulesets.apicommons.org/
      - type: Specification
        url: https://www.rfc-editor.org/rfc/rfc9457
---
