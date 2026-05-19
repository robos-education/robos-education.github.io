# 배포 방식 업그레이드

지금까지 사용한 배포 방식은 잘 작동하지만, GitHub는 더 깔끔한 방식을 제공한다.
관심이 있다면 아래 방법으로 전환해본다.

---

## 두 가지 배포 방식 비교

현재 사용 중인 방식과 GitHub Actions 전용 방식의 차이는 차이는 gh-pages branch의 유무다.

| | `gh-pages` branch 방식 | GitHub Actions 전용 방식(단일 branch) |
|---|---|---|
| **Branch** | `main` + `gh-pages` | `main` 하나 |
| **Pages 설정** | Deploy from a branch | GitHub Actions |
| **workflow 파일** | 직접 작성 | GitHub 제공 템플릿 사용 |  

두 방식 모두 GitHub Actions를 사용한다. 차이는 `gh-pages` branch의 유무다.  
현재 방식은 `main`과 `gh-pages` branch를 함께 운영하고, 새 방식은 GitHub Actions 자체 배포 기능을 사용해 `gh-pages` branch 없이 `main` 하나로 운영한다.

---

## 전환 순서

### 1. 기존 workflow 파일 삭제

repository → `Code` 탭 → `.github/workflows/deploy.yml` 클릭 → 오른쪽 위 휴지통 아이콘 클릭 → **Commit changes**

---

### 2. GitHub Pages 설정 변경

1. repository → **Settings** → **Pages** 클릭
2. **Build and deployment → Source**를 `Deploy from a branch`에서 **`GitHub Actions`**로 변경

> 변경하면 branch 선택 메뉴가 사라지는 것이 정상이다.

---

### 3. 새 workflow 파일 생성

Source를 변경하면 화면에 템플릿 카드들이 나타난다. **[Static HTML] 카드의 [Configure]** 버튼을 클릭하면 `.github/workflows/static.yml` 편집 화면으로 이동한다.

---

### 4. workflow 파일 수정(.github/workflows/static.yml)

편집 화면에서 `steps:` 섹션을 찾아 아래 내용으로 교체한다.

```yaml
name: Deploy MkDocs to GitHub Pages

on:
  push:
    branches: ["main"]

permissions:
  contents: read
  pages: write
  id-token: write

concurrency:
  group: "pages"
  cancel-in-progress: false

jobs:
  deploy:
    environment:
      name: github-pages
      url: ${{ steps.deployment.outputs.page_url }}
    runs-on: ubuntu-latest
    
    steps:
      - name: Checkout
        uses: actions/checkout@v4

      # 1. 가상 가상 서버에 파이썬을 설치합니다.
      - name: Set up Python
        uses: actions/setup-python@v5
        with:
          python-version: '3.x'

      # 2. MkDocs 및 테마 의존성을 설치합니다.
      - name: Install dependencies
        run: pip install mkdocs-material

      # 3. 마크다운 문서를 HTML 웹사이트로 빌드합니다. (site 폴더 생성)
      - name: Build with MkDocs
        run: mkdocs build

      - name: Setup Pages
        uses: actions/configure-pages@v5

      # 4. [핵심] 빌드 결과물인 'site' 폴더를 지정하여 업로드합니다.
      - name: Upload artifact
        uses: actions/upload-pages-artifact@v3
        with:
          path: './site'

      - name: Deploy to GitHub Pages
        id: deployment
        uses: actions/deploy-pages@v5
```

> `mkdocs gh-deploy`가 아니라 `mkdocs build`를 사용하는 것에 주의한다.

수정 후 오른쪽 위 **Commit changes** 클릭 → **Commit changes**

---

### 5. Actions 실행 확인

repository → **Actions** 탭에서 배포 진행 상황을 확인한다.

| 아이콘 | 상태 |
|--------|------|
| 🟡 노란 원 | 실행 중 |
| ✅ 초록 체크 | 성공 |
| ❌ 빨간 X | 실패 |

성공하면 기존과 같은 주소로 사이트가 열린다.

```
https://<username>.github.io
```

---

### 6. `gh-pages` branch 삭제 (선택)

전환이 완료되면 더 이상 사용하지 않는 `gh-pages` branch를 삭제할 수 있다.

repository → **Code** 탭 → View all branches → `gh-pages` 오른쪽 휴지통 아이콘 클릭
