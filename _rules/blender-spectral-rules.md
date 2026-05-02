---
categories:
- blender
description: Spectral linting rules defining API design standards and conventions for Blender.
layout: rules
name: Blender API Rules
provider_name: Blender
provider_slug: blender
rule_count: 5
rules:
- description: Addon ID must be lowercase with underscores only
  given: $.components.schemas.AddonManifest.properties.id
  name: blender-addon-id-format
  severity: warn
- description: Blender addon version must follow semantic versioning
  given: $.components.schemas.AddonManifest.properties.version
  name: blender-version-semver
  severity: warn
- description: Operator bl_idname must use category.name format
  given: $.components.schemas.BpyOperator.properties.bl_idname
  name: blender-operator-idname-format
  severity: warn
- description: Addon manifest should include category tags
  given: $.components.schemas.AddonManifest.properties.tags
  name: blender-tags-present
  severity: warn
- description: License identifiers should use SPDX format
  given: $.components.schemas.AddonManifest.properties.license
  name: blender-license-spdx
  severity: warn
rules_file: rules/blender-spectral-rules.yml
rules_url: https://raw.githubusercontent.com/api-evangelist/blender/refs/heads/main/rules/blender-spectral-rules.yml
severity_counts:
  error: 0
  hint: 0
  info: 0
  warn: 5
slug: blender-spectral-rules
source_filename: blender-spectral-rules.yml
source_heading: Spectral Ruleset
source_yaml: "rules:\n  blender-addon-id-format:\n    description: Addon ID must be lowercase with underscores only\n    message: \"Addon ID must match pattern ^[a-z][a-z0-9_]*$\"\n    given: \"$.components.schemas.AddonManifest.properties.id\"\n    then:\n      field: pattern\n      function: truthy\n\n  blender-version-semver:\n    description: Blender addon version must follow semantic versioning\n    message: \"Version field should describe semver format\"\n    given: \"$.components.schemas.AddonManifest.properties.version\"\n    then:\n      field: description\n      function: truthy\n\n  blender-operator-idname-format:\n    description: Operator bl_idname must use category.name format\n    message: \"bl_idname must match pattern ^[a-z_]+\\\\.[a-z_]+$\"\n    given: \"$.components.schemas.BpyOperator.properties.bl_idname\"\n    then:\n      field: pattern\n      function: truthy\n\n  blender-tags-present:\n    description: Addon manifest should include category tags\n    message: \"\
  Addon should specify at least one tag for discovery\"\n    given: \"$.components.schemas.AddonManifest.properties.tags\"\n    then:\n      field: type\n      function: pattern\n      functionOptions:\n        match: \"^array$\"\n\n  blender-license-spdx:\n    description: License identifiers should use SPDX format\n    message: \"License should use SPDX identifier format\"\n    given: \"$.components.schemas.AddonManifest.properties.license\"\n    then:\n      field: description\n      function: truthy\n"
source_yaml_url: https://raw.githubusercontent.com/api-evangelist/blender/refs/heads/main/rules/blender-spectral-rules.yml
tags:
- 3D
- Animation
- Game Development
- Modeling
- Open Source
- Python
- Rendering
- VFX
- Spectral
- Linting
- API Governance
---
