---
apis-json-apis-properties-video-info:
  description: API Properties Video
  message: >-
    Offering a video channel that is dedicated to your API helps increase
    engagement with consumers and help ensure they are more aware of what is
    happening.
  severity: info
  given:
    - $.apis.*.properties.*
    - $.common.*
  then:
    - field: type
      function: pattern
      functionOptions:
        notMatch: \b(videos|Videos)\b
---