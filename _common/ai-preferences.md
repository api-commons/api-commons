---
name: AI Preferences
description: >-
  What an API provider says about AI: whether its content and API output may be used to train AI or generative AI, used for AI inference or search, and whether an AI agent may sign up, act or buy on a person's behalf, plus the machine signals it publishes (an AIPREF header, Content Signals, ai.txt, llms.txt).
image: /images/openai.png
url: '#'
machineReadable: true
source: legal
tags:
  - Legal
  - AI
  - Agents
aliases:
  - AI Policy
  - AI Terms
  - AIPREF
  - Content Signals
yaml_example: |
  - name: AI Preferences
    type: AIPreferences
    description: The ai preferences of the Example Weather API, harvested from its own page.
    url: ai-preferences/example-weather-api-ai-preferences.yml
    source_date: '2026-11-09'
    data:
      ai_preferences: 0.1.0
      provider: Example Weather API
      aid: example-weather-api
      url: https://weather.example.com/legal/api-terms
      source_date: '2026-11-09'
      x-apis-io-derivation:
        synthetic: false
        method: harvested
        read: '2026-11-09'
        tool: engine/business/harvest-business.py
        model: claude-haiku-4-5
      train_ai:
        stance: prohibited
        text: You may not use API output to train machine learning or artificial intelligence models.
      train_genai:
        stance: prohibited
        text: You may not use API output to train machine learning or artificial intelligence models.
      ai_use:
        stance: allowed
        text: You may use API output as input to AI assistants that answer end-user questions.
      agent_onboarding:
        stance: unstated
      agent_actions:
        stance: conditional
        text: Automated agents may call the API only with a key issued to the account holder.
      agent_purchases:
        stance: unstated
      signals:
        aipref_header: false
        content_signals: true
        ai_txt_url: null
        llms_txt_url: https://weather.example.com/llms.txt

standards:
  - name: API Commons AI Preferences schema
    url: https://github.com/api-commons/ai-preferences
    kind: API Commons (CC BY-NC-SA 4.0 artifacts, Apache-2.0 code)
  - name: IETF AIPREF Working Group
    url: https://datatracker.ietf.org/wg/aipref/about/
    kind: IETF
  - name: Content Signals
    url: https://contentsignals.org/
    kind: Community spec
  - name: llms.txt
    url: https://llmstxt.org/
    kind: Community spec
  - name: ai.txt (Spawning)
    url: https://site.spawning.ai/spawning-ai-txt
    kind: Community spec

tools:
  - name: API Commons AI Preferences schema + validator
    url: https://github.com/api-commons/ai-preferences
    license: Apache-2.0
    category: Machine-readable schema

related_properties:
  - terms-of-service
  - license
  - llms-txt
  - agent-skills
  - model-context-protocol
---
