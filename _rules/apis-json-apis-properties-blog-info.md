---
apis-json-apis-properties-blog-info:
  description: API Properties Blog
  message: >-
    Offering a blog that is dedicated to your API helps increase engagement with
    consumers and help ensure they are more aware of what is happening.
  severity: info
  given:
    - $.apis.*.properties.*
    - $.common.*
  then:
    - field: type
      function: pattern
      functionOptions:
        notMatch: \b(blog|Blog)\b
---