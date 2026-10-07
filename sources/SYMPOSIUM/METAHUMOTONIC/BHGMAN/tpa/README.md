# BHGMAN/tpa/ — TPA 역방향 사이클의 신화 측 미러

> 본 폴더 = BHGMAN(비행기맨) 의 *TPA 역방향 사이클* 발현 자리.
> 4 sub-phase {tcw, st, sp, ta} 각자 README.md 채워짐 (2026-05-09).
> ✅ **폴더명 drift 정정 완료** (2026-05-09): 기존 `sa/sp/st/scw` (APT 차용 오류) → canonical `tcw/st/sp/ta` rename 완료. CLAUDE.md TPA hardening iter 2 (lesson-tpa-hardening-iter2-plateau-2026-05-06, "9-layer propagation invariant") 정합.

---

## 위치

```
신화 측 (METAHUMOTONIC):                공학 측 (THEORY/SKILLS):
  BHGMAN/tpa/                            THEORY/TPA/SOURCES.md
    ├── tcw/README.md                      SKILLS/tpa/SKILL.md (orchestrator, 역방향)
    ├── st/README.md                       SKILLS/tpa-tcw/SKILL.md  ← TargetCodeWorld
    ├── sp/README.md                       SKILLS/tpa-st/SKILL.md   ← TargetTwin
    └── ta/README.md                       SKILLS/tpa-sp/SKILL.md   ← TargetPyramid
                                           SKILLS/tpa-ta/SKILL.md   ← TargetAnchor
```

→ `THEORY/TPA/SOURCES.md` 와 `SKILLS/tpa-*/SKILL.md` 가 정본. 본 폴더는 *신화 측 역방향 발현 매핑*.

---

## 비행기맨 ↔ TPA 4 phase 매핑 (역방향)

| TPA phase | README | 비행기맨 핵심 발현 | 5위상 호출 |
|---|---|---|---|
| **TCW** (TargetCodeWorld) | [`tcw/README.md`](tcw/README.md) | code 측에서 cover 시작 (AST 역추출) | **Longinus** + Prometheus + Naesengmoon + Harness |
| **ST** (TargetTwin) | [`st/README.md`](st/README.md) | Contract 역추출 (AptContract vs ConventionalContract) | Prometheus + Naesengmoon + Longinus + Harness |
| **SP** (TargetPyramid) | [`sp/README.md`](sp/README.md) | DesignPattern 매칭 (51 pattern, INSTANCE_OF/RESEMBLES) | 재배맨 + Prometheus + Naesengmoon + **Longinus** + Harness |
| **TA** (TargetAnchor) | [`ta/README.md`](ta/README.md) | 재anchoring 결단 (5 drift + coverage_ratio 0.8) | **Longinus** + Naesengmoon + Prometheus + Harness |

→ TPA 4 phase 모두 비행기맨 5위상 의 *역발현*. APT 거울. Longinus 가 역방향에서 가장 무겁게 발현 (code → KG 추출).

---

## 짝패: APT (정방향) ↔ TPA (역방향)

```
APT:  (사용자 요구) → SA → SP → ST → SCW → (코드 산출)
                                                    ↓
                                                TPA 시작
                                                    ↓
TPA:  (코드) → TCW → ST → SP → TA → (재anchoring)
```

→ 두 사이클이 만나면 round-trip. `(SA→SCW) ∘ (TCW→TA) ≅ id` (가설, BX laws 정합).

→ APT/SA 5 field ↔ TPA/TA 5 drift = 거울 invariant. APT 가 박은 anchor 가 TPA 가 5 drift 모두 0 으로 회수 가능 = 완벽한 round-trip.

---

## TPA 고유 testable consequence (Lakatos progressive)

APT 의 mere replication 이 아닌 5 progressive evidence:

1. **TR15 Essential ✗ theorem** — lossy recovery 인정 (완벽한 reverse mapping 불가능)
2. **5-drift coverage_ratio threshold 0.8** — TPA 고유 invariant
3. **TR5 manifest assertion** — `skipped_files = 0` 강제
4. **INSTANCE_OF/RESEMBLES lattice** — confidence ≥ 0.7 cutoff
5. **Distributed pattern math verification** — 88-Naesengmoon (`--lens mathematical`) 강제

→ 5 invariant 중 어느 하나도 APT 에 없음. TPA 는 progressive.

---

## TPA dogfood 결과 (3 instance, internal vs external)

| Execution | Routing | Coverage | Drift | Lessons | Type |
|---|---|---|---|---|---|
| `tpa-execution-symposium-self-2026-05-06` | 2-B REUSE | **1.0** | 모두 0 | 0 | self → consistency proof |
| `tpa-execution-cd-mind-lean-formalization-2026-05-06` | 2-A NEW | 0.84 | Orphan=2, PatternDiv=1 | 3 | external → Lakatos progressive |
| `tpa-execution-cd-server-hooks-2026-05-06` | 2-C BRANCH | 0.82 | (TBD) | 2 | external cumulative |

→ **internal-vs-external evidence distinction** — self 는 consistency, external 은 novelty.

---

## TPA hardening 정전 (CLAUDE.md iter 1-2)

- **8 :TpaErrorPattern** (TR_BatchShortcut / TR_PatternHallucination / TR_DistributedNameOnly / TR_ManifestSkip / TR_ParserMismatch / TR_OntologyPollution / TR_DriftSilenced / TR_LessonGap)
- **3 추가 (iter 2)**: TR_StaleLesson / TR_LongiusBindingMissing / TR_CoverageOverride (총 11개)
- **9-file references parity** (APT 수준): theory/quick_ref/gates/validation/adversarial/error_handling/kg_logging/phases/gate_check_template
- **4 phase-level world.md** (iter 2): tcw_world.md / st_world.md / sp_world.md / ta_world.md
- **5 SkillVersion v1.2.0** (sibling sync iter 2)
- **9-layer propagation invariant** (lesson-tpa-hardening-iter2-plateau-2026-05-06): folder / frontmatter / KG ATOM / autoboot / body sed / hook case branch / Cypher patterns / CLAUDE.md / `~/.claude/skills/` symlink

→ score 10/10 PROGRESSIVE_CONFIRMED (iter 2 plateau).

---

## 정정 history

| Date | Event | KG ref |
|---|---|---|
| 2026-04-29 | 4 sub-phase 빈 placeholder 생성 (sa/sp/st/scw mis-named) | (initial) |
| 2026-05-06 | TPA hardening iter 1-2 — phase prefix 통일 (tt → st, tp → sp) at SKILLS/ | tpa-hardening-master-plan-2026-05-06 |
| 2026-05-09 | **본 폴더 4 sub-phase rename** (sa→tcw, sp→st, st→sp, scw→ta) + 4 README.md 작성 | ATOM_BHGMAN_tpa_2026-05-09 |

---

# KG: ATOM_BHGMAN_tpa_2026-05-09
# Refs: tpa-hardening-master-plan-2026-05-06 / lesson-tpa-hardening-iter2-plateau-2026-05-06 / TPA_methodology_v10
