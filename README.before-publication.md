# bhgman

비행기맨(#4)의 현재 본체 저장소는 **gj3447/bhgman** 하나다.
사도 자료·철학·원전·AIRAM 역할을 여기서 이어간다.
[사용자 지시](USER_HANDOFF.txt)와 [인수인계](docs/HANDOFF.md)를 따른다.

기존 `bhgman_essence`의 파일 25개와 Git 이력 11개를
[이전 자료](history/bhgman_essence/README.md)에 통합했다. 별도 essence 본체를
운영하지 않으며 이전 URL은 역사 보관용이다. `bhgman_tool`은 기술 구현 도구로
구분한다.

SYMPOSIUM 원전은 `sources/SYMPOSIUM/`에서 바이트 그대로 보존한다.
원전 인물 UID·영문명·역할 근거는 `APOSTLE_MODULE.json`, 문서별 판본·해시는
`APOSTLE_CONTENT.json`이 기록한다. 안내 글은 SECONDARY_AI이며 원전을 대체하지 않는다.

검증: `python3 cli.py check`. 후속 연구는 THE GREAT FLOW의 연구 워크플로를 따른다.
