# 📚 Chapter 4. Markdown과 MkDocs

Web page는 HTML 형식으로 작성되어야 하지만 형식과 문법이 매우 복잡하다.   
GitHub는 Markdown으로 작성된 문서를 HTML로 변환하는 기능을 지원하기 때문에,  
여러 분야에서 널리 사용되는 Markdown으로 문서를 작성한다.   
이후 GitHub의 변환 기능을 이용해 web page로 배포한다.

## 📖 1. Markdown과 MkDocs 
 
Markdown은 Text만으로 문서의 구조(제목, 목록, 링크등의 서식)를 만드는 언어이다.  
`#`, `*`, `-` 같은 기호로 문서 서식을 표현하며 복잡한 규칙이 없어 HTML, PDF등 다른 형식으로 쉽게 변환할 수 있다.
우리가 보고 있는 AI Chat의 화면이 Markdown 기반이다.

아래와 같은 곳에서 널리 사용되고 있다.

- **GitHub** — README 파일, 이슈, 코멘트가 모두 Markdown이다.
- **Notion · Obsidian** — 메모와 문서 작성에 Markdown 문법을 사용한다.
- **AI 프롬프트** — ChatGPT, Claude 같은 AI 도구의 답변도 Markdown으로 출력된다.
- **기술 블로그** — 개발자들이 가장 많이 쓰는 문서 형식이다.

우리가 만들 Web Page도 Markdown으로 작성하려고 한다.   
`.md` 파일을 읽어서 HTML 페이지로 변환하고(MkDocs 이용), 그 결과가 web site로 배포된다.


## 📖 2. MkDocs 

그리고 **MkDocs**라는 도구를 사용하면 편리하게 Web Site를 만들고 관리할 수 있다.

[MkDocs](https://www.mkdocs.org/)

```
내가 쓴 Markdown 파일  ── MkDocs ──▶  예쁜 웹사이트  ── GitHub Pages ──▶  인터넷 공개
```

- Markdown으로 작성된 file을 자동으로 Web Page로 변환해 준다.
- 내용을 설명하는 Document 형식의 디자인을 자동으로 구성해 준다.
- GitHub Pages와 연결이 쉽다.

---

## 📖 3. Markdown 연습

VSCode를 열고 `practice.md` 파일을 새로 만든다.

### 제목

`#`의 개수로 제목 크기를 조절한다.

```markdown
# 제목 1
## 제목 2
### 제목 3
```

### 굵게 · 기울임

```markdown
**굵게** 표시한다.
*기울임* 표시한다.
***굵게 + 기울임*** 도 된다.
```

### 목록

순서 없는 목록은 `-`로, 순서 있는 목록은 숫자로 시작한다.

```markdown
- 사과
- 바나나
- 포도

1. 첫 번째
2. 두 번째
3. 세 번째
```

### 링크 · 이미지

```markdown
[표시할 텍스트](URL)

[GitHub](https://github.com)
```

이미지는 링크 앞에 `!`를 붙인다.

```markdown
![대체 텍스트](이미지 URL)
```

### 코드 블록

인라인 코드는 백틱(`` ` ``) 하나로 감싼다.

```markdown
`print("Hello")`
```

여러 줄 코드는 백틱 세 개로 감싼다. 언어 이름을 쓰면 색상이 입혀진다.

````markdown
```python
def hello():
    print("Hello, World!")
```
````

### 인용문

`>`로 인용 블록을 만든다.

```markdown
> 이것은 인용문이다.
```

### 표

`|`로 열을 구분하고, 두 번째 줄에 `-`를 넣어 표를 만든다.

```markdown
| 이름 | 나이 | 지역 |
|------|------|------|
| 홍길동 | 17 | 서울 |
| 김철수 | 16 | 부산 |
```

---

## VSCode 미리보기

작성한 `.md` 파일을 바로 확인할 수 있다.

1. VSCode에서 `practice.md` 파일을 열어둔다.
2. Ctrl + Shift + V — 현재 탭이 미리보기로 전환된다.
3. Ctrl + K, V — 편집 창 옆에 미리보기 창이 나란히 열린다.

편집 창과 미리보기 창을 나란히 놓으면 실시간으로 확인하면서 작업할 수 있다.
  
> **팁** 파일을 저장할 때마다 미리보기가 자동으로 갱신된다.

---

## 정리

Markdown 문법은 기호 몇 가지만 알면 된다.   
지금 배운 내용으로 대부분의 Web Page를 작성할 수 있다.   
다음 Chapter에서는 MkDocs를 설치하고, 이 `.md` 파일들이 실제 web site로 어떻게 만들어지는지 알아보자.

