# Chapter 2. 내 코드를 인터넷에 올리자 — GitHub와 Tech Log 시작하기

> Chapter 1에서 작성한 HTML을 Web에 배포하는 과정을 알아본다.(github.com을 사용)  
> GitHub에 대하여 알아보고, 자신의 Web Blog를 만들기 위한 설정을 알아본다.

---

## 1. GitHub란?

GitHub는 Code를 Cloud에 저장하고 관리하는 Platform으로 크게 세 가지 역할을 한다.

### ① 저장소 (Repository)
코드와 파일을 Cloud에 저장하는 공간  

```
내 컴퓨터 (local)  ── push ──▶  GitHub (remote)
                 ◀── pull ──
```

### ② 버전 관리 (Version Control)
파일을 수정할 때마다 **이전 상태를 기억**시킬 수 있다. 
따라서 언제든지 과거의 상태로 돌아갈 수 있다.

- Commit: 버전 관리의 기본 단위로 파일을 수정하고 저장할 때마다 누가, 언제, 어떤 내용을 변경했는지 기록을 남길 수 있다.  
이를 통해 우리는 과거 지점으로 code를 되돌릴 수 있고, 어떤 과정으로 수정되어 왔는지 추적할 수 있다.
- Branch: 기존의 코드 작성에서 가지를 쳐서 독립적인 공간을 만드는 기능  
새로운 수정을 서비스되고 있는 code에 영향을 주지 않고 적용시켜 Test 할 수 있다.  
여러 개발자가 동시에 각기 다른 수정을 병렬 작업으로 시행할 수 있다.  
- Pull Request & Merge: 개별 Branch에서 Test가 끝난 Code를 Main Code에 합치는 과정  

### ③ 협업 (Collaboration)
Repository에 저장된 내용을 공개·비공개로 설정할 수 있으며,
공개 설정 시 인터넷이 되는 곳이라면 어디서든 누구나 참여하여 협업할 수 있다.

---

## 2. GitHub Pages — 무료 웹 호스팅

GitHub의 **GitHub Pages**기능을 이용하면 개인의 Web Site를 구성할 수 있다.
Repository에 올린 파일을 자동으로 웹사이트를 만들어 주는 Hosting Service다.

```
내 컴퓨터                         GitHub                     인터넷
calculator.html  ── push ──▶  repository  ──▶  https://내아이디.github.io/calculator
```
---

## 3. Markdown과 MkDocs 
### Markdown이란?
 
Markdown은 Text만으로 문서의 구조(제목, 목록, 링크등의 서식)를 만드는 언어이다.  
복잡한 규칙이 없어 HTML, PDF등 다른 형식으로 쉽게 변환할 수 있다.
우리가 보고 있는 AI Chat의 화면이 Markdown 기반이다.
 
| 내가 쓰는 것 | 화면에 보이는 것 |
|------------|---------------|
| `# 제목` | 큰 제목 |
| `**굵게**` | **굵게** |
| `- 항목` | • 항목 (목록) |
| ` ```코드``` ` | `코드` (코드 강조) |


공부한 내용을 **Markdown**으로 기록하고 **GitHub Pages**로 배포하려고 한다.
이 때, **MkDocs**라는 도구를 사용하면 편리하게 Web Site를 만들고 관리할 수 있다.

```
내가 쓴 Markdown 파일  ── MkDocs ──▶  예쁜 웹사이트  ── GitHub Pages ──▶  인터넷 공개
```

### MkDocs
- Markdown으로 작성된 file을 자동으로 Web Page로 변환해 준다.
- 내용을 설명하는 Document 형식의 디자인을 자동으로 구성해 준다.
- GitHub Pages와 연결이 쉽다.

---

## ✅ 정리

Markdown과 MkDocs를 이용하면 우리의 자료를 Text file과 비슷한 format으로 보관하고 관리할 수 있고  
Web Page로의 변환도 쉽게 할 수 있다.

- GitHub: 코드 저장소 + 버전 관리 + 협업 도구
- GitHub Pages: 내 파일을 무료 웹사이트로 만들어 주는 기능
- MkDocs: Markdown 파일을 웹사이트로 변환해 주는 도구
---
