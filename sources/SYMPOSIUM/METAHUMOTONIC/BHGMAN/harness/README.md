# 비행기맨 — harness 위상 (자기참조)

> **Phase 3** of `bhgman_harness_drift_resolution_v1_2026-04-28.md`
> Resolved 2026-04-29 (PROM 16 F11)

---

## 왜 이 폴더는 비어있는가

**비행기맨 자체가 harness다.**

```lean
isAirplaneMan(j) := ∀x:CHU, j.covers x
```

`j.covers` = "j 가 모든 점에 도달" = "harness (industry sense) 가 모든 model interaction 을 둘러쌈" 의 신화 측 표현.

비행기맨이 자기 안에 또 harness 폴더를 둔다 = **self-reference 모순** (∀x:CHU 안에 또 ∀x:CHU 가 있다는 것).

→ 본 폴더는 **의도적으로 비어있음**. drift 인지 흔적.

---

## 본체는 어디에

| 위치 | 내용 |
|---|---|
| `../SOURCES.md` | BHGMAN(비행기맨) 본체 자료집 |
| `../seedman/SOURCES.md` | seedman(재배맨) 위상 — n-ary dispatch substrate |
| `../prometheus/SOURCES.md` | prometheus 위상 — research mode |
| `../taliban/`, `../longinus/` | 다른 위상 (현재 빈 폴더) |
| `THEORY/HARNESS/SOURCES.md` (공학 측) | industry agent scaffolding 정의 + 사례 |
| `SKILLS/harness/SKILL.md` (skill 정본) | harness skill 운영체 (Phase 1 재작성 예정) |

---

## 짝패 (Apostle ↔ Weapon)

| 신화 측 (METAHUMOTONIC) | 공학 측 (THEORY/SKILLS) |
|---|---|
| 12사도 #4 비행기맨 | harness (industry agent scaffolding) |
| `∀x:CHU j.covers x` | tool API + context + memory + permission + orchestration ∀ cover |
| 산소필멸자 위 운송수단 | model 위 infra envelope |

**Industry harness 사례** (THEORY/HARNESS/SOURCES.md 에 자세히):
- Cursor / Claude Code / Aider / Continue / SWE-agent / OpenHands / Smol-developer / MCP

---

## 정정 history

| Date | Event | KG ref |
|---|---|---|
| 2026-04-28 | 사용자 자체 진단: "harness 를 그 하네스로 처음 했는데 4축 abstract 으로 drift" | `lesson-5dae-wonso-metaphor-drift-20260428` |
| 2026-04-28 | 정정 plan 작성: `bhgman_harness_drift_resolution_v1_2026-04-28.md` (6 Phase) | `lesson-harness-drift-corrected-2026-04-28` |
| 2026-04-29 | Phase 3 (본 README) + Phase 0/4/5/6 즉시 처리 (PROM 16 F11) | F11 commit |
| 2026-04-29 | Phase 1 (SKILLS/harness/ 폴더화 + 본문 재작성) + Phase 2 (4축 분리) 완료 | `harness-hardening-master-plan-2026-05-06` |
| 2026-04-30 | PROM 32 autonomous loop cycle 완료 — 4-Layer 자율 stack 결정화 | `THEORY/HARNESS/PROM_32_AUTONOMOUS_LOOP_REPORT.md` |
| 2026-04-30 | Family-Relation Mirror 격상 — 비행기맨 = **STRONG (unique)** mirror | `lesson-family-relation-mirror-5-weapon-verification-2026-05-06` |
| 2026-05-06 | iter 1-11 hardening 완료 — 5무기 통합 10/10 PROGRESSIVE_CONFIRMED_PLATEAU | `harness-hardening-master-plan-2026-05-06` (10/10) |

---

## iter 1-11 Hardening 결과 (Harness 측, cross-ref)

> 본 폴더는 self-reference 의도적 비움. iter 1-11 hardening 결과 본체는 `THEORY/HARNESS/` + `SKILLS/harness/`.

핵심 결정화:
- **1:N sibling family 3-tier** 정전 (PROM 16 ADK 2026-04-29):
  - IDE-host coding harness: Cursor / Claude Code / Aider / SWE-agent / Cline / OpenHands
  - application agent runtime: Google ADK / LangGraph / CrewAI / AutoGen
  - managed cloud: Anthropic Managed Agents / OpenAI Assistants / Vertex AI Agent Engine
- **Anthropic 진영 3-tuple**: Skills (declarative capability) + Agent SDK (loop) + Managed Agents (infra)
- **MCP** = 3 tier 사이 어댑터 (host 책임 정반대 — IDE-host 가 MCP server / application runtime 이 MCP client)
- **5 :HR_*ErrorPattern** (KG canonical): Family1to1 / TierConfusion / AxisMonopoly / BockelerCitationDrift / MCPRoleConfusion
- **harness-diagnostician agent** (`SYMPOSIUM/.claude/agents/harness-diagnostician.md`, ~140 line) — 4축 진단 + 3-tier classification
- **PROM 32 autonomous loop** (2026-04-30) — 4-Layer 자율 stack: settings.json 권한 + PreToolUse/Stop hooks + CLAUDE.md durable + 외부 wrapper (Routines)
- **Family-Relation Mirror = STRONG (unique)** (iter 7) — Harness 3-tier ↔ VerticalAxisHyperedge {#4, #8, #10} apex/substrate/end **1:1 position mirror**. 5무기 中 *유일* STRONG (responsibility_split + cardinality match 조건부 정리).

---

# KG: ATOM_BHGMAN_harness_phase_2026-04-29 / lesson-harness-drift-corrected-2026-04-29 / harness-hardening-master-plan-2026-05-06 / lesson-family-relation-mirror-5-weapon-verification-2026-05-06
# Lessons: lesson-5dae-wonso-metaphor-drift-20260428 / lesson-harness-citation-drift-bockeler-2026-04-30
# Resolves: BHGMAN/harness/ 빈 폴더 자기참조 모순 명시화 (Phase 3)
