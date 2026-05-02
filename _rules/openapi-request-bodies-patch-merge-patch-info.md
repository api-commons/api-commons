---
slug: openapi-request-bodies-patch-merge-patch-info
icon: edit-3
name: OpenAPI Request Bodies PATCH Merge Patch
description: >-
  PATCH operations should use application/merge-patch+json content type as defined in RFC 7396, providing a standardized approach for partial updates to resources.
message: PATCH operations SHOULD use application/merge-patch+json content type.
given: $.paths[*].patch.requestBody.content
severity: info
view_sort: B
tags:
  - OpenAPI
  - Request Bodies
  - PATCH
  - Content Type
guidance: OpenAPI
guidanceUrl: https://guidance.apievangelist.com/openapi
rule:
  openapi-request-bodies-patch-merge-patch-info:
    description: >-
      PATCH operations should use application/merge-patch+json content type as defined in RFC 7396, providing a standardized approach for partial updates to resources.
    message: PATCH operations SHOULD use application/merge-patch+json content type.
    given: $.paths[*].patch.requestBody.content
    severity: info
    then:
      field: application/merge-patch+json
      function: truthy
---
