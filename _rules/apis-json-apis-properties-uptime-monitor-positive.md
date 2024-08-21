---
apis-json-apis-properties-uptime-monitor-positive:
  description: API Properties Uptime Monitor
  message: Has an uptime monitor.
  severity: info
  given:
    - $.apis.*.properties.*
    - $.common.*
  then:
    - field: type
      function: pattern
      functionOptions:
        notMatch: \b(api-uptime-monitor|uptime-monitor|UptimeMonitor)\b
---