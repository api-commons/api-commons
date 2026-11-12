---
name: API Identifier (aid)
description: >-
  The aid property of an APIs.json / apis.yml document: a stable, lowercase identifier for a provider (stripe) and for each of its APIs (stripe:payment-intents). Catalogs use it as the primary key for indexing, the page slug, the join key between artifacts, and the handle for prefix search and filtering. The standard defines its grammar, eight MUST rules that make it a usable key, naming recommendations that make it meaningful, and aliases so a rename never breaks a link.
image: /images/api-index.png
url: '#'
machineReadable: true
source: commons
tags:
  - Discovery
  - Catalog
  - Identifiers
aliases:
  - aid
  - API ID
  - API Identifier
  - Provider Identifier
yaml_example: |
  aid: example-weather-com
  name: Example Weather API
  apis:
    - aid: example-weather-com:forecasts
      name: Forecasts API
    - aid: example-weather-com:historical-observations
      name: Historical Observations API
      x-aid-aliases:
        - example-weather-com:example-weather-com-history-api

standards:
  - name: API Commons aid specification
    url: https://github.com/api-commons/aid
    kind: API Commons (CC BY-NC-SA 4.0 artifacts, Apache-2.0 code)
  - name: APIs.json
    url: https://apisjson.org/
    kind: Community spec

tools:
  - name: API Commons aid schema + reference linter (aid.py)
    url: https://github.com/api-commons/aid
    license: Apache-2.0
    category: Machine-readable schema

related_properties:
  - api-index
  - ai-preferences
---
