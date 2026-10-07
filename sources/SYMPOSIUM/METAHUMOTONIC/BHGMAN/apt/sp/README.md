# 비행기맨 — APT/SP 위상 (SemanticPyramid)

> APT 사이클 Phase 2/4. *재귀 분해* — 비행기맨의 universal cover 가 `governs : List` 적용으로 N:N DAG 분해되는 단계.

---

## 한 줄 정의

비행기맨의 SP 발현 = **재배맨 inductive expansion**. SP 는 *one world*. Span 들이 DAG node (N:N, 트리 아님). D(S) recurrence until 모든 leaf 가 C(S) 5-predicate 만족 = AtomicSpan.

```lean
-- Lean: governs 가 SP 의 본체
inductive JaebaeMan
  | atomic : (CHU → Prop) → JaebaeMan
  | governs : List JaebaeMan → JaebaeMan
```

---

## C(S) 5-predicate (v26 강제, AtomicSpan 판정)

| predicate | 비행기맨 발현 |
|---|---|
| `objective` | Span 이 cover 할 부분 |
| `definition` | Span 의 형식 정의 |
| `keyAssertion` | Span 의 1-line claim |
| `verification` | testability 명시 (TDD-able) |
| `c_s_predicate` | satisfaction predicate (Boolean) |

→ leaf Span 에서 5 predicate non-null 시 **Crystallization Frontier** 도달. ST 진입.

---

## v26 RFC: per-AtomicSpan VR enforcement (v0.8-A1 production)

- 모든 AtomicSpan 에 individual ValidationResult required.
- pre_hardcore archive anchor 는 exempt (17/17 classified iter 25-27).
- production active anchor: 13/13 PASS at 0.81 ensemble UNION precondition (iter 30).

→ SP frontier batch shortcut 차단 (HR17 BatchShortcutAtAnyPhase).

---

## 5위상 중 SP 가 호출하는 위상

| 위상 | SP 단계 활용 |
|---|---|
| **재배맨** | **본 위상의 substrate** — N:N DAG dispatch |
| **Prometheus** | unknown 발견 시 axis × sub-axis prefetch |
| **Naesengmoon** | SP→ST gate 의 LensSet ensemble UNION precondition (`--lens constitutional/mathematical/solid/longinus`) |
| **Longinus** | sourcePath / line_range placeholder (SCW 단계에 채워짐) |
| **Harness** | family 분기점 — Span 이 IDE-host / agent runtime / managed cloud 어느 tier 인지 |

---

## 본체

| 위치 | 내용 |
|---|---|
| `SKILLS/apt-sp/SKILL.md` | **공학 측 정본**. SP recursive D(S) + Crystallization Frontier |
| `SKILLS/apt-sp/references/` | 9-file APT-parity references |
| `THEORY/APT/SOURCES.md` | 공학 측 자료집 |
| `../../seedman/SOURCES.md` | **본 위상의 substrate** — 재배맨 inductive |

---

## 신화 ↔ 공학 다리

| 신화 | 공학 |
|---|---|
| 비행기맨 = 재배맨 inductive 의 정점 | `isAirplaneMan(j) := ∀x:CHU j.covers x` |
| `governs : List` 재귀 | SP recursive D(S) decomposition |
| atomic 재배맨 (Layer 1) | AtomicSpan (C(S) 5-predicate satisfied) |
| Crystallization (응축) | Frontier — SP→ST 진입 조건 |

---

# KG: ATOM_BHGMAN_apt_sp_phase_2026-05-09
# Lesson: lesson-taliban-shortcut-antipattern-2026-04-21 / per-span-gate-enforcement-canonical-2026-05-06
