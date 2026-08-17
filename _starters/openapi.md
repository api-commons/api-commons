---
name: Starter OpenAPI
description: >-
  The smallest OpenAPI 3.1 document complete enough to be useful — one resource with a list, a create, and a read by id, and RFC 9457 problem details on every error. It returns zero findings under both spectral:oas and the API Commons Problem Details ruleset, which is the point: whatever you build on top starts from zero, so the first warning you ever see is one you introduced. Copy it, rename the Thing, and grow it.
image: /images/openapi.png
url: https://github.com/api-commons/starters
tags:
  - OpenAPI
  - Starter
  - REST

apis:

  - name: The starter
    description: OpenAPI 3.1 — copy this file and edit it.
    properties:
      - type: OpenAPI
        url: https://raw.githubusercontent.com/api-commons/starters/main/starter-openapi.yml

  - name: Repository
    description: Every starter, with a validator that checks them.
    properties:
      - type: GitHubRepository
        url: https://github.com/api-commons/starters

  - name: Specification
    description: The specification this starter is written against.
    properties:
      - type: Specification
        url: https://spec.openapis.org/oas/latest.html
---
