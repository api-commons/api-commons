---
apis-json-apis-properties-url-info:
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
        notMatch: >-
          ^((http|https)://)[-a-zA-Z0-9@:%._\+~#?&//=]{2,256}\.[a-z]{2,6}\b([-a-zA-Z0-9@:%._\+~#?&//=]*)$
---