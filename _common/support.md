---
name: Support
description: Offering a standardized set of API support for consumers to tap into helps ensure that onboarding is as frictionless as possible while helping build trust with consumers. Support can be as simple as email, or as structured as a ticketing system, but whatever is offered, it should work to keep API consumers taken care of throughout their journey.
image: /images/support.png
url: '#'
machineReadable: true
source: commons
tags:
  - Support
  - Help
  - Troubleshooting
aliases:
  - Help
  - Helpdesk
  - Customer Service
yaml_example: |
  - type: Support
    url: https://support.example.com/

standards:
  - name: schema.org ContactPoint
    url: https://schema.org/ContactPoint
    kind: schema.org
  - name: schema.org contactType (customer support)
    url: https://schema.org/contactType
    kind: schema.org
  - name: RFC 9457 — Problem Details for HTTP APIs
    url: https://www.rfc-editor.org/rfc/rfc9457
    kind: IETF
  - name: RFC 7807 — Problem Details (obsoleted by 9457)
    url: https://www.rfc-editor.org/rfc/rfc7807
    kind: IETF
  - name: RFC 8288 — Web Linking
    url: https://www.rfc-editor.org/rfc/rfc8288
    kind: IETF
  - name: IANA Link Relation — help
    url: https://www.iana.org/assignments/link-relations/link-relations.xhtml
    kind: IANA

headers:
  - name: Link
    direction: response
    spec: RFC 8288
    description: Can carry rel="help" pointing to support documentation or contact endpoint.

media_types:
  - type: application/problem+json
    spec: RFC 9457
  - type: application/problem+xml
    spec: RFC 9457

openapi_expression:
  - field: info.contact.url
    spec: OpenAPI 3.x
    description: Often points to a support portal or contact form.
  - field: info.contact.email
    spec: OpenAPI 3.x
    description: Direct support mailbox for the API.
  - field: externalDocs
    spec: OpenAPI 3.x
    description: Frequently references a support / help center URL.

link_relations:
  - rel: help
    spec: IANA (HTML 4.01 origin)
    description: Refers to context-sensitive help.

governance_rules:
  - id: oas-info-contact
    source: Spectral built-in
    description: info.contact must be present so consumers can reach support.
  - id: oas-info-contact-properties
    source: Spectral built-in
    description: info.contact should include name, url, and email.

risk:
  compliance:
    - GDPR Art. 12 — transparent communication channels for data-subject requests
    - SOC 2 CC2.2 — internal and external communication of responsibilities
  security_implications: Support channels are a frequent social-engineering target. Verify identity before resetting credentials; never accept tokens or full card numbers in ticket bodies; sanitize attachments.

tools:
  - name: Zendesk
    url: https://developer.zendesk.com/api-reference/
    category: Ticketing platform
  - name: Intercom
    url: https://developers.intercom.com/
    category: Messaging / support
  - name: Freshdesk
    url: https://developers.freshdesk.com/api/
    category: Ticketing platform
  - name: HubSpot Service Hub
    url: https://developers.hubspot.com/docs/api/overview
    category: CRM / support
  - name: Jira Service Management
    url: https://developer.atlassian.com/cloud/jira/service-desk/rest/
    category: Service desk
  - name: GitHub Support
    url: https://support.github.com/
    category: Provider helpdesk

metrics:
  - name: first_response_p50_hours
    description: Median time to a human first response on a ticket.
  - name: time_to_resolution_p90_hours
    description: 90th-percentile time from ticket open to resolved.
  - name: csat_score
    description: Customer satisfaction score on closed tickets.
  - name: deflection_rate
    description: Share of help-center visitors who do not open a ticket.

examples:
  - provider: Stripe
    url: https://providers.apis.io/providers/stripe/
    note: 24/7 chat plus email support tied to dashboard identity.
  - provider: Twilio
    url: https://providers.apis.io/providers/twilio/
    note: Tiered support plans with SLAs.
  - provider: GitHub
    url: https://providers.apis.io/providers/github/
    note: support.github.com with separate enterprise channels.
  - provider: AWS
    url: https://providers.apis.io/providers/aws/
    note: AWS Support API for programmatic case management.

related_properties:
  - contact
  - forums
  - status
  - error-codes
  - sla
---
