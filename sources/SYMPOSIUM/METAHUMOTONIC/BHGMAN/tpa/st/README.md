# 비행기맨 — TPA/ST 위상 (TargetTwin)

> TPA 역방향 사이클 Phase 2/4. *암묵 → 명시* — 각 pub 심볼의 암묵적/명시적 Contract 추출. APT/ST 의 *거울 결정화*.

---

## 한 줄 정의

비행기맨의 TPA-ST 발현 = **Contract 역추출**. AptContract (명시 interface/trait) vs ConventionalContract (암묵 시그니처) 분리 라벨. pre/postcondition 주석 파싱. APT 측 ST 가 *prose → typed structure* 라면 TPA-ST 는 *code → typed structure*.

---

## AptContract vs ConventionalContract

| 라벨 | 의미 | 예 |
|---|---|---|
| **AptContract** | 명시 interface/trait/abstract class | Java interface, Rust trait, TypeScript interface |
| **ConventionalContract** | 암묵 signature only | Python duck-typed function, JavaScript object shape |

→ 두 종류 모두 Contract v2 9-axis 로 결정화. 단, Conventional 은 `pre/post/invariant` 가 *추론* 기반 (lower confidence).

---

## LOC>100 giant method 위임

```
LOC > 100  →  SP 로 위임 (giant method 분해 후)
LOC ≤ 100  →  ST 에서 Contract 추출 가능
```

→ 거대 method 는 *one Contract* 가 안 됨. SP recursive D(S) 적용 후 leaf 에서 Contract 추출.

---

## 5위상 중 TPA-ST 가 호출하는 위상

| 위상 | TPA-ST 단계 활용 |
|---|---|
| **Prometheus** | Unknown pattern/algorithm 학문 정전 lookup (TR_PatternHallucination 차단) |
| **Naesengmoon** | ST→SP gate (Contract v2 9-axis valid 검증) |
| **Longinus** | recovered Contract → ReferenceSite binding (역방향) |
| **재배맨** | (호출 안 함 — ST 는 single Contract extraction per pub) |
| **Harness** | Contract 가 어느 layer 의 envelope 인지 분류 |

---

## 본체

| 위치 | 내용 |
|---|---|
| `SKILLS/tpa-st/SKILL.md` | **공학 측 정본**. AptContract vs ConventionalContract + LOC 위임 |
| `SKILLS/tpa/references/` | 13-file TPA references |
| `THEORY/TPA/SOURCES.md` | 공학 측 자료집 |

---

## 신화 ↔ 공학 다리

| 신화 | 공학 |
|---|---|
| 비행기맨이 *암묵을 명시화* | ConventionalContract → AptContract 격상 |
| `∀x:CHU j.covers x` 의 *역결정화* | code → typed Contract 추출 |
| Crystallization 거울 (응축의 역) | typed structure 로 응축된 prose 의 *재발견* |

---

# KG: ATOM_BHGMAN_tpa_st_phase_2026-05-09
# Lesson: TR_PatternHallucination / TR_OntologyPollution
# Note: 폴더명 정정 완료 2026-05-09 (sp → st, drift resolved per CLAUDE.md TPA hardening iter 2)
