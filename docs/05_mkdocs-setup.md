# Chapter 5. MkDocs 설치 · 프로젝트 구조 설정

앞에서 우리는 markdown 대하여 알아보았다.  
Github web page는 Markdown 문서를 html로 렌더링해주는 기능을 가지고 있기 때문에   
편리한 Markdown 문서를 사용하기로 했다.  
이번 Chapter에서는 Markdown 파일을 HTML 웹 페이지로 변환해서 Web Page 형태로 만들고 local browser에서 확인해보는 방법에 대하여 알아본다.  

---

## MkDocs 설치

MkDocs는 Markdown 파일을 활용해 정적 사이트(HTML)를 생성해 주는 도구로,   
주로 **소프트웨어 문서화(Documentation)**를 위해 설계되었다.   
Python 기반으로 구축되었으며, 사용법이 매우 간단하고 빠르다.

MkDocs는 Python으로 만들어진 도구라서 python이 설치되어 있다면 pip를 이용하여 설치할 수 있다.

```
pip install mkdocs-material
```

`mkdocs-material`은 MkDocs 본체와 Material 테마를 함께 설치한다.

설치가 완료되면 확인한다.

```
mkdocs --version
```

버전 번호가 출력되면 설치 성공이다.

---

## 프로젝트 폴더 구조

원하는 위치에 폴더를 하나 만든다.  
우리는 현재 note로 사용하는 이곳을 프로젝트 폴더로 설정한다.
(VSCode에서 **File → Open Folder**로 이 폴더를 연다.)

터미널에서 MkDocs 프로젝트를 초기화한다.

```
mkdocs new .
```

실행 후 폴더 구조가 다음과 같이 생성된다.

```
프로젝트 폴더/
├── docs/
│   └── index.md
└── mkdocs.yml
```

| 항목 | 역할 |
|---|---|
| `docs/` | Markdown 파일을 저장하는 폴더 |
| `docs/index.md` | Web Site 첫 화면에 표시되는 파일 |
| `mkdocs.yml` | Web Site 설정 파일 (제목, 테마 등) |

---

## mkdocs.yml 설정

YML은 데이터를 읽기 쉽도록 구성하기 위해 사용하는 데이터 직렬화 양식이다.  
주로 설정 파일(config), 데이터 교환, 혹은 시스템 간의 메시지 전달에 널리 사용된다.

특히, 들여쓰기(indentation)을 엄격하게 지키는 구조로 되어 있다.(tab이 아닌 space로 작성해야 한다.)

`mkdocs.yml`을 열고 다음과 같이 수정한다.

```yaml
site_name: My Tech Log
# site_url:

theme:
  name: material
  language: ko
```

`site name:`  원하는 Web Site 이름
`site url:` 나중에 인터넷에 배포할 때 github 주소를 입력한다.
theme: 테마 이름과 언어입력
파일을 저장한다 (Ctrl+S).

---

## 로컬 미리보기

설정이 끝나면 내 컴퓨터에서 Web Site를 미리 확인할 수 있다.

```
mkdocs serve
```

터미널에 다음 메시지가 나타난다.

```
INFO    -  Serving on http://127.0.0.1:8000/
```

Serving on 메시지가 return되면 local에서 Web Site의 서버가 작동되고 있음을 알려준다.  
Web Browser를 열어 주소 창에 URL을 입력하면 docs/index.md 파일의 내용이 보이게 된다.

```
http://127.0.0.1:8000
```

Material 테마가 적용된 디자인이고,  `docs/index.md`를 수정하고 저장하면 화면이 자동으로 업데이트된다.
미리보기를 종료할 때는 터미널에서 **Ctrl+C**를 누른다.  
local 설정에 의해 반영되지 않으면 Terminal에서 종료후 다시 serve를 실행시키고 확인한다. 

---

## Test:
지금까지 작성한 파일 중 하나를 docs로 복사하여 Web Site에 반영되는 것을 확인하자.
**markdown** 파일이어야 한다.

## 정리:  
> 내 컴퓨터에서 web site가 동작하는 것을 확인
> 다음 Chapter에서는 전 Chapter에서 만든 github에 배포하는 방법을 알아본다.
