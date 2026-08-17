---
name: Images API
description: >-
  Images have been done. There is no good reason every application invents its own upload endpoint, its own metadata shape, and its own way of asking for a smaller version of the same picture. This is a base Images API you copy into your own service. Upload is two steps — create the record, then PUT the bytes to a short-lived URL — which keeps large binaries off the JSON API and means a failed upload does not lose the metadata. Renditions are requested rather than enumerated, and `alt` is on the base, because an image API that makes the text alternative easy to skip produces an inaccessible product downstream. Errors are RFC 9457 problem details, identical to every other base.
image: /images/images.png
url: https://github.com/api-commons/images
tags:
  - Images
  - Photos
  - Media
  - OpenAPI

apis:

  - name: OpenAPI
    description: OpenAPI 3.1 for the base Images API — upload, metadata, renditions and deletion.
    properties:
      - type: OpenAPI
        url: https://raw.githubusercontent.com/api-commons/images/main/openapi.yml

  - name: APIs.json
    description: The APIs.json index for this base.
    properties:
      - type: APIsJSON
        url: https://raw.githubusercontent.com/api-commons/images/main/apis.yml

  - name: Repository
    description: The repository for the base.
    properties:
      - type: GitHubRepository
        url: https://github.com/api-commons/images

  - name: Spectral Ruleset
    description: >-
      The errors in this base are RFC 9457 problem details, checked by the API Commons
      Problem Details ruleset. The base lints clean under it.
    properties:
      - type: GitHubRepository
        url: https://github.com/api-commons/spectral-problem-details-ruleset
---
