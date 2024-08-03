---
apis-json-tags-upper-case-info:
  description: Tags are useful for defining the bounded context of API operations, and it helps to ensure they are consistently capitalized for better display within documentation and other resources. Emsuring that the first letter is upper cased, acronyms properly cased, and other terms, helps make sure things are readable, and act as a vocabulary for API operations. You can find details about the <a href="https://apisjson.org/schema/tags/">tags property for APIs.json</a>, and explore <a href="https://apievangelist.com/guidance/bounded-context/apis-json-tags/" target="_blank">tagging</a> more via API Evangelist.
  message: Tags Upper Case
  severity: info
  given: $.tags.*
  then:
    function: pattern
    functionOptions:
      notMatch: '[A-Z]\w*'
---