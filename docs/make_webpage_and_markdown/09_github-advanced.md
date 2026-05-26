# Chapter 9. GitHub 더 알아보기

GitHub의 Repository를 web에서 직접 관리하면 Local 파일 구조와 달라지거나,  
여러 변경사항을 한꺼번에 확인하기 어렵고, 메뉴를 찾아가는 불편함이 있다.  

또한,  반복적인 작업을 자동화하고, 미세한 버전 관리를 제어할 수 있다.  
따라서 실제 개발자들은 Terminal에서 Git 명령어로 원격 Repository를 관리하는 경우가 많다.

이전 Chapter에서 배운 Git 기초(add -> commit -> push)로 web site를 운영할 수 있다.  
이 챕터에서는 실제 개발자들이 매일 쓰는 Git 명령어를 추가로 익히고,  
GitHub가 단순한 web page를 넘어 어떤 기능들이 있는지 살펴본다.

---

## 1. Terminal로 Git 다루기
 
Terminal을 직접 쓰면 더 빠르고, 할 수 있는 것도 많아진다.

### 원격 Repository와 Local 폴더 일치 시키기

1. VSCode에서 새로운 폴더를 열었을 경우:
  
    - Terminal 실행
    - clone할 폴더 위치로 이동:  `cd 폴더명`
    - clone: `git clone https://github.com/username/repository.git .`
      - .을 넣지 않으면 현재 폴더에 repository 폴더를 만들고 clone한다.
    - git clone은 git init(초기화) -> git remote add origin URL(remote repository 연결)을 포함한다.
  
2. VSCode에서 기존에 작업 폴더가 있을 경우:

    - Terminal 실행
    
    - git 초기화(.git 폴더 생성):  
    `git init`
    
    - GitHub repository와 연결:  
    `git remote add origin https://github.com/username/repository.git`
    
    - GitHub의 최신 내용 받아오기:  
    `git pull origin main`
    
    - 로컬에만 있는 파일은 그대로 유지되고, 이름·경로가 같은 파일은 GitHub 버전으로 덮어쓴다.

3. 현재 VSCode의 폴더 내용을 그대로 GitHub에 올리기

    - Terminal 실행
    
    - git 초기화(.git 폴더 생성):  
    `git init`
    
    - GitHub repository와 연결:  
    ```git remote add origin https://github.com/username/repository.git```
    
    - commit에 대상 추가(폴더 내용 전체):  
    `git add .`
    
    - 메시지와 함께 commit:  
    `git commit -m "reset"`
    
    - branch에 적용 및 upstream 등록 (이후부터 `git push`만 해도 됨):  
    `git push -u origin main`  

    - branch에 강제 적용 (GitHub에만 있던 파일 모두 삭제):  
    `git push -f origin main`  

!!! danger "주의: 데이터 유실 위험 (Partial Commit + Force Push)"  
    * 부분 커밋(Partial Commit)**을 한 상태에서 `-f` 옵션으로 강제 푸시를 하면, **`git add`에 포함되지 않은 원격 저장소의 파일이나 작업 내역이 영구적으로 삭제**될 수 있습니다.  
    * **원인:** 강제 푸시는 "현재 내 로컬 커밋 상태"를 정답으로 간주하고 원격을 덮어씁니다.   
    * **결과:** 내 로컬 커밋에 없는 원격의 파일들은 '불필요한 것'으로 간주되어 타임라인에서 제거됩니다.  
    * **해결:** 로컬 작업이 100% 완료된 것이 아니라면 `--force-with-lease`를 사용하거나, `stash`를 활용해 안전하게 작업해야 한다.  
    * local에 있는 게 100% 최종본이 아니라면, -f 근처도 가지말자. ^^

### 버전 관리 (commit 히스토리 보기)

Git의 핵심은 변경 이력을 저장하는 것이다.   
commit이 쌓이면 언제 무엇이 바뀌었는지, 누가 추가했는지 추적할 수 있고 이전 시점으로 돌아갈 수 있다.   

블로그를 운영하면서 자연스럽게 쌓인 commit은 포트폴리오가 된다.

### branch

지금까지는 `main` branch 하나에서만 작업했다.  
branch는 작업을 분기해서 독립적으로 진행할 수 있게 해준다.

```
main ──●──●──●──────────●  (배포 중인 안정 버전)
              \        /
  feature      ●──●──●      (새 기능 작업 중)
```

branch를 사용하는 이유:

- 기존 사이트를 유지하면서 새 디자인을 테스트할 수 있다. 
- 협업 시 서로의 작업에 영향을 주지 않는다. 
- 실험이 실패해도 `main`에 영향이 없다.  
- 완성되면 `main`에 합친다(merge).

### Pull Request · Issues

GitHub에 내장된 협업 도구다. Issues는 할 일·버그·아이디어를 기록하고, Pull Request는 branch의 변경사항을 main에 합치기 전에 검토 요청하는 기능이다.

### fork · Star · Watch

| 기능 | 설명 |
|------|------|
| Star | 관심 있는 repository에 북마크 |
| Watch | repository 변경사항 알림 받기 |
| fork | 다른 사람의 repository를 내 계정으로 복사. 수정 후 PR로 원본에 기여할 수 있다 |

### 오픈소스와 GitHub

소스 코드가 공개된 소프트웨어다.  
누구나 읽고, 사용하고, 개선안을 제안할 수 있다.  
우리 학습에서 사용한 MkDocs, Material for MkDocs, VS Code 모두 오픈소스다.  
기여 방법은 코드 작성 외에도 문서 번역, 오탈자 수정, 버그 리포트, 기능 제안 등이 있다.

### GitHub Profile

`github.com/사용자명` 페이지는 개발 포트폴리오로 활용할 수 있다.  
commit을 하면 그 날짜에 초록색 칸이 채워지는 contribution graph가 쌓이고, 프로필에 대표 repository를 고정(Pinned repositories)해두면 방문자가 내 작업물을 바로 볼 수 있다.


## 2. 자주 쓰는 Git 명령어

| 명령어 | 설명 |
|--------|------|
| `git clone URL .` | GitHub repository를 현재 폴더에 복사. init·remote 설정 포함 |
| `git pull` | `git fetch` + `git merge`. GitHub 최신 내용을 받아와서 로컬에 반영 |
| `git fetch` | GitHub 변경사항 정보만 받아오기. 로컬 파일은 건드리지 않음 |
| `git push` | 로컬 commit을 GitHub에 올리기 |
| `git push -u origin main` | 처음 push할 때 기본 원격 저장소·branch 등록. 이후부터는 `git push`만 해도 됨 |
| `git push -f origin main` | 로컬 내용으로 GitHub를 강제 교체. GitHub에만 있던 파일은 삭제되므로 신중하게 사용 |
| `git remote -v` | local repository가 현재 어느 remote repository와 연결되어 있는지 확인 |
| `git status` | 로컬에서 수정된 파일, 추가된 파일 확인 (원격과 무관) |
| `git diff` | 마지막 commit 이후 수정 내용을 줄 단위로 확인 |
| `git add .` | 모든 변경사항 스테이징 |
| `git commit -m "메시지"` | commit 생성 |
| `git log --oneline` | commit 기록을 한 줄씩 요약해서 보기 |
| `git restore 파일명` | 수정한 파일을 마지막 commit 시점으로 되돌리기. 복구 불가 |
| `git checkout 커밋해시 -- 파일명` | 특정 commit 시점의 파일로 복원 |
| `git branch` | branch 목록 확인. 현재 위치는 `*`로 표시 |
| `git branch 이름` | 새 branch 만들기 |
| `git checkout 브랜치명` | branch 이동 |
| `git checkout -b 이름` | branch 만들면서 바로 이동 |
| `git merge 이름` | 현재 branch에 이름 branch 합치기 |
| `git revert 커밋해시` | 해당 commit을 취소하는 새 commit을 만든다. 이력이 남아서 안전하다 |
| `git reset 커밋해시` | 해당 commit 시점으로 되돌린다. 이후 commit 이력이 사라진다 |

Git은 명령어를 외워서 쓰는 도구가 아니다.  
`status -> add -> commit -> push` 흐름을 반복하다 보면 자연스럽게 손에 익는다.  
모르는 게 생기면 `git --help` 또는 검색을 활용한다.

---

## 정리

- Terminal에서 Git 명령어로 Local과 GitHub를 동기화할 수 있다
- branch로 작업을 분리하고 merge로 합친다
- Issues, Pull Request, fork 등 GitHub 협업 도구를 활용할 수 있다
- GitHub Profile은 개발 포트폴리오로 활용할 수 있다

