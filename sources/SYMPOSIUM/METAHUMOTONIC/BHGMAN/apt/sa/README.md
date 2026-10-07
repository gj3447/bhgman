# 비행기맨 — APT/SA 위상 (SemanticAnchor)

> APT 사이클 Phase 1/4. *시작점* — 비행기맨의 `∀x:CHU j.covers x` cover 가 어디서 시작될지 anchor 결정.

---

## 한 줄 정의

비행기맨의 SA 발현 = **anchor identity 확정**. `objective / definition / keyAssertion / C_S / contextBudget` 5 core field 로 cycle 의 *원점* 박기. KG-first 탐색이 이 anchor 에서 출발.

---

## SA 5 mandatory core field (lesson-sa-contract-v2-rejected-redesign-2026-04-20)

| field | 비행기맨 발현 |
|---|---|
| `objective` | "이번 cycle 이 cover 할 CHU 부분집합" |
| `definition` | anchor 의 형식 정의 (자기참조 방지 wff) |
| `keyAssertion` | 본 cycle 의 핵심 주장 1줄 |
| `C_S` | 5-predicate satisfaction criteria |
| `contextBudget` | budget envelope (token / 시간 / 깊이) |

→ 5 field 누락 = 비행기맨 cover 기능 없는 anchor. SP 진입 차단 (Gate Hook).

---

## 5위상 중 SA 가 호출하는 위상

| 위상 | SA 단계 활용 |
|---|---|
| **Prometheus** | SA 진입 전 KG-first prefetch (axis × sub-axis prefetch) |
| **Longinus** | 기존 anchor 와 ReferenceSite 충돌 검사 |
| **재배맨** | (호출 안 함 — SA 는 single anchor decision) |
| **Naesengmoon** | (호출 안 함 — Gate 는 SP→ST/ST→SCW 단계) |
| **Harness** | anchor 가 family 어느 tier 에 속하는지 결정 (3-tier 분류) |

---

## 본체

| 위치 | 내용 |
|---|---|
| `SKILLS/apt-sa/SKILL.md` | **공학 측 정본**. SA cycle 운영체 |
| `SKILLS/apt-sa/references/` | 9-file APT-parity references |
| `THEORY/APT/SOURCES.md` | 공학 측 자료집 |
| `../../SOURCES.md` | 비행기맨 본체 (`∀x:CHU j.covers x`) |
| `../../seedman/SOURCES.md` | 재배맨 위상 (SP 단계 dispatch substrate) |

---

## 신화 ↔ 공학 다리

| 신화 | 공학 |
|---|---|
| 비행기맨 *시작점* — 어디서 cover 시작할지 결정 | SemanticAnchor 노드 결정 + objective declaration |
| *높이의 사도* — 위에서 내려다보며 시야 확보 | contextBudget 으로 cover 범위 한정 |
| `∀x:CHU j.covers x` 의 *진입* 게이트 | SA→SP gate (5 field 검증) |

---

# KG: ATOM_BHGMAN_apt_sa_phase_2026-05-09
# Lesson: lesson-sa-contract-v2-rejected-redesign-2026-04-20
