---
name: Blockchain
description: >-
  Nobody ratified the Ethereum JSON-RPC interface as a standard for every other chain. It
  became one because every EVM chain and every node provider implemented it, and a client
  written for one now points at hundreds by changing a URL. This profile measures what that
  actually gets you — by calling the methods.
cohort: reimplementation — independent nodes and gateways serving one method set
status: Published — 78 methods graded from 42 live endpoint probes, 40 adopters recorded
repository: https://github.com/api-commons/blockchain
image: /images/api-commons-icon.png

profiles:

  - name: The Ethereum JSON-RPC Interface
    standard_id: eth-jsonrpc
    originator: Ethereum
    description: >-
      The eth_* method set as public endpoints actually serve it. 22 methods are core here
      against 2 for the OpenAI interface — the EVM ecosystem is far more uniformly
      implemented than the model layer.
    source:
      name: ethereum/execution-apis
      url: https://github.com/ethereum/execution-apis
      license: CC0-1.0
      pinned: 5aebdfdd45cadeb723be4bd45b4611b71c8b1c85
      note: >-
        OpenRPC 1.2.4, release v1.0.0-beta.7 — 78 methods across eth, engine, debug, txpool
        and net. Public domain, the cleanest source of any standard in this programme.
    measurement: >-
      Not read — called. A JSON-RPC provider exposes one endpoint and a method name in the
      body, so there are no paths to count; of 86 providers claiming EVM compatibility, some
      publish a path per method, some a single slash, most nothing at all. The endpoints are
      public and unauthenticated by design, so 42 were probed read-only and 21 produced
      usable results. Only JSON-RPC error -32601 proves a method absent: any other error
      code means the method exists and rejected the call.
    tiers:
      - name: Core
        count: 22
        description: >-
          Served by a majority of probed endpoints. eth_blockNumber, eth_chainId,
          eth_estimateGas, eth_gasPrice, eth_getBlockByNumber and net_version all sit at
          95.2%. The median endpoint serves 20 of the 22 and eight serve every one — the
          core is what a majority serve method by method, which is not the same as any one
          endpoint serving all of it.
      - name: Extended
        count: 6
        description: >-
          eth_coinbase (47.6%), eth_config and txpool_status (28.6%), the debug namespace,
          and eth_capabilities at 9.5%.
      - name: Vendor
        count: 50
        description: >-
          Under 5%, or not probed. This includes all 25 engine_* methods — the
          consensus-layer API, spoken between a node's execution and consensus clients over
          an authenticated port. No public endpoint served any of them, and that is the
          correct result rather than a gap.
    adopters:
      count: 40
      as_of: '2026-09-13'
      url: https://github.com/api-commons/blockchain/blob/main/adopters/eth-jsonrpc.yml
      matrix_url: https://github.com/api-commons/blockchain/blob/main/adopters/eth-jsonrpc-matrix.md
      evidence:
        - grade: tested
          count: 21
          description: >-
            The methods were called against a live public endpoint. This is the only profile
            in the programme where `tested` is the ordinary grade rather than the
            aspirational one, because the endpoints cost nothing to reach.
        - grade: prose
          count: 19
          description: >-
            Could not be probed — unreachable, refused at the edge, or failed the negative
            control. No tier is recorded for any of them: an endpoint we could not read is
            not an endpoint that failed.
        - grade: declared
          count: 0
          description: >-
            Nobody in this cohort publishes an OpenRPC document we could lint. The ruleset
            exists for when they do.
    apis:
      - name: OpenRPC
        description: The artifact of record — the profile in the protocol's own format, x-tier on every method.
        properties:
          - type: OpenRPC
            url: https://raw.githubusercontent.com/api-commons/blockchain/main/standard/eth-jsonrpc/openrpc.json
      - name: OpenAPI
        description: >-
          A labelled convenience: one path, method as a const in the body. A path per method
          would read more naturally and would describe an API nobody serves.
        properties:
          - type: OpenAPI
            url: https://raw.githubusercontent.com/api-commons/blockchain/main/standard/eth-jsonrpc/openapi.yml
      - name: Profile
        description: All 78 methods with their tier and the probe evidence behind it.
        properties:
          - type: Profile
            url: https://raw.githubusercontent.com/api-commons/blockchain/main/standard/eth-jsonrpc/profile.yml
      - name: Spectral Ruleset
        description: Generated from the profile — 22 core-method rules plus three hygiene rules.
        properties:
          - type: SpectralRules
            url: https://raw.githubusercontent.com/api-commons/blockchain/main/standard/eth-jsonrpc/spectral/eth-jsonrpc-profile.yaml
      - name: Arazzo
        description: eth_chainId, then eth_blockNumber, then the block at that height.
        properties:
          - type: Arazzo
            url: https://raw.githubusercontent.com/api-commons/blockchain/main/standard/eth-jsonrpc/arazzo/core-conformance.yml
      - name: MCP Tools
        description: MCP tool definitions for all 22 core methods.
        properties:
          - type: MCP
            url: https://raw.githubusercontent.com/api-commons/blockchain/main/standard/eth-jsonrpc/mcp/tools.json

licensing: >-
  The profile is independently authored from a public-domain source. ethereum/execution-apis
  is CC0-1.0, which carries no obligations beyond honesty about provenance. API Commons
  artifacts are CC BY-NC-SA 4.0 and code is Apache-2.0. Ethereum JSON-RPC is a community
  specification; nothing here implies endorsement by the Ethereum Foundation or by any
  provider named in the registry.

tags:
  - Blockchain
  - Ethereum
  - Web3
  - Cryptocurrency

further_reading:
  - name: The adopters building block
    url: https://github.com/api-commons/adopters
    description: >-
      The schema behind the registry. Probing these endpoints added `inconclusive` to it —
      an endpoint that fails its negative control misleads in both directions.
  - name: The adopter matrix
    url: https://github.com/api-commons/blockchain/blob/main/adopters/eth-jsonrpc-matrix.md
    description: Method by endpoint, with the core-coverage spread.
---
