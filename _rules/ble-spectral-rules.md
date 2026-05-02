---
categories:
- ble
description: Spectral linting rules defining API design standards and conventions for BLE.
layout: rules
name: BLE API Rules
provider_name: BLE
provider_slug: ble
rule_count: 5
rules:
- description: GATT service and characteristic UUIDs should follow Bluetooth SIG format
  given: $.components.schemas[*].properties.uuid
  name: ble-uuid-format
  severity: warn
- description: RSSI values must be within valid BLE range (-127 to 0 dBm)
  given: $.components.schemas.AdvertisingPacket.properties.rssi
  name: ble-rssi-range
  severity: warn
- description: GATT characteristic properties must use defined values
  given: $.components.schemas[*].$defs.GattCharacteristic.properties.properties.items
  name: ble-characteristic-properties-enum
  severity: warn
- description: BLE device MAC address must follow XX:XX:XX:XX:XX:XX format
  given: $.components.schemas.AdvertisingPacket.properties.address
  name: ble-address-format
  severity: warn
- description: GATT service definitions must include a UUID
  given: $.components.schemas.GattService
  name: ble-service-uuid-required
  severity: warn
rules_file: rules/ble-spectral-rules.yml
rules_url: https://raw.githubusercontent.com/api-evangelist/ble/refs/heads/main/rules/ble-spectral-rules.yml
severity_counts:
  error: 0
  hint: 0
  info: 0
  warn: 5
slug: ble-spectral-rules
source_filename: ble-spectral-rules.yml
source_heading: Spectral Ruleset
source_yaml: "rules:\n  ble-uuid-format:\n    description: GATT service and characteristic UUIDs should follow Bluetooth SIG format\n    message: \"UUID must be a 16-bit hex value or full 128-bit UUID string\"\n    given: \"$.components.schemas[*].properties.uuid\"\n    then:\n      field: pattern\n      function: truthy\n\n  ble-rssi-range:\n    description: RSSI values must be within valid BLE range (-127 to 0 dBm)\n    message: \"RSSI field must define minimum and maximum constraints\"\n    given: \"$.components.schemas.AdvertisingPacket.properties.rssi\"\n    then:\n      field: minimum\n      function: defined\n\n  ble-characteristic-properties-enum:\n    description: GATT characteristic properties must use defined values\n    message: \"Characteristic properties must use enum values from the GATT specification\"\n    given: \"$.components.schemas[*].$defs.GattCharacteristic.properties.properties.items\"\n    then:\n      field: enum\n      function: truthy\n\n  ble-address-format:\n\
  \    description: BLE device MAC address must follow XX:XX:XX:XX:XX:XX format\n    message: \"BLE address must match MAC address pattern\"\n    given: \"$.components.schemas.AdvertisingPacket.properties.address\"\n    then:\n      field: pattern\n      function: truthy\n\n  ble-service-uuid-required:\n    description: GATT service definitions must include a UUID\n    message: \"GATT service must include a uuid field\"\n    given: \"$.components.schemas.GattService\"\n    then:\n      field: required\n      function: schema\n      functionOptions:\n        schema:\n          type: array\n          contains:\n            const: uuid\n"
source_yaml_url: https://raw.githubusercontent.com/api-evangelist/ble/refs/heads/main/rules/ble-spectral-rules.yml
tags:
- BLE
- Bluetooth
- Embedded
- IoT
- Protocols
- Standards
- Wireless
- Spectral
- Linting
- API Governance
---
