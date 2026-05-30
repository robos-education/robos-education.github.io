# Chapter 7 · 실전 프로젝트 + AI 바이브코딩

---

## 수업 목표

- 지금까지 배운 class 개념을 종합하여 하나의 프로젝트를 완성한다.
- AI에게 정확한 요구사항을 전달하는 방법을 익힌다.
- AI가 만든 코드를 분석하고 검증할 수 있다.

---

## 프로젝트 1: 텍스트 RPG 전투 게임

- Game Flow
- 핵심 class 직접 구현
- 직접 구현한 class 구조와 게임 흐름 등을 이용하여 AI에게 전달할 요구사항 작성
- AI가 만든 코드 검증 (Verification Checklist)
- Test

---

## Game Flow

1. Player 이름 입력
2. Character의 직업을 선택 (1. Warrior, 2. Wizard, 3. Healer)
3. Monster가 random으로 등장
4. Turn-Based Combat (턴제 전투)
   - Player Turn: 1. 공격  2. 특수 능력  3. 회복 아이템 사용
   - Monster Turn: random 공격
5. Monster를 처치하면 경험치를 획득, 다음 Monster가 등장
6. 3마리 Monster 처치 시 승리, Player 사망 시 Game Over
7. 전투 종료 후 결과 출력

### 기타 주의 사항

- `input()`으로 사용자 이름 입력받기
- 잘못된 입력에 대한 예외 처리 포함
- 전투 상황을 읽기 쉽게 출력

---

## 핵심 class 직접 구현

AI에게 요구사항을 전달하기 전에 핵심 class를 직접 구현한다.

> 별도 첨부 코드 파일 참고

---

## AI에게 전달할 요구사항 작성

### 요구사항 작성 팁

간략하게 전달하고, AI의 결과를 보면서 부족한 부분을 보완하자.

- **1차 요청**: class code + game flow + 기본 문법 요구사항
- **2차 요청**: 결과를 보고 "이 부분을 이렇게 수정해 줘" (구체적 수정 요청)
- **3차 요청**: test 중 발견한 bug 수정 요청

> 이 과정이 실제 개발에서 AI를 활용하는 방식이다.

### 필요한 내용들

1. Project 개요
2. Class 구조
3. Game Flow
4. 기본 문법 요구사항

### 요구사항 작성 예시

```
첨부한 class code를 사용하여 text RPG combat game을 만들어 줘.

Game Flow:
1. Player 이름을 input()으로 입력받는다.
2. 직업을 선택한다. (1: Warrior, 2: Wizard, 3: Healer)
3. Monster가 random으로 등장한다. (Monster.create_random() 사용)
4. Turn-based combat:
   - Player turn: 1.Attack  2.Special Ability  3.Healing Item (3개 제한)
   - Monster turn: random attack
5. Monster 처치 시 experience 획득, 다음 Monster 등장
6. 3마리 처치 시 Victory, Player 사망 시 Game Over
7. 전투 종료 후 결과 출력

주의사항:
- 첨부한 class code를 수정하지 말고 그대로 사용할 것
- 잘못된 입력에 대한 exception handling 포함
- 전투 상황을 읽기 쉽게 출력할 것
- game() 함수로 실행할 수 있도록 할 것
```

---

## AI 결과 검증 (Verification Checklist)

AI가 만든 game loop code를 아래 기준으로 검증한다.

### 게임 흐름

- [ ] Player 이름 입력이 정상 동작하는가?
- [ ] 직업 선택이 정상 동작하는가? (1: Warrior, 2: Wizard, 3: Healer)
- [ ] Monster가 difficulty에 따라 등장하는가?
- [ ] turn 순서가 올바른가? (Player → Monster)
- [ ] Monster를 물리친 후 경험치 획득 및 다음 Monster가 등장하는가?
- [ ] Victory / Game Over 조건이 올바르게 동작하는가?
- [ ] 게임 종료 후 결과가 출력되는가?

### 입력 처리

- [ ] 잘못된 입력 시 exception handling이 되는가? (문자, 범위 밖 숫자 등)
- [ ] 잘못된 입력 시 turn을 낭비하지 않고 다시 입력받는가?

### class 활용

- [ ] 직접 만든 class code를 수정 없이 사용하고 있는가?
- [ ] 각 직업의 `attack()`, `special()`이 다르게 동작하는가? (polymorphism)
- [ ] `Monster.create_random()`을 사용하여 Monster를 생성하는가?

### 출력

- [ ] 전투 상황이 읽기 쉽게 출력되는가?
- [ ] Player와 Monster의 상태(`__str__`)가 매 turn 표시되는가?

---

## Test

1. 각 직업(Warrior, Wizard, Healer)으로 한 번씩 Play해 보자.
2. 잘못된 입력을 넣어 보자. (숫자 대신 문자, 범위 밖 숫자 등)
3. AI가 만든 code에서 문제가 발견되면?
   - 문제를 정확히 설명해서 AI에게 수정을 요청한다.
   - 예: "Healer의 special()에서 자기 자신을 치유해야 하는데 Monster를 치유하고 있어. 수정해 줘."
4. 직접 수정할 수 있는 부분은 직접 수정해 보자.

---

## 확장 과제 (도전)

AI에게 아래 기능 중 하나를 추가해 달라고 요청해 보자.  
요구사항을 직접 정리해서 전달한다.

**1. Item System**
- Inventory class 추가 (Chapter 3 Inventory 활용)
- Monster를 물리치면 random으로 item 획득

**2. Boss Monster**
- 3번째 Monster를 Boss로 등장
- 특수 pattern attack

**3. Party System**
- 2~3명의 Character로 party 구성
- turn마다 행동할 Character 선택

**4. Battle Log**
- BattleLog class를 만들어 전투 기록 저장
- Game 종료 후 전체 기록 출력
