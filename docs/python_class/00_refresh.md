# 📚 사전학습 (복습)

- **Attribute(속성)** — object의 상태나 data를 저장하는 변수
- **Method(메서드)** — class 내부에 정의된 함수로 object의 동작(behavior)을 정의한다.
- **Constructor(생성자)** — object가 생성될 때 자동으로 호출되는 special method
- **Inheritance(상속)** — 기존 class의 attribute와 method를 자식 class가 물려받아 재사용하는 기능
- **Method Overriding(재정의 메서드)** — 부모 class에서 정의한 method를 자식 class에서 동일한 이름으로 다시 정의하여 동작을 바꾸는 것
- **Operator Overloading(연산자 중복 정의)** — `+`, `-`, `==` 같은 연산자를 class에서 special method(예: `__add__`, `__eq__`)로 재정의하여, 해당 class의 object에서도 연산자를 사용할 수 있게 하는 기능


---

## 📖 예제 1: 속성

```python
class Character:
    def __init__(self, name, hp, speed):
        self.name = name
        self.hp = hp
        self.speed = speed

player1 = Character("Noop", 100, 16)
player2 = Character("Pro", 150, 20)
player3 = player1
player3.name = "cocoa"
```

- instance variable을 찾아보자.
- `player1`의 이름과 speed를 출력하고 이유를 설명하라.
- `player2`의 hp를 200 감소시키고 출력하라. (단, -hp는 0으로 저장한다.)

---

## 📖 예제 2: Method

AI를 이용하여 코드를 완성하자.

위 코드에 공격받기와 캐릭터의 상태를 return 하는 method를 추가하라.

**조건**
- 공격받기 기능은 hp가 0 이하로 내려가면 `False`, 아니면 `True`를 return 한다.
- 상태 기능은 `이름: xxx, HP: xxx, Alive(or Dead)` 형태로 return 한다.
- class만 복사하고 아래 test code는 직접 작성하라.

**Test**
- Character 만들기 (`'상진'`, 100, 10)
- 처음 상태 출력
- 공격 받음: damage 50
- 상태 출력
- 공격 받음: damage 70
- 상태 출력

---

### 📄예제 답안(Google Jemini)

```python
class Character:
    def __init__(self, name, hp, speed):
        self.name = name
        self.hp = hp
        self.speed = speed
        self.is_alive = True  # 생존 여부를 관리하는 속성 추가

    # 1. 공격받기 (take_damage) Method
    def take_damage(self, damage):
        self.hp -= damage
        if self.hp <= 0:
            self.hp = 0
            self.is_alive = False
            return False  # 사망 시 False 리턴
        return True  # 생존 시 True 리턴

    # 2. 상태 확인 (get_status) Method
    def get_status(self):
        status = "Alive" if self.is_alive else "Dead"
        return f"이름: {self.name}, HP: {self.hp}, Status: {status}"
```

```
# Test
sangjin = Character("상진", 100, 10)
print(sangjin.get_status())   # 이름: 상진, HP: 100, Status: Alive

sangjin.take_damage(50)
print(sangjin.get_status())   # 이름: 상진, HP: 50, Status: Alive

sangjin.take_damage(70)
print(sangjin.get_status())   # 이름: 상진, HP: 0, Status: Dead
```

---

## 📖 예제 3: Constructor

위 코드에서 생성자는 무엇이고 기능은 무엇인가 설명하라.

---

## 📖 예제 4: Method Override

위 Character에는 `Warrior`와 `Wizard` 두 종류가 있다.  
Character의 특성을 그대로 가지는 별도의 class로 구현 할 수 있다.  
아래 code의 출력 결과를 예측하고 상속의 의미를 설명하라.

```python
class Character:
    def __init__(self, name, hp):
        self.name = name
        self.hp = hp

    def attack(self):
        print(f"{self.name} basic attack!")

    def status(self):
        print(f"{self.name} | HP: {self.hp}")

class Warrior(Character):
    pass

class Wizard(Character):
    pass

arthur = Warrior("Arthur", 200)
merlin = Wizard("Merlin", 120)

arthur.attack()                       # ① ?
merlin.attack()                       # ② ?
arthur.status()                       # ③ ?
print(isinstance(arthur, Character))  # ④ ?
print(isinstance(merlin, Warrior))    # ⑤ ?
```

---

### 📄 설명  
   
    - 상속은 parents class의 속성과 method를 child class가 code 중복 없이 그대로 물려받는 기법이다. 
    - Warrior와 Wizard는 모두 Character의 특성을 가지고 있기 때문에 중복하여 속성과 method를 작성할 필요 없이 상속하면 된다.
    - 메모리에는 모두 복사되어 생성된다.
    - `isinstance()` 함수를 이용하여 관계를 알아낼 수 있다.
    - `arthur`는 Character의 child class → `True`
    - Wizard와 Warrior는 sibling 관계 → `False`

---

## 예제 5: Method Override

Warrior의 `attack`과 Wizard의 `attack`은 서로 다른 기능을 가진다.  
아래 코드의 출력 결과를 예측하고 test 하라.

```python
class Character:
    def __init__(self, name, hp):
        self.name = name
        self.hp = hp

    def attack(self):
        print(f"{self.name} basic attack!")

    def status(self):
        print(f"{self.name} | HP: {self.hp}")

class Warrior(Character):
    def attack(self):
        print("Sword Slash")

class Wizard(Character):
    def attack(self):
        print("Fireball!! +area damage")

party = [Warrior("arthur", 100), Wizard("Merlin", 50)]

for member in party:
    member.attack()
```

---

### 📄 설명:
- **Method Overriding** : parent method를 child가 같은 이름으로 덮어쓰는 것 (내용이 달라야 하는 경우)

---

## 📖 예제 6: Operator Overloading

Python에서는 overloading은 없고 **연산자 오버로딩 (Operator Overloading)** 만 있다.  
Python의 내장 special method(`__add__`, `__gt__` 등)를 재정의하는 것이다.

아래 코드의 출력 결과를 예측하라.

```python
class Character:
    def __init__(self, name, hp):
        self.name = name
        self.hp = hp

    def __str__(self): # 원형은 어떤 문자열을 return하는 method
        return f"{self.name} | HP: {self.hp}"

    def __add__(self, other):   # + 연산자
        party_name = f"{self.name} & {other.name}"
        total_hp = self.hp + other.hp
        return Character(party_name, total_hp)

    def __gt__(self, other):    # greater than 연산자
        return self.hp > other.hp

    def __eq__(self, other):    # = 연산자
        return self.hp == other.hp

arthur = Character("Arthur", 200)
merlin = Character("Merlin", 120)
slime  = Character("Slime", 120)

print(arthur)               # ① ?
party = arthur + merlin
print(party)                # ② ?
print(arthur > merlin)      # ③ ?
print(merlin == slime)      # ④ ?
```

---

### 📄 설명

```
① Arthur | HP: 200
② Arthur & Merlin | HP: 320
③ True
④ True
```

- `__str__`, `__add__`, `__gt__`, `__eq__`는 모두 Python 내부에 이미 정의되어 있는 method이고 이것을 재정의하는 형태이므로 overriding이 맞다.
- 하지만 연산자의 동작을 바꾼다는 의미로 관행적으로 **operator overloading** 이라고 부른다.  
---

<br><br><br>
---
#### Appendix
---
**비교 연산자 special method 정리**

| Method | 연산자 | 의미 |
|--------|--------|------|
| `__lt__` | `<` | less than |
| `__le__` | `<=` | less than or equal |
| `__eq__` | `==` | equal |
| `__ne__` | `!=` | not equal |
| `__gt__` | `>` | greater than |
| `__ge__` | `>=` | greater than or equal |

---

**[Chapter 1 · 상속 심화 →](01_inheritance_advanced.md)**
