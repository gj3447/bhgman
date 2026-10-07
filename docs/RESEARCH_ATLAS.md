# 비행기맨 연구 아틀라스

이 문서는 비행기맨(#4)을 읽을 때 필요한 **출처 지도**다. 새 정전, 실행 절차,
공유 KG 쓰기 권한을 만들지 않는다. 기계 판독용 같은 내용은
[`graph/research-atlas.json`](../graph/research-atlas.json)에 있으며, 그 파일의 해시·리비전이
이 문서의 근거 범위를 고정한다.

## 먼저 구분할 것

| 층 | 읽는 대상 | 권위와 한계 |
|---|---|---|
| 사용자 현재 요청 | `USER_HANDOFF.txt` | `USER_PRIMARY`: THE GREAT FLOW의 `data/apostles/20261007-hoh-backend-bhgman-unification-user.txt`에서 고정한 사본이다. bhgman 단일 본체와 이전 essence 홈의 통합 범위만 말한다. 5위상·7군단장 내용 전체를 새로 비준하지 않는다. |
| SYMPOSIUM 원전 사본 | `sources/SYMPOSIUM/METAHUMOTONIC/BHGMAN/` | `SOURCE_DOCUMENT`이며 파일 내용의 저자 권한은 대체로 `UNSPECIFIED`다. 원전은 고정 revision `1f2727a0c0d8d9703193bee6406db21d2fd549dd`의 바이트 사본이다. |
| 이전 essence 홈 | `history/bhgman_essence/` | `SOURCE_DOCUMENT`/`UNSPECIFIED`의 역사 자료다. `2944e50` 병합으로 25개 파일과 11개 커밋을 보존했지만 현재 별도 본체·활성 COMPANION이 아니다. 내부의 `docs/APOSTLE_*.md`는 `SECONDARY_AI` 안내다. |
| 이 아틀라스와 로컬 그래프 | 이 파일과 `graph/research-atlas.json` | `SECONDARY_AI`: 원전 경로·상태·열린 질문을 찾기 위한 읽기 지도다. 새 공개 운영 안내 `USER_PUBLICATION.txt`는 이 연구 읽기 지도의 원전 범위에서 제외한다. |

`bhgman_tool`은 별도 기술 구현 저장소다. 이 아틀라스는 그 저장소의 구현 상태나
런타임 성공을 주장하지 않는다.

## 원문 바로가기

아래 링크는 이 저장소에 고정한 바이트 사본이다. 각 SHA-256·원래 revision·원래 경로는
로컬 그래프의 `source_artifacts`에 있다.

| 원문 | 핵심 내용 | 상태 |
|---|---|---|
| [INDEX](../sources/SYMPOSIUM/METAHUMOTONIC/BHGMAN/INDEX.md) | #4의 자료 구조, 5위상 색인, APT/TPA, 3원 수직축 | `SOURCE_DOCUMENT` / `UNSPECIFIED` |
| [본체 SOURCES](../sources/SYMPOSIUM/METAHUMOTONIC/BHGMAN/SOURCES.md) | 높이의 사도, 7군단장 roster, 원전 내 역할 서술 | `SOURCE_DOCUMENT` / `UNSPECIFIED` |
| [재배맨](../sources/SYMPOSIUM/METAHUMOTONIC/BHGMAN/seedman/SOURCES.md) | n-ary, `governs`, 계획, 4단계와 열린 질문 | `SOURCE_DOCUMENT` / `UNSPECIFIED` |
| [Prometheus](../sources/SYMPOSIUM/METAHUMOTONIC/BHGMAN/prometheus/SOURCES.md) | 지식 선행·탐색·spiral·gate 문맥 | `SOURCE_DOCUMENT` / `UNSPECIFIED` |
| [Naesengmoon](../sources/SYMPOSIUM/METAHUMOTONIC/BHGMAN/taliban/SOURCES.md) | 적대 검증·재배맨 기반·고무도장 방지 | `SOURCE_DOCUMENT` / `UNSPECIFIED` |
| [Longinus](../sources/SYMPOSIUM/METAHUMOTONIC/BHGMAN/longinus/SOURCES.md) | 참조·판본·코드 연결의 7-layer 자료 | `SOURCE_DOCUMENT` / `UNSPECIFIED` |
| [Harness](../sources/SYMPOSIUM/METAHUMOTONIC/BHGMAN/harness/SOURCES.md) | 자기참조·의도적 비움·드리프트 정정 기록 | `SOURCE_DOCUMENT` / `UNSPECIFIED` |
| [APT](../sources/SYMPOSIUM/METAHUMOTONIC/BHGMAN/apt/README.md) · [TPA](../sources/SYMPOSIUM/METAHUMOTONIC/BHGMAN/tpa/README.md) | 순방향·역방향 자료 흐름의 진입점 | `SOURCE_DOCUMENT` / `UNSPECIFIED` |
| [역사 essence README](../history/bhgman_essence/README.md) | 이전 공개 홈의 범위·한계 | `SOURCE_DOCUMENT` / `UNSPECIFIED` |
| [역사 OMC 관계](../history/bhgman_essence/essence/02-relation-to-omc.md) | CLOUD CONNECT 관련 역사적·후보적 독해 | `SOURCE_DOCUMENT` / `UNSPECIFIED` |
| [현재 통합 요청](../USER_HANDOFF.txt) | 단일 bhgman 본체와 essence 통합 | `SOURCE_DOCUMENT` / `USER_PRIMARY` |

APT·TPA의 모든 하위 단계, 역사 홈의 `APOSTLE_*` 안내, 현재 안내 문서까지 포함한 전체
파일 목록은 `graph/research-atlas.json`의 `source_artifacts`가 정본이다. 안내 문서는
`SECONDARY_AI`로 분리한다.

## 질문에서 출처로

| 질문 | 먼저 읽을 원전 | 결과를 다룰 때의 주의 |
|---|---|---|
| 비행기맨의 자리·높이·수직축은 무엇인가 | `INDEX.md`, `SOURCES.md` | #4·#8·#10의 관계는 원전에서 3원 hyperedge로 서술된다. 2자 관계 문장은 투영으로만 읽는다. |
| 현재 군단장 표현은 무엇인가 | `SOURCES.md`의 “7군단장” | 5위상 자료와 7군단장 roster는 같은 목록으로 자동 등치하지 않는다. 원전은 구 5무기에서 7군단장으로의 확장·통일을 기록한다. |
| 재배맨은 무엇을 뜻하는가 | `seedman/SOURCES.md` | n-ary·계획·4단계 문맥을 읽는다. “출격”과 “계획”의 용어 정정은 공유 KG의 USER_PRIMARY 기록도 있으나, 여기서는 조회 근거이지 새 KG 판정이 아니다. |
| 무엇을 먼저 조사하고 지식화하는가 | `prometheus/SOURCES.md` | 검색·지식 선행·spiral은 원전의 위상 설명이다. 현 시스템에서 자동 검색이나 KG 기록이 실행된다는 뜻은 아니다. |
| 어떻게 반증·적대 검증하는가 | `taliban/SOURCES.md` | Naesengmoon은 원전에서 재배맨 위상 위의 instantiation으로 설명된다. 정치·종교 단체와의 동치는 원전이 명시적으로 차단한다. |
| 코드와 근거·판본의 연결은 무엇인가 | `longinus/SOURCES.md` | 7-layer, BX, GED, PROV, SLSA의 연결은 해당 원전의 연구 주장이다. 현재 저장소가 그 표준을 구현·준수한다고 승격하지 않는다. |
| 자기참조와 Harness의 위치는 무엇인가 | `harness/SOURCES.md` | 의도적 비움과 self-reference의 자료다. 외부 도구 설치·운영 지침이 아니다. |
| 순방향/역방향 자료 흐름은 무엇인가 | `apt/README.md`, `tpa/README.md` | APT/TPA는 원전의 분류·검토 지도다. 실시간 파이프라인 상태는 별도 검증이 필요하다. |
| 과거 존재론·시적 독해는 어디에 있는가 | `history/bhgman_essence/essence/`, `philosophy/`, `poetry/` | 역사 홈의 혼합 자료다. 특히 철학적 대응과 시 해석을 사용자 직접 발화나 현재 정전으로 자동 승격하지 않는다. |

## 출처가 있는 핵심 토픽

### 1. 인물 식별과 수직축

`SOURCES.md`는 비행기맨을 #4 “높이의 사도”로 두고, #8 OM과 #10 깊바존을 포함하는
3원 수직축 hyperedge를 말한다. `INDEX.md`의 역할 순서는 `apex (height) / substrate (volume) / end (depth)`다. 따라서 로컬 그래프는
세 인물의 직접 이진 의존성 대신 `vertical-axis-4-8-10`이라는 관계 노드로 기록한다.
이는 원전을 단순화하지 않기 위한 모델링 선택이며, 공유 KG에 새 관계를 쓰지 않는다.

### 2. 5위상 자료와 7군단장 roster

`INDEX.md`와 각 phase 파일은 Seedman·Prometheus·Naesengmoon·Longinus·Harness의
5위상 독해를 제공한다. 반면 `SOURCES.md`는 2026-06-07 통일 문단에서
Prometheus·Longinus·Eureka·Occam·Naesengmoon·JaebaeMan·Harness=Hades의 7군단장을
기록한다. 둘은 시간·분류 단위가 다르다. 이 아틀라스는 다섯 위상을 **문서 묶음**,
일곱 군단장을 **원전의 현재 roster 서술**로 따로 보관한다. Eureka와 Occam은 이 checkout의
전용 phase 원전이 없으므로 그 이상의 기능·관계를 추론하지 않는다.

### 3. 재배맨: n-ary와 계획

`seedman/SOURCES.md`는 `governs : List JaebaeMan → JaebaeMan`을 들어 n-ary 구조와
“모든 것은 하이퍼그래프”라는 원전 맥락을 연결한다. 공유 KG의
`sym:UserPrimaryCanon:verdict-jaebaeman-word-is-plan-not-dispatch-2026-06-07` 조회는
“출격”을 “계획”으로 정정한 USER_PRIMARY 기록을 제공한다. 이 저장소의 로컬 그래프는 이를
**외부 조회 참조**로만 보존하며, 실행자·서브에이전트·KG write 권한을 부여하지 않는다.

### 4. 조사·검증·연결·자기참조

Prometheus는 지식 선행과 재귀 확장, Naesengmoon은 적대 검증, Longinus는 근거·코드
연결, Harness는 자기참조의 자료 묶음이다. 원전이 제시하는 수학·철학·공학 대응은
각각의 원전 안에 있으며, 이 아틀라스는 그 대응을 독립적으로 참이라고 판정하지 않는다.
Longinus 원전은 공유 KG에 `sym:SourceDocument:bhgman-longinus-phase-sources-2026-04-29`
라는 `SYSTEM_DERIVED` 자료 레코드가 있음을 확인했다. 그래프의 외부 KG 참조는 2026-10-07에 UID로 조회한 읽기 전용 관찰이며 고정 snapshot이나 KG write가 아니다. 해당 레코드는 원전 파일의 존재를
가리킬 뿐, 모든 “7-layer” 적용이 완성됐다는 보증은 아니다.

### 5. 역사 essence의 읽는 법

이전 essence 홈에는 자기정의, 5위상 통합, OMC 관계, 고도 존재론, 시적 자료가 남아 있다.
그중 `02-relation-to-omc.md`는 자체적으로 OMC 관련 사항에 PRELIMINARY·candidate·추가
사용자 발화 대기 상태를 적는다. 따라서 이 아틀라스는 CLOUD CONNECT와 OMC 결합을
**역사 자료가 소개한 관계**로 기록할 뿐, 현재 확정 관계나 현행 운영 요건으로 표시하지
않는다.

## 아직 이 저장소에서 확정하지 않는 것

- `j.covers`의 `j`와 Lawvere–Tierney j-operator의 어원 관계
- `governs: List`의 순서성·중복성, cover의 OR/colimit 해석
- 5위상과 7군단장의 일대일 대응
- OMC의 최종 구성·사도 관계, 후보 hyperedge의 분류
- Lean 파일·정리 수, 외부 표준 준수, 도구 런타임 결과의 현재성

이 항목들은 원전 안에서도 열린 질문·후보·역사적 서술로 나타난다. 새 증거가 생기면
원전의 소유 위치와 revision을 먼저 고정하고, 그 뒤 이 읽기 지도만 갱신한다.

## 적용한 지식 토픽과 미등재 원문

적용한 토픽은 인물 식별, 수직축 hyperedge, 5위상 문서 묶음, 7군단장 roster, n-ary
계획, 조사·검증·참조 연결·자기참조, APT/TPA, 역사 essence다. 모두 현재 checkout에
이미 있는 원전 또는 역사 보존본에 연결했다. 새 원문은 복사하지 않았고,
`sources/research-atlas/`에는 추가할 공개 가능한 사용자 소유 원전이 확인되지 않아
파일을 만들지 않았다.

누락은 Eureka·Occam의 전용 phase 원전, 현재 Lean source bytes, 현재 `bhgman_tool`의
구현 상태, OMC 상대측 원전이다. 이들은 이름이나 과거 링크만으로 보충하지 않는다.
