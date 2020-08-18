# Django_pybo

1일차
-
장고 프로젝트를 위한 가상환경 mysite구현 및 urls.py, view.py를 통한 chrome과 local sever의 연결.

2일차
-
admin, auth, contenttypes, sessions 등 앱들이 사용하는 테이블 생성을 위한 migrate 실행 및 DB Browser for SQLite 학습 + 모델 작성.

3일차
-
[python manage.py createsuperuser] 명령어를 통한 관리자 화면에 접속할 수 있는 슈퍼유저(superuser) 생성 + 목록조회 및 탬플릿 태그의 유형, HTTP주요 응답오류 학습.

4일차
-
별칭 사용 및 동일 가상환경에서의 여러 앱이 실행하는 경우에 대비해 네임스페이스 적용 학습 + 답변 저장 구현 및 이에 대한 url추가, 뷰함수 추가 및 보안관련 {% csrf_token %} 학습.

5일차
-
스타일시트 파일 저장을 위한 스태틱(이미지, js, css) 다이어리 구현 및 부트스트랩 학습 + 템플릿내의 동일한 내용 중복방지 및 스타일시트명 변경에 대비한 상속 템플릿 구현.

6일차
-
질문 등록 폼 추가 및 템플릿 적용, {{ form.as_p }}을 사용했을 경우의 디자인제약 벗어나기 위해 수동 폼 작성.답변 등록 폼(form.py)작성. 네비게이션 바 템플릿 추가 및 (base.html)에 {% include "navbar.html" %} 적용 및 jquery, bootstrap.min.js파일 적용.

7일차
-
장고에서 제공하는 Paginator클래스를 이용해 페이징기능 적용, 장고 쉘을 이용해 대량 테스트 데이터 생성. @register.filter 어노테이션을 이용해 템플릿에서 해당 함수를 필터로 사용. 답변개수 표시 및 프로젝트 생성 시 settings.py에 자동으로 생성되는 django.contib.auth앱 이용해 관리의 용이성을 위해 가상환경에 [django-admin startapp common] 실행 후 common앱에 로그인/로그아웃 기능 구현.

8일차
-
django.contib.auth앱 이용하여 "계정생성"구현, usercreationform속성 학습. Question, Answer모델에 author속성 추가. 로그인 필요한 함수에 @login_required 어노테이션 적용해 로그인 화면으로 이동구현. 로그인 성공 후 연결 url설정(next파라미터 사용), 로그인 전 답변작성 못하도록 disabled설정.

9일차
-
글쓴이 표시, 수정과 삭제 구현(모델속성 변경), 댓글모델 추가. 질문 댓글 등록, 수정 및 삭제 구현. 가독성 및 관리위해 방대해진 views.py 분리.

10일차
-
질문, 답변에 추천기능 추가(모델 수정->voter속성 추가). 원하는 지점으로 스크롤되도록 앵커(anchor태그 사용)설정, 원하는 조건으로 정렬 및 검색할 수 있도록 OR조건으로 데이터 조회에 사용되는 Q함수 적용 및 구현. 


