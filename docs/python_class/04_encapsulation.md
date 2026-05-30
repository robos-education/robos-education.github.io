# Chapter 4 · Encapsulation

**소재:** 게임 캐릭터 시스템  
**핵심 질문:** "HP를 -999로 바꿔버리면 어떡하지?"

---

## 학습 내용

- 왜 속성(Attribute)을 숨겨야 하는가?
- Python의 이름 관례 - public, _protected, __private
- __private 동작 원리 - Name Mangling
- getter/setter 직접 만들기
- 도전 과제 - 다른 소재 예제 (문제 형식)

---

## 1. 왜 속성을 숨겨야 하는가?

아래 code의 결과를 확인하고 문제 상황을 예측해 보자.

```python
class Character:
    def __init__(self, name, hp, level):
        self.name = name
        self.hp = hp
        self.level = level

    def __str__(self):
        return f"[Lv.{self.level}] {self.name} (HP: {self.hp})"

hero = Character("Arthur", 100, 5)
print(hero)  # [Lv.5] Arthur (HP: 100)

# 외부에서 속성 변경하기
hero.hp = -999
hero.level = 0
hero.name = ""
print(hero)
```

**출력:**
```
[Lv.5] Arthur (HP: 100)
[Lv.0]  (HP: -999)
```

> 현재 모든 속성이 public이라 외부에서 아무 제한 없이 변경이 가능하다.  
> HP가 음수가 되거나, Level이 0이 되는 건 게임 로직상 있어서는 안 되는 일이다.  
> 이런 문제를 방지하기 위해 속성을 숨기고 접근을 제한하는 것이 Encapsulation이다.

---

## 2. Python의 이름 관례

Python은 접근 제한자(public, private 등)를 문법으로 강제하지 않는다.  
대신 이름 관례(naming convention)로 구분한다.

### 참고

> "We're all consenting adults here."  
> Python은 개발자를 신뢰한다는 철학을 가지고 있다.  
> 간결함과 자유를 중시하는 언어이다.

```python
class Character:
    def __init__(self, name, hp, level):
        self.name = name          # public: 누구나 접근 가능
        self._hp = hp             # protected: 접근 가능하지만 "건드리지 마세요"라는 약속
        self.__level = level      # private: 외부에서 직접 접근 불가 (Name Mangling)

    def __str__(self):
        return f"[Lv.{self.__level}] {self.name} (HP: {self._hp})"
```

```python
hero = Character("Arthur", 100, 5)

# public - 접근 가능
print(hero.name)      # Arthur

# protected - 접근은 가능하지만 관례상 외부에서 사용하지 않는다.
print(hero._hp)       # 100

# private - 접근 불가
# print(hero.__level) # AttributeError!
```

> `public` (self.name): 제한 없음  
> `_protected` (self._hp): class 내부용이라는 개발자 간의 약속  
> `__private` (self.__level): Python이 이름을 변환(Name Mangling)하여 외부 접근이 불가능

---

## 3. Name Mangling이란?

`__`로 시작하는 속성은 Python이 내부적으로 이름을 변경한다.  
`self.__level` → `self._Character__level`로 변경한다.

참고: [Python 공식 스타일 가이드 (PEP 8)](https://peps.python.org/pep-0008/)

```python
hero._Character__level = 4
print(hero._Character__level)  # 4 ← 접근 가능하지만 이렇게 쓰면 안 된다!
```

> Name Mangling은 완벽한 속성 보호는 아니다.  
> 실수로 접근하는 것을 방지하는 정도로 이해한다.

---

## 4. getter와 setter 만들기

속성을 숨겼으면 해당 속성에 안전하게 접근하는 method를 제공해야 한다.

```python
class Character:
    def __init__(self, name, hp, level):
        self.name = name
        self.__hp = hp
        self.__level = level

    def __str__(self):
        return f"[Lv.{self.__level}] {self.name} (HP: {self.__hp})"

    # getter: 속성값을 읽는 method
    def get_hp(self):
        return self.__hp

    def get_level(self):
        return self.__level

    # setter: 속성값을 변경(write)하는 method (유효성 검사 포함)
    def set_hp(self, value):
        if value < 0:
            print("HP는 0보다 작을 수 없습니다.")
            self.__hp = 0
        elif value > 999:
            print("HP는 999를 초과할 수 없습니다.")
            self.__hp = 999
        else:
            self.__hp = value

    def set_level(self, value):
        if value < 1:
            print("레벨은 1보다 작을 수 없습니다!")
            return
        self.__level = value
```

```python
hero = Character("Arthur", 100, 5)

# getter로 읽어오기
print(f"HP: {hero.get_hp()}")        # HP: 100
print(f"Level: {hero.get_level()}")  # Level: 5

# setter로 값 변경 (유효성 검사가 동작한다)
hero.set_hp(150)
print(hero)          # [Lv.5] Arthur (HP: 150)

hero.set_hp(-999)    # HP는 0보다 작을 수 없습니다.
print(hero)          # [Lv.5] Arthur (HP: 0)

hero.set_level(0)    # 레벨은 1보다 작을 수 없습니다!
print(hero)          # [Lv.5] Arthur (HP: 0) ← 레벨은 변경되지 않음
```

**출력:**
```
HP: 100
Level: 5
[Lv.5] Arthur (HP: 150)
HP는 0보다 작을 수 없습니다.
[Lv.5] Arthur (HP: 0)
레벨은 1보다 작을 수 없습니다!
[Lv.5] Arthur (HP: 0)
```

> `getter`: 숨겨진 속성을 읽을 수 있게 해준다.  
> `setter`: 값을 변경할 때 유효성 검사를 유도할 수 있다.  
> 외부에서 직접 속성에 접근하는 것을 막아 프로그램의 안정성을 높인다.

---

## 5. Encapsulation이 적용된 전투 시스템

- 공격 method: `attack(self, other)` → other의 공격 받기 method 호출
- 공격 받기 method: `take_damage(self, damage)` → HP의 유효성 검사 포함
- 생존 여부 method: `is_alive(self)` → bool 반환

```python
class Character:
    def __init__(self, name, hp, attack_power):
        self.name = name
        self.__hp = hp
        self.__attack_power = attack_power

    def __str__(self):
        return f"{self.name} (HP:{self.__hp})"

    def get_hp(self):
        return self.__hp

    def is_alive(self):
        return self.__hp > 0

    def take_damage(self, damage):
        if damage < 0:
            print("Damage는 음수일 수 없습니다.")
            return
        self.__hp -= damage
        if self.__hp < 0:
            self.__hp = 0
        print(f"{self.name}이 {damage}의 Damage를 받았습니다! (남은 HP: {self.__hp})")

    def attack(self, other):
        print(f"{self.name}이 {other.name}을 공격합니다.")
        other.take_damage(self.__attack_power)
```

```python
# Character 생성
hero = Character("Arthur", 100, 25)
monster = Character("Goblin", 50, 10)

# 전투
hero.attack(monster)
monster.attack(hero)
hero.attack(monster)

print()
print(hero)
print(monster)
print(f"Goblin 생존 여부: {monster.is_alive()}")
```

**출력:**
```
Arthur이 Goblin을 공격합니다.
Goblin이 25의 Damage를 받았습니다! (남은 HP: 25)
Goblin이 Arthur을 공격합니다.
Arthur이 10의 Damage를 받았습니다! (남은 HP: 90)
Arthur이 Goblin을 공격합니다.
Goblin이 25의 Damage를 받았습니다! (남은 HP: 0)

Arthur (HP:90)
Goblin (HP:0)
Goblin 생존 여부: False
```

> `__hp`를 직접 수정할 수 없으므로 `take_damage()`를 통해서만 HP가 감소한다.  
> `take_damage()` 안에서 HP가 0 미만이 되지 않도록 프로그램의 안전성을 지키고 있다.  
> 이와 같은 활용을 Encapsulation이라고 한다.

---

## 전체 정리

캡슐화란 속성을 숨기고, 안전한 method로만 접근하게 하는 것이다.

| 이름 관례 | 접근 범위 | 용도 |
|-----------|-----------|------|
| `self.name` | 어디서든 접근 가능 (public) | 외부에 공개할 속성 |
| `self._hp` | 접근 가능, 관례상 내부용 (protected) | 내부 로직에서 사용 |
| `self.__level` | 외부 접근 차단 (private) | 반드시 보호해야 할 속성 |

- `getter`: 숨긴 속성을 읽는 method
- `setter`: 속성을 변경하는 method (유효성 검사 포함)

---

## 도전 과제 1 - 은행 계좌 (BankAccount)

### 조건

**BankAccount class 만들기**
- 속성: `owner` (public), `__balance` (private, 초기값 0)
- `deposit(amount)`: 입금. 음수면 `"입금액은 0보다 커야 합니다"` 출력
- `withdraw(amount)`: 출금. 잔액보다 크면 `"잔액이 부족합니다"` 출력
- `get_balance()`: 잔액 조회
- `__str__`: `"소유자님의 계좌 (잔액: 0원)"` 형태로 출력

**테스트:**
- 계좌를 만들고 입금, 출금을 테스트하라.
- 잔액보다 큰 금액을 출금 시도하라.
- `__balance`에 직접 접근을 시도하라. (에러 확인)

---

## 도전 과제 2 - 학생 성적 관리 (Student)

### 조건

**Student class 만들기**
- 속성: `name` (public), `__scores` (private, 빈 리스트)
- `add_score(score)`: 점수 추가. 0~100 범위가 아니면 `"유효하지 않은 점수입니다"` 출력
- `get_average()`: 평균 점수 반환. 점수가 없으면 0 반환
- `get_highest()`: 최고 점수 반환
- `get_scores()`: 전체 점수 리스트 반환
- `__str__`: `"이름 (평균: 00.0점, 최고: 00점)"` 형태로 출력

**테스트:**
- 학생을 만들고 점수 5개를 추가하라. (유효하지 않은 점수 포함)
- 평균과 최고 점수를 출력하라.
- `__scores`에 직접 접근을 시도하라. (에러 확인)

---

**[Chapter 5 · @property와 Decorator →](05_property_and_decorator.md)**





<br><br><br>
---
#### Appendix
---

**__slots__의 활용**

    # Python class는 instance의 속성을 관리하기 위해 내부에 __dict__를 사용한다.
    # 이것은 유연함은 가질 수 있지만 overhead가 크고 object에서 얼마든지 속성을 추가하거나 __dict__을 사용하여 여전히 private 속성에 접근할 수 있다.
    
    # 그래서 Python에서는 __slots__(tuple)을 정의하면 __dict__의 사용을 없애고 정의한 속성외 추가를 막는다.
    # 따라서 메모리 절약, 속도 향상, 속성 추가 방지등의 효과를 만들 수 있다.

```python
# self.__dict__ member를 관리하는 class와 __slots__로 관리하는 class 비교

class Point_3D:

    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z
    
    def __str__(self):
        return f"{self.x}, {self.y}, {self.z}"

class Point_3D_slots:

    __slots__ = ("x", "y", "z")
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z
    
    def __str__(self):
        return f"{self.x}, {self.y}, {self.z}"

import timeit

def main():
    start = timeit.default_timer()
    p = Point_3D(1,1,1)
    for i in range(5000):
        for j in range(5000):
            p.x += 1
            p.y += 1
            p.z += 1
    print(p)
    print(timeit.default_timer() - start)

    start = timeit.default_timer()
    p = Point_3D_slots(1,1,1)
    for i in range(5000):
        for j in range(5000):
            p.x += 1
            p.y += 1
            p.z += 1
    print(p)
    print(timeit.default_timer() - start)

main()

```