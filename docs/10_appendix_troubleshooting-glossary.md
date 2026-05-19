# 부록

---

## 트러블슈팅

설치나 배포 과정에서 막히는 상황을 모아뒀다. 오류 메시지를 잘 읽으면 대부분 원인을 찾을 수 있다.

---

### 설치 · 환경

#### Python이 설치되어 있는데 `mkdocs` 명령이 안 된다

`mkdocs`를 설치했지만 terminal에서 `command not found`가 뜨는 경우다.

**원인**: Python 설치 시 "Add Python to PATH" 옵션을 체크하지 않았거나, 설치 후 terminal을 재시작하지 않은 경우다.

**해결**:
1. terminal을 완전히 닫았다가 다시 연다.
2. 그래도 안 되면 Python을 재설치한다. 설치 화면에서 **Add Python to PATH**에 반드시 체크한다.

---

#### `pip install mkdocs-material` 중에 오류가 난다

**원인**: pip 자체가 오래된 버전이거나, 인터넷 연결이 불안정한 경우다.

**해결**:
```
python -m pip install --upgrade pip
pip install mkdocs-material
```
pip를 먼저 최신 버전으로 업그레이드한 뒤 다시 설치한다.

---

#### `mkdocs serve` 실행 후 web browser에서 페이지가 안 열린다

**원인**: web browser에 주소를 잘못 입력한 경우다.

**해결**: web browser 주소창에 정확히 `http://127.0.0.1:8000` 을 입력한다. `https`가 아니라 `http`다.

---

#### `mkdocs serve`를 실행했는데 포트가 이미 사용 중이라고 한다

오류 메시지 예시:
```
ERROR - Address already in use. Use --dev-addr to specify a different address.
```

**원인**: 이미 다른 terminal에서 `mkdocs serve`가 실행 중이다.

**해결**: 다른 terminal 탭이나 창을 확인해서 이미 실행 중인 프로세스를 종료한다(`Ctrl + C`). 또는 다른 포트를 지정해서 실행한다.
```
mkdocs serve --dev-addr=127.0.0.1:8001
```

---

### Markdown · MkDocs

#### 페이지를 추가했는데 사이트에 나타나지 않는다

**원인**: `mkdocs.yml`의 `nav` 항목에 새 파일을 추가하지 않은 경우다.

**해결**: `mkdocs.yml`을 열고 `nav` 섹션에 해당 파일을 추가한다.
```yaml
nav:
  - Home: index.md
  - 새 페이지: new-page.md   # 이 줄을 추가
```

---

#### 이미지가 깨져서 나온다 (엑스 박스)

**원인**: 이미지 파일 경로가 잘못됐거나, 파일이 `docs` 폴더 안에 없는 경우다.

**해결**:
1. 이미지 파일이 `docs/` 폴더(또는 그 하위 폴더) 안에 있는지 확인한다.
2. Markdown에서 경로를 정확히 적었는지 확인한다.
```markdown
![설명](images/photo.png)   <!-- docs/images/photo.png 에 파일이 있을 때 -->
```

---

#### 줄바꿈이 반영되지 않는다

**원인**: Markdown에서 줄바꿈은 Enter 한 번으로는 적용되지 않는다.

**해결**: 문단을 나누려면 Enter를 두 번 누른다(빈 줄 하나 삽입). 같은 문단 안에서 줄바꿈을 하려면 줄 끝에 공백을 두 칸 넣고 Enter를 누른다.  
또는, 문자의 끝에 `\`를 입력하고 Enter를 눌러도 줄 바꿈이 된다.

---

#### 코드 블록이 제대로 표시되지 않는다

**원인**: 백틱(`` ` ``) 개수가 맞지 않거나, 코드 블록 앞뒤에 빈 줄이 없는 경우다.

**해결**: 코드 블록은 ` ``` ` 세 개로 시작하고 세 개로 끝낸다. 코드 블록 바로 위아래는 빈 줄을 하나씩 둔다.

---

### Git · GitHub

#### `git push` 후 GitHub Pages 사이트가 업데이트되지 않는다

**원인**: GitHub Actions가 배포를 완료하는 데 1~3분 정도 걸린다.

**해결**: 잠시 기다린 뒤 web browser에서 강력 새로고침(`Ctrl + Shift + R` 또는 `Cmd + Shift + R`)을 한다. 그래도 안 되면 repository의 **Actions** 탭에서 배포 상태를 확인한다.

---

#### GitHub Pages 주소로 들어갔는데 404 오류가 난다

**원인** (여러 가지):
- GitHub Pages가 아직 활성화되지 않은 경우
- `gh-pages` branch가 아직 생성되지 않은 경우
- `mkdocs gh-deploy`를 아직 실행하지 않은 경우

**해결**:
1. repository → **Settings** → **Pages** 에서 Source가 `gh-pages` branch로 설정되어 있는지 확인한다.
2. `mkdocs gh-deploy` 명령을 terminal에서 실행했는지 확인한다.
3. Actions 탭에서 오류가 없는지 확인한다.

---

#### `git push`할 때 인증 팝업이 뜬다

**원인**: Git for Windows에 포함된 GCM(Git Credential Manager)이 GitHub 로그인을 요청하는 것이다. 처음 `git push`할 때 한 번만 나타난다.

**해결**: 팝업에서 **"Sign in with your browser"** 를 선택한다. web browser에서 GitHub에 로그인하면 인증이 완료된다. 한 번 인증하면 이후에는 팝업이 다시 뜨지 않는다.

팝업 없이 terminal에서 username/password를 직접 묻는다면 Git 버전이 오래된 경우다.  
[git-scm.com](https://git-scm.com)에서 최신 버전을 재설치한다.

---

#### `git push` 후 `rejected` 오류가 난다

오류 메시지 예시:
```
! [rejected] main -> main (fetch first)
```

**원인**: GitHub에 있는 내용과 내 로컬 내용이 달라서 충돌이 생긴 경우다. GitHub 웹에서 직접 파일을 수정하면 이런 상황이 발생한다.

**해결**: 먼저 `git pull`로 GitHub의 내용을 받아온 뒤 다시 `git push`한다.
```bash
git pull origin main
git push origin main
```

---

#### VSCode에서 Git 관련 기능이 보이지 않는다

**원인**: Git이 설치되지 않았거나, VSCode가 Git을 인식하지 못하는 경우다.

**해결**:
1. terminal에서 `git --version`을 입력한다. 버전 정보가 나오면 Git은 설치된 것이다.
2. 버전 정보가 없으면 [git-scm.com](https://git-scm.com)에서 Git을 설치한다.
3. 설치 후 VSCode를 완전히 재시작한다.

---

#### commit 메시지를 잘못 입력했다 (아직 push 전)

**원인**: commit에서 메시지를 잘못 입력  

**해결**: 아직 push하지 않은 마지막 commit의 메시지는 수정할 수 있다.
```
git commit --amend -m "올바른 메시지"
```

---

### GitHub 웹 · 기타

#### Repository를 Private으로 만들었더니 GitHub Pages가 작동하지 않는다

**원인**: GitHub Free 계정에서는 Private repository에 GitHub Pages를 사용할 수 없다.

**해결**: repository → **Settings** → **General**에서 repository를 **Public**으로 변경한다.  
repository는 Private으로 유지하면서 web site만 공개하는 것은 유료 계정(Pro 이상)에서 가능하다.

---

#### 파일 이름에 한글이 들어갔더니 오류가 난다

**원인**: 일부 시스템에서 파일 이름의 한글이 제대로 처리되지 않는 경우가 있다.

**해결**: 파일 이름은 영문 소문자, 숫자, 하이픈(`-`)만 사용한다.
```
좋은 예: my-first-note.md, python-study.md
나쁜 예: 내첫노트.md, 파이썬공부.md
```

---
---

## 용어 정리(Glossary)

---

**branch**
repository 안에서 독립적으로 작업할 수 있는 공간이다. 기본 branch 이름은 `main`이다. 기존 내용을 건드리지 않고 새 기능을 시험해볼 때 사용한다.

**browser**
인터넷 페이지를 보여주는 프로그램이다. Chrome, Edge, Firefox 등이 있다.

**client**
server에 요청을 보내는 쪽이다. 웹에서는 web browser가 client 역할을 한다.

**commit**
파일 변경 내용을 Git에 저장하는 행위다. 저장할 때 메시지를 함께 남긴다.

**deploy**
만든 사이트나 프로그램을 실제로 인터넷에 올리는 것이다.

**fork**
다른 사람의 repository를 내 계정으로 복사하는 것이다. 원본에 영향을 주지 않고 자유롭게 수정할 수 있다.

**Git**
파일 변경 기록을 관리하는 버전 관리 시스템이다. 내 컴퓨터에서 실행된다.

**GitHub**
Git repository를 인터넷에 저장하고 공유할 수 있는 서비스다.

**GitHub Actions**
GitHub에서 특정 이벤트(예: push)가 발생했을 때 자동으로 정해진 작업을 실행해주는 기능이다.

**GitHub Pages**
GitHub repository의 내용을 웹사이트로 배포해주는 무료 서비스다.

**`gh-pages`**
MkDocs가 빌드된 사이트 파일을 자동으로 올리는 branch 이름이다. GitHub Pages가 이 branch를 읽어서 사이트를 보여준다.

**HTML (HyperText Markup Language)**
웹 페이지의 구조를 만드는 언어다. web browser가 읽어서 화면에 표시한다.

**HTTP / HTTPS**
web browser와 서버가 데이터를 주고받는 규칙(프로토콜)이다. HTTPS는 HTTP에 보안이 추가된 버전이다.

**issue**
GitHub에서 버그 신고, 기능 제안, 질문 등을 남기는 게시판 기능이다.

**Markdown**
간단한 기호를 사용해 문서를 작성하는 형식이다. `.md` 확장자를 사용한다.

**MkDocs**
Markdown 파일을 웹사이트로 변환해주는 도구다. Python으로 만들어졌다.

**`mkdocs.yml`**
MkDocs 프로젝트의 설정 파일이다. 사이트 이름, 테마, 메뉴 구조 등을 지정한다.

**pip**
Python 패키지를 설치하는 도구다. `pip install 패키지명` 형식으로 사용한다.

**pull**
원격 repository(GitHub)의 변경 내용을 내 컴퓨터로 가져오는 것이다.

**Pull Request (PR)**
내 branch의 변경 내용을 다른 branch에 합치자고 제안하는 것이다. 협업할 때 주로 사용한다.

**push**
내 컴퓨터의 commit 내용을 원격 repository(GitHub)에 올리는 것이다.

**repository (repo)**
Git이 관리하는 프로젝트 폴더다. 파일과 변경 기록이 함께 저장된다.

**server**
데이터를 저장하고 요청이 오면 응답해주는 컴퓨터 또는 프로그램이다.

**terminal**
텍스트 명령어로 컴퓨터를 제어하는 프로그램이다. Windows에서는 명령 프롬프트(cmd), PowerShell, Git Bash 등이 있다.

**URL (Uniform Resource Locator)**
인터넷에서 특정 페이지나 파일의 주소다. `https://example.com`처럼 생겼다.

**VSCode (Visual Studio Code)**
Microsoft에서 만든 코드 편집기다. 다양한 확장 기능을 설치해서 사용할 수 있다.

**YAML**
사람이 읽고 쓰기 쉽게 설계된 설정 파일 형식이다.  
이름은 "YAML Ain't Markup Language"의 약자로, 데이터를 사람 눈에 직관적으로 표현하는 것을 목표로 한다.  
mkdocs.yml, GitHub Actions 워크플로, Docker, Kubernetes 등 요즘 대부분의 개발 도구가 YAML을 기본 설정 형식으로 사용한다.  
들여쓰기로 구조를 표현하므로 스페이스 수가 하나만 틀려도 오류가 발생한다.

