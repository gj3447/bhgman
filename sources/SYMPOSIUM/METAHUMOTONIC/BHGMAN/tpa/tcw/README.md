# 비행기맨 — TPA/TCW 위상 (TargetCodeWorld)

> TPA 역방향 사이클 Phase 1/4. *시작점* — 외부/레거시 코드에서 실제 존재하는 모든 pub 심볼 추출. APT/SCW 의 *거울 시작점*.

---

## 한 줄 정의

비행기맨의 TCW 발현 = **code 측에서 cover 시작**. AST 기반 pub 심볼 추출. Unknown 발견 시 ResearchProvider (Prometheus) 자동 호출. 비행기맨이 *반대 방향에서* `∀x:CHU j.covers x` 시작.

---

## TCW 핵심 작업

| 단계 | 비행기맨 발현 |
|---|---|
| **AST 파싱** | tree-sitter / LSP 로 모든 pub symbol 추출 |
| **manifest 생성** | `skipped_files = 0` 강제 (TR5 invariant) |
| **Unknown 탐지** | 외부 dependency / 외부 paradigm 발견 시 Prometheus 자동 dispatch |
| **종료 gate** | AdversarialValidator (Naesengmoon) gate 통과 |

→ TR5 manifest assertion: `assert skipped_files == 0`. 1개라도 누락 = TCW gate BLOCK.

---

## v0.8-A1 per-AtomicSpan VR enforcement (recovered Contracts)

- recovered Contract 도 individual ValidationResult required (APT 거울).
- coverage_ratio < 0.8 → status='SUSPENDED' 강제 (TPA 고유 invariant).
- pre_hardcore exemption mechanism applies (APT 거울).

---

## 5위상 중 TCW 가 호출하는 위상

| 위상 | TCW 단계 활용 |
|---|---|
| **Longinus** | **본 위상의 substrate** — code → KG 7-Layer Reference 역방향 |
| **Prometheus** | Unknown symbol/library/paradigm 발견 시 학문 정전 lookup |
| **재배맨** | (호출 안 함 — TCW 는 single AST scan) |
| **Naesengmoon** | TCW→ST gate (manifest assertion + Unknown classification) |
| **Harness** | code 가 어느 family tier 의 산출물인지 분류 (3-tier) |

---

## 본체

| 위치 | 내용 |
|---|---|
| `SKILLS/tpa-tcw/SKILL.md` | **공학 측 정본**. AST scan + manifest + Unknown handling |
| `SKILLS/tpa/references/` | 13-file TPA references (orchestrator + phase-level) |
| `THEORY/TPA/SOURCES.md` | 공학 측 자료집 |
| `../../longinus/SOURCES.md` | **본 위상의 substrate** — 7-Layer Reference 역방향 |

---

## 신화 ↔ 공학 다리

| 신화 | 공학 |
|---|---|
| 비행기맨이 *반대편 출발* — 코드에서 의미로 | TCW = code → ST (Contract 추출) → SP (분해) → TA (재anchoring) |
| 롱기누스 창의 *역방향* | reverse 7-Layer Reference (code → KG) |
| `∀x:CHU j.covers x` 의 *역추론* | universal cover 의 후험적 검증 |

---

# KG: ATOM_BHGMAN_tpa_tcw_phase_2026-05-09
# Lesson: TR_ManifestSkip / TR_DistributedNameOnly / TR_ParserMismatch
# Note: 폴더명 정정 완료 2026-05-09 (sa → tcw, drift resolved)
