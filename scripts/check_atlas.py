#!/usr/bin/env python3
"""Validate the repository-local BHGMAN source-navigation atlas."""
from __future__ import annotations
import argparse, copy, hashlib, json, re, sys
from pathlib import Path, PurePosixPath

ROOT = Path(__file__).resolve().parents[1]
ATLAS = ROOT / "graph" / "research-atlas.json"
SHA256 = re.compile(r"[0-9a-f]{64}\Z")
REVISION = re.compile(r"[0-9a-f]{40}\Z")
SCOPE = "Repository-local reading map; not a shared-KG write or runtime declaration."

def fail(msg): raise ValueError(msg)
def digest(path): return hashlib.sha256(path.read_bytes()).hexdigest()
def local_file(root, value):
    if not isinstance(value, str): fail("source artifact path is not a string")
    rel = PurePosixPath(value)
    if rel.is_absolute() or ".." in rel.parts or str(rel) in {"", "."}: fail("unsafe source artifact path: " + value)
    path = root.joinpath(*rel.parts)
    for parent in (path, *path.parents):
        if parent == root.parent: break
        if parent.is_symlink(): fail("symlinked source artifact component: " + value)
    try: path.resolve(strict=True).relative_to(root.resolve(strict=True))
    except (OSError, ValueError) as exc: raise ValueError("source artifact escapes repository: " + value) from exc
    if not path.is_file() or path.is_symlink(): fail("missing source artifact: " + value)
    return path

def validate(root, atlas):
    if atlas.get("schema") != "bhgman-research-atlas/1" or atlas.get("scope") != SCOPE: fail("schema or source-navigation scope invalid")
    contracts = {x.get("type"): x for x in atlas.get("predicate_contracts", [])}
    if len(contracts) != len(atlas.get("predicate_contracts", [])): fail("duplicate predicate contract")
    for x in contracts.values():
        if set(x) != {"type","domain","range","direction","cardinality","meaning"} or x["direction"] != "source_to_target" or not x["meaning"]: fail("invalid predicate contract")
    ids, paths = set(), {}
    req = {"uid","local_path","original_repository","original_revision","original_path","sha256","bytes","artifact_authority","content_authority"}
    for x in atlas.get("source_artifacts", []):
        if set(x) != req or not isinstance(x["uid"], str) or x["uid"] in ids: fail("invalid or duplicate source artifact")
        ids.add(x["uid"]); path = local_file(root, x["local_path"]); paths[x["uid"]] = path
        if not SHA256.fullmatch(x["sha256"]) or digest(path) != x["sha256"]: fail("source digest mismatch: " + x["local_path"])
        if x["bytes"] is not None and (not isinstance(x["bytes"], int) or x["bytes"] != path.stat().st_size): fail("source byte mismatch: " + x["local_path"])
        if not REVISION.fullmatch(x["original_revision"]): fail("invalid source revision")
        if x["artifact_authority"] not in {"SOURCE_DOCUMENT","SECONDARY_AI"} or x["content_authority"] not in {"USER_PRIMARY","UNSPECIFIED","SECONDARY_AI"}: fail("invalid source authority")
    manifest = json.loads((root / "APOSTLE_CONTENT.json").read_text(encoding="utf-8"))
    manifest_docs = {x["repository_path"]: x for x in manifest.get("documents", [])}
    for x in atlas["source_artifacts"]:
        doc = manifest_docs.get(x["local_path"])
        if not doc: continue  # Atlas-only guides and historical navigation pins are separately versioned.
        expected = {"original_repository": doc.get("source_repository"), "original_revision": doc.get("source_revision"), "original_path": doc.get("source_path"), "sha256": doc.get("sha256"), "bytes": doc.get("bytes"), "artifact_authority": doc.get("authority")}
        if any(x[key] != value for key, value in expected.items()): fail("source artifact disagrees with APOSTLE_CONTENT: " + x["local_path"])
        declared_content_authority = doc.get("content_authority", "UNSPECIFIED")
        if x["content_authority"] != declared_content_authority: fail("source content authority disagrees with APOSTLE_CONTENT: " + x["local_path"])
    nodes = {x.get("uid"): x for x in atlas.get("nodes", [])}
    if not nodes or len(nodes) != len(atlas.get("nodes", [])): fail("invalid node UIDs")
    for uid, x in nodes.items():
        if not isinstance(uid, str) or not uid.startswith("bhgman:") or not x.get("type") or not x.get("label"): fail("invalid local node")
        if any(pin not in ids for pin in x.get("sources", [])): fail("node references missing source")
        if x.get("type") == "ExternalKGRecord":
            required = {"external_uid", "authority", "state", "observation_scope", "observed_at", "query", "returned_authority"}
            if not required.issubset(x) or x["observation_scope"] != "READ_ONLY_LOOKUP_NOT_SNAPSHOT" or x["state"] != "READ_ONLY_REFERENCE": fail("external KG reference lacks read-only observation metadata")
            if x["authority"] != x["returned_authority"] or not x["external_uid"] or not x["query"]: fail("external KG reference authority/query mismatch")
    persona = nodes.get("bhgman:persona:airplane-man")
    if not persona or persona.get("stable_entity_uid") != "sym:Character:비행기맨": fail("persona stable entity UID missing")
    vertical = nodes.get("bhgman:topic:vertical-axis-4-8-10")
    wanted = [("#4 비행기맨","apex"),("#8 OM","substrate"),("#10 깊바존","end")]
    if not vertical or [(x.get("source_designator"),x.get("role")) for x in vertical.get("qualified_participants", [])] != wanted: fail("vertical-axis participants incomplete")
    edgeids = set()
    for x in atlas.get("edges", []):
        if not x.get("uid","").startswith("bhgman:") or x["uid"] in edgeids: fail("invalid edge UID")
        edgeids.add(x["uid"]); contract = contracts.get(x.get("type")); source, target = nodes.get(x.get("source")), nodes.get(x.get("target"))
        if not contract or not source or not target: fail("edge endpoint or predicate missing")
        if source["type"] != contract["domain"] or target["type"] != contract["range"]: fail("edge violates predicate domain/range")
        if not isinstance(x.get("sources"), list) or not x["sources"] or any(pin not in ids for pin in x["sources"]): fail("edge lacks valid source pins")
        if x.get("authority") not in {"SOURCE_DOCUMENT","SECONDARY_AI"}: fail("edge authority invalid")
        if x["type"] == "REFERENCES" and x["authority"] != "SECONDARY_AI": fail("reading-map references must be SECONDARY_AI")
    claimids = set()
    for x in atlas.get("claims", []):
        if set(x) != {"uid","authority","status","text","source_quote","source_pins"} or not x["uid"].startswith("bhgman:") or x["uid"] in claimids: fail("invalid claim")
        claimids.add(x["uid"])
        if x["authority"] != "SECONDARY_AI" or not x["status"] or not x["text"] or not x["source_quote"]: fail("claim lacks secondary boundary")
        if not x["source_pins"] or any(pin not in ids for pin in x["source_pins"]): fail("claim source pins invalid")
        if not any(x["source_quote"] in paths[pin].read_text(encoding="utf-8") for pin in x["source_pins"]): fail("claim quote absent from pinned source")
    for x in atlas.get("open_questions", []):
        if not x.get("uid","").startswith("bhgman:open:") or x.get("state") not in {"NOT_ASSERTED","SOURCE_NOT_PRESENT_IN_THIS_REPOSITORY"}: fail("invalid open question")
        if not x.get("sources") or any(pin not in ids for pin in x["sources"]): fail("open question source pins invalid")
    cqs = {x.get("uid"):x for x in atlas.get("competency_queries", [])}
    if len(cqs) < 3 or len(cqs) != len(atlas.get("competency_queries", [])): fail("need three unique competency queries")
    for x in cqs.values():
        answer, pins = nodes.get(x.get("answer_uid")), x.get("source_pins")
        if not x.get("uid","").startswith("bhgman:cq:") or not answer or not isinstance(pins,list) or not pins: fail("invalid competency query")
        if any(pin not in ids for pin in pins) or not set(pins).intersection(answer.get("sources", [])): fail("CQ answer lacks matching source evidence")

def self_test():
    good = json.loads(ATLAS.read_text(encoding="utf-8")); validate(ROOT, good)
    forged = copy.deepcopy(good); forged["claims"][0]["source_quote"] = "__forged_quote__"
    endpoint = copy.deepcopy(good); endpoint["edges"][0]["target"] = "bhgman:persona:airplane-man"
    escaped = copy.deepcopy(good); escaped["source_artifacts"][0]["local_path"] = "../../etc/passwd"
    for bad in (forged, endpoint, escaped):
        try: validate(ROOT, bad)
        except ValueError: continue
        fail("counterexample unexpectedly passed")

def main():
    parser=argparse.ArgumentParser(); parser.add_argument("--self-test",action="store_true"); args=parser.parse_args()
    validate(ROOT, json.loads(ATLAS.read_text(encoding="utf-8")))
    if args.self_test: self_test()
    print("research-atlas check: PASS")
if __name__ == "__main__":
    try: main()
    except (OSError,ValueError,KeyError,TypeError,json.JSONDecodeError) as exc:
        print("research-atlas check: FAIL: "+str(exc),file=sys.stderr); sys.exit(1)
