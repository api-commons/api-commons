---
apis-json-apis-properties-communications-video-positive:
  description: API Properties Communications Video
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