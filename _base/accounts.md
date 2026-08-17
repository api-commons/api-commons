---
name: Accounts
description: >-
  We need an account for everything these days. Every new service reinvents the same account resource, the same onboarding flow, and the same set of errors — each one slightly different, which is exactly what makes integration expensive. This is a base Accounts API you copy into your own service: list, create, read, update and close. Updates are RFC 7396 JSON Merge Patch and writes are conditional on an ETag, so a client changes one field without sending the whole account back and without clobbering a concurrent write. Errors are RFC 9457 problem details, identical to every other base.
image: /images/accounts.png
url: https://github.com/api-commons/accounts
tags:
  - Accounts
  - Onboarding
  - Users
  - OpenAPI

apis:

  - name: OpenAPI
    description: OpenAPI 3.1 for the base Accounts API — list, create, read, merge-patch and close.
    properties:
      - type: OpenAPI
        url: https://raw.githubusercontent.com/api-commons/accounts/main/openapi.yml

  - name: APIs.json
    description: The APIs.json index for this base.
    properties:
      - type: APIsJSON
        url: https://raw.githubusercontent.com/api-commons/accounts/main/apis.yml

  - name: Repository
    description: The repository for the base.
    properties:
      - type: GitHubRepository
        url: https://github.com/api-commons/accounts

  - name: Spectral Ruleset
    description: >-
      The errors in this base are RFC 9457 problem details, checked by the API Commons
      Problem Details ruleset. The base lints clean under it.
    properties:
      - type: GitHubRepository
        url: https://github.com/api-commons/spectral-problem-details-ruleset
---
