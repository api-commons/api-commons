---
name: Problem Details for HTTP APIs
description: This is a base OpenAPI for the Problem Details for HTTP APIs, as a way to carry machine-readable details of errors in a HTTP response to avoid the need to define new error response formats for HTTP APIs. This was originally developed by Bump.sh as part of their [Train Travel API template](https://bump.sh/bump-examples/doc/train-travel-api), but reduced here to provide a base just for showcasing Problem Details for HTTP APIs.
image: /images/problems.png
url: https://datatracker.ietf.org/doc/html/rfc7807
tags:
  - Problems
  - Errors
  - IETF 

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
---