---
name: Videos API
description: >-
  Videos have been done. Every product that handles video rebuilds the same upload flow, the same transcoding wait, and the same playback URLs, slightly differently each time. This is a base Videos API you copy into your own service — the sibling of the Images base, deliberately sharing its shape, with the one difference that actually matters: video is not ready when the bytes finish uploading. Transcoding takes real time, so status moves through processing and the base ships webhooks rather than asking clients to poll. Captions are a first-class sub-resource. Errors are RFC 9457 problem details, identical to every other base — including on the failure webhook.
image: /images/videos.png
url: https://github.com/api-commons/videos
tags:
  - Videos
  - Media
  - Captions
  - OpenAPI

apis:

  - name: OpenAPI
    description: OpenAPI 3.1 for the base Videos API — upload, transcoding, renditions, captions and webhooks.
    properties:
      - type: OpenAPI
        url: https://raw.githubusercontent.com/api-commons/videos/main/openapi.yml

  - name: APIs.json
    description: The APIs.json index for this base.
    properties:
      - type: APIsJSON
        url: https://raw.githubusercontent.com/api-commons/videos/main/apis.yml

  - name: Repository
    description: The repository for the base.
    properties:
      - type: GitHubRepository
        url: https://github.com/api-commons/videos

  - name: Spectral Ruleset
    description: >-
      The errors in this base are RFC 9457 problem details, checked by the API Commons
      Problem Details ruleset. The base lints clean under it.
    properties:
      - type: GitHubRepository
        url: https://github.com/api-commons/spectral-problem-details-ruleset
---
