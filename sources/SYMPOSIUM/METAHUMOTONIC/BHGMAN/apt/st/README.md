# 비행기맨 — APT/ST 위상 (SemanticTwin)

> APT 사이클 Phase 3/4. *결정화* — AtomicSpan 들이 Contract + Task + 8 ST Decision Areas 로 결정화되는 단계.

---

## 한 줄 정의

비행기맨의 ST 발현 = **Crystallization 자체**. AtomicSpan (의미) → Contract (typed DTO/Schema) + Task (200-500 line semantic unit) + 8 decision area. *prose* 가 *typed structure* 로 응축.

---

## 8 ST Decision Areas (v27 exhaustive cover, lesson-st-cover-scope-exhaustive-2026-04-29)

| Tier | Area | 비행기맨 발현 |
|---|---|---|
| **1 ★** | AST | code structure 위 type signature 결정 |
| **1 ★** | Workflow | sequential / parallel / event-driven 분기 |
| **1 ★** | DesignPattern | 51 pattern library matching |
| **1 ★** | DataFlow | input/output 경로 |
| **1 ★** | Store | persistence layer (KG / RDBMS / file) |
| 3 | ProjectStructure | folder layout |
| 3 | Algorithm | 핵심 algorithm 선택 |
| 3 | ClassDesign | OOP/FP class boundary |

→ Tier 1 5 area 모두 결정 후 SCW 진입. Tier 3 는 SCW 단계로 deferred 가능.

---

## Contract v2 9-axis (v26 A2, RFC)

| axis | 의미 |
|---|---|
| `name` | unique id |
| `inputs` | typed input |
| `outputs` | typed output |
| `pre` | precondition (DbC) |
| `post` | postcondition (DbC) |
| `invariant` | class/struct invariant |
| `error_variants` | exhaustive error enum |
| `access_rights_closure` | 권한 envelope (newly added) |
| `cross_axis_invariant` | 6 invariant (cross-axis consistency) |

→ Mathlib-free Lean skeleton: `MIND/lean_formalization/contract_v2_9axes_standalone/` (lake build PASS, 8 theorem 6 sorry).

---

## 5위상 중 ST 가 호출하는 위상

| 위상 | ST 단계 활용 |
|---|---|
| **재배맨** | (호출 안 함 — ST 는 single crystallization decision) |
| **Prometheus** | DesignPattern matching 시 unknown pattern 학문 정전 lookup |
| **Naesengmoon** | ST→SCW gate (Contract v2 9-axis valid 검증) |
| **Longinus** | Contract → ReferenceSite 7-tuple binding (SCW 진입 직전) |
| **Harness** | 4축 中 *Constrain* 발현 (Contract = constraint envelope) |

---

## 본체

| 위치 | 내용 |
|---|---|
| `SKILLS/apt-st/SKILL.md` | **공학 측 정본**. 8 decision area + Contract v2 |
| `SKILLS/apt-st/references/` | 9-file APT-parity references |
| `THEORY/APT/SOURCES.md` | 공학 측 자료집 |

---

## 신화 ↔ 공학 다리

| 신화 | 공학 |
|---|---|
| 비행기맨이 cover 한 영역의 *형식 결정* | Contract v2 9-axis crystallization |
| `∀x:CHU` 가 typed schema 로 표현 | Contract.shared=true (cross-Span 공유 타입) |
| Crystallization Frontier 통과 | C(S) 5-predicate 만족한 leaf 들의 ST 진입 |

---

# KG: ATOM_BHGMAN_apt_st_phase_2026-05-09
# Lesson: lesson-st-cover-scope-exhaustive-2026-04-29 / SA_Contract_v2_DbC_Interface_2026-04-21_v2
