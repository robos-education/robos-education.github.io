# 📚 Chapter 3. Git으로 배포하는 방법 (참고)

위에서는 GitHub 웹 화면에서 직접 파일을 올렸다.
실제 개발 현장에서는 **Git**이라는 도구를 사용해서 터미널에서 파일을 올린다.

Git은 파일의 변경 이력을 관리하는 도구다.
GitHub는 Git으로 관리되는 파일을 저장하는 원격 저장소다.

터미널에서 아래 순서로 진행한다.

## 📖 1. Git 설치 확인

```bash
git --version
```

버전 정보가 출력되면 설치된 상태다.
설치가 안 되어 있으면 [git-scm.com](https://git-scm.com)에서 다운로드한다.

## 📖 2. 최초 1회: 사용자 정보 등록

```bash
git config --global user.name "이름"
git config --global user.email "이메일"
```

## 📖 3. Repository 연결 · 파일 올리기

```bash
# 1. 작업 폴더로 이동
cd calculator-폴더-경로

# 2. Git 초기화
git init

# 3. 원격 repository 연결
git remote add origin https://github.com/<username>/calculator.git

# 4. 파일을 스테이징 (올릴 파일 지정)
git add 01_calcu_03.html

# 5. 변경 내용 저장 (commit)
git commit -m "calculator 추가"

# 6. GitHub에 올리기 (push)
git branch -M main
git push -u origin main -f
# -f 옵션: 강제 실행, 꼭 필요할 경우만

# 7. login 정보 지우기
control /name Microsoft.CredentialManager
# 윈도우가 뜨면 목록에서 git:https://github.com을 찾는다.
# 해당 항목의 오른쪽 화살표를 눌러 **[제거]**
git push
# 로그인 창이 다시 나타난다면 자격증명이 지워진 것
```

Push가 완료되면 GitHub repository에 파일이 올라간다.
이후 GitHub Pages 설정은 웹 방식과 동일하다.

> **이번 챕터 실습은 웹에서 직접 올리는 방식으로 진행한다.**  
> Git 명령어는 Chapter 7에서 실제로 사용한다.

---

## ✅ 4. 정리

