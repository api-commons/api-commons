#!/usr/bin/env python3
"""Generate the API Commons /rules/ and /rulesets/ content from the API Commons
rule catalog — the single source of truth in the sibling common-openlint-validator checkout
(rules/all-rules.yaml). Re-runnable; commit the output.

Writes:
  _data/rules_catalog.json                the rule index for /rules/
  _rulesets/experience-<exp>.md                    one ruleset per experience tag
  assets/rulesets/experience-<exp>.yaml  a runnable ruleset (rules inlined)
  assets/rulesets/functions/*.js                   custom functions those rulesets use
"""
import json
import re
import shutil
from pathlib import Path
import yaml

ROOT = Path(__file__).resolve().parent.parent          # api-commons/
SRC = ROOT.parent / "common-openlint-validator" / "rules" / "all-rules.yaml"
FN_SRC = ROOT.parent / "common-openlint-validator" / "src" / "functions"

# The rule catalog lives in a SIBLING checkout, not in this repo. Check for it
# up front and say so plainly — the catalog's original remote was
# lost once, and a run against a missing or stale checkout silently regenerates
# _data/rules_catalog.json from whatever happens to be on disk. That is how
# corrected content (e.g. the RFC 7807 -> RFC 9457 pass) gets quietly reverted.
if not SRC.exists():
    raise SystemExit(
        f"Rule catalog not found: {SRC}\n\n"
        "This script reads the API Commons rule catalog from a sibling checkout.\n"
        "Clone it next to this repo, then re-run:\n\n"
        "    git clone https://github.com/api-commons/common-openlint-validator.git "
        f"{ROOT.parent / 'common-openlint-validator'}\n\n"
        "Do not hand-edit _data/rules_catalog.json as a\n"
        "workaround — it is generated, and the next run overwrites it."
    )
SITE = "https://apicommons.org"
# The ruleset format these files follow is the OpenLint Ruleset Specification.
DOC = "https://spec.openlint.org/"

# all-rules.yaml groups by format key; the site uses an artifact id.
FMT_TO_ARTIFACT = {"jsonschema": "json-schema"}
ARTIFACT_ORDER = ["openapi", "apis-json", "asyncapi", "arazzo", "json-schema",
                  "json-structure", "json-ld", "mcp", "plans", "rate-limits",
                  "finops", "agent-skill"]
ARTIFACT_LABEL = {
    "openapi": "OpenAPI", "apis-json": "APIs.json", "asyncapi": "AsyncAPI",
    "arazzo": "Arazzo", "json-schema": "JSON Schema", "json-structure": "JSON Structure",
    "json-ld": "JSON-LD", "mcp": "MCP", "plans": "Plans", "rate-limits": "Rate Limits",
    "finops": "FinOps", "agent-skill": "Agent Skill",
}
ARTIFACT_DESC = {
    "openapi": "REST API descriptions — paths, operations, schemas, and security.",
    "apis-json": "API discovery metadata — providers, APIs, and their artifacts.",
    "asyncapi": "Event-driven API descriptions — channels, messages, and operations.",
    "arazzo": "API workflow descriptions — multi-step calls across operations.",
    "json-schema": "JSON Schema documents — types, constraints, and validation.",
    "json-structure": "JSON Structure documents — data shapes and modeling.",
    "json-ld": "Linked-data JSON — context, identifiers, and vocabularies.",
    "mcp": "Model Context Protocol servers — tools, resources, and prompts.",
    "plans": "API product plans — tiers, limits, and pricing.",
    "rate-limits": "Rate-limit descriptions — quotas, windows, and policies.",
    "finops": "FinOps artifacts — cost, usage, and billing governance.",
    "agent-skill": "Agent skills — SKILL.md metadata and tooling.",
}
# Experience tags, in display order (most rules first), with consumer-framed copy.
EXPERIENCES = [
    ("consistency", "Consistency", "Uniform shapes, conventions, and structure so every endpoint behaves predictably."),
    ("documentation", "Documentation", "Descriptions, summaries, examples, and references that make the API self-explanatory."),
    ("reliability", "Reliability", "Defensive contracts — status codes, error shapes, and required fields that hold up in production."),
    ("data-modeling", "Data Modeling", "Well-formed schemas, types, and constraints for clean, validatable data."),
    ("discoverability", "Discoverability", "Metadata, indexing, and links that help humans and machines find the API."),
    ("governance", "Governance", "Policy, ownership, and lifecycle signals that keep an API portfolio accountable."),
    ("usability", "Usability", "Developer-experience details that make the API easy to learn and consume."),
    ("naming", "Naming", "Casing, vocabulary, and naming conventions applied consistently across the surface."),
    ("security", "Security", "Authentication, authorization, and the OWASP API Security Top 10 as machine checks."),
    ("agentic-access", "Agentic Access", "Execution contracts for AI agents — scope, audience, consequence, short-lived tokens, and human-in-the-loop escalation checked in the API description."),
    ("error-handling", "Error Handling", "Standardized, informative error responses across every operation."),
    ("performance", "Performance", "Caching, payload, and efficiency signals that keep the API fast."),
    ("versioning", "Versioning", "Explicit, predictable versioning so changes don't break consumers."),
    ("pagination", "Pagination", "Consistent paging of collection responses."),
    ("observability", "Observability", "Tracing, correlation, and logging hooks for operating the API."),
]


def tagvals(tags, ns):
    return [t[len(ns) + 1:] for t in (tags or []) if t.startswith(ns + ":")]


def flatten_funcs(node, local):
    """Rewrite namespaced function refs (trimble:x -> trimble-x) and record them."""
    if isinstance(node, list):
        return [flatten_funcs(n, local) for n in node]
    if isinstance(node, dict):
        out = {}
        for k, v in node.items():
            if k == "function" and isinstance(v, str) and ":" in v:
                local.add(v)
                out[k] = v.replace(":", "-")
            else:
                out[k] = flatten_funcs(v, local)
        return out
    return node


# The ruleset format only allows these properties on a rule; the catalog's
# own metadata (title, reference, prompt, tags) makes a linter reject the file.
RULE_KEYS = {"description", "message", "severity", "given", "then", "formats",
             "recommended", "resolved", "documentationUrl", "type", "extensions"}


# Functions every Spectral-compatible linter ships. A rule calling anything else
# that is not a bundled custom function (e.g. headingCount) only runs in the
# API Commons validator, so it stays out of the downloadable ruleset.
CORE_FUNCS = {"alphabetical", "casing", "defined", "enumeration", "falsy", "length",
              "or", "pattern", "schema", "truthy", "typedEnum", "undefined",
              "unreferencedReusableObject", "xor"}


def funcs_of(node):
    if isinstance(node, list):
        return set().union(*(funcs_of(n) for n in node)) if node else set()
    if isinstance(node, dict):
        out = {node["function"]} if isinstance(node.get("function"), str) else set()
        for v in node.values():
            out |= funcs_of(v)
        return out
    return set()


def portable(x):
    return all(f in CORE_FUNCS or ":" in f for f in funcs_of(x["body"].get("then")))


def runnable_rule(x):
    rule = {k: v for k, v in x["body"].items() if k in RULE_KEYS}
    rule.setdefault("documentationUrl", x["detail_url"])
    return rule


data = yaml.safe_load(SRC.read_text())

records = []
for fmt, rules in data.items():
    art = FMT_TO_ARTIFACT.get(fmt, fmt)
    for slug, r in rules.items():
        body = {k: v for k, v in r.items() if k != "source"}
        records.append({
            "artifact": art, "local": slug, "gslug": f"{art}-{slug}",
            "name": r.get("title") or slug, "severity": r.get("severity", "info"),
            "description": r.get("description", ""),
            "experience": tagvals(r.get("tags"), "experience"),
            "spec": tagvals(r.get("tags"), "spec"),
            "topic": tagvals(r.get("tags"), "topic"),
            "owasp": tagvals(r.get("tags"), "owasp"),
            "detail_url": f"{SITE}/rules/#{art}-{slug}",
            "builtin": r.get("source") == "builtin",
            "body": body,
        })

# ---- _data/rules_catalog.json (the /rules/ index) -------------------------
artifacts_out = []
for art in ARTIFACT_ORDER:
    rs = sorted((x for x in records if x["artifact"] == art), key=lambda x: x["name"].lower())
    if not rs:
        continue
    artifacts_out.append({
        "id": art, "label": ARTIFACT_LABEL[art], "description": ARTIFACT_DESC[art],
        "count": len(rs),
        "rules": [{
            "slug": x["gslug"], "name": x["name"], "severity": x["severity"],
            "description": x["description"], "experience": x["experience"], "spec": x["spec"],
            "topic": x["topic"], "owasp": x["owasp"], "detail_url": x["detail_url"],
            "rule": {x["local"]: x["body"]},
        } for x in rs],
    })

exp_counts = {}
for x in records:
    for e in x["experience"]:
        exp_counts[e] = exp_counts.get(e, 0) + 1
experiences_out = [{"id": eid, "label": lbl, "description": desc, "count": exp_counts.get(eid, 0)}
                   for eid, lbl, desc in EXPERIENCES if exp_counts.get(eid, 0)]

# (data file written at the end, once experience_rules is assembled)

# ---- experience rulesets (collection docs + runnable assets) ----------------
# Experience rulesets are regular pages under rulesets/ (NOT a _rulesets
# collection): collection documents expose next/previous, and Jekyll's
# prev/next resolution recurses into this layout — regular pages have no such
# chain, so they render cleanly.
rsdir = ROOT / "rulesets"
rsdir.mkdir(exist_ok=True)
for f in rsdir.glob("experience-*.html"):
    f.unlink()
legacy = ROOT / "_rulesets"
if legacy.exists():
    for f in legacy.glob("*.md"):
        f.unlink()
assetdir = ROOT / "assets" / "rulesets"
if assetdir.exists():
    shutil.rmtree(assetdir)
(assetdir / "functions").mkdir(parents=True, exist_ok=True)

used_funcs = set()
experience_rules = {}
for eid, label, desc in EXPERIENCES:
    members = [x for x in records if eid in x["experience"]]
    if not members:
        continue
    runnable = [x for x in members if not x["builtin"] and portable(x)]

    local = set()
    rules_map = {x["gslug"]: flatten_funcs(runnable_rule(x), local) for x in runnable}
    used_funcs |= local
    ruleset = {"documentationUrl": DOC}
    if local:
        ruleset["functions"] = sorted(f.replace(":", "-") for f in local)
        ruleset["functionsDir"] = "./functions"
    ruleset["rules"] = rules_map
    (assetdir / f"experience-{eid}.yaml").write_text(
        yaml.safe_dump(ruleset, sort_keys=False, width=120, allow_unicode=True))

    listed = sorted(members, key=lambda x: (x["artifact"], x["name"].lower()))
    # The rule list lives in the data file (keyed by experience), not in the
    # collection doc's front matter — large front-matter arrays blow Jekyll's
    # per-document prev/next computation.
    experience_rules[eid] = [{
        "slug": x["gslug"], "name": x["name"], "artifact": x["artifact"],
        "artifact_label": ARTIFACT_LABEL[x["artifact"]], "severity": x["severity"],
        "detail_url": x["detail_url"], "builtin": x["builtin"],
    } for x in listed]
    fm = {
        "layout": "rulesets", "permalink": f"/rulesets/experience-{eid}/",
        "name": f"{label} Ruleset", "title": f"{label} Ruleset",
        "slug": f"experience-{eid}", "experience": eid, "description": desc,
        "count": len(members), "runnable_count": len(runnable),
        "ruleset_url": f"/assets/rulesets/experience-{eid}.yaml",
    }
    (rsdir / f"experience-{eid}.html").write_text(
        "---\n" + yaml.safe_dump(fm, sort_keys=False, width=120, allow_unicode=True) + "---\n")

for fn in used_funcs:
    srcf = FN_SRC.joinpath(*fn.split(":")).with_suffix(".js")
    if srcf.exists():
        # A downloaded function must not import a linter's core package: OpenLint
        # resolves only @openlint/openlint-core, Spectral only @stoplight/spectral-core.
        # These functions use createRulesetFunction with no input/options schema, which
        # only wraps the function, so a local pass-through keeps them portable.
        src = re.sub(
            r"import (?:\* as )?__sc from '@(?:openlint/openlint|stoplight/spectral)-core';\nconst \{ createRulesetFunction \} = __sc;",
            "// Portable: no linter-specific import (see scripts/generate-rules.py).\n"
            "const createRulesetFunction = (_schema, fn) => fn;",
            srcf.read_text())
        (assetdir / "functions" / f"{fn.replace(':', '-')}.js").write_text(src)
    else:
        print(f"  WARN missing function file: {fn}")

(ROOT / "_data").mkdir(exist_ok=True)
(ROOT / "_data" / "rules_catalog.json").write_text(json.dumps({
    "total": len(records), "artifact_count": len(artifacts_out),
    "experience_count": len(experiences_out),
    "artifacts": artifacts_out, "experiences": experiences_out,
    "experience_rules": experience_rules,
}, indent=1))

print(f"rules: {len(records)} across {len(artifacts_out)} artifacts")
print(f"experience rulesets: {len(experiences_out)} ({len(used_funcs)} custom functions bundled)")
