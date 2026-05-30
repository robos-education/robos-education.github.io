# Chapter 2 · 오버라이딩 심화 (Overriding Advanced)

**소재:** 게임 캐릭터 성장 시스템  
**핵심 질문:** "부모 클래스의 기능을 상속받았는데, 바꾸고 싶으면 어떻게 하지?"

---

## Override란?

부모 클래스에 이미 있는 메서드를 자식 클래스에서 **다시 정의**하는 것이다.

실전에서는 두 가지 선택이 생긴다.

1. 부모의 기능을 **완전히 버리고** 새로 쓸 것인가?
2. 부모의 기능을 **살리면서** 추가할 것인가?

---

## 1. 완전히 새로 쓰는 Override

부모의 동작이 전혀 맞지 않을 때, `super()`를 사용하지 않고 메서드를 완전히 새로 작성한다.

```python
class Character:
    def __init__(self, name, hp):
        self.name = name
        self.hp = hp

    def attack(self):
        print(f"{self.name}: basic attack!")

    def introduce(self):
        print(f"나는 {self.name}이다.")

class Ninja(Character):
    def __init__(self, name, hp):
        super().__init__(name, hp)

    # 닌자는 자기소개를 하지 않는다.
    def introduce(self):
        print("...")

class Bard(Character):
    def __init__(self, name, hp):
        super().__init__(name, hp)

    # 음유시인은 노래로 자기소개를 한다.
    def introduce(self):
        print(f"🎵 나의 이름은~ {self.name}~ 🎵")
```

```python
party = [Character("병사", 50), Ninja("하야부시", 80), Bard("음유시인", 40)]

for member in party:
    member.introduce()
```

**출력:**
```
나는 병사이다.
...
🎵 나의 이름은~ 음유시인~ 🎵
```

> 각 클래스의 `introduce()`는 모두 다르기 때문에 `super()`를 사용하지 않았다.  
> 각 클래스가 완전히 자기만의 동작을 정의한 것이다.

---

## 2. 부모의 기능을 살리면서 확장하는 Override

부모의 동작은 유지하되 추가 기능이 필요할 때 `super().method()`를 사용한다.

모든 Character는 `level` 속성을 가지고 있고, 하위 클래스에서는 고유의 상태 속성이 있다.  
`level_up()` 에서는 기본 레벨 속성도 올려야 하고, 하위 클래스 고유의 속성도 올려줘야 한다.

```python
class Character:
    def __init__(self, name, hp):
        self.name = name
        self.hp = hp
        self.level = 1

    def level_up(self):
        self.level += 1
        self.hp += 20
        print(f"{self.name} → Lv.{self.level}! HP +20")


class Warrior(Character):
    def __init__(self, name, hp, armor):
        super().__init__(name, hp)
        self.armor = armor

    def level_up(self):
        super().level_up()          # 부모의 레벨업 (레벨 +1, HP +20)
        self.armor += 10            # 전사만의 추가 효과
        print(f"  → armor +10! (현재 armor: {self.armor})")


class Wizard(Character):
    def __init__(self, name, hp, mana):
        super().__init__(name, hp)
        self.mana = mana

    def level_up(self):
        super().level_up()          # 부모의 레벨업 (레벨 +1, HP +20)
        self.mana += 30             # 마법사만의 추가 효과
        print(f"  → mana +30! (현재 mana: {self.mana})")
```

```python
arthur = Warrior("Arthur", 100, 50)
merlin = Wizard("Merlin", 80, 100)

arthur.level_up()
merlin.level_up()
merlin.level_up()
```

**출력:**
```
Arthur → Lv.2! HP +20
  → armor +10! (현재 armor: 60)
Merlin → Lv.2! HP +20
  → mana +30! (현재 mana: 130)
Merlin → Lv.3! HP +20
  → mana +30! (현재 mana: 160)
```

### 정리

| 상황 | 방법 |
|------|------|
| 부모의 동작이 전혀 맞지 않을 때 | 완전히 새로 쓰기 |
| 부모의 동작 + 추가 기능이 필요할 때 | `super().method()` 사용 |

### 주의

`__init__()`도 메서드이기 때문에 override 된다.
자식 클래스에서 `__init__`을 정의하지 않으면 부모의 `__init__`이 자동으로 실행된다.
하지만 자식 클래스에서 `__init__`을 새로 정의하면서 `super().__init__()`을 **생략하면**
부모의 `__init__`이 실행되지 않아 해당 속성들이 만들어지지 않는다. (흔한 실수!)  

---

## 3. 다형성 (Polymorphism) 체감하기

다형성이란 **같은 이름의 메서드**를 호출하지만, 각 객체가 **자기만의 동작**을 실행하는 것을 말한다.

```python
class Character:
    def __init__(self, name, hp):
        self.name = name
        self.hp = hp

    def attack(self):
        return f"{self.name}: 기본 공격! (10 damage)"

    def special(self):
        return f"{self.name}: 특수 능력 없음"


class Warrior(Character):
    def attack(self):
        return f"{self.name}: 검 베기! (25 damage)"

    def special(self):
        return f"{self.name}: 방어 태세! (armor +50)"


class Wizard(Character):
    def attack(self):
        return f"{self.name}: 파이어볼! (30 damage)"

    def special(self):
        return f"{self.name}: 마나 회복! (mana +40)"


class Healer(Character):
    def attack(self):
        return f"{self.name}: 지팡이 때리기! (5 damage)"

    def special(self):
        return f"{self.name}: 전체 치유! (HP +30)"
```

```python
party = [Warrior("Arthur", 200), Wizard("Merlin", 80), Healer("Aria", 100), Warrior("Gawain", 180)]

print("=== 전투 시작 ===")
for member in party:
    print(member.attack())

print("=== 특수 능력 ===")
for member in party:
    print(member.special())
```

**출력:**
```
=== 전투 시작 ===
Arthur: 검 베기! (25 damage)
Merlin: 파이어볼! (30 damage)
Aria: 지팡이 때리기! (5 damage)
Gawain: 검 베기! (25 damage)

=== 특수 능력 ===
Arthur: 방어 태세! (armor +50)
Merlin: 마나 회복! (mana +40)
Aria: 전체 치유! (HP +30)
Gawain: 방어 태세! (armor +50)
```

> `for` 문은 상대가 Warrior인지 Wizard인지 **모른 채** `.attack()`만 호출할 뿐이다.  
> 각각의 객체가 자신의 메서드를 알아서 실행한다.  
> 나중에 새로운 Character가 추가되어도 `for` 문은 수정 없이 정상 작동한다.  
> 이것이 **다형성(Polymorphism)** 이다.

---

## 도전 과제

아래 조건을 만족하는 코드를 작성하라.  
AI를 사용해도 좋지만, **요구사항은 직접 정리해서** 전달하라.

### 조건

### 조건

각 몬스터는 기본 Monster와 다른 고유한 공격 방식을 가지고 있다.
기본 공격이 맞지 않는 몬스터는 완전히 새로 쓰고,
기본 공격에 추가 동작이 필요한 몬스터는 super()를 활용하라.

**Monster 클래스 만들기**
- 속성: `name`, `hp`, `attack_power`
- 메서드: `attack()` → `"{name} Attacks!! Deals {attack_power} damage"` 반환

**Monster를 상속받아 3종류의 몬스터 만들기**
- `Slime` : 기본 공격과 완전히 다름(공격력이 1/2) → attack override → `"{name} Sticks!! Deals {damage} damage"` 반환
- `Dragon` : 기본 공격과 완전히 다름(공격력이 x2) → attack override → `"{name} Breathes fire!! Deals {damage} damage"` 반환
- `Mimic` : 기본 공격 앞에 추가 대사 → attack override → `"Thought it was a treasure chest, didn't you?"` + 기본 공격(super() 활용) 반환

**몬스터 리스트를 만들고 `for` 문으로 전부 `attack()`을 실행하라.**

**(추가)** 새로운 몬스터 `Ghost`를 추가하라. (`attack_power` → 5)
- 기본 공격 앞에 추가 대사 → attack override → `"유령이라 공격이 매우 약해"` + 기본 공격(super() 활용)
- `for` 문을 수정하지 않고 동작하는지 확인하라. (Polymorphism)

### 예시 답안

```python
class Monster:
    def __init__(self, name, hp, attack_power):
        self.name = name
        self.hp = hp
        self.attack_power = attack_power

    def attack(self):
        return f"{self.name} Attacks!! Deals {self.attack_power} damage"


class Slime(Monster):
    def attack(self):
        damage = self.attack_power * 0.5
        return f"{self.name} Sticks!! Deals {damage} damage"

class Dragon(Monster):
    def attack(self):
        damage = self.attack_power * 2
        return f"{self.name} Breathes fire!! Deals {damage} damage"

class Mimic(Monster):
    def attack(self):
        return "Thought it was a treasure chest, didn't you? " + super().attack()


class Ghost(Monster):
    def attack(self):
        return f"{self.name}'s Attack Power is very low. " + super().attack()
```

```python
monsters = [Slime("슬라임", 100, 50), Dragon("드래곤", 50, 150), Mimic("미믹", 60, 10)]

for member in monsters:
    print(member.attack())
```

**출력:**
```
슬라임 Sticks!! Deals 25.0 damage
드래곤 Breathes fire!! Deals 300 damage
Thought it was a treasure chest, didn't you? 미믹 Attacks!! Deals 10 damage
```

```python
# Ghost 추가 — for 문은 수정하지 않는다!
monsters.append(Ghost("유령", 20, 5))

for member in monsters:
    print(member.attack())
```

**출력:**
```
슬라임 Sticks!! Deals 25.0 damage
드래곤 Breathes fire!! Deals 300 damage
Thought it was a treasure chest, didn't you? 미믹 Attacks!! Deals 10 damage
유령's Attack Power is very low. 유령 Attacks!! Deals 5 damage
```

> `Ghost`를 추가했지만 `for` 문은 한 줄도 수정하지 않았다. 이것이 다형성의 힘이다.

---

**[Chapter 3 · Special Methods (Dunder Methods) →](03_special_methods.md)**
