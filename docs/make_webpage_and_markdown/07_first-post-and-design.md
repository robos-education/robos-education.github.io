# Chapter 8. Note Posting과 MkDocs Design

실제 contents를 GitGub page에 posting하고 MkDocs 설정과 CSS를 이용하여 Web site를 디자인한다.

---

## 1. 지금까지 작성한 note 준비

Chapter 1부터 학습한 Note을 모두 markdown을 변경하여 Web Site에 Posting한다.

---

## 2. AI chat으로 Markdown 변환

note 내용을 AI chat에 붙여넣고 Markdown으로 변환을 요청한다.

**프롬프트 예시**

```
아래 내용을 MkDocs에 올릴 Markdown 형식으로 변환해줘.
제목은 ## 로, 중요한 내용은 굵게, 코드는 코드 블록으로 정리해줘.

[note 내용 붙여넣기]
```

---

## 3. VSCode에서 확인·수정

1. VSCode에서 `docs/` 폴더 안에 새 파일을 만든다.
   - 파일명 예시: `chapter1-html.md`, `html-note.md`
2. AI가 변환한 내용을 붙여넣는다.
3. `Ctrl + Shift + V` (Mac: `Cmd + Shift + V`)로 미리보기를 열고 내용을 확인한다.
4. 내용을 점검하고 어색한 부분은 직접 수정한다.

---

## 4. GitHub 웹에서 commit → 사이트 확인

1. GitHub에서 `<username>.github.io` repository로 이동한다.
2. `docs/` 폴더로 들어간다.
3. 오른쪽 상단 **Add file → Upload files** 를 클릭한다.
4. VSCode에서 작성한 `.md` 파일을 끌어다 놓는다.
5. 하단 **Commit changes** 버튼을 클릭한다.
6. GitHub Actions 자동 배포
7. Web Browser 확인

```
https://<username>.github.io
```

---

## 6. mkdocs.yml 디자인

MkDocs의 설정 테스트는 GitHub에서 직접할 경우 배포시간을 매번 기다려야 하기 때문에 이전 Chapter에서 학습한 `mkdocs serve` local에서 한다.  

로컬 서버가 켜진 상태에서 VSCode에서 아래 내용을 수정하면서 테스트한다.  
저장할 때마다 web browser에서 확인하려면 mkdocs를 재 실행해야 할 수 있다.

---

### 사이트 기본 정보

최상위 key인 site_name, theme, nav든 순서와 상관없이 작성할 수 있다.  

```yaml
site_name: 내 Tech Log    # web browser의 탭과 site 좌측 상단 header에 표시
site_description: HTML부터 GitHub까지 공부 기록 # web site 화면에는 보이지 않음
site_author: 홍길동                           # HTML의 <meta> 태그로 들어가 검색엔지이 읽는 정보가 된다.
```

---

### 색상 바꾸기

```yaml

theme:
  name: material               # 기본 디자인 테마(필수, 전용 옵션이 있기때문에 변경하지 않는다.)
  palette:                     # 색상 설정
    scheme: default            # default: 밝은 테마 / slate: 어두운 테마
    primary: indigo            # 상단 바 색상
    accent: indigo             # 링크·버튼 강조 색상
```

**primary · accent 색상 옵션**

`red` / `pink` / `purple` / `deep purple` / `indigo` / `blue` / `light blue` / `cyan` / `teal` / `green` / `light green` / `lime` / `yellow` / `amber` / `orange` / `deep orange` / `brown` / `grey` / `blue grey` / `black` / `white`
20가지의 color 이름이 지정되어 있고 RGB Code를 이용하려면 CSS로 설정해야 한다. 

---

### 밝은/어두운 테마 토글 추가

```yaml
theme:
  name: material
  palette:
    - scheme: default                 # Dark Mode
      primary: indigo
      accent: indigo
      toggle:                         
        icon: material/brightness-7   # Toggle Button 옵션
        name: Dark Mode 전환           # Button에 Mouse를 올렸을 때 표시되는 Text
    - scheme: slate                   # Bright Mode
      primary: indigo
      accent: indigo
      toggle:
        icon: material/brightness-4
        name: Bright Mode 전환
```

---

### 폰트 바꾸기

```yaml
theme:
  font:
    text: Noto Sans KR         # 본문 폰트 (Google Fonts 이름 그대로 입력)
    code: Roboto Mono          # 코드 폰트
```

[Google Fonts](http://fonts.google.com)에서 원하는 폰트 이름을 찾아 그대로 입력하면 된다.  ]
한국어가 포함된 사이트라면 `Noto Sans KR` 사용을 권장한다.

---

### 로고·파비콘 넣기

```yaml
theme:
  logo: assets/logo.png
  favicon: assets/favicon.png
```

`docs/assets/` 폴더를 만들고 이미지 파일을 넣은 뒤 경로를 입력한다.

---

### features 옵션

필요한 것만 골라서 넣는다.

```yaml
theme:
  features:
    - navigation.top           # 스크롤 내리면 맨 위로 버튼 표시
    - navigation.footer        # 페이지 하단에 이전/다음 페이지 버튼
    - navigation.tabs          # 상단에 탭 메뉴 표시
    - search.highlight         # 검색 결과 강조
    - search.suggest           # 검색 자동완성
    - content.code.copy        # 코드 블록에 복사 버튼 추가
```

---

### 커스텀 CSS

mkdocs.yml의 palette, font로 바꿀 수 있는 세부 style은 CSS로 직접 조정할 수 있다.
mkdocs.yml에 아래를 추가한다.
단, MkDocs의 meterial theme는 고유의 디자인 설정을 가지고 있으 CSS가 적용이 까다롭다.

```yaml
extra_css:
  - stylesheets/extra.css
```

`docs/stylesheets/extra.css` 파일을 만들고 원하는 스타일을 작성한다.

```css
/* ----------------------------------------
   색상 변수 재정의
   Material 테마는 :root가 아닌
   [data-md-color-scheme]으로 덮어써야 적용된다.
---------------------------------------- */

/* Bright Mode 색상 */
[data-md-color-scheme="default"] {
  --md-primary-fg-color: #e91e63;        /* 상단 바 색상 */
  --md-primary-bg-color: #cc7a95;        /* 상단 바 텍스트 색상 */
}
/* Dark Mode 색상 */
[data-md-color-scheme="slate"] {
  --md-primary-fg-color: #ea779d;
  --md-primary-bg-color: #750d30;        /* 상단 바 텍스트 색상 */
}

/* ----------------------------------------
   타이포그래피
---------------------------------------- */

/* 본문 font color */
.md-typeset {
    color: #888888;
}
/* link font color */
.md-typeset a {
  color: #e91e63;
}
/* Code font size */
.md-typeset code {
  font-size: 0.85em; /* 1em = 부모 폰트 크기, 0.85em = 85% */
}
```
CSS는 디자인 형식에 대한 설정이므로 코드가 명확하지 않아도 Web Page가 기능적으로 문제가 생기지 않는다.  
Web Browser의 개발자 도구를 통해 HTML 코드를 분석하면서 실험적으로 테스트하며 설정하는 것이 편리하다.

---

### 메뉴 구성 (nav)

```yaml
nav:
  - 홈: index.md
  - HTML 기초: chapter1-html.md
  - GitHub 시작하기: chapter2-github.md
```

`nav`를 작성하지 않으면 `docs/` 폴더 구조가 자동으로 메뉴가 된다.

---

### 저작권 표시

```yaml
copyright: Copyright &copy; 2025 홍길동
```

---

## 7. 완성되면 push → 배포

디자인이 마음에 들면 변경 사항을 GitHub에 올리고 배포한다.

GitHub -> Repository -> Code -> + Upload file  
폴더 구조의 유의하여 commit하고  Actions에서 배포상태를 확인한다.

```bash
git add .
git commit -m "디자인 수정"
git push
mkdocs gh-deploy
```

브라우저에서 최종 사이트를 확인한다.

```
https://<username>.github.io
```

바뀌지 않으면 강력 새로고침을 한다.

- Windows: `Ctrl + Shift + R`
- Mac: `Cmd + Shift + R`

---

## terminal 작업이 유용한 이유

이번 챕터에서 GitHub 웹과 terminal을 함께 사용해 봤다.  
웹 메뉴로도 대부분의 작업이 가능하지만, terminal에서 직접 명령을 입력하면 더 편한 상황이 있다.

| 상황 | 웹 메뉴 | terminal |
|------|---------|----------|
| 파일 한 개 수정 | 편하다 | 비슷하다 |
| 여러 파일 한 번에 올리기 | 번거롭다 | `git add .` 한 줄로 끝 |
| 로컬 서버 실행 | 불가능 | `mkdocs serve` |
| 배포 | 불가능 | `mkdocs gh-deploy` |
| 작업 속도 | 느리다 | 빠르다 |

처음에는 terminal이 낯설게 느껴지지만, 자주 쓰다 보면 웹 메뉴보다 훨씬 빠르고 정확하다는 걸 알게 된다.  
앞으로 파일이 많아질수록 terminal의 장점이 더 크게 느껴진다.
