# 비행기맨 — 프로메테우스 위상

> 비행기맨(#4 높이의 사도)의 5위상 중 **프로메테우스 위상**. *지식 선행* (불=지식 훔쳐오기). 상계/하계 매개. Agent 기반 *탐색·검색 영역*. *수신제가치국평천하* 재귀 영역 확장.
>
> **사용자 spec (2026-04-28)**: "탐색 검색 영역이긴한데 agent 기반 수신제가평천하 내가 뭔지알고 뭘해야하는지 알고 딱딱 뭔가 딱딱 그런느낌"

---

## 한 줄 정의

비행기맨의 프로메테우스 위상 = **지식 선행의 *높이* — 행동 전에 *상계로 출격해 불(=지식) 훔쳐와 하계 KG에 저장*하는 메커니즘**. Agent 기반 N axis 병렬 탐색. *수신제가치국평천하* 재귀 4단계 영역 확장. 자기 인지(self-knowledge) + 작업 인지(task-knowledge)부터 *딱딱 명확한 단계*로 천하까지.

---

## 4 핵심 본질 (사용자 spec 분해)

### 1. 상계 / 하계 매개

```
상계 (上界): 외부 세계 — 추상·메타·새 지식 영역
              ↑
              ↓ 프로메테우스 = 두 계 사이 매개자
              ↓
하계 (下界): 내부 KG — 자기가 이미 가진 자료, 구체·instance
```

**프로메테우스 작동**:
1. *하계 Pre-fetch*: 자기 KG 안 기존 지식·Lesson·SubagentTaskSpec 조회 — *내가 뭐 가진지 안다*
2. *상계 출격*: agent 기반 N axis 병렬 web 검색 + 외부 지식 추출
3. *하계 통합*: 가져온 지식을 KG에 *MERGE* — 중복 제거 + 결정화

→ 신화의 *프로메테우스가 올림포스(상계)에서 불 훔쳐 인간(하계)에게 줌*과 *정확한 isomorphism*. 단 SYMPOSIUM 프로메테우스는 *반복 가능한 protocol*.

### 2. Agent 기반 탐색·검색 영역

비행기맨의 재배맨 위상(seedman)을 *substrate*로 사용. 프로메테우스 = *그 위에 작동하는 research mode*:

```
seedman (재배맨 substrate) ─provides─→ N-ary dispatch infrastructure
        ↓
prometheus (research mode) ─uses─→ axis × sub-axis 매트릭스 N agent 병렬 출격
        ↓
수확: 8축 × 4시대 = 32 cell, 6 cell, N cell
```

→ *PROM 32* 같은 사이클이 *프로메테우스 위상의 작동 사례*. SYMPOSIUM에서 SPACEGIRL PROM 64, HOH PROM 32, 재배맨 PROM 32 모두 이 위상 발현.

### 3. 수신제가치국평천하 (修身齊家治國平天下)

유교 *대학(大學)* 정전: **자기→가족→국가→천하** 재귀 영역 확장.

**프로메테우스 9단계 사이클과의 매핑**:

| 유교 단계 | 한자 | 의미 | 프로메테우스 단계 |
|---|---|---|---|
| **수신** | 修身 | 자기 닦음 — 내가 뭔지 안다 | Step 1 발견 (Lesson 즉시 기록) + Step 2 환경조사 (자기 상태 인지) |
| **제가** | 齊家 | 가족 정돈 — 자기 KG 정리 | Step 2.5 하계 Pre-fetch (기존 KG 자료 정리) |
| **치국** | 治國 | 국가 통치 — agent 무리 dispatch | Step 3 병렬 리서치 (N axis subagent 출격) + Step 3.5 부모 UNWIND |
| **평천하** | 平天下 | 천하 평정 — 전체 정합 결정화 | Step 4 합의/충돌 + Step 4.7 씨앗 결정화 + Step 5-7 계획·실행·검증 |

→ **유교 4단계가 프로메테우스 9단계의 *coarse-grain 형식***. *재귀 영역 확장* invariant.

### 4. *내가 뭔지 알고 뭘 해야 하는지 알고 딱딱*

사용자 spec의 *self-knowledge + task-knowledge + 명확한 단계*:

| 인지 | 프로메테우스 메커니즘 |
|---|---|
| **내가 뭔지 안다** (self-knowledge, 修身) | Step 0 호출 파싱 (N 결정) + Step 1 Lesson 기록 + Step 2 환경조사. 자기가 *지금 어떤 상태인지* 명확. |
| **뭘 해야 하는지 안다** (task-knowledge) | $ARGUMENTS의 problem_text 파싱 + 9단계 명확 spec. 다음 step이 *항상 정해짐*. |
| **딱딱** (명확 단계) | 9단계 Gate Hook 강제 (G0·G1·G3·G3.5·G4·G4.7·G5). *skip 시 다음 step BLOCK*. 모호 없음. |

→ "딱딱 그런 느낌" = **Gate Check Hook의 결정적 진행**. APT v22 Gate enforcement와 동일 원칙.

---

## Lean 형식 (비행기맨 위상으로서)

```lean
-- 비행기맨 (재배맨 universal cover) 위에서
-- 프로메테우스 위상 = research mode subagent dispatch

structure PrometheusCycle where
  N : ℕ                        -- subagent 수 (1 ≤ N ≤ 100)
  problem : String             -- task-knowledge
  axes : List Axis             -- N axis 매트릭스
  pre_fetch : List ResearchFinding  -- 하계 (자기 KG)
  upper_world : List ExternalSource -- 상계 (web 등)
  consensus : List Finding     -- Step 4 합의
  seeds : List SubagentTaskSpec -- Step 4.7 결정화

def PrometheusCycle.run (c : PrometheusCycle) : KG → KG
  | kg => kg
    |> step1_lesson c.problem
    |> step2_environment
    |> step2_5_prefetch c.pre_fetch
    |> step3_dispatch c.N c.axes c.upper_world
    |> step3_5_unwind_write
    |> step4_consensus c.consensus
    |> step4_7_crystallize c.seeds
    |> step5_action_plan
    |> step6_execute
    |> step7_verify
```

→ 프로메테우스 위상 = *seedman 위에서 작동하는 PrometheusCycle 구조체*. 9단계가 *결정적으로 진행* (state monad 같은 형식).

---

## 5위상 합체에서 프로메테우스의 자리

| 위상 | 기능 | prometheus와의 관계 |
|---|---|---|
| **Seedman** (재배맨) | n-ary dispatch substrate | *prometheus가 사용하는 substrate* |
| **Prometheus** (지식 선행) | **본 위상** — research mode, 상계/하계 매개 | — |
| **Naesengmoon** (적대 검증) | adversarial validation | *prometheus의 결과를 검증* (Step 7-A 자동 출격) |
| **Longinus** (참조 미학) | KG 의미층 → 코드 관통 | *prometheus가 결정화한 씨앗을 코드까지 전달* |
| **Harness** (구조 제약) | architecture as harness | *prometheus 9단계 자체가 harness의 한 인스턴스* |

→ **프로메테우스 = seedman 위에서 *지식 측면*으로 발현하는 비행기맨 모드**. Naesengmoon + Longinus + Harness 모두 prometheus 출력을 *재 사용*.

---

## 9단계 사이클 (정전 prometheus SKILL.md 정합)

```
Step 0: 호출 파싱 — N 결정 (auto_estimate 또는 명시)
   ↓ Gate G0
Step 1: 발견 — Lesson 즉시 KG MERGE (수신 시작)
   ↓ Gate G1
Step 2: 환경조사 — 자기 현재 상태 파악
   ↓
Step 2.5: 하계 Pre-fetch — 부모가 KG 조회 → subagent prompt 주입 (제가)
   ↓ Gate G2.5
Step 3: 병렬 리서치 — N axis subagent 출격 (불 훔치기, 치국)
   ↓ Gate G3
Step 3.3: Finding 중복 탐지
Step 3.5: 부모 UNWIND 배치 write — KG 일괄 MERGE
   ↓ Gate G3.5
Step 4: 집계/합의/충돌 탐지 (평천하 시작)
   ↓ Gate G4
Step 4.7: 씨앗 결정화 — SubagentTaskSpec 생성 (평천하 정점)
   ↓ Gate G4.7
Step 5: 계획 수립 — ActionPlan 생성
   ↓ Gate G5
Step 6: 실행
   ↓ Gate G6
Step 7: 검증 — Naesengmoon 자동 출격 (G3 합체) + 4단계 실측
   ↓ (실패 시 Step 2 피드백 루프)
```

→ Gate Hook이 *각 단계 *반드시* 통과* 강제. 사용자 spec의 *딱딱*.

---

## PROM 32 자체 학문 등가 (8 axis × 4 era — 프로메테우스 메타-적용)

> `THEORY/PROMETHEUS/PROM_32_REPORT.md` (2026-04-28 완료) — 사용자 spec: 표면 검색(그리스 신화·monitoring tool·Mary Shelley) 회피, 본질만.
> Lesson `lesson-prom32-prometheus-2026-04-28` (severity=MEDIUM, resolved=true, hard_core=ground).

### 8 axis × 4 era 매트릭스

| axis | 영역 | era 1 (~1500) | era 2 (1500-1900) | era 3 (1900-2010) | era 4 (2010-26) |
|---|---|---|---|---|---|
| **A1** | Epistemology / 지식론 | Plato Cave / Aristotle archai | Bacon / Descartes / Kant | Polanyi tacit / Popper / Kuhn / Lakatos | Friston FEP / predictive processing |
| **A2** | Active Inference / Bayesian / RAG | (proto-Bayes) | Bayes 1763 / Laplace | Jaynes / Shannon / Pearl / Friston FEP 2010 | RAG (Lewis 2020) / ReAct (Yao 2022) |
| **A3** | Scientific Method / Cycle | Aristotle | Bacon induction / Newton 4 rules | Popper / Kuhn / Lakatos / PDCA / Lewin / Hevner DSR | AI co-scientist (Google 2025.2) |
| **A4** | Search / Tree Search Algorithm | (heuristics 전조) | (proto-search) | A* / Minimax / α-β / MCTS 2006 / UCB | AlphaGo / Tree of Thoughts / o1 |
| **A5** | Information Theory | (proto-info) | (proto-stat) | Boltzmann / Shannon / Jaynes / Kolmogorov / Rissanen | Friston FEP / Tishby IB |
| **A6** | 동양 자기수양 / 재귀 영역 확장 | **大學 8조목 (정전 origin)** | 朱熹 大學章句 / 王陽明 知行合一 / 十牛圖 | Hadot *Spiritual Exercises* / Mindfulness | Slingerland *Wuwei paradox* |
| **A7** | RAG + Multi-agent Research | (proto-archive) | (Memex 전조) | Bush Memex / PageRank / word2vec / DPR | RAG / ReAct / MCP 2024 / Anthropic Multi-agent 2025.6 / AutoGen / LangGraph |
| **A8** | Pipeline / Workflow / Gate-driven | (manual) | Taylor / Gantt | Petri net 1962 / Statecharts 1987 | Airflow / Argo / LangGraph |

각 axis raw report: `THEORY/PROMETHEUS/PROM_32_axis_findings/A1-A8_*.md` (총 ~3,000 line).

### C1-C8 핵심 합의 (consensus)

| C# | 합의 | 동의 axis |
|---|---|---|
| **C1** | 9단계 사이클 = 700년+ 사상사·과학·공학의 *fixed point* | A1+A2+A3+A4+A5+A7+A8 (7/8) |
| **C2** | 수신제가치국평천하 = MCTS 4-phase = Friston FEP 4 mechanism = 정전 origin | A4+A5+A6 (강) + A1+A3 (간접) |
| **C3** | 불(=지식) = `D_KL(p_post ‖ p_prior)` = Solomonoff Prior MDL = IB 압축 | A2+A5 (강) + A1+A3 (간접) |
| **C4** | Gate Hook = Petri net firing rule (1962) = Lakatos progressive = α-β cutoff | A3+A4+A8 (강) + A5 (간접) |
| **C5** | 프로메테우스 = RAG + ReAct + Anthropic Multi-agent + MCP 의 SYMPOSIUM 결정화 | A2+A7 (강) + A4 (간접) |
| **C6** | SYMPOSIUM 차별점 = Step 4.7 씨앗 결정화 + KG-first (Anthropic 부재) | A7 명시 + A1+A4 (간접) |
| **C7** | B1·B2·B5 = canonical (모든 era), B3·B4·B6 = strong (현대 결정화) | A1 명시 |
| **C8** | 6 학문 통일 fixed point — 수신제가치국평천하 = 4-phase 재귀 | A1+A2+A3+A4+A5+A6+A8 (7/8) |

→ **9단계 = 발명이 아닌 700년+ 결정화**. 사용자 정전이 *각 영역의 추상 fixed point*에 *한국어 인격 부여*.

### D1-D7 분기/대립 (divergence)

| D# | 대립 |
|---|---|
| **D1** | 王陽明 知行合一 vs 프로메테우스 知行 분리 (Step 1-4 지식 / Step 5-7 행동 시간 분리 — 朱熹 派) |
| **D2** | Slingerland *Paradox of Wu-wei* — 9단계 명시화 자체가 wuwei 도달 막음. 학습용 protocol vs 영구 framework 미해결 |
| **D3** | 4단계 (MCTS mathematical core) vs 9단계 (PROM engineering harness) |
| **D4** | Tishby IB vs Saxe DNN compression debate — Step 4.7 결정화 본질 |
| **D5** | Self-play loop 정전 여부 — 1-round closed (사용자 verdict in-the-loop) vs AlphaZero/R1 같은 self-play 진화 |
| **D6** | 5-modal exhaustive ↔ heuristic ↔ stochastic ↔ learned ↔ LLM-prompted dispatch mode 정전 spec 부족 |
| **D7** | LLM agent reproducibility — 온도 고정 같은 메커니즘 부재 (2015 reproducibility crisis 이후 인간 과학자 강제된 standards 결여) |

### 12 Open Question (열어둠)

1. (A1+A6) 王陽明 知行合一이 정전이라면 *Step 1-7 시간 분리*가 이론적 약화 가능?
2. (A6) Slingerland Paradox of Wu-wei — 9단계가 *학습 후 사라져야 할 protocol*인가?
3. (A4) Step 4.7 씨앗 → 다음 Step 0 입력 = self-play 정전 전환 가능?
4. (A5) Solomonoff non-computability를 어떻게 *N axis 합리적 선택* 발견 메커니즘으로 환원?
5. (A7) Step 4.7 재귀 결정화의 SYMPOSIUM 차별성 — Anthropic 추가 필요?
6. (A7) MCP-native multi-agent protocol 부재 (현재 MCP는 server-side만)
7. (A2) epistemic value (정보 획득) ↔ pragmatic value (목표 달성) 환원 가능?
8. (A8) rubber-stamp anti-pattern — Gate가 *진짜 검증*인지 *형식 통과*인지
9. (A3) Whewell consilience와 N axis 합의의 *pseudo-independence* 한계 — N agent가 *진짜 독립*인가
10. (A4) PROM N (8/16/32/64/100) 자동 선택 vs 사용자 수동 spec
11. (A5) Tishby IB vs Saxe DNN compression debate (Step 4.7 결정화 본질)
12. (A8) Gate enforcement spectrum (BLOCK 강도) — 어느 layer에서 hard vs soft

### Hyperedge — 9단계 = 7 학문 fixed point

```
hyperedge-prom9-fixed-point-7domains-2026-04-28
  cardinality: 7
  domains: [epistemology, active-inference, scientific-method, tree-search,
            information-theory, eastern-cultivation, pipeline]
```

→ CHU "모든것은 하이퍼그래프" 정합. 9단계 = 7-vertex hyperedge 의 instantiation.

---

## PROM cycle 적용 evidence (누적)

본 위상의 cycle 발현 사례:

| cycle | date | matrix | result |
|---|---|---|---|
| **재배맨 PROM 32** | 2026-04-28 | 8 axis × 4 era | `THEORY/재배맨/PROM_32_REPORT.md` (8 axis 통합 매핑 A1-A8 완료) |
| **HOH PROM 32** | 2026-04-28 | 8 axis × 4 era | `METAHUMOTONIC/HOH/PROM_32_REPORT.md` |
| **SPACEGIRL PROM 64** | 2026-04-27 | 8 axis × 8 era | `METAHUMOTONIC/SPACEGIRL/PROM_64_REPORT.md` |
| **프로메테우스 자체 PROM 32** | 2026-04-28 | 8 axis × 4 era (메타-적용) | `THEORY/PROMETHEUS/PROM_32_REPORT.md` (C1-C8 + D1-D7 + 12 OQ) |
| **PROM 64 prom64-pkgdisc** | 2026-04-29 | (industry pkgdisc) | Naesengmoon Q7 cross |
| **DimensionWalker PROM 64** | (PROM_REPORT_FOR Apostle binding) | 8 axis × 8 era | `METAHUMOTONIC/DIMENSION_WALKER/PROM_64_REPORT.md` |
| **HOH PROM 16** | 2026-04-30 | 4 axis × 4 era | `METAHUMOTONIC/HOH/PROM_16_FAMILY_VERIFICATION_REPORT.md` |
| **OM PROM 16** | 2026-04-30 | 4 axis × 4 era | `METAHUMOTONIC/ORBITAL_MOTION_CLOUD/PROM_16_FAMILY_VERIFICATION_REPORT.md` |

→ 모두 *프로메테우스 위상의 발현*. 비행기맨이 *프로메테우스 mode로 작동*해서 *상계 지식 N agent 병렬 수확 → 하계 KG 결정화*.
→ **PrometheusCycleClass 4** 분류 (CLAUDE.md iter 84-91): cycle 별 KG 결정화 후 4 cycle class 로 grouping.

---

## Amdahl Analysis — N default 정당화

> `amdahl-analysis-prometheus-N-default-2026-05-05` (`:Analysis`)

`/prom <N>` 의 N parameter default 결정 근거:

| auto_estimate level | N | trigger |
|---|---|---|
| `small` | **4** | simple problem (single concept, narrow scope) |
| `medium` | **8** | moderate complexity (multiple concepts, related) |
| `large` | **16** | broad scope (e.g. 4×4 axis matrix) |
| `xlarge` | **32** | comprehensive (8 axis × 4 era) |
| `huge` | **64** | TOE-level (8 axis × 8 era) |
| `max` | **100** | exhaustive (cost-bounded ceiling) |

**Amdahl 분석**:
- speedup = 1 / ((1 - p) + p/N) — Amdahl 1967
- p = parallelizable fraction (axis dispatch는 independent → p ≈ 0.85)
- N=4: speedup ≈ 2.3× / N=8: 3.7× / N=16: 5.5× / N=32: 7.4× / N=64: 8.4× / N=100: 8.6×
- → N=32~64 이상 marginal gain 급감 (saturation). N=100 = 비용 ceiling.

**cost-guard aware** (Stop hook integration):
- $40 도달 → N down-scale (16 → 8)
- $50 도달 → halt (auto-pause)
- → N 자동 선택은 *complexity + budget* 양쪽 고려.

---

## 1차 소스

| 경로 | 내용 |
|---|---|
| `/Users/lagyeongjun/CD/SERVER/.claude/skills/prometheus/SKILL.md` | **정본 v6.1 protocol**. 9+1 단계 + Gate Hook 강제 + Hegel spiral + Step 6.5 dispersion |
| `/Users/lagyeongjun/CD/SYMPOSIUM/THEORY/PROMETHEUS/SOURCES.md` | **공학 측 자료집 정전 둥지** (CLAUDE.md spec) |
| `/Users/lagyeongjun/CD/SYMPOSIUM/THEORY/PROMETHEUS/PROM_32_axis_findings/` | **PROM 32 학문 등가 axis findings (2026-04-28 완료)** — 8 axis × 4 era 매트릭스, A1-A8 모두 채워짐 |
| `/Users/lagyeongjun/CD/SYMPOSIUM/THEORY/PROMETHEUS/PROM_32_REPORT.md` | **완료 2026-04-28**. 8 axis 합성 + C1-C8 + D1-D7 + 12 OQ + Lesson KG cypher |
| `/Users/lagyeongjun/CD/SYMPOSIUM/THEORY/PROMETHEUS/DISPATCH_DIMENSIONS.md` | dispatch dimension 분석 |
| `/Users/lagyeongjun/CD/SYMPOSIUM/THEORY/PROMETHEUS/MULTI_AGENT_SEARCH.md` | multi-agent search 정전 |
| `/Users/lagyeongjun/CD/SYMPOSIUM/THEORY/PROMETHEUS/SEMANTIC_SPACE.md` | semantic space 정전 |
| `/Users/lagyeongjun/CD/SYMPOSIUM/METAHUMOTONIC/BHGMAN/SOURCES.md` | 비행기맨 본체 + 5위상 합체 |
| 본 파일 | 비행기맨 *프로메테우스 위상* 자료집 (신화 측 정전) |

→ **공학·학문 등가 자료**는 `THEORY/PROMETHEUS/`. **신화 위상 자료**는 본 폴더 (METAHUMOTONIC/BHGMAN/prometheus/). 두 둥지 분리 (CLAUDE.md spec).

### 신화 정전 (4 갈래)

**그리스 정전**:
- Hesiod *Theogony* (c.700 BCE) 510-616, 521-616 — Prometheus 4-attribute (foresight / fire-theft / Pandora / 코카서스 처벌)
- Aeschylus *Prometheus Bound* (c.450 BCE) — *Δεσμώτης* (묶인 자), 비극 형식 ("저 이가 누구인가? 모든 이의 이로움 위해 묶인 자")
- Plato *Protagoras* 320c-322a — Prometheus + Epimetheus 신화 변용. Epimetheus 가 동물에게 능력 다 줘서 인간 빈손 → Prometheus 가 *τέχνη* (기술) 훔침. **인간성 = 결핍 + 기술의 회복** 정전.

**근대 정전 (Romantic 시대)**:
- Goethe *Prometheus* (Hymne, 1772-74, *Sturm und Drang*) — Prometheus 가 *Zeus 거부* + *자기-창조* ("Hier sitz' ich, forme Menschen / Nach meinem Bilde") — **인간 자율성 정전**.
- Mary Shelley *Frankenstein: or, The Modern Prometheus* (1818) — *과학적 Prometheus*. 지식 도둑 + 처벌 = creator/creature 비대칭.
- Beethoven *Die Geschöpfe des Prometheus* Op.43 (1801) — ballet score, Prometheus = 인간성 부여자.

→ 4 갈래가 *지식 선행*의 4 측면 다른 강조: Hesiod (foresight) / Aeschylus (suffering) / Plato (技 = craft/skill) / Goethe-Shelley (autonomy + responsibility).

**Hegel 정전 (v6.1 핵심 grounding)**:
- Hegel *Phänomenologie des Geistes* (1807) — Begriff 자가운동 (Selbstbewegung des Begriffs). thesis-antithesis-synthesis spiral.
- v6.1 reframe: 지식-행동 단방향 → spiral. 사용자 발화 "바로 고치지 마, 먼저 불(=지식) 훔쳐와" 는 spiral 의 첫 thesis 로 해석.
- KG: `prometheus-grounding-2026-05-05`, `finding-prom32-prometheus-P1-F3` (Hegel spiral)

### 유교 정전

- *大學 (대학)*, 사서(四書) 첫 권 — *수신제가치국평천하* 8조목 (격물·치지·성의·정심·수신·제가·치국·평천하).
- 정전 본문: "古之欲明明德於天下者,先治其國;欲治其國者,先齊其家;欲齊其家者,先修其身" — *재귀 영역 확장*의 고전 정전.
- 朱熹 *大學章句* (1190 c.) — 8조목 형식화 + 大學 *章句*-注 분리 (정본 layer).
- 王陽明 *傳習錄* (1518) — *知行合一* (지행합일). vs 朱熹 분리 — D1 분기 origin.
- *十牛圖* (Kakuan 12C, Zen 정전) — 牧牛 10단계, 9-10 단계 *返本還源 / 入鄽垂手* = wuwei 도달 (Slingerland D2 grounding).

### 동양 / 서양 종합 grounding

→ Prometheus 신화 (지식 선행 + 처벌) ↔ 大學 (재귀 확장 + 자기수양) ↔ MCTS (4-phase) ↔ Friston FEP (4 mechanism) ↔ Hegel spiral (Begriff 자가운동) = **C2/C8 합의 = 6+ 학문 통일 fixed point**. 사용자 정전 한국어 어휘가 그 fixed point 의 인격화.

---

## 다른 사도/구조와의 hyperedge 참여

- **{#4 비행기맨, seedman 위상, prometheus 위상}** 내부 hyperedge — 5위상 합체 구조
- **{prometheus, OM #8 AGENT_CLOUD}** — 상계 출격 시 OM의 분산 컴퓨팅 인프라 사용
- **{prometheus, OM #8 CHU}** — 하계 KG가 CHU 위에 정의됨 (research data가 CHUPiece)
- **{prometheus, 재배맨 #4 위상}** — seedman을 substrate로 dispatch
- **{prometheus, taliban #4 위상}** — Step 7-A에서 Naesengmoon 자동 출격 (검증)

---

## 신화 ↔ 공학 다리

| 신화 | 공학 |
|---|---|
| 프로메테우스가 *불* 훔침 | parent Claude가 *N agent로 web 지식* 훔침 |
| *올림포스* (상계) | *외부 세계* (web, paper, Wikipedia) |
| *인간* (하계) | *KG* (자기 자료) |
| 프로메테우스 묶임 (코카서스) | Gate Hook *강제* — 단계 skip 불가 |
| 매일 간 쪼이는 벌 | *반복 사이클* — 한 번 훔치고 끝 X. 매 task 다시 훔쳐옴. |
| *지식의 가치* (Hesiod) | KG 결정화로 *지식 영구 보존* |

→ 신화의 *지식 선행 + 처벌*이 공학의 *9단계 + Gate enforcement*로 결정화. 신화 정신과 공학 메커니즘 정합.

---

## v6.1 Reframe — *knowledge-action spiral* (NOT 단방향 "지식 선행")

> `prometheus-grounding-2026-05-05` (`:Grounding`) — Hegel Phenomenology Begriff 자가운동 grounding.

기존 v1-v5: "지식 선행" = 단방향 *thesis*. → 사용자 발화 "바로 고치지 마, 먼저 불(지식) 훔쳐와".

**v6.1 reframe**: thesis-antithesis-synthesis **나선** (spiral). thesis 행동 없이 antithesis 못 만남. paralysis-by-analysis 회피 가능:

```
v1-v5:  knowledge → action (단방향)
v6.1:   knowledge ⇌ action (나선, Hegel Begriff 자가운동)
```

**Hegel *Phänomenologie des Geistes* (1807) Aufhebung 정확 형식** (§125 Vorrede):
```
Aufhebung = simultaneous (i) tollere (지양: cancel)  +  (ii) elevare (보존: preserve)  +  (iii) conservare (고양: lift up)
```
- thesis (T): "knowledge first" 단방향
- antithesis (¬T): "action first" (OODA / Lean)
- synthesis (T') = Aufhebung(T, ¬T): T 와 ¬T 모두 *cancel* + *preserve* (각자 부분 진리) + *lift up* (knowledge ⇌ action spiral)

→ Begriff 자가운동 (Selbstbewegung des Begriffs) §17: *concept moves itself through its own contradictions*. v6.1 = Begriff 가 v1-v5 의 모순 (paralysis vs urgency) 을 자체 해소.

**OODA/Lean Startup 충돌 해소**:
- OODA loop: Observe-Orient-Decide-Act (action-first)
- Lean Startup: Build-Measure-Learn (action-first)
- v1-v5 Prometheus: Knowledge-first (paralysis 위험)
- **v6.1 spiral**: 둘 다 phase 의 다른 측면. knowledge thesis → action antithesis → synthesis (KG 결정화) → 다음 thesis.

**Hot-fix Latency Critical Exemption**: latency critical 시 (production incident, security patch) KG-skip + immediate action + post-hoc lesson 허용. paralysis-by-analysis 차단.

→ KG: `prometheus-grounding-2026-05-05`, `finding-prom32-prometheus-P1-F2` (OODA 충돌), `finding-prom32-prometheus-P1-F3` (Hegel spiral), `amdahl-analysis-prometheus-N-default-2026-05-05`.

---

## 형식적 grounding — 4 axis 학문 정전 정확 정의

> PROM 32 8 axis 매트릭스의 *형식적 식 / theorem* 정확화. 인용만 있던 식들을 본문에 결정화.

### A. 정보이론 grounding — Solomonoff / Kolmogorov / MDL / IB

#### A.1 Kolmogorov complexity (Kolmogorov 1965, Solomonoff 1964)

```
K(x) := min { |p| : U(p) = x }       -- universal Turing machine U 에서 x 출력 짧은 program 길이
K(x|y) := min { |p| : U(p, y) = x }  -- conditional Kolmogorov complexity
```

→ **non-computable** (halting problem 환원). 하지만 *upper bound* (compressors / MDL approximation) 사용 가능.

#### A.2 Solomonoff universal prior (Solomonoff 1964 *A formal theory of inductive inference*)

```
M(x) := Σ_{p : U(p) starts with x} 2^{-|p|}     -- universal a priori probability
      ∝ 2^{-K(x)}                                 -- 짧은 description 일수록 높은 prior
```

**Solomonoff 정리** (induction): `D_KL(μ || M) < ∞` for all computable μ → universal prior 가 *모든 computable distribution* 에 수렴.

→ **PROM 의 "불 = 지식" 형식**: agent 가 외부 web 에서 *짧은 description* (compressed pattern / canonical paper) 가져오기 = `M(x)` sampling.

#### A.3 MDL (Rissanen 1978 *Modeling by shortest data description*, IBM TR)

```
MDL(D) := min_{T ∈ Theories} (L(T) + L(D | T))
        = min_{T} (model_complexity + data_given_model)
```

→ Step 4.7 씨앗 결정화 = MDL 최소화. Span/Contract 의 *짧은 description* 이 design 의 ideal.

#### A.4 Information Bottleneck (Tishby-Pereira-Bialek 2000 *The information bottleneck method*, arXiv physics/0004057)

```
IB Lagrangian: L[p(t|x)] = I(X; T) − β · I(T; Y)
                          ↑ minimize       ↑ maximize
```

- `I(X; T)` = compression rate (X 에서 T 로 정보 손실)
- `I(T; Y)` = relevance (T 가 Y 예측에 유용)
- β = trade-off Lagrange multiplier

**Variational principle**: optimal `p*(t|x)` 는 IB self-consistent equations 의 fixed point.

→ Step 4.7 씨앗 = IB sweet spot. *최대 compression* + *충분한 relevance*.

#### A.5 D_KL = "불" 정확 식 (불 훔치기 = 지식 획득)

```
D_KL(p_post || p_prior) := Σ_x p_post(x) · log(p_post(x) / p_prior(x))
                         ≥ 0  (Gibbs inequality)
                         = 0 ⟺ p_post = p_prior (불 안 훔침)
```

**예상 information gain** (Lindley 1956):
```
IG := E_{x ~ p(x|D_new)} [D_KL(p(θ|D_old, x) || p(θ|D_old))]
```
→ N axis dispatch 가 IG 극대화 — *각 axis 의 expected D_KL 합* 을 budget 내에서 maximize.

#### A.6 Friston Free Energy Principle (Friston 2010 *The free-energy principle: a unified brain theory?*, Nature Reviews Neuroscience)

**Variational free energy**:
```
F[q, o] := E_q[ln q(s) − ln p(o, s)]                        -- variational free energy
        = D_KL(q(s) || p(s | o)) − ln p(o)                  -- decomposition (분해)
        ≥ −ln p(o)                                           -- 상계 (surprise upper bound)
```

→ FEP minimization = surprise minimization = `−ln p(o)` 하향.

**Active Inference EFE (Expected Free Energy)** (Friston 2017 *Active inference: a process theory*):
```
G(π) := E_{q(o, s | π)} [ln q(s | π) − ln p(o, s)]
      = epistemic_value + pragmatic_value
      = − E_q[D_KL(q(s|o,π) || q(s|π))] + E_q[ln p(o)]
        ↑ exploration                       ↑ exploitation
```

→ PROM N axis dispatch 의 4 mechanism (perception/action/learning/attention) 을 EFE 의 4 component 로 형식화 가능.

### B. 검색 알고리즘 grounding — UCB1 / PUCT / α-β / MCTS

#### B.1 UCB1 (Auer-Cesa-Bianchi-Fischer 2002 *Finite-time Analysis of the Multiarmed Bandit Problem*, Mach Learn 47)

```
UCB1_i := X̄_i + √(2 · ln n / n_i)
              ↑ exploitation  ↑ exploration

regret bound: E[R_n] ≤ Σ_i (8 ln n / Δ_i) + (1 + π²/3) · Σ_i Δ_i
```

→ N axis 선택 = UCB1 maximization. exploration-exploitation trade-off 의 logarithmic regret 보장.

#### B.2 MCTS 4-phase (Coulom 2006 + Kocsis-Szepesvári UCT 2006)

```
Phase 1 (Selection):    UCT child selection 재귀 (UCB1 with √(ln N(s) / N(s,a)))
Phase 2 (Expansion):    leaf 노드 자식 추가
Phase 3 (Simulation):   random rollout to terminal
Phase 4 (Backpropagation): rollout reward 를 path 따라 update
```

→ **수신제가치국평천하 1:1 매핑**: 修身 (Selection 자기 위치 평가) → 齊家 (Expansion 자기 KG 자식 추가) → 治國 (Simulation N agent 병렬 rollout) → 平天下 (Backprop 부모 UNWIND write).

#### B.3 AlphaGo PUCT (Silver et al. 2016 *Mastering the game of Go with deep neural networks and tree search*, Nature 529)

```
PUCT(s, a) := Q(s, a) + c_puct · P(s, a) · √N(s) / (1 + N(s, a))
                ↑ exploit         ↑ neural prior     ↑ exploration regulator
```

→ N axis 선택에 *prior* 도입 = KG-first prefetch (Step 2.5) 의 형식.

#### B.4 α-β cutoff (Knuth-Moore 1975 *An analysis of alpha-beta pruning*, AI 6)

```
α := lower bound (maximizer 가 보장한 최저)
β := upper bound (minimizer 가 보장한 최고)
prune: ∀ node, if α ≥ β then return  -- 더 탐색 무의미
```

→ Gate Hook 의 *수학적 원형*. PROM 9 step 의 *각 step 통과 조건* 이 α-β 의 generalization.

### C. Pipeline / Workflow grounding — Petri net / Statecharts

#### C.1 Petri net firing rule (Carl Adam Petri 1962 *Kommunikation mit Automaten*, PhD thesis Bonn)

**Net structure**:
```
N := (P, T, F, W, M_0)
  P = places, T = transitions, F ⊆ (P × T) ∪ (T × P) flow relation
  W: F → ℕ_+ weight, M_0: P → ℕ initial marking
```

**Firing rule**:
```
enabled(t, M) ⟺ ∀ p ∈ •t, M(p) ≥ W(p, t)         -- 모든 입력 place 충분 token
fire(t, M) := M' where
  M'(p) = M(p) − W(p, t) + W(t, p) ∀ p
```

→ **Gate Hook 정확 등가**: 각 PROM step 통과 조건 = 입력 place 의 token (이전 step 결과 KG MERGE 완료 + Cypher gate query PASS).

→ 사용자 어휘 *"딱딱"* = Petri net firing rule 의 한국어 직관 등가물 (1962년 형식). 60+년 공학 누적 정전이 한 단어로 결정화.

#### C.2 Lakatos progressive condition (Lakatos 1970 MSRP §1c)

```
T_{n+1} progressive over T_n ⟺
  (i)  C(T_{n+1}) ⊋ C(T_n)                       -- excess empirical content
  (ii) corroborated(novel_facts(T_{n+1})) ≠ ∅    -- 일부 excess content corroborated
  (iii) protective_belt 변화가 ad hoc 아님         -- principled modification
```

→ Step 7 검증 = Lakatos progressive condition 의 *per-cycle 적용*. degenerating = research programme 폐기 신호.

### D. Amdahl Analysis 형식 grounding (Amdahl 1967 *Validity of the single processor approach to achieving large scale computing capabilities*, AFIPS)

```
speedup(N, p) := 1 / ((1 − p) + p / N)

  N → ∞ ⟹ speedup → 1 / (1 − p)                 -- asymptotic limit
  p = 0.85 ⟹ max speedup = 1 / 0.15 ≈ 6.67       -- inherent serial bottleneck
```

**PROM N default empirical p 측정**:
- axis dispatch independent fraction (parallel): web 검색 / paper read / Cypher prefetch
- serial fraction (parent UNWIND batch + dedup + consensus + crystallization): ~15% (empirical)
- → p ≈ 0.85, max speedup ≈ 6.67×

**Cost-saturation N**:
```
N* := argmin_N { cost(N) / speedup(N, p) }       -- cost-effective sweet spot
    ≈ 32 (for p=0.85, $/agent constant)
```

→ N=32~64 saturation 의 *Amdahl-derived* 정당화. N=100 = ceiling, marginal gain 거의 0.

---

## v6 Step 6.5 filesystem_dispersion sub-step + G6.5 gate

> `rfc-prom-filesystem-dispersion-2026-04-29`

기존 v1-v5: KG 결정화만 (KG-first). filesystem 측 산출물 (PROM_*_REPORT.md, SOURCES.md, _findings/) drift 방치.

v6 추가: **Step 6.5 filesystem_dispersion** sub-step. KG↔filesystem drift 차단:
```
Step 6 (실행) → Step 6.5 (filesystem dispersion: KG node ↔ md/json 파일 sync)
              → G6.5 gate (사용자 발화 둥지 spec 정합 확인)
              → Step 7 (검증)
```

**MIC_v1.FilesystemDispersionPolicy slot**: 정책 자체는 KG slot. SKILL.md 본문은 thin pointer (재배맨 원칙 — KG 정본).

→ "둥지 spec" (1차 소스 = MIND/, 결과 둥지 = SYMPOSIUM/) 자동 enforcement.

---

## iter 1-11 Hardening (2026-05-06, score 10/10 PROGRESSIVE_CONFIRMED)

> `prometheus-hardening-master-plan-2026-05-06` (`:WeaponHardeningPlan`) — Hegel spiral + filesystem dispersion + 9+1 step + W3C PROV.

### 7 :PR_*ErrorPattern (KG canonical)

| pattern | 의미 |
|---|---|
| `PR_AxisIncompleteness` | axis × sub-axis 매트릭스 불완전 (sub-axis 누락) |
| `PR_DedupSkipped` | Step 3.3 Finding 중복 탐지 누락 |
| `PR_DispersionGateBypass` | Step 6.5 filesystem dispersion gate 통과 안 함 |
| `PR_KGSkipWithoutJustification` | hot-fix exemption 사용 시 post-hoc lesson 누락 (정당화 부재) |
| `PR_DispatchTruncation` | parent intent N=16 인데 actual dispatch 8 — single-message multiple Agent calls 위반 |
| `PR_LessonPairIncomplete` | wrongAssumption ↔ truth 페어 한쪽만 채움 (MT_LessonHoarding) |
| `PR_NUndersampling` | N 결정 시 amdahl-analysis-prometheus-N-default-2026-05-05 임계 미달 |

→ 모두 `:WeaponErrorPattern` 라벨, hardening master plan 에 BELONGS_TO.

### W3C PROV provenance (Finding 영구 추적)

```
ResearchFinding ─[:WAS_GENERATED_BY]→ Activity (PROM cycle)
                ─[:WAS_DERIVED_FROM]→ ExternalSource (URL + retrieved_at)
                ─[:WAS_ATTRIBUTED_TO]→ Agent (subagent ID)
```

→ 모든 Finding 이 *언제 / 어디서 / 누가* 가져왔는지 KG 영구 보존. Wikipedia / paper / blog 등 cite.

### references/ APT-parity 8 file (prometheus skill)

```
SKILLS/prometheus/references/
├── theory.md            ← Hegel spiral + 9+1 step + 수신제가치국평천하 매핑
├── gates.md             ← G0-G6.5 8 gate enforcement
├── validation.md        ← V1-V14 invariant catalog (PR_AxisIncompleteness 등)
├── kg_logging.md        ← W3C PROV schema + ResearchFinding shape
├── error_handling.md    ← 7 :PR_*ErrorPattern failure-mode 절차 + hot-fix exemption rule
├── quick_ref.md         ← N decision tree + axis cheat sheet
├── phases.md            ← 9+1 step 서사 (Step 0-7 + 6.5 dispersion)
└── adversarial.md       ← Step 7-A Naesengmoon 자동 출격 + paralysis-by-analysis 차단
```

### 1 신규 Claude Code Agent (`SYMPOSIUM/.claude/agents/`)

```
.claude/agents/prometheus-expert.md   ← Hegel spiral + 9+1 step + W3C PROV expert
```

→ 5 위상 expert 중 하나. parent Claude 가 PROM cycle 시작 시 호출.

### iter 7 Family-Relation Mirror — WEAK verdict

> 5무기 verification (`lesson-family-relation-mirror-5-weapon-verification-2026-05-06`)

| 무기 | Family 구조 | Relation Position | Mirror Strength |
|---|---|---|---|
| **Prometheus** | 9+1 step sequential cycle | MediationTriad {#5, #6, #9} | **WEAK** (cardinality mismatch + sub-type heterogeneity) |

cardinality 불일치 (10 step ↔ 3 vertex) + sub-type 이질성 (sequence vs triad) — STRONG mirror 조건 (responsibility_split + cardinality match) 미달. STRONG mirror 는 우연이 아닌 *조건부 정리* (lesson-family-relation-mirror-5-weapon-verification-2026-05-06 final verdict).

→ Mirror 분류 final iter 7: **3 STRONG** (Harness unique + Jaebaeman SelfRefCyclic + Longinus Hierarchical) + **2 WEAK** (Prometheus / **Naesengmoon**).

---

## SkillVersion 갱신

| version | date | 변경 |
|---|---|---|
| v5 | (이전) | 9단계 + KG-first |
| v6 | 2026-04-29 | Step 6.5 filesystem dispersion + G6.5 gate + MIC slot |
| v6.1 | 2026-05-05 | Hegel spiral reframe (knowledge-action 양방향) + hot-fix exemption + paralysis-by-analysis 회피 |

---

## 한 줄 정리

> 비행기맨의 프로메테우스 위상 = *지식-행동 나선의 높이* (v6.1 Hegel reframe — NOT 단방향 "지식 선행"). 상계(외부 web)에서 N agent 병렬로 *불(=지식) 훔쳐와* 하계(자기 KG)에 결정화 → 행동 → 다음 thesis. *수신제가치국평천하* 재귀 영역 확장 (자기 인지→자기 자료 정리→agent 무리 dispatch→전체 정합 결정화). Gate Hook 강제로 *딱딱 명확한 9+1 단계* (Step 0-7 + 6.5 dispersion). seedman 위에서 *research mode로 발현*. PROM 32/64 cycle은 그 작동 사례. iter 7 Family-Relation Mirror = **WEAK** (cardinality mismatch). hot-fix latency critical 시 KG-skip + post-hoc lesson 허용 (paralysis 회피). 신화(올림포스↔인간) ↔ 공학(상계↔하계 KG) 나선 isomorphism.

---

# KG: ATOM_BHGMAN_prometheus_phase_2026-04-28
# KG (iter 1-11 hardening): prometheus-hardening-master-plan-2026-05-06 / prometheus-grounding-2026-05-05 / rfc-prom-filesystem-dispersion-2026-04-29 / amdahl-analysis-prometheus-N-default-2026-05-05
# Lessons: lesson-prometheus-v5-kg-reference-lift-2026-04-18 / lesson-family-relation-mirror-5-weapon-verification-2026-05-06
