# 비행기맨 — TPA/TA 위상 (TargetAnchor)

> TPA 역방향 사이클 Phase 4/4. *재anchoring* — recovered design 이 SemanticAnchor 로 결정화 + 5종 drift 측정 + Longinus 전수 binding. APT/SA 의 *거울 종료점*.

---

## 한 줄 정의

비행기맨의 TA 발현 = **재anchoring 결단**. SemanticAnchor 라우팅 (2-A 신규 / 2-B 재사용 / 2-C 브랜치). 5종 drift 측정. coverage_ratio < 0.8 → status='SUSPENDED' 강제. 비행기맨이 *반대편에서 만든 anchor* 가 기존 anchor 와 어떻게 일치/충돌하는지 결단.

---

## SemanticAnchor 라우팅 3-way

| 라우팅 | 조건 | 의미 |
|---|---|---|
| **2-A NEW** | 기존 anchor 와 충분히 다름 | 새 anchor 결정화 (e.g. `mind-lean-formalization-2026-05-06`) |
| **2-B REUSE** | 기존 anchor 와 일치 (consistency proof) | 흡수 — coverage_ratio=1.0 (e.g. SYMPOSIUM self) |
| **2-C BRANCH** | 기존 anchor 의 변형 | 새 sub-anchor (e.g. `cd-server-hooks-production-2026-05-06`) |

---

## 5종 Drift 측정 (TPA 고유 testable consequence)

| Drift | 측정 |
|---|---|
| **Missing** | code 는 있으나 KG ref 없음 (Longinus L4 위반) |
| **Orphan** | KG ref 있으나 code 없음 (반대 위반) |
| **SigMismatch** | sig 불일치 (AST diff) |
| **PatternDiv** | 동일 대상 상충 ref |
| **LabelRot** | 라벨/이름 변경 미반영 |

→ TPA 고유 invariant: 5 drift 모두 0 = 완벽한 round-trip.
→ APT 의 mere replication 아닌 progressive (Lakatos test 통과).

---

## coverage_ratio threshold

```
coverage_ratio = recovered_contracts / total_pub_symbols

coverage_ratio ≥ 0.8  →  status='ACTIVE' (TA 통과)
coverage_ratio < 0.8  →  status='SUSPENDED' (강제 차단)
```

→ TR_CoverageOverride: coverage 미달 안에서 ACTIVE 강제 = 반칙. user verdict 필수.

---

## 5위상 중 TA 가 호출하는 위상

| 위상 | TA 단계 활용 |
|---|---|
| **Longinus** | **본 위상의 finale** — recovered Contract 전수 ReferenceSite binding + sha256 baseline |
| **Naesengmoon** | 최종 gate (5 drift + coverage + 라우팅 결정 검증) |
| **Prometheus** | 새 anchor 결정 시 학문 정전 cross-check |
| **재배맨** | (호출 안 함 — TA 는 single anchor decision) |
| **Harness** | recovered design 이 어느 family tier 의 instance 인지 final classification |

---

## TPA dogfood 결과 (2 instance)

| TPA execution | routing | coverage | drift | lessons |
|---|---|---|---|---|
| `tpa-execution-symposium-self-2026-05-06` | 2-B REUSE | **1.0** (perfect) | 모두 0 | 0 (consistency proof) |
| `tpa-execution-cd-mind-lean-formalization-2026-05-06` | 2-A NEW | 0.84 | Orphan=2, PatternDiv=1 | 3 (external dogfood proof) |
| `tpa-execution-cd-server-hooks-2026-05-06` | 2-C BRANCH | 0.82 | (TBD) | 2 (cumulative external dogfood) |

→ self-application = consistency proof (no novelty). external = Lakatos progressive evidence.

---

## 본체

| 위치 | 내용 |
|---|---|
| `SKILLS/tpa-ta/SKILL.md` | **공학 측 정본**. SemanticAnchor 라우팅 + 5 drift + Longinus 전수 binding |
| `SKILLS/tpa/references/` | 13-file TPA references |
| `THEORY/TPA/SOURCES.md` | 공학 측 자료집 |

---

## 신화 ↔ 공학 다리

| 신화 | 공학 |
|---|---|
| 비행기맨이 *반대편에서 도착* | TA = TCW 시작점의 거울 종료점 |
| `∀x:CHU j.covers x` 의 *재확인* | recovered design 이 기존 anchor 와 일치/분기 |
| round-trip 완성 | `(SA→SCW) ∘ (TCW→TA) ≅ id` (가설, BX laws 정합) |
| coverage_ratio = 1.0 | 완벽한 거울 (lossless) |
| coverage_ratio < 0.8 | TR15 Essential ✗ theorem 발현 (lossy recovery) |

---

# KG: ATOM_BHGMAN_tpa_ta_phase_2026-05-09
# Lesson: TR_CoverageOverride / TR_DriftSilenced / tpa-execution-symposium-self-2026-05-06 / tpa-execution-cd-mind-lean-formalization-2026-05-06
# Note: 폴더명 정정 완료 2026-05-09 (scw → ta, drift resolved per CLAUDE.md TPA hardening iter 2)
