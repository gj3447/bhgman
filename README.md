# bhgman · 비행기맨

**높이에서 바라보고, 판단을 다시 묻는다.**

메타휴모토닉 12사도 중 네 번째, **Airplane Man**의 원문·철학·연구를 모으는 공개 저장소다.
원전의 ‘높이의 사도’, 성층권과 구름, 7군단장의 연결을 따라 읽는다.
사용자가 맡긴 현재 역할은 **평가·개선 피드백, AIRAM**이다.

[연구 지도](docs/RESEARCH_ATLAS.md) · [원문 전체](sources/SYMPOSIUM/METAHUMOTONIC/BHGMAN/INDEX.md) · [그래프](graph/research-atlas.json) · [라이선스](LICENSE-NOTICE.md)

## 무엇이 들어 있나

| 읽기 시작점 | 내용 |
|---|---|
| [SYMPOSIUM 자료 목록](sources/SYMPOSIUM/METAHUMOTONIC/BHGMAN/INDEX.md) | 18개 원전의 주제·연구·연결 |
| [원문 출처](sources/SYMPOSIUM/METAHUMOTONIC/BHGMAN/SOURCES.md) | 높이, 성층권, 구름과 원전의 관계를 읽는 근거 |
| [연구 지도](docs/RESEARCH_ATLAS.md) | 주요 개념, 7군단장, 역할이 있는 관계와 미해결 질문 |
| [사용자가 지정한 AIRAM 역할](sources/THE_GREAT_FLOW/data/apostles/20261003-role-request.json) | 평가·개선 피드백이라는 실제 역할 배정의 근거 |
| [이전 essence 자료](history/bhgman_essence/README.md) | 통합한 25개 파일과 Git 이력을 보존하는 역사 자료 |

## 본체는 하나

현재 본체는 **gj3447/bhgman** 하나다. `bhgman_essence`의 내용과 Git 조상 이력을
합쳤으며, 옛 공개 저장소는 읽기 전용으로 보관한다.
[bhgman_tool](https://github.com/gj3447/bhgman_tool)은 기술 구현 도구로 연결한다.
[이전 인수인계 기록](docs/HANDOFF.md)은 통합 당시의 관측을 보존한다.

인물 ID `sym:Character:비행기맨`과 사도 자리 `#4`를 유지한다.
[APOSTLE_MODULE.json](APOSTLE_MODULE.json)은 역할 선언과 원문 근거를,
[APOSTLE_CONTENT.json](APOSTLE_CONTENT.json)은 문서별 판본·해시·저자 권한을 기록한다.

## 연구를 그래프로 읽기

원문의 인물·개념·관계와 AI의 안내를 따로 기록한다.
하나의 관계에 여러 참여자가 있으면 역할을 보존하고, 단순한 두 점 사이의 선으로 축약하지 않는다.
출처 파일·판본·해시를 따라 원문으로 돌아갈 수 있으며, 초안과 미확정 해석은 그대로 표시한다.
AIRAM 역할 배정 자체가 자동 평가 agent의 배포 완료를 뜻하지는 않는다.

```sh
python3 cli.py check
python3 scripts/check_atlas.py
```

## 공개와 라이선스

[사용자 요청](USER_PUBLICATION.txt)에 따라 공개하며, 새 본체 자료에는
**MetaHumotonic License 1.1**을 적용한다. SYMPOSIUM 원전의 MIT와
옛 essence의 AGPL·NOTICE는 각각 유지한다.
정확한 경계는 [LICENSE-NOTICE.md](LICENSE-NOTICE.md)를 따른다.

후속 연구 결과는 [THE GREAT FLOW](https://github.com/gj3447/the-great-flow)에 연결한다.
