# ST_course_registration
### - 프로그램 소개
- 수강신청 관련 3가지 기능을 제공하는 프로그램입니다.

### - 프로그램 기획 배경, 의도


### - 프로젝트 기간
- 2025.02.05 ~ 2025.02.07 (학교 1학기 수강신청 기간 / 실제 사용하면서 개발)


### - 프로그램 기능
1. 장바구니 목록 저장 (장바구니에 과목 있는 유저들 대상)
    - 기능 사용1: 수강페이지 열릴때 선착순
    - 기능 사용2: 페이지 열린 이후 과목 주울때 (여러 과목 한번에 신청 시도할 때)
2. 다수의 과목 반복 수강 신청
    - 기능 사용1: 수강페이지 열릴때 선착순
    - 기능 사용2: 페이지 열린 이후 여러 과목 주울때 (1-2 활용 어려울 시)
3. 현재 시간표 확인
    - 기능 사용: 현재 수강 중인 내 시간표를 확인하고 싶을때


### - 개발 환경 
    - windows 11
    - python 3.11.9
    - selenium 4.28.1

## 작성 요망
### - 프로그램 동작 (캡처 화면)
### - 프로그램 로직 흐름
### - 문제 해결점
      - 서버와 프로그램의 시간 차, 최대한 빠르게 클릭 가능하게 (서버 시간 가져오는 것도 몰랐고, cs지식적으로 시스템 시간 줄여서 프로그램 적용하는것...)


### - 개선점
0. 서버 시간 가져와서 기반한 서비스 (장바구니는 필수) --- 핵심!!!!!!!!!!
1. 캡차 우회 or 로그인 이후 화면에서 서비스 가능하게
2. 최대한 동작 시간 줄이기 (시스템적으로)
3. 다양한 환경의 시스템에서 동작 가능하게 설계 (속도가 느린 환경에서도 동작하게 - time.sleep 사용자제 / 웹이 새로고침되는 것 최대한 자제)
    - 새로고침이 길 경우 time.sleep으로는 이후 요청들이 다 씹힌다
4. 모바일이나 웹 혹은 데스크톱 앱 플랫폼 개발 + 백그라운드 동작 및 비동기 프로그래밍 : 뒤로가기 기능, 로그인 이후 기능 왔다갔다
5. 비밀번호 입력 시 값이 보이는거 보안 개선
6. 2번 기능 아무 키나 누르면 프로그램 종료 하는것
7. 2번 기능 while 문 중간에 스스로 꺼지는 것
8. 예외처리!!!!!
9. 지금은 웹브라우저 컨트롤하여 빨리 요청보내는건데, 직접 사이트에 신청에 해당하는 http 요청 보내는 것은? (개발자 도구 이용)


### - 아쉬운 점
1. 프로그래밍 언어에 대한 이해 부족 + 예외처리 부족 / 변수명, 변수선언 위치...
2. 로직 설계 능력 부족 (+ 추가로 설계의 중요성을 느낌)
3. 주먹 구구식 개발, 설계 충분히 하지 않은 것 / 쓰는 라이브러리나 기술에 대한 충분한 공부x
4. 사전에 기획과 설계, 쓸 기술 선정등 확실히 준비
5. html, css, js 지식 부족


### - 공부한 부분
-  selenium(언어 플랫폼 무관)이라는 브라우저 자동화 도구를 알 수 있게됨 (브라우저 드라이버, html 요소 조작 메서드, html 요소 찾기 메서드, 브라우저 조작 메서드, 키보드 / 마우스 이벤트, js실행)
- 크롬 브라우저의 개발자 도구 보는 방법과 활용
- html, css, js에 대한 약간의 이해와 웹사이트 구조 / 웹사이트의 기술 스택 파악


최종 성능 테스트 하기 : 장시간 실행, 모든 경우의 수 실행, 내재 기능 모두 테스트등...