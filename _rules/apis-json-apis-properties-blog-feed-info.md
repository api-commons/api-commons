---
apis-json-apis-properties-blog-feed-info:
  description: API Properties Blog Feed
  message: >-
    Offering a blog feed that is dedicated to your API helps increase engagement with
    consumers and help ensure they are more aware of what is happening.
  severity: info
  given:
    - $.apis.*.properties.*
    - $.common.*
  then:
    - field: type
      function: pattern
      functionOptions:
        notMatch: \b(blog-feed|BlogFeed)\b
---