# 🎬 영화 리뷰 커뮤니티 사이트

## 페어 프로그래밍 흐름

### 개발환경설정

#### 1번 개발자

1. 깃허브 저장소와 장고 프로젝트를 생성
   - 2번 사람을 콜라보레이터로 초대

2. 생성한 저장소에 장고 프로젝트를 push

   - .gitignore : 가상환경을 ignore

   - pip freeze > requirements.txt : 패키지 목록을 생성

#### 2번 개발자

3. 2번 사람이 clone
4. 2번사람만 가상환경 생성과 requirements.txt 설치
   - pip install -r requirements.txt 

5. 2번사람만 앱을 생성
6. add / commit / push
7. 1번 pull
   - git pull
### 개발 진행

드라이버 <-> 네비게이터 전환할 때

드라이버 :` add commit push`

네비게이터 : `pull`

항상 두 사람이 같은 코드를 유지해야한다.

<br>

## 구현

### 목표

> 두 사람이 팀을 이뤄서 영화 리뷰 커뮤니티 서비스의 CRUD 기능과 페이지를 구현한다.

- #### 리뷰 목록 페이지 index

  - 리뷰 ID / 리뷰 제목 / 리뷰 작성 시간
    - 리뷰 제목 클릭 시 해당 리뷰의 detail 페이지로 이동

  - 작성 버튼
    - 버튼 클릭 시 new 페이지로 이동

- #### 리뷰 작성 페이지 new

  - 리뷰 제목 / 리뷰 내용
  - 생성 버튼
    - 버튼 클릭 시 새로운 리뷰 생성 create
    - 작성 후 detail 페이지로 이동

- #### 리뷰 보기 페이지 detail

  - 리뷰 제목 / 리뷰 내용 / 리뷰 작성 시간
  - 수정 버튼
    - 버튼 클릭 시 edit 페이지로 이동
  - 삭제 버튼
    - 버튼 클릭 시 리뷰 삭제 delete

- #### 리뷰 수정 페이지 edit

  - 작성 폼에 원본 리뷰의 제목 과 내용이 작성된 상태.
  - 수정 버튼
    - 버튼 클릭 시 해당 리뷰 데이터 수정 update