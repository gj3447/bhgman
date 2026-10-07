# 비행기맨 — APT/SCW 위상 (SourceCodeWorld)

> APT 사이클 Phase 4/4. *물질화* — Contract 가 TDD 로 코드 결정화되는 단계. KG ↔ source code *관통* (Longinus 위상 발현).

---

## 한 줄 정의

비행기맨의 SCW 발현 = **Contract → Code 의 TDD 결정화**. RED(test first) → GREEN(code) → REFACTOR. 모든 코드 line 에 KG ref 주석 (Longinus ReferenceSite 7-tuple). same-layer Task 병렬 가능.

---

## TDD 흐름 + Longinus 관통

```
Contract → RED (test 작성, 실패)
                ↓
            GREEN (code 작성, test pass)
                ↓
            REFACTOR (code clean, test still pass)
                ↓
            ReferenceSite 7-tuple binding (Longinus L1~L7)
                ↓
            sha256 baseline (drift detection 활성)
```

→ KG ref 누락 = Longinus L4 Semiotic Binding 위반 (Sinn/Bedeutung 미연결).

---

## v26 A5 FulfillmentGate 7 checks

| check | 의미 |
|---|---|
| `executor != critic` | 같은 agent 가 만들고 검증 = 0-distance 자기검증 차단 |
| `LensSet completeness` | constitutional + mathematical + solid + longinus 모두 있는지 |
| `prior VR APPROVED` | ST→SCW gate VR 통과 후에만 |
| `TDAD impact_tests` | 영향 받는 test 식별 (mandatory) |
| `vibe_coding bounds` | sweet/min/hard_max via MethodologyConfig slot |
| `Longinus binding` | ReferenceSite 7-tuple 모두 채워짐 |
| `sha256 baseline` | drift detection daemon 활성 |

→ 7 checks 모두 통과 시 cycle 완결. 1개라도 누락 = SCW gate BLOCK.

---

## 5위상 중 SCW 가 호출하는 위상

| 위상 | SCW 단계 활용 |
|---|---|
| **재배맨** | same-layer Task 병렬 dispatch |
| **Prometheus** | (호출 안 함 — research 끝났음) |
| **Naesengmoon** | SCW gate 의 *executor != critic* enforcement + lens ensemble 재공격 |
| **Longinus** | **본 위상의 핵심** — 7-Layer Reference 관통 + sha256 daemon |
| **Harness** | 4축 中 *Verify + Correct* 발현 (test = verify, refactor = correct) |

---

## 본체

| 위치 | 내용 |
|---|---|
| `SKILLS/apt-scw/SKILL.md` | **공학 측 정본**. TDD + ReferenceSite + FulfillmentGate |
| `SKILLS/apt-scw/references/` | 9-file APT-parity references |
| `SKILLS/bin/longinus_sha256_daemon.py` | 91.2% baseline + drift detection (production template) |
| `THEORY/APT/SOURCES.md` | 공학 측 자료집 |
| `../../longinus/SOURCES.md` | **본 위상 핵심 위상** — 7-Layer Reference Model |

---

## 신화 ↔ 공학 다리

| 신화 | 공학 |
|---|---|
| 비행기맨이 cover 한 의미가 *물질화* | Contract → 실제 코드 |
| 롱기누스 창 — 7 layer 동시 관통 | ReferenceSite 7-tuple binding |
| *영원한 창* (성유물) | sha256 baseline = 영구 reference |
| `∀x:CHU j.covers x` 의 *코드 발현* | KG ref 주석 100% 커버 (모든 line) |

---

# KG: ATOM_BHGMAN_apt_scw_phase_2026-05-09
# Lesson: ATOM_APT_v26_Gate_Hook_Lens_Enforcement_2026-04-21 / longinus-sha256-daemon-canonical-2026-05-06
