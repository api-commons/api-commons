---
name: Starter APIs.json
description: >-
  The smallest APIs.json document that validates — one index, one API, and the properties a consumer actually needs to find their way in. Where an OpenAPI describes one API's surface, this describes where an API lives, who runs it, and which artifacts sit alongside it: documentation, a portal, a changelog, a status page, terms. Written against specificationVersion 0.22 and validated against the published schema.
image: /images/api-index.png
url: https://github.com/api-commons/starters
tags:
  - APIs.json
  - Starter
  - Discovery

apis:

  - name: The starter
    description: APIs.json 0.22 — copy this file and edit it.
    properties:
      - type: APIsJSON
        url: https://raw.githubusercontent.com/api-commons/starters/main/starter-apis.yml

  - name: Repository
    description: Every starter, with a validator that checks them.
    properties:
      - type: GitHubRepository
        url: https://github.com/api-commons/starters

  - name: Specification
    description: The specification this starter is written against.
    properties:
      - type: Specification
        url: https://apisjson.org
---
