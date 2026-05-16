---
name: Contact
description: API providers should be afraid to make contact information to consumers, making it easy to access a contact form, email address, or other way to contact. Contact information is often replace with forums and other self-service way to engage with a community, but nothing replaces a form or email.
image: /images/contact.png
url: '#'
machineReadable: false
source: concept
tags:
  - Contact
  - Communication
aliases:
  - Contact Info
  - Reach Us
  - Get in Touch
yaml_example: |
  - type: Contact
    url: https://developers.example.com/contact

standards:
  - name: schema.org ContactPoint
    url: https://schema.org/ContactPoint
    kind: schema.org
  - name: vCard Format Specification (RFC 6350)
    url: https://www.rfc-editor.org/rfc/rfc6350
    kind: IETF
  - name: RFC 6068 — mailto URI scheme
    url: https://www.rfc-editor.org/rfc/rfc6068
    kind: IETF
  - name: RFC 3966 — tel URI for telephone numbers
    url: https://www.rfc-editor.org/rfc/rfc3966
    kind: IETF
  - name: RFC 9116 — A File Format to Aid in Security Vulnerability Disclosure (security.txt)
    url: https://www.rfc-editor.org/rfc/rfc9116
    kind: IETF
  - name: IANA Link Relation — author
    url: https://www.iana.org/assignments/link-relations/link-relations.xhtml
    kind: IANA

well_known:
  - path: /.well-known/security.txt
    spec: RFC 9116
    description: Security contact and disclosure policy for the domain.

media_types:
  - type: text/vcard
    spec: RFC 6350
  - type: application/vcard+json
    spec: RFC 7095
    note: jCard JSON serialization of vCard.

openapi_expression:
  - field: info.contact.name
    spec: OpenAPI 3.x
  - field: info.contact.url
    spec: OpenAPI 3.x
  - field: info.contact.email
    spec: OpenAPI 3.x

link_relations:
  - rel: author
    spec: IANA / HTML
    description: Refers to the context's author — often used for an organizational contact page.

governance_rules:
  - id: oas-info-contact
    source: Spectral built-in
    description: info.contact MUST be present.
  - id: oas-info-contact-properties
    source: Spectral built-in
    description: info.contact should include name, url, and email.
  - id: oas-contact-properties
    source: Spectral (built-in alias)
    description: Encourages a complete contact block instead of a single field.

risk:
  compliance:
    - GDPR Art. 13/14 — identity and contact details of the controller must be provided
    - CAN-SPAM / GDPR — published email addresses become regulated channels
  security_implications: Public mailboxes invite phishing and spam; pair with security.txt (RFC 9116) so vulnerability reports have a dedicated, monitored channel separate from general support.

tools:
  - name: securitytxt.org
    url: https://securitytxt.org/
    category: security.txt generator
  - name: vCard validators
    url: https://en.wikipedia.org/wiki/VCard
    category: Format reference

metrics:
  - name: contact_form_submissions
    description: Volume of contact-form leads per period.
  - name: response_time_p50_hours
    description: Median time to respond to inbound contact.
  - name: bounce_rate
    description: Share of emails to listed mailbox that bounce — early signal of stale info.

examples:
  - provider: Stripe
    url: https://providers.apis.io/providers/stripe/
    note: info.contact in OpenAPI plus a dedicated sales/support contact page.
  - provider: GitHub
    url: https://providers.apis.io/providers/github/
    note: Publishes /.well-known/security.txt with a dedicated security contact.
  - provider: Google
    url: https://providers.apis.io/providers/google/
    note: Contact pathways differ per product area; security@google.com for vuln reports.

related_properties:
  - support
  - forums
  - security
  - terms-of-service
---
