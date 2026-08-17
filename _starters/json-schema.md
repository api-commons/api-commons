---
name: Starter JSON Schema
description: >-
  The smallest JSON Schema worth copying — an object, typed properties, one constraint, one required field, and a description on everything. Written against 2020-12, the dialect OpenAPI 3.1 uses, so it drops straight into components.schemas with no translation. Its own examples are validated against the properties they sit on, because a starter whose examples do not validate is worse than no starter.
image: /images/json-schema.png
url: https://github.com/api-commons/starters
tags:
  - JSON Schema
  - Starter
  - Contracts

apis:

  - name: The starter
    description: JSON Schema 2020-12 — copy this file and edit it.
    properties:
      - type: JSONSchema
        url: https://raw.githubusercontent.com/api-commons/starters/main/starter-json-schema.yml

  - name: Repository
    description: Every starter, with a validator that checks them.
    properties:
      - type: GitHubRepository
        url: https://github.com/api-commons/starters

  - name: Specification
    description: The specification this starter is written against.
    properties:
      - type: Specification
        url: https://json-schema.org/draft/2020-12/schema
---
