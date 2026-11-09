---
name: License
description: The license for the API's code, SDKs, or supporting artifacts.
image: /images/interface-license.png
url: '#'
machineReadable: true
source: legal
tags:
  - License
  - Legal
  - Open Source
yaml_example: |
  - name: Data License
    type: DataLicense
    description: The data license of the Example Weather API, harvested from its own page.
    url: data-license/example-weather-api-data-license.yml
    source_date: '2026-11-09'
    data:
      data_license: 0.1.0
      provider: Example Weather API
      aid: example-weather-api
      url: https://weather.example.com/legal/data-license
      source_date: '2026-11-09'
      x-apis-io-derivation:
        synthetic: false
        method: harvested
        read: '2026-11-09'
        tool: engine/business/harvest-business.py
        model: claude-haiku-4-5
      outputs:
        license: custom
        stance_commercial: allowed
        text: Forecast responses may be used in commercial applications subject to these Terms.
      data:
        license: CC-BY-4.0
        stance_commercial: allowed
        text: Historical observation data is licensed under Creative Commons Attribution 4.0 (CC
          BY 4.0).
      attribution:
        required: true
        text: Applications must display "Weather data by Example Weather API" wherever the data
          is shown.
      interface_license:
        url: null

standards:
  - name: API Commons Data License schema
    url: https://github.com/api-commons/data-license
    kind: API Commons (CC BY-NC-SA 4.0 artifacts, Apache-2.0 code)
  - name: SPDX License List
    url: https://spdx.org/licenses/
    kind: Linux Foundation

tools:
  - name: API Commons Data License schema + validator
    url: https://github.com/api-commons/data-license
    license: Apache-2.0
    category: Machine-readable schema
---
