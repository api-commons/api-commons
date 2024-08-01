---
apis-json-apis-properties-url-positive:
  description: API Properties URL
  message: API Properties URL
  severity: info
  given:
    - $.apis.*.properties.*
    - $.common.*
  then:
    - field: url
      function: pattern
      functionOptions:
        match: >-
          ^((http|https)://)[-a-zA-Z0-9@:%._\+~#?&//=]{2,256}\.[a-z]{2,6}\b([-a-zA-Z0-9@:%._\+~#?&//=]*)$
---