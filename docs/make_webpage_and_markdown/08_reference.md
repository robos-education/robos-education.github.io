# Chapter 8. Markdown · MkDocs 레퍼런스

이 챕터는 앞에서 배운 내용을 빠르게 찾아볼 수 있는 레퍼런스다.  
새 문법이 필요할 때, 옵션이 기억나지 않을 때 펼쳐서 확인한다.

---

## 1. Markdown 치트시트

### 제목 (Heading)

```markdown
# 제목 1
## 제목 2
### 제목 3
#### 제목 4
```
> `#` 뒤에 반드시 공백을 하나 넣는다.

??? success "[결과 보기]"
    # 제목 1
    ## 제목 2
    ### 제목 3
    #### 제목 4

---

### 텍스트 강조

| 문법 | 결과 보기 |
|------|------|
| `**굵게**` | **굵게** |
| `*기울임*` | *기울임* |
| `~~취소선~~` | ~~취소선~~ |
| `**_굵고 기울임_**` | **_굵고 기울임_** |

---

### 목록

**순서 없는 목록**

```markdown
- 항목 1
- 항목 2
  - 하위 항목 (상위 항목에서 2칸 들여쓰기)
```
??? success "[결과 보기]"
    - 항목 1
    - 항목 2
        - 하위 항목 (상위 항목에서 2칸 들여쓰기)

**순서 있는 목록**

```markdown
1. 첫 번째
2. 두 번째
3. 세 번째
```

> 들여쓰기는 스페이스 2칸 또는 4칸을 일관되게 사용한다.

??? success "[결과 보기]"
    1. 첫 번째
    2. 두 번째
    3. 세 번째

---

### 링크와 이미지

```markdown
[링크 텍스트](https://example.com)
[링크 텍스트](https://example.com "마우스를 올렸을 때 표시되는 문자열")

![이미지 설명](이미지경로.png)
![이미지 설명](https://example.com/image.png)
```
??? success "[결과 보기]"
    ![스마트 러닝센터 삼산학원](images/smart_learningcenter.png "스마트 러닝센터 삼산학원")

---

### 인용문 (Blockquote)

```markdown
> 인용문 내용  
> 여러 줄도 가능하다.

> 첫 번째 인용
>> 중첩 인용
```
??? success "[결과 보기]"
    > 인용문 내용  
    > 여러 줄도 가능하다.

    > 첫 번째 인용
    >> 중첩 인용
---

### 코드

**인라인 코드** — 문장 안에 코드를 넣을 때

```markdown
`print("Hello")    # inline code`
```

**코드 블록** — 여러 줄 코드

````markdown
```python
def hello():
    print("Hello, World!")
```
````

언어 이름을 지정하면 문법 강조(syntax highlighting)가 적용된다.  
자주 쓰는 언어 이름: `python`, `javascript`, `html`, `css`, `bash`, `markdown`

??? success "[결과 보기]"
    `print("Hello")    # inline code`

    ```python
    def hello():
        print("Hello, World!")
    ```

---

### 표 (Table)

```markdown
| 항목 | 설명 | 비고 |
|------|------|------|
| A | 내용 A | - |
| B | 내용 B | - |
```

**정렬 지정**

```markdown
| 왼쪽 | 가운데 | 오른쪽 |
|:-----|:------:|-------:|
| 텍스트 | 텍스트 | 텍스트 |
```

> `:` 위치로 정렬 방향을 결정한다.

??? success "[결과 보기]"
    | 왼쪽 | 가운데 | 오른쪽 |
    |:-----|:------:|-------:|
    | 텍스트 | 텍스트 | 텍스트 |

---

### 수평선

```markdown
---
```
??? success "[결과 보기]"
    ---

---

### 체크박스 (Task List)

```markdown
- [x] 완료된 항목
- [ ] 미완료 항목
```

GitHub, MkDocs에서 체크박스로 렌더링된다.

??? success "[결과 보기]"
    - [x] 완료된 항목
    - [ ] 미완료 항목

---

### 각주 (Footnote)  


```markdown
본문에 각주를 넣는다.[^1]

[^1]: 각주 내용은 여기에 적는다.  숫자가 아니어도 상관없다.

```
??? success "[결과 보기]"
    본문에 각주를 넣는다.[^1]

    [^1]: 각주 내용은 여기에 적는다.  숫자가 아니어도 상관없다.

---

### 줄바꿈

Markdown에서 줄을 바꾸려면 두 가지 방법이 있다.

```markdown
첫 번째 줄  
두 번째 줄 (줄 끝에 스페이스 2칸)

첫 번째 단락

두 번째 단락 (빈 줄 하나)
```

> 빈 줄이 없으면 같은 단락으로 합쳐진다.

??? success "[결과 보기]"
    첫 번째 줄  
    두 번째 줄 (줄 끝에 스페이스 2칸)

    첫 번째 단락

    두 번째 단락 (빈 줄 하나)

---

### 이스케이프 (Escape)

Markdown 기호를 그대로 출력하려면 `\`를 앞에 붙인다.

```markdown
\*별표를 그대로 출력\*
\# 해시를 그대로 출력
```
??? success "[결과 보기]"
    \*별표를 그대로 출력\*
    \# 해시를 그대로 출력

---

## 2. mkdocs.yml 옵션 정리

`mkdocs.yml`은 MkDocs 사이트 전체를 제어하는 설정 파일이다.  
들여쓰기는 **스페이스 2칸**을 사용한다. 탭(Tab)은 사용하지 않는다.

---

### 기본 설정

```yaml
site_name: 내 기술 노트          # 사이트 이름 (필수)
site_url: https://username.github.io/repo-name/  # 배포 URL
site_description: 공부 기록 모음  # 사이트 설명 (검색 엔진용)
site_author: 홍길동               # 작성자 이름
```

---

### docs_dir / site_dir

```yaml
docs_dir: docs      # Markdown 파일이 있는 폴더 (기본값: docs)
site_dir: site      # 빌드 결과물 폴더 (기본값: site, .gitignore에 추가)
```
우리가 만든 local server나 GitHub의 gh-pages는 생성한 HTML을 site 폴더에 만들지 않는다.  
local server는 memory에 생성하고 GitHub는 gh-pages branch에 생성한다.

---

### nav — 목차 구성

```yaml
nav:
  - 홈: index.md
  - Chapter 1 - HTML:
      - 소개: 01_html.md
  - Chapter 2 - GitHub:
      - 개요: 02_github-mkdocs.md
  - 레퍼런스: 08_reference.md
```

- `nav`를 생략하면 MkDocs가 파일 구조를 자동으로 목차로 만든다.
- 항목 이름과 파일 경로는 `이름: 파일명.md` 형식으로 적는다.
- 하위 항목은 들여쓰기로 표현한다.
- docs/의 정렬 구조와 다른 순서를 만들거나 HTML 파일을 메뉴에 표시하려면 필수적으로 작성해야 한다.

---

### theme — 테마 설정

```yaml
theme:
  name: material          # 테마 이름 (material 또는 mkdocs)
  language: ko            # 언어 설정
  palette:
    scheme: default       # default (밝은 테마) / slate (어두운 테마)
    primary: indigo       # 상단 바 색상
    accent: indigo        # 강조 색상
  font:
    text: Roboto          # 본문 폰트
    code: Roboto Mono     # 코드 폰트
  features:
    - navigation.tabs         # 상단 탭 네비게이션
    - navigation.top          # 맨 위로 버튼
    - navigation.expand       # 사이드바 자동 펼침
    - search.highlight        # 검색 결과 강조
    - content.code.copy       # 코드 블록 복사 버튼
```

**자주 쓰는 primary 색상값**

| 값 | 색상 |
|----|------|
| `red` | 빨강 |
| `pink` | 분홍 |
| `indigo` | 남색 |
| `blue` | 파랑 |
| `teal` | 청록 |
| `green` | 초록 |
| `orange` | 주황 |
| `grey` | 회색 |
| `black` | 검정 |
| `white` | 흰색 |

---

### 다크/라이트 모드 전환 버튼

```yaml
theme:
  name: material
  palette:
    - scheme: default                 # light mode
      toggle:
        icon: material/brightness-7   # png 사용 불가
        name: 다크 모드로 전환
    - scheme: slate                   # dark mode
      toggle:
        icon: material/brightness-4
        name: 라이트 모드로 전환
```

---

### icon — 로고와 파비콘

```yaml
theme:
  icon:
    logo: material/book-open-page-variant   # Material 내장 아이콘 사용
  favicon: assets/favicon.png               # 이미지 파일 사용
```

`logo`는 site 상단 왼쪽에 표시되는 아이콘이다. Material 테마 내장 아이콘 또는 이미지 파일을 사용할 수 있다.  
`favicon`은 Web browser 탭에 표시되는 아이콘이다. 이미지 파일 경로를 지정한다.

---

### plugins — 플러그인

```yaml
plugins:
  - search:          # 검색 기능 (default)
      lang: ko       # 한국어 검색 지원
```

---

### markdown_extensions — Markdown 확장

Markdown의 기본 기능을 넘어 **수식, 도표, 각주, 하이라이트** 등 강력한 추가 기능을 활성화하는 도구이다.

```yaml
markdown_extensions:
  - admonition                        # 주석 박스 (Note, Warning 등)
  - pymdownx.details                  # 접을 수 있는 블록
  - pymdownx.superfences              # 코드 블록 확장 (중첩 등)
  - pymdownx.highlight:               # 코드 강조
      anchor_linenums: true
  - pymdownx.inlinehilite             # 인라인 코드 강조
  - pymdownx.tasklist:                # 체크박스
      custom_checkbox: true           # true: Material theme 모양
  - tables                            # 표(default)
  - toc:                              # 목차 자동 생성(default)
      permalink: true                 # 각 제목에 링크 아이콘 추가
  - footnotes                         # 각주
  - attr_list                         # HTML 속성 추가
  - md_in_html                        # HTML 블록 안에 Markdown 사용
```
pymdownx 계열은 mkdocs-material을 설치할 때 함께 설치된다.  
설정 code만 작성하면 된다.

---

### extra — 추가 정보

web page의 **맨 아래(Footer)**에 SNS 바로가기 아이콘 버튼을 만든다.
`generator: false`를 추가하면 web page의 **맨 아래(Footer)**에 "Made with Material for MkDocs" 문구를 숨길 수 있다.

```yaml
extra:
  generator: false    # 하단 "Made with Material for MkDocs" 문구 숨김
  social:
    - icon: fontawesome/brands/github       # MkDocs 테마가 내장하고 있다.
      link: https://github.com/username
    - icon: fontawesome/brands/instagram
      link: https://instagram.com/username
```

---

### copyright

web page의 **맨 아래(Footer)**에 저작권 표시를 넣는다.

```yaml
copyright: Copyright &copy; 2025 홍길동
```

---

### repo 연동

web page의 **상단**에 표시되는 Repository 링크이다.

```yaml
repo_name: username/repo-name
repo_url: https://github.com/username/repo-name
edit_uri: edit/main/docs/        # 각 페이지에 GitHub 편집 링크 표시
```

---

### admonition (주석 박스) 사용법

`markdown_extensions`에 `admonition`을 추가한 후 사용한다.

```markdown
!!! note "제목"
    내용을 여기에 적는다.
    들여쓰기는 4칸이다.

!!! warning
    경고 내용

!!! tip "팁"
    유용한 정보
```
??? success "[결과 보기]"
    !!! note "제목"
        내용을 여기에 적는다.
        들여쓰기는 4칸이다.

    !!! warning
        경고 내용

    !!! tip "팁"
        유용한 정보

**자주 사용하는 admonition type과 color**

| 타입 | 색상 |
|------|------|
| `note` | 파랑 |
| `tip` | 초록 |
| `warning` | 주황 |
| `danger` | 빨강 |
| `info` | 하늘 |
| `success` | 초록 |
| `question` | 초록 |
| `example` | 보라 |

admonition을 접고 열기  

- !!!: 항상 열림, block을 접을 수 없다.  
- ???: 클릭해서 block을 열 수 있다.
- ???+: block이 열려있다. 클릭으로 접을 수 있다.

```markdown
??? note "클릭해서 열기"
    기본적으로 닫혀 있다.

???+ note "기본으로 열려있기"
    기본적으로 열려 있다.
```
??? note "[결과 보기]"
    ??? note "클릭해서 열기"
        기본적으로 닫혀 있다.

    ???+ note "기본으로 열려있기"
        기본적으로 열려 있다.
---

### 전체 예시

```yaml
site_name: 나의 기술 노트
site_url: https://username.github.io/tech-log/
site_description: 공부한 내용을 정리한 기술 노트
site_author: 홍길동

repo_name: username/tech-log
repo_url: https://github.com/username/tech-log

theme:
  name: material
  language: ko
  icon:
    logo: material/book-open-page-variant
  favicon: assets/favicon.png
  palette:
    - scheme: default
      primary: indigo
      accent: indigo
      toggle:
        icon: material/brightness-7
        name: 다크 모드
    - scheme: slate
      primary: indigo
      accent: indigo
      toggle:
        icon: material/brightness-4
        name: 라이트 모드
  features:
    - navigation.tabs
    - navigation.top
    - search.highlight
    - content.code.copy

plugins:
  - search:
      lang: ko

markdown_extensions:
  - admonition
  - pymdownx.details
  - pymdownx.superfences
  - pymdownx.highlight:
      anchor_linenums: true
  - pymdownx.inlinehilite
  - pymdownx.tasklist:
      custom_checkbox: true
  - tables
  - toc:
      permalink: true
  - footnotes                         # 각주
  - attr_list                         # HTML 속성 추가
  - md_in_html                        # HTML 블록 안에 Markdown 사용

nav:
  - 홈: index.md
  - Chapter 1: 01_html.md
  - Chapter 2: 02_github-mkdocs.md
  - 레퍼런스: 08_reference.md

extra:
  generator: false                              # 하단 "Made with Material for MkDocs" 문구 숨김
  social:
    - icon: fontawesome/brands/github           # MkDocs 테마가 내장하고 있다.
      link: https://github.com/username
    - icon: fontawesome/brands/instagram
      link: https://instagram.com/username

copyright: Copyright &copy; 2025 홍길동
```

---

## 3. 정리

Markdown과 MkDocs의 기능은 이 레퍼런스에서 언제든 찾아볼 수 있다.  
처음부터 모두 외울 필요는 없고, 필요할 때 꺼내 쓰는 방식으로 활용한다.
  
다음 Chapter 9에서는 GitHub를 더 깊이 들여다본다.  
버전 관리의 원리, branch, Pull Request, 오픈소스 등을 살펴본다.
