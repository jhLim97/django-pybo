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
django.contib.auth앱 이용하여 "계정생성"구현, usercreationform속성 학습. 
