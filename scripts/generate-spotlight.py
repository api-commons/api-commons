#!/usr/bin/env python3
"""Generate the API Commons /rules/ and /rulesets/ content from the Spotlight
catalog — the single source of truth in the sibling spotlight-validator checkout
(rules/all-rules.yaml). Re-runnable; commit the output.

Writes:
  _data/spotlight_rules.json                       the rule index for /rules/
  _rulesets/experience-<exp>.md                    one ruleset per experience tag
  assets/rulesets/experience-<exp>.spotlight.yaml  a runnable ruleset (rules inlined)
  assets/rulesets/functions/*.js                   custom functions those rulesets use
"""
import json
import shutil
from pathlib import Path
import yaml

ROOT = Path(__file__).resolve().parent.parent          # api-commons/
SRC = ROOT.parent / "spotlight-validator" / "rules" / "all-rules.yaml"
FN_SRC = ROOT.parent / "spotlight-validator" / "src" / "functions"
SITE = "https://spotlight-rules.com"
DOC = SITE + "/spec/"

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
            "detail_url": f"{SITE}/spec/rules/{art}/{slug}/",
            "builtin": r.get("source") == "builtin",
            "body": body,
        })

# ---- _data/spotlight_rules.json (the /rules/ index) -------------------------
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
    runnable = [x for x in members if not x["builtin"]]

    local = set()
    rules_map = {x["gslug"]: flatten_funcs(x["body"], local) for x in runnable}
    used_funcs |= local
    ruleset = {"documentationUrl": DOC}
    if local:
        ruleset["functions"] = sorted(f.replace(":", "-") for f in local)
        ruleset["functionsDir"] = "./functions"
    ruleset["rules"] = rules_map
    (assetdir / f"experience-{eid}.spotlight.yaml").write_text(
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
        "ruleset_url": f"/assets/rulesets/experience-{eid}.spotlight.yaml",
    }
    (rsdir / f"experience-{eid}.html").write_text(
        "---\n" + yaml.safe_dump(fm, sort_keys=False, width=120, allow_unicode=True) + "---\n")

for fn in used_funcs:
    srcf = FN_SRC.joinpath(*fn.split(":")).with_suffix(".js")
    if srcf.exists():
        (assetdir / "functions" / f"{fn.replace(':', '-')}.js").write_text(srcf.read_text())
    else:
        print(f"  WARN missing function file: {fn}")

(ROOT / "_data").mkdir(exist_ok=True)
(ROOT / "_data" / "spotlight_rules.json").write_text(json.dumps({
    "total": len(records), "artifact_count": len(artifacts_out),
    "experience_count": len(experiences_out),
    "artifacts": artifacts_out, "experiences": experiences_out,
    "experience_rules": experience_rules,
}, indent=1))

print(f"rules: {len(records)} across {len(artifacts_out)} artifacts")
print(f"experience rulesets: {len(experiences_out)} ({len(used_funcs)} custom functions bundled)")
