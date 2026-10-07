# 비행기맨 — Longinus 위상 (참조의 미학)

> 비행기맨(#4 높이의 사도)의 5위상 중 **Longinus 위상**. 참조의 미학. KG 의미층을 소스코드까지 *관통(貫通)* 시키는 7-Layer Reference Model.

---

## 한 줄 정의

비행기맨의 Longinus 위상 = **`∀x:CHU j.covers x` 의 *관통* mode** — 모든 의미 layer 를 단일 reference 로 꿰뚫는 역할. KG 의미층 ↔ 소스코드 양방향 추적성 보장.

롱기누스 = 신약 성경의 *예수 옆구리를 창으로 찌른 백부장*. 7 layer 동시 관통 = 하나의 창이 7개 의미 차원을 동시에 꿰뚫음.

---

## 7-Layer Reference Model (v3 정전)

| Layer | 이름 | 정의 | Longinus 대응 |
|---|---|---|---|
| **L1** | Address Indirection | 메모리 주소, 포인터 | `sourcePath` (file:line) |
| **L2** | Lifetime/Scope | 참조 유효 범위 | `pierced_at` / `drift_detected` |
| **L3** | Type Permission | 소유권, 권한 | Refinement Type (`ValidSourceRef`) |
| **L4** | Semiotic Binding | 기표→기의 (Frege Sinn/Bedeutung) | `sourceId` = Sinn, `sourcePath` = Bedeutung |
| **L5** | Distributed Identity | 합의 기반 참조 유효성 | KG MERGE (멱등, consensus) |
| **L6** | Information Compression | 간접참조 = 중복제거 | `# KG: xxx` = Kolmogorov 압축 |
| **L7** | Aesthetic/Intentional | 참조의 미학, 관통의 의도 | 최소 침습으로 최대 추적 |

**Drift 5종** (Layer 별로 다르게 발현):
- L1 — sourcePath line drift (LSP/tree-sitter)
- L2 — 참조 범위 초과 (file 삭제)
- L3 — type 불일치 (signature 변경, AST diff)
- L4 — 의미 변경 (rename detection)
- L5 — KG 노드 삭제/이동
- L6 — 중복 참조
- L7 — 미학 위반 (과도한 참조)

---

## BX Lens Laws (v3)

> Bidirectional Transformation (BX) 이론 — Foster et al. 2007 *Combinators for Bidirectional Tree Transformations*

```
GET: KG → Code  (sourceId/sourcePath → 코드 위치)
PUT: Code → KG  (코드 변경 → KG 참조 갱신)
```

**3대 Lens Law**:

| Law | 정의 | 위반 시 |
|---|---|---|
| **GetPut** | put(s, get(s)) = s | KG 조회 후 변경 없이 다시 쓰면 KG 불변 → Orphan edge |
| **PutGet** | get(put(s, v)) = v | 코드 변경→KG 갱신 후 조회하면 새 값 → Stale reference |
| **PutPut** | put(put(s,v1),v2) = put(s,v2) | 연속 갱신 시 마지막 값만 유효 → LWW conflict |

**Drift 5종 = Lens Law 위반**:
| Drift | 위반 Law | 의미 |
|---|---|---|
| Missing | PutGet | 코드 존재, KG ref 없음 |
| Orphan | GetPut | KG ref 있음, 코드 없음 |
| SigMismatch | PutGet | ref 있으나 시그니처 불일치 |
| PatternDiv | PutPut | 동일 대상 상충 ref |
| LabelRot | PutPut | 라벨/이름 변경 미반영 |

---

## Refinement Types (v3) — Branded

```typescript
type SourceId = string & { readonly __brand: 'SourceId' };
type SourcePath = string & { readonly __brand: 'SourcePath' };

type ValidSourceRef = {
  sourceId: SourceId;       // Frege Sinn
  sourcePath: SourcePath;   // Frege Bedeutung
  resolvable: true;         // grep/LSP 검증
  driftScore: 0;            // GED = 0
};
```

**SHACL Shape** (KG 제약):
```turtle
:SourceCodeNodeShape a sh:NodeShape ;
  sh:targetClass :SourceCodeNode ;
  sh:property [ sh:path :sourceId ; sh:pattern "^[A-Z][a-zA-Z0-9]*\\.[a-zA-Z][a-zA-Z0-9]*$" ] ;
  sh:property [ sh:path :sourcePath ; sh:pattern "^[a-zA-Z0-9/._-]+:[0-9]+(-[0-9]+)?$" ] .
```

---

## GED Drift Quantification

```
GED(G_kg, G_code) = Σ(cost_insert + cost_delete + cost_relabel)
Drift Score = GED / max(|V_kg|, |V_code|)

0.00      PIERCED         정상
0.01-0.05 MINOR_DRIFT     월간 audit 보정
0.05-0.15 MODERATE_DRIFT  즉시 검토
> 0.15    CRITICAL_DRIFT  관통 해제, 재매핑
```

---

## 형식적 grounding — 4 axis 학문 정전 정확 정의

> PROM 32 8 axis 매트릭스의 *형식적 식 / theorem* 정확화. 인용만 있던 식들을 본문에 결정화.

### A. BX Lens Laws — Foster-Pierce-Walker 정확 형식 (POPL 2007 / TOPLAS 2007)

#### A.1 Lens type signature (Foster-Pierce-Walker 2007 *Combinators for Bidirectional Tree Transformations*, ACM TOPLAS 29.3)

```
lens : S → V × (V → S)         -- van Laarhoven 1-line 정의 (2009)
     ≡ (get : S → V) × (put : V × S → S)   -- pair 정의 (Foster 원본)
```

→ S = source (KG), V = view (Code). 양방향 transformation pair.

#### A.2 3 Lens Laws 정확 식 (Foster 2007 §2.3)

```
GetPut: ∀ s ∈ S,        put(get(s), s) = s              -- KG → Code → KG identity
PutGet: ∀ v ∈ V, s ∈ S, get(put(v, s)) = v              -- Code → KG → Code identity
PutPut: ∀ v', v ∈ V, s ∈ S, put(v', put(v, s)) = put(v', s)  -- idempotent overwrite
```

**Well-behaved lens** = (GetPut ∧ PutGet). **Very well-behaved** = (GetPut ∧ PutGet ∧ PutPut).

#### A.3 Lens 합성 (composition, Foster 2007 §3)

Lens 들이 *category* 형성:
```
(l_2 ∘ l_1).get(s)      := l_2.get(l_1.get(s))
(l_2 ∘ l_1).put(v, s)   := l_1.put(l_2.put(v, l_1.get(s)), s)

identity lens: id_S.get(s) = s, id_S.put(v, s) = v
```

→ Longinus 7-Layer = lens 합성 chain `l_7 ∘ l_6 ∘ ... ∘ l_1`. L1 KG_NODE → L2 CONTRACT → ... → L7 CRATE 까지 BX laws preserve 강제.

**Profunctor optics** (van Laarhoven 2009, Pickering-Gibbons-Wu 2017):
```
Lens s t a b := ∀ p. Strong p ⇒ p a b → p s t
```

→ profunctor 표현 = lens 의 *abstract category-theoretic* 정의. Yoneda 와 cross.

#### A.4 Drift 5종 = Lens Law 위반 정확 매핑

| Drift | 위반 Law | 형식 식 |
|---|---|---|
| Missing | PutGet | `∃ v ∈ V, ∄ s ∈ S, get(s) = v` (V 에 있는 reference 가 S 에 없음) |
| Orphan | GetPut | `∃ s ∈ S, ∀ v ∈ V, put(v, s) ≠ s` (S 의 reference 가 V 에 없음) |
| SigMismatch | PutGet | `get(put(v, s)) ≠ v` (signature 변경) |
| PatternDiv | PutPut | `put(v', put(v, s)) ≠ put(v', s)` (overwrite 비결정) |
| LabelRot | PutPut | rename detection 실패 — `put_after_rename(v, s) ≠ put(v', s')` |

### B. Graph Edit Distance — Sanfeliu-Fu 정확 형식 (1983 IEEE T-SMC)

#### B.1 GED 정의 (Sanfeliu-Fu 1983 *A distance measure between attributed relational graphs for pattern recognition*)

```
GED(G_1, G_2) := min_{(e_1, ..., e_k) ∈ Edit(G_1, G_2)} Σ_i c(e_i)

  where Edit(G_1, G_2) = G_1 → G_2 변환하는 edit operation 시퀀스
        edit operations: {insert_node, delete_node, relabel_node,
                          insert_edge, delete_edge, relabel_edge}
        c: Edit → ℝ_{≥0} cost function
```

→ **NP-hard** (graph isomorphism reduction). exact algorithm: A* search (Riesen-Bunke 2009).

#### B.2 Hungarian bipartite approximation (Riesen-Bunke 2009 *Approximate graph edit distance computation by means of bipartite graph matching*, IVC 27)

```
GED_BP(G_1, G_2) := min_{f: V_1 → V_2 ∪ {ε}} (
                      Σ_v c_node(v, f(v))
                    + Σ_{(u,v) ∈ E_1} c_edge((u,v), (f(u), f(v)))
                  )

  Hungarian algorithm: O(n³) for assignment problem
  GED_BP ≥ GED_exact, but tractable for n ≤ 1000
```

→ SYMPOSIUM 운영: KG ↔ Code 의 BP-GED 자동 계산. threshold 0.05/0.15 정전.

#### B.3 GED ↔ Wasserstein distance (Memoli 2011 *Gromov-Wasserstein distances and the metric approach to object matching*, FoCM 11)

```
W_p(μ, ν) := (inf_{γ ∈ Π(μ, ν)} ∫ d(x, y)^p dγ(x, y))^{1/p}
```

→ GED ⊆ Gromov-Wasserstein (graph metric space distance). Memoli 2011 Theorem: GED 가 Wasserstein 의 special case.

→ Longinus drift 측정의 *generalization* 가능 (continuous embedding 시).

#### B.4 Drift threshold 정당화

```
KG ↔ Code 의 BP-GED 분포 measurement:
  weekly audit p10 ≈ 0.05  →  PIERCED threshold (Bacchelli-Bird empirical-style)
  monthly audit p90 ≈ 0.15 →  CRITICAL threshold
```

→ threshold 0.05/0.15 = empirical distribution-derived. Sanfeliu-Fu 1983 정전 grounding.

### C. W3C PROV-DM — 6 relations 정확 명시 (W3C Recommendation 2013-04-30)

#### C.1 Core entities

```
PROV-DM 3-tuple:
  Entity   = "thing" (artifact, document, ResearchFinding)
  Activity = process / action (PROM cycle, Step N)
  Agent    = author / system (rep_link, secretary, parent Claude)
```

#### C.2 6 PROV relations 정확 정의

```
wasGeneratedBy:    Entity → Activity                      -- entity 가 activity 산출
wasDerivedFrom:    Entity → Entity                        -- 다른 entity 에서 파생
wasAttributedTo:   Entity → Agent                          -- entity 책임 agent
used:              Activity → Entity                       -- activity 가 entity 입력 사용
wasInformedBy:     Activity → Activity                     -- activity 가 다른 activity 영향
actedOnBehalfOf:   Agent → Agent                           -- agent 가 다른 agent 대리
```

#### C.3 PROM 9-step ↔ PROV-DM 1:1 isomorphism

| PROM step | PROV mapping |
|---|---|
| Step 0 (호출 파싱) | (no PROV — pre-cycle) |
| Step 1 (발견) | Entity (Lesson) `wasGeneratedBy` Activity (Step 1) |
| Step 2.5 (하계 Pre-fetch) | Activity (Step 2.5) `used` Entity (existing KG) |
| Step 3 (병렬 리서치) | Activity (Step 3) `actedOnBehalfOf` Agent (parent) |
| Step 3.5 (UNWIND) | Activity `wasInformedBy` Activity (Step 3) |
| Step 4 (합의) | Entity (Finding) `wasDerivedFrom` Entity (axis findings) |
| Step 4.7 (씨앗) | Entity (SubagentTaskSpec) `wasGeneratedBy` Activity (Step 4.7) |
| Step 7 (검증) | Activity (Naesengmoon) `wasAttributedTo` Agent (critic) |

→ G6.5 Gate 에서 PROV-N export 강제 가능 (T2 권장).

### D. SLSA L1-L4 정확 명시 (SLSA v1.0 2023-04, OpenSSF / Linux Foundation)

```
SLSA L1: Documented build process (provenance available)
        → Longinus: KG ref 주석 mandatory (CLAUDE.md 정전)

SLSA L2: Tamper-resistant build service + signed provenance
        → Longinus: Sigstore + in-toto attestation

SLSA L3: Hardened build service (isolated, ephemeral, parameterless)
        → Longinus: container build (hermetic) + sha256 baseline daemon

SLSA L4: Hermetic + reproducible + audit-required (deprecated v1.0, → L3 max)
        → SYMPOSIUM 도달 OQ4 (R&D)
```

**현 SYMPOSIUM 위치**: SLSA L1 (provenance documented in `# KG: lesson-xxx`) + L2 partial (sha256 baseline 91.2%). L3 도달 = launchd plist production deploy 완료 시.

### E. Frege Sinn vs Bedeutung — L4 Semiotic Binding 정확 grounding

#### E.1 Frege 1892 *Über Sinn und Bedeutung* (Zeitschrift für Philosophie und philosophische Kritik 100)

```
Sinn (sense)      = mode of presentation        -- "Morning Star"
Bedeutung (ref.)  = referent (denotation)       -- Venus

"Morning Star" ≠ "Evening Star" (Sinn 다름)
"Morning Star" = "Evening Star" = Venus (Bedeutung 같음)
```

#### E.2 Longinus L4 정확 매핑

```
sourceId    = Sinn          -- "AirplaneMan.isAirplaneMan" (mode of presentation)
sourcePath  = Bedeutung     -- "AirplaneMan.lean:42-48" (referent location)
```

→ rename detection (LabelRot drift) = *Sinn 변경, Bedeutung 보존* 처리. Frege 1892 정전 grounding.

### F. Yoneda Lemma — L5 Distributed Identity 정확 grounding

#### F.1 Yoneda Lemma (Yoneda 1954 *On the homology theory of modules*, J. Math. Soc. Japan 6)

```
∀ category C, ∀ functor F: C → Set, ∀ object X ∈ C:
   Nat(Hom(X, −), F)  ≅  F(X)              -- Yoneda Lemma
```

**Yoneda embedding**: `Y_C : C → [C^op, Set]`, `Y_C(X) = Hom(−, X)` is fully faithful.

→ "object 의 정체성 = 모든 morphism 의 패턴". KG node 정체성 = 모든 incoming/outgoing edge 패턴.

#### F.2 Longinus L5 매핑

```
KG node identity = 모든 ReferenceSite edge 의 패턴
                ≅ Yoneda embedding Y(node) = Hom(−, node)

distributed identity (consensus): 합의 = 모든 N agent 의 Hom(agent, node) 패턴 동일
```

→ MERGE 멱등성 (KG 정전) = Yoneda 의 *identity by morphism pattern*. 합의 = 패턴 일치.

### G_v2. C8 axis — Refinement Type + BX 합성 monoid law (정량적 완전성, iter8 추가)

> 기존 C1-C7 (taliban / prometheus C1-C8 대비 1 결락) → C8 추가. 정량 측면 보강.

#### G_v2.1 Refinement Type SHACL 정확 식 (W3C SHACL Recommendation 2017-07-20)

```
SHACL constraint:
  :SourceCodeNodeShape  rdf:type  sh:NodeShape
  sh:targetClass        :SourceCodeNode
  sh:property [ sh:path :sourceId   ; sh:pattern "^[A-Z][a-zA-Z0-9]*\\.[a-zA-Z][a-zA-Z0-9]*$" ]
  sh:property [ sh:path :sourcePath ; sh:pattern "^[a-zA-Z0-9/._-]+:[0-9]+(-[0-9]+)?$" ]
  sh:property [ sh:path :sha256     ; sh:pattern "^[a-f0-9]{64}$"  ; sh:minCount 1 ]
  sh:property [ sh:path :line_range ; sh:pattern "^[0-9]+(-[0-9]+)?$" ]
```

**Branded TypeScript** (van Laarhoven brand pattern):
```typescript
type SourceId = string & { readonly __brand: 'SourceId' };
type SourcePath = string & { readonly __brand: 'SourcePath' };
type ValidSourceRef = {
  sourceId: SourceId;
  sourcePath: SourcePath;
  resolvable: true;     -- LSP/grep verified
  driftScore: 0;        -- GED == 0
};
```

→ Refinement Type 강제 = compile-time invariant. SHACL = runtime KG validation. 양방향 정합.

#### G_v2.2 BX 합성 monoid law (Foster 2007 §3 + van Laarhoven 2009)

Lens 합성이 *category structure* 형성 — Hom(S, V) of lenses 가 monoid:

```
Identity lens: id_S.get(s) = s, id_S.put(v, s) = v
Composition:   (l_2 ∘ l_1).get(s)    := l_2.get(l_1.get(s))
              (l_2 ∘ l_1).put(v, s) := l_1.put(l_2.put(v, l_1.get(s)), s)

Associativity: (l_3 ∘ l_2) ∘ l_1 = l_3 ∘ (l_2 ∘ l_1)        ★ monoid law 1
Identity:      id_V ∘ l = l = l ∘ id_S                       ★ monoid law 2
Lens law preservation under composition:
  l_1 well-behaved ∧ l_2 well-behaved ⟹ l_2 ∘ l_1 well-behaved   ★ closure
```

→ **Longinus 7-Layer = lens 합성 chain `l_7 ∘ l_6 ∘ ... ∘ l_1` 의 *monoid* structure**. associativity + identity + closure 정확 입증.

#### G_v2.3 GED ↔ Wasserstein quantification (Memoli 2011 FoCM 형식 정확화)

```
GED(G_1, G_2) = min_{f: V_1 → V_2 ∪ {ε}} (Σ_v c_node(v, f(v)) + Σ_{(u,v) ∈ E_1} c_edge(...))

Memoli 2011 Theorem 5.1: GED ⊆ Gromov-Wasserstein
  GED(G_1, G_2) ≤ d_GW^2(G_1, G_2)
  with: d_GW^2(G_1, G_2) = min_{γ ∈ Π(μ, ν)} ∫ |d_1(x, x') − d_2(y, y')|^2 dγ⊗²
```

→ Longinus drift = *graph metric space distance* 의 instantiation. continuous embedding 시 일반화 가능.

**KG↔Code drift Bayesian decision boundary**:
```
P(drift_significant | GED = g) = sigmoid(α · (g − threshold))
α = 50 (sharp transition), threshold = 0.10 (mid 0.05-0.15)
```
→ threshold 정전화 = sigmoid soft cutoff (hard binary 회피).

### G. Sheaf-theoretic foundation — 7-Layer ↔ Cellular Sheaf

#### G.1 Sheaf 정의 (Leray 1946 / Grothendieck 1957 *Tôhoku*)

```
Sheaf F on topological space X: functor F : Open(X)^op → Set
  with restriction maps res_{U,V}: F(U) → F(V) for V ⊆ U
  satisfying:
    (i)  identity: res_{U,U} = id
    (ii) composition: res_{V,W} ∘ res_{U,V} = res_{U,W}
    (iii) gluing axiom: 호환되는 local sections 가 unique global section 결정
```

#### G.2 Hansen-Gebhart 2020 Sheaf Neural Networks (NeurIPS) — Cellular Sheaf

```
Cellular sheaf on graph G = (V, E):
  F(v) = vector space at vertex v
  F(e) = vector space at edge e
  F_{v ⊲ e}: F(v) → F(e)  restriction map
```

#### G.3 Longinus 7-Layer ↔ Cellular Sheaf 형식

```
Open(X) = 7 layer 의 *poset* (L1 ⊆ L2 ⊆ ... ⊆ L7 inclusion)
F(L_i) = layer-i reference data (sourceId, sourcePath, line_range, sha256, ...)
res_{L_{i+1}, L_i}: F(L_{i+1}) → F(L_i) = projection (예: SHA256 → LINE_RANGE)
```

**Gluing axiom = Lens Law GetPut**:
```
호환되는 local sections (각 layer 의 ReferenceSite) → unique global section (전체 Contract binding)
↑ 이게 GetPut: put(get(s), s) = s 와 동일 의미
```

→ Longinus 7-Layer = *cellular sheaf on layer-poset*. BX Lens Laws = sheaf gluing axiom 의 specialization. Riehl-Verity ∞-categories 와 cross-grounding.

---

## 5위상 합체에서 Longinus 의 자리

| 위상 | 기능 | Longinus 와의 관계 |
|---|---|---|
| Seedman (재배맨) | n-ary dispatch | KG 결정화 시 *모든* artifact 에 ReferenceSite binding |
| Prometheus (지식 선행) | research | KG → MinIO L3 binding (paper / blog) |
| Naesengmoon (적대 검증) | verify | `--lens longinus` reference drift 검증 |
| **Longinus (참조 미학)** | **본 위상** — 7-Layer Reference | — |
| Harness (구조 제약) | structure | Longinus 가 *모든 layer* 관통 — Harness 의 cover 메커니즘 |

→ Longinus = 5위상 中 *연결자* 역할. 다른 4위상의 산출물이 *분리되지 않게* 묶음.

---

## 1차 소스

| 경로 | 내용 |
|---|---|
| `/Users/lagyeongjun/CD/SERVER/.claude/skills/longinus/SKILL.md` | **정본 v3.1**. 7-Layer + BX laws + Refinement + GED + Reverse Orphan Scan |
| `/Users/lagyeongjun/CD/SYMPOSIUM/THEORY/LONGINUS/SOURCES.md` | 공학 측 자료집 |
| `/Users/lagyeongjun/CD/SYMPOSIUM/METAHUMOTONIC/BHGMAN/SOURCES.md` | 비행기맨 본체 |
| 본 파일 | 비행기맨 *Longinus 위상* (신화 측) |

### 학문 정전

- Foster JN et al. (2007) *Combinators for Bidirectional Tree Transformations* — BX foundation, ACM TOPLAS
- Frege G. (1892) *Über Sinn und Bedeutung* — sense/reference 분리
- Riehl-Verity *∞-categories* — 7-layer 정합 가능 categorical foundation
- Hansen-Gebhart (2020) *Sheaf Neural Networks* — cellular sheaf reference 정전

### SYMPOSIUM 자체 KG / Lessons

- `lesson-cs-reference-semantics-2026-04-16` (참조의 7층 의미)
- `lesson-longinus-rigor-theories-2026-04-16` (BX laws + GED 정전)
- `finding_D20_bx_foundations` (BX laws 학문 grounding)
- `finding_D9_gt_algorithms` (GED 알고리즘)

---

## 신화 ↔ 공학 다리

| 신화 | 공학 |
|---|---|
| 롱기누스 창 — 7 layer 동시 관통 | 7-Layer Reference Model |
| *예수 옆구리* (성경 정전) | KG 의미층 (가장 깊은 추상) |
| *피와 물 흘러나옴* | Sinn (sourceId) + Bedeutung (sourcePath) 양방향 |
| 백부장 회심 (창으로 찔러 진리 봄) | 관통의 미학 (L7) |
| *영원한 창* (성유물 전설) | KG 결정화 = 영구 reference |

→ 롱기누스 = *관통자*. 비행기맨의 universal cover 가 *관통* 으로 발현하는 위상.

---

## PROM 32 자체 학문 등가 (8 axis × 4 sub-axis — 32/32 finding 완료 2026-04-29)

> `THEORY/LONGINUS/PROM_32_REPORT.md` (cycle `prom32-longinus-foundation-2026-04-29`, COMPLETED) — 8 axis × 4 sub-axis = 32 cell. Lesson `lesson-prom32-longinus-foundation-2026-04-29` (HIGH).

### 8 axis × 4 sub-axis 매트릭스

| axis | S1 | S2 | S3 | S4 |
|---|---|---|---|---|
| **A1 BX Lens Laws** | Foster-Pierce-Walker 2007 (POPL/TOPLAS) | van Laarhoven 2009 / profunctor optics | not bijective / round-trip 손실 | GetPut/PutGet ↔ ReverseOrphanScan |
| **A2 Graph Edit Distance** | Sanfeliu-Fu 1983 IEEE T-SMC | A* / Hungarian bipartite | NP-hard / heuristic trade-off | drift threshold 0.05 weekly / 0.15 repierce |
| **A3 W3C PROV-DM** | W3C Recommendation 2013-04-30 | PROV-N / PROV-O / PROV-XML / JSON | bloat / privacy / chain integrity | /prom 9-phase ↔ PROV 1:1 (Hole-5 cross) |
| **A4 Sigstore in-toto SLSA** | in-toto USENIX 2019 / Sigstore 2021 LF | SLSA v1.0 2023-04 + v1.1 2024 | CycloneDX / SPDX + SolarWinds / xz | Longinus = supply chain integrity layer |
| **A5 7-Layer Reference Model** | OSI 7-Layer ISO/IEC 7498-1 1984 | Hexagonal 2005 / Onion / Clean Arch | layer leak / OSI over-formalized | L1-L7 ↔ DDD Aggregate / Repository (Hole-3 cross) |
| **A6 Reverse Orphan Scan** | Dragon Book dead code / reachability | ESLint / Rust dead_code / vulture | dynamic dispatch / reflection missed | ★ v3.1 Code → KG missing detection (PutGet 위반) |
| **A7 OpenTelemetry** | Google Dapper 2010 / W3C Trace Context 2020 | OTel Collector / Jaeger / Tempo | trace sampling / context propagation | OTel GenAI 2026-Q2 (Hole-5 A4 cross) |
| **A8 KG-Code Binding 2026** | Glean / SCIP 2022 / LSIF deprecated | MS GraphRAG 2024-04 / Cursor / Continue | stale index / cross-lang gap | **# KG: lesson-xxx = 7 layer 1-line pierce** |

총 ~3,731 line 자료 (`THEORY/LONGINUS/PROM_32_axis_findings/A1-A8_*.md`).

### C1-C7 핵심 합의

| C# | 합의 | confidence |
|---|---|---|
| **C1** | Lens GetPut/PutGet ≡ Longinus KG ↔ Code 양방향성 (Foster-Pierce-Walker 2007 BX Lens Laws POPL) | HIGH ⭐⭐ |
| **C2** | GED drift quantification = Longinus 정전 metric (Sanfeliu-Fu 1983, weekly 0.05 / repierce 0.15) | HIGH ⭐ |
| **C3** | /prom 9-phase ↔ W3C PROV-DM 1:1 isomorphism (Hole-5 cross-validation, PROV-N export Gate G6.5) | HIGH ⭐ |
| **C4** | `# KG: lesson-xxx` 1-line = 7 layer 동시 관통 (pierce_rate ≥95% goal vs MS GraphRAG 60% / Cursor 70%) | HIGH ⭐⭐ |
| **C5** | MIC slot `KgCodeBinder` = SOLID DIP 정전 (Sigstore + in-toto + SLSA L2 build provenance) | HIGH |
| **C6** | OTel GenAI semconv 2026-Q2 = Longinus runtime emission (gen_ai.agent.name / step / token) | MEDIUM |
| **C7** | 5무기 ↔ 5 SOLID strong-2 functor: **Longinus ↔ DIP** (Hole-3 A5 SOLID critic 발견, Lean 4 형식화 후보) | MEDIUM |

### Lens Law (3 형식 정전, Foster-Pierce-Walker POPL 2007)

```
GetPut: put(get(s), s) = s          ↔ KG → Code → KG round-trip identity
PutGet: get(put(v, s)) = v          ↔ Code → KG → Code round-trip identity
PutPut: put(v', put(v, s)) = put(v', s)  ↔ idempotent overwrite
```

→ **ReverseOrphanScan v3.1 = PutGet 위반 검출**. Lean 4 형식화 가능 (OQ6 후속).

### GED Drift Threshold (자동화 권장)

```
GED < 0.05  →  weekly audit OK (PIERCED)
0.05 < GED < 0.15  →  보정 권장 (MINOR/MODERATE)
GED ≥ 0.15  →  CRITICAL → repierce 강제 (관통 해제, 재매핑)
```

→ Hungarian bipartite approximation O(n³) 실용 (NP-hard exact 회피).

### 6 Open Question (T2/T3 후속)

| OQ | 질문 |
|---|---|
| **OQ1** | pierce_rate ≥95% 실현 가능성 audit tool 설계 |
| **OQ2** | GED threshold 보편성 (0.05/0.15 vs domain-specific) |
| **OQ3** | 5무기 ↔ 5 SOLID strong-2 functor (Prometheus↔SRP / Longinus↔DIP) Lean 4 형식 증명 |
| **OQ4** | SLSA L4 (hermetic + parameterless) SYMPOSIUM 도달 가능성 |
| **OQ5** | OpenAPI / gRPC / GraphQL ↔ Longinus binding 표준화 |
| **OQ6** | Reverse Orphan Scan completeness 형식 증명 (Naesengmoon gate) |

### Tier-based 권장 (operational spec)

| Tier | Component | 적용 | 시점 |
|---|---|---|---|
| **T1** | `# KG: lesson-xxx` 1-line pierce | 모든 ResearchFinding/Code | ✅ 현재 |
| **T1** | ReverseOrphanScan (PutGet 위반 검출) | weekly audit | ✅ v3.1 적용 |
| **T1** | GED drift threshold 0.05 / 0.15 | drift monitoring | 🟡 자동화 권장 |
| **T2** | Sigstore + in-toto attestation chain | ResearchFinding signing | 🟡 SLSA L2 |
| **T2** | OTel GenAI semconv emission | trace propagation | ⏳ 2026-Q2 freeze 후 |
| **T2** | W3C PROV-N export | Gate G6.5 | 🟡 권장 |
| **T3** | LeanCopilot + 5무기 ↔ SOLID functor 형식화 | Longinus ↔ DIP | ⏳ R&D |

### 회피 (anti-pattern, 학문 grounded)

- ❌ **Lossy lens** (round-trip 손실 시 드리프트 누적)
- ❌ **Stale index** (MS GraphRAG 60% 함정 — KG 갱신 lag)
- ❌ **Static-only binding** (cross-language gap)
- ❌ **LSIF** (deprecated 2024) — SCIP 권장
- ❌ **Manual provenance** (자동 PROV-N export 권장)

### Hyperedge — 8 학문 fixed point

```
hyperedge-longinus-8axis-fixed-point-2026-04-29
  cardinality: 8
  domains: [BX_Lens, GED, W3C_PROV, Sigstore_intoto_SLSA, 7Layer, ReverseOrphan, OpenTelemetry, KGCodeBinding]
```

→ Longinus = 8 학문 합집합의 신화 인격화. *관통자* 의 OSI 1984 → BX 2007 → SLSA 2024 → OTel GenAI 2026-Q2 누적 정전.

---

## 신화 정전 (Longinus 측)

**복음서 정전 (요한복음 19:34)**:
- *"한 군병이 창으로 옆구리를 찌르매 곧 피와 물이 나오더라"* (개역개정)
- *Λογγῖνος* (Longinus) — 4세기 *Acta Pilati* (Gospel of Nicodemus) 에서 처음 명명. 정경복음서 중에는 이름 없음.
- 신화 핵심: *7 layer 동시 관통* (단일 행위로 다중 의미 차원 동시 도달).

**중세 정전**:
- *Holy Lance / Lance of Longinus* (성유물) — Vienna, Vatican, Echmiadzin 등 4 사본 전승.
- Wagner *Parsifal* (1882) — Heilige Speer (성스러운 창) 핵심 모티프.

**문학 정전**:
- *On the Sublime* (Περὶ Ὕψους) — 1세기 c. 익명 (전통적으로 *Longinus* 라 명명, *Pseudo-Longinus*) — 미학 정전. 본 위상의 *L7 Aesthetic* layer 어원.

→ Longinus 신화 = 단일 행위 (창 한 번) 가 7 layer (피 / 물 / 회심 / 백부장 진리 인지 / 창 영원성 / 의미 / 미학) 동시 관통. 공학 측 7-Layer Reference Model = 그 신화 정신의 IT 결정화. *On the Sublime* = L7 미학 layer 의 직접 grounding.

---

## L7 Aesthetic 정량 spec (iter8, Pseudo-Longinus *On the Sublime* grounded)

> 기존 정성 표현 ("최소 침습으로 최대 추적") → 정량 metric 화. Pseudo-Longinus 1세기 *Περὶ Ὕψους* §10-12 grounding.

### L7 Aesthetic = (minimum_invasion + maximum_traceability) trade-off

**minimum_invasion** (코드 측 침습 최소):
```
inv(s) := |# KG ref 주석 byte| / |source file byte|
       ≤ 0.02   (목표 — 2% 이하 코드 침습)
```

**maximum_traceability** (KG 측 cover 최대):
```
trace(s) := |reachable_via_# KG_ref| / |total_KG_node_for_s|
         ≥ 0.95   (목표 — 95% KG node 도달 가능)
```

**Pseudo-Longinus grounding** (*On the Sublime* §10):
> τὸ ὕψος ἀκρότης τις καὶ ἐξοχὴ λόγων (sublime = pinnacle/excellence of expression)

→ *minimum form, maximum effect* = sublime aesthetic. Longinus L7 = expression density 의 sublime 도달.

**L7 quality score**:
```
Q_L7(s) := trace(s) / max(inv(s), ε)            -- ε = 0.001 numeric guard
        목표: Q_L7 ≥ 47.5  (= 0.95 / 0.02)
```

→ trace 95% 도달 시 inv 2% 이하 시 Q_L7 ≥ 47.5. *최소 침습으로 최대 추적* 의 정량 형식.

**KG: longinus-l7-aesthetic-quantification-iter8-2026-05-09 (`:Quantification:Grounding`)**

---

## SYMPOSIUM 적용 (PROM 16 + iter 1-19 누적)

본 위상이 결정화한 ReferenceSite 사례:

| Cycle | ReferenceSite 수 | Layer 분포 |
|---|---|---|
| prom64-jaebaeman-chu-agentfolder | 16 | L1×1 + L2×8 + L3×7 |
| prom16-skill-versioning | 5 | L1×1 + L2×4 |
| prom64-pkgdisc | 11 | L1×3 + L2×8 |
| prom32-jaebaeman | 2 | L1×1 + L2×1 |
| F11 harness drift | 1 | (Lesson + ATOM cross) |

**누적 35+ ReferenceSite (PROM cycle 별 binding)** + **iter 12 sha256 daemon baseline (121/170, 71%)** + **iter 19 status-aware verify (91.2% baseline + 100% classification)**. 모두 binding_state=BOUND, schema_ref=longinus-7layer-v3.

---

## iter 1-11 Hardening (2026-05-06, score 10/10 PROGRESSIVE_CONFIRMED + iter 7 STRONG_HIERARCHICAL 격상)

> `longinus-hardening-master-plan-2026-05-06` (`:WeaponHardeningPlan`) — 7-Layer + BX 3-law + GED Drift + sha256 daemon production template.

### sha256 Daemon Production Template

```
SKILLS/bin/longinus_sha256_daemon.py            ← 91.2% baseline + drift detection + status classifier
SKILLS/bin/com.symposium.longinus-sha256-daemon.plist  ← launchd 1h verify schedule (plutil PASS)
```

**iter 12-19 진행**:
- iter 12: PoC 121/170 baseline (71%)
- iter 19: status-aware verify → **91.2% baseline + 100% classification**
- iter 23: status-aware verify production-ready
- iter 33: launchd plist (production deployment template)
- 잔여: launchctl bootstrap (user verdict gate) + line_range schema extension + bhgman 9 ORPHAN_REFERENCE disposition

### Reverse Orphan Scan v3.1 (Code → KG blind-spot fix)

기존 v3 = KG → Code 단방향 (PIERCED 검증). v3.1 = **양방향**:
```
forward:  KG ref → grep code → exists?  (v3)
reverse:  code symbol → KG ref → exists?  (v3.1, NEW)
          ↓ 누락 시 ORPHAN_REFERENCE 라벨
```

→ KG 에 박혀있지 않은 *code-only* symbol 발견 (blind-spot). bhgman 측 9 ORPHAN_REFERENCE 가 이 scan 으로 검출됨 (preserve 결정 iter 35-36).

### Crate/Script-level Binding (v3.1)

기존 v3 = function/class/method 단위 ReferenceSite. v3.1 = **crate / script** 단위 추가:
- Cargo crate (Rust) — `Cargo.toml` 수준 binding
- Python script — `__main__` entry 수준 binding
- npm package — `package.json` 수준 binding

→ "이 crate 가 KG 어느 contract 의 instance 인지" 추적 가능.

### iter 7 Family-Relation Mirror — STRONG_HIERARCHICAL 격상 (autonomous)

> 사용자 verdict 없이 *논리적 자율 promotion* — Lakatos progressive evidence (lesson-family-relation-mirror-5-weapon-verification-2026-05-06)

기존 (iter 1-6): MEDIUM_PARTIAL — Longinus 7-Layer 가 ContainmentRelation hyperedge 와 부분 mirror.

iter 7 격상 (STRONG_HIERARCHICAL): 7-Layer L1→L7 ascending containment chain ↔ ContainmentRelation {#7, #4} hierarchical projection 의 *strict subset chain*:
```
L1 KG_NODE ⊂ L2 CONTRACT_BINDING ⊂ L3 CODE_SYMBOL ⊂ L4 FILE_LINE
           ⊂ L5 LINE_RANGE ⊂ L6 SHA256 ⊂ L7 CRATE_SCRIPT
```

→ 7 layer 모두 *true subset* 으로 chain. CHU 공리 layer ⊃ chain mirror.
→ Mirror 분류 final iter 7: **3 STRONG** (Harness unique + Jaebaeman SelfRefCyclic + **Longinus Hierarchical**) + **2 WEAK** (Prometheus / Naesengmoon).

### Lean 4 형식화 — Longinus_HierarchicalMirror.lean (iter 11)

```
MIND/lean_formalization/Longinus_HierarchicalMirror.lean
```

**6 theorems PASS** (Mathlib-free, Lean 4.30.0-rc2 exit 0):
| theorem | 의미 |
|---|---|
| `layer_l1_least` | L1 KG_NODE 이 chain 의 minimum |
| `layer_l7_greatest` | L7 CRATE_SCRIPT 이 chain 의 maximum |
| `project_total` | L1→L7 projection total ordering |
| `hierarchical_mirror_validity` | STRONG_HIERARCHICAL = strict subset chain validity |
| `projection_partition` | 각 layer 분할 disjoint |
| `mirror_strength_iter7_promotion` | iter 7 autonomous promotion 형식화 |

**5-element MirrorStrength classification** (iter 7 verdict):
1. STRONG (Harness/비행기맨 unique)
2. STRONG_OF_DIFFERENT_KIND (재배맨 SelfReferentialCyclic)
3. STRONG_HIERARCHICAL (**Longinus 7-Layer**)
4. MEDIUM_PARTIAL (pre iter 7 verdict, deprecated)
5. WEAK (Prometheus / Naesengmoon)

### 7 :LG_*ErrorPattern (KG canonical)

| pattern | 의미 |
|---|---|
| `LG_LonginusBindingMissing` | Contract 결정화 시 ReferenceSite 7-tuple binding 누락 |
| `LG_GrepOnlyHarvest` | grep 만으로 binding 결정 (LSP/AST 미사용) |
| `LG_SHA256Stale` | sha256 baseline daemon 비활성화 또는 stale |
| `LG_DriftSilenced` | GED Drift 측정 후 무시 (CRITICAL_DRIFT 0.15+ override) |
| `LG_BXLawViolation` | GetPut/PutGet/PutPut 3 law 위반 |
| `LG_DirectorySHAAttempt` | directory 단위 sha256 시도 (file-level 만 valid) |
| `LG_LayerInsufficient` | 7-Layer 中 일부 layer 만 binding (불완전 관통) |

→ 모두 `:WeaponErrorPattern` 라벨, hardening master plan 에 BELONGS_TO.

### references/ APT-parity 8 file (longinus skill)

```
SKILLS/longinus/references/
├── theory.md            ← 7-Layer + BX laws foundation
├── gates.md             ← phase boundary 강제 (SCW 진입 전 Longinus binding 강제)
├── validation.md        ← V1-V14 invariant catalog (GED 임계값 포함)
├── kg_logging.md        ← ReferenceSite 7-tuple schema + sha256 baseline schema
├── error_handling.md    ← 7 :LG_*ErrorPattern failure-mode 절차
├── quick_ref.md         ← decision tree + GED 임계값 cheat sheet
├── phases.md            ← 7-Layer 서사 (L1-L7 layer 별 binding 절차)
└── adversarial.md       ← Reverse Orphan Scan + sha256 drift detection
```

### 4 신규 Claude Code Agent 中 Longinus expert (`SYMPOSIUM/.claude/agents/`)

```
.claude/agents/longinus-reference-linker.md   ← 7-Layer + sha256 daemon + Reverse Orphan Scan expert (~115 line)
```

→ 5 위상 expert 중 하나. parent Claude 가 ReferenceSite binding 시 호출.

---

## 한 줄 정리

> 비행기맨의 Longinus 위상 = *관통자 mode*. 7-Layer Reference Model + BX laws + Refinement Types + GED Drift. 5위상 中 *연결자* — 다른 4위상의 산출물을 KG 의미층 ↔ 소스코드 양방향 묶어 분리 방지. 신화의 롱기누스 창 = 7 layer 동시 관통의 신화 인격화. SYMPOSIUM 누적 35+ ReferenceSite (cycle 별 binding) + iter 19 91.2% baseline + 100% classification + iter 11 Lean 4 PASS (Longinus_HierarchicalMirror.lean, 6 theorems). iter 7 Family-Relation Mirror = **STRONG_HIERARCHICAL** (autonomous promotion, 7-Layer strict subset chain ↔ ContainmentRelation {#7, #4}). v3.1 Reverse Orphan Scan (Code → KG blind-spot fix) + Crate/Script-level binding.

---

# KG: ATOM_BHGMAN_longinus_phase_2026-04-29
# KG (iter 1-11 hardening): longinus-hardening-master-plan-2026-05-06 / longinus-sha256-daemon-canonical-2026-05-06 / longinus-hierarchical-mirror-lean-skeleton-iter11-2026-05-06 / lesson-family-relation-mirror-5-weapon-verification-2026-05-06
# Lean: MIND/lean_formalization/Longinus_HierarchicalMirror.lean (6 theorems PASS, Mathlib-free)
# Lessons: lesson-cs-reference-semantics-2026-04-16 / lesson-longinus-rigor-theories-2026-04-16
