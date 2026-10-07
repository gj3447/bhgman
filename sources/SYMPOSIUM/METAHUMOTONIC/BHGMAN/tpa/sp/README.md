# 비행기맨 — TPA/SP 위상 (TargetPyramid)

> TPA 역방향 사이클 Phase 3/4. *Pattern Library 매칭* — Contract 가 51 DesignPattern 중 어느 것에 INSTANCE_OF / RESEMBLES 인지 결정. APT/SP 의 *거울 분해*.

---

## 한 줄 정의

비행기맨의 TPA-SP 발현 = **DesignPattern 매칭**. confidence ≥ 0.7 → INSTANCE_OF, < 0.7 → RESEMBLES. 카테고리별 검증 전략 분기. APT 측 SP 가 *N:N DAG 분해* 라면 TPA-SP 는 *기존 pattern 으로 분류*.

---

## Pattern Library 매칭 전략 (카테고리별)

| 카테고리 | 검증 전략 | 위임 위상 |
|---|---|---|
| **Distributed** | MetaVerifier (Naesengmoon `--lens mathematical`) | Naesengmoon (mathematical 113-lens) |
| **Structural** | AST 비교 | Longinus (code-structure binding) |
| **Behavioral** | call graph 분석 | Longinus (sourcePath chain) |
| **Creational** | grep / signature matching | Longinus (sourceId matching) |
| **PL (Programming Language)** | ResearchProvider (학문 정전 lookup) | Prometheus |

→ Pattern Library 57 post-canonicalization (iter 2 audit, >51 target met). 13 lowercase→PascalCase normalize, 4 null→Behavioral 추론, 1 residual UI Navigation pending.

---

## INSTANCE_OF vs RESEMBLES (confidence cutoff 0.7)

```
confidence ≥ 0.7  →  INSTANCE_OF (strict matching)
confidence 0.4~0.7  →  RESEMBLES (weak matching)
confidence < 0.4  →  Pattern Library drought → 학문 정전 lookup
```

→ TR15 Essential ✗ theorem: 완벽한 reverse mapping 불가능 (lossy recovery 인정). RESEMBLES 가 정직.

---

## 5위상 중 TPA-SP 가 호출하는 위상

| 위상 | TPA-SP 단계 활용 |
|---|---|
| **재배맨** | Pattern matching parallel dispatch (51+ pattern 동시 비교) |
| **Prometheus** | Pattern Library drought 시 학문 정전 lookup |
| **Naesengmoon** | Distributed pattern 의 mathematical verification (`--lens mathematical`) |
| **Longinus** | 매칭된 pattern 과 code 의 ReferenceSite binding |
| **Harness** | pattern 이 어느 family tier 의 idiom 인지 분류 |

---

## 본체

| 위치 | 내용 |
|---|---|
| `SKILLS/tpa-sp/SKILL.md` | **공학 측 정본**. Pattern Library 매칭 + 카테고리 분기 |
| `SKILLS/tpa/references/` | 13-file TPA references |
| `THEORY/TPA/SOURCES.md` | 공학 측 자료집 |

---

## 신화 ↔ 공학 다리

| 신화 | 공학 |
|---|---|
| 비행기맨이 *기존 형식과 비교* | DesignPattern Library matching |
| `∀x:CHU j.covers x` 의 *분류* | 51 pattern 중 위치 결정 |
| 정전과의 *거리 측정* | confidence score (0~1) |
| RESEMBLES = *유사하나 불완전* | TR15 Essential ✗ theorem (lossy recovery) |

---

# KG: ATOM_BHGMAN_tpa_sp_phase_2026-05-09
# Lesson: TR_PatternHallucination / TR_DistributedNameOnly / tpa-pattern-library-audit-iter2-2026-05-06
# Note: 폴더명 정정 완료 2026-05-09 (st → sp, drift resolved per CLAUDE.md TPA hardening iter 2)
