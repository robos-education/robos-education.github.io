# Chapter 6 · class variable, class method, staticmethod

**소재:** 게임 캐릭터 시스템  
**핵심 질문:** "모든 Character가 공유하는 data는 어디에 저장하는가?"

---

## 학습 내용

- instance variable vs class variable
- class variable 활용
- class method (@classmethod)
- static method (@staticmethod)
- 도전 과제

---

## 1. instance variable vs class variable

문제 상황: 지금까지 생성된 Character의 총 수를 알고 싶다.  
각 instance에 저장하면 각자 따로 가지고 있어서 전체의 수를 알 수 없다.

```python
class Character:
    # class variable: 모든 instance가 공유한다.
    # class 자체도 object이기 때문에 class의 __dict__에 저장된다.
    total_count = 0
    max_level = 99

    def __init__(self, name, hp, level):
        # instance variable: 각 instance가 개별적으로 가지는 변수
        self.name = name
        self.hp = hp
        self.level = level
        Character.total_count += 1  # 캐릭터가 생성될 때마다 +1

    def __str__(self):
        return f"[Lv.{self.level}] {self.name} (HP: {self.hp})"
```

```python
# Character 생성
hero = Character("Arthur", 100, 5)
mage = Character("Merlin", 60, 7)
healer = Character("Aria", 50, 3)

# class variable은 class 이름으로 접근한다.
print(f"총 캐릭터 수: {Character.total_count}")   # 3
print(f"최대 레벨: {Character.max_level}")        # 99

# instance에서 접근 시도
print(f"총 캐릭터 수: {hero.total_count}")         # 3
hero.total_count = 10                              # hero에 새로운 instance variable이 생성된 것
print(f"총 캐릭터 수: {hero.total_count}")         # 10 ← Character.total_count와는 별개의 변수
```
---
설명: 
> `instance variable` (self.name): 각 object가 개별적으로 소유  
> `class variable` (Character.total_count): 모든 object가 공유  
>  
> 만일 object에서 class variable에 접근하면  
> → 읽기는 가능  
> → 쓰기를 하는 순간 instance variable이 새로 생성된다. (함수 안에서의 변수 사용법과 비슷)  
>  
> class variable은 `Class명.변수명`으로 접근하는 것이 원칙이다.

---

## 2. class method (@classmethod)

class method는 instance가 아닌 class 자체를 다루는 method이다.  
첫 번째 parameter로 class 자신을 가리키는 변수(관례적으로 `cls`)를 넣는다.
decorator 문법을 시용하여 간결하게 정의할 수 있다.

```python
class Character:
    total_count = 0
    max_level = 99

    def __init__(self, name, hp, level):
        self.name = name
        self.hp = hp
        self.level = level
        Character.total_count += 1

    def __str__(self):
        return f"[Lv.{self.level}] {self.name} (HP: {self.hp})"

    # class method: 주로 class variable을 다루는 method
    # get_total_count = classmethod(get_total_count)의 간결한 문법
    @classmethod
    def get_total_count(cls):
        return cls.total_count

    # set_max_leve = classmathod(set_max_level)
    @classmethod
    def set_max_level(cls, value):
        if value < 1:
            print("최대 레벨은 1이상 이어야 한다.")
            return
        cls.max_level = value
        print(f"최대 레벨이 {value}로 변경되었습니다.")

    # create_character = classmethod(creat_character)
    # class method로 object를 생성하는 패턴 (Factory Method)
    @classmethod
    def create_character(cls, name, hp, level):
        return cls(name, hp, level)
```

```python
# class method는 class 이름으로 호출한다
print(f"총 캐릭터 수: {Character.get_total_count()}")  # 0

hero = Character("Arthur", 100, 5)
mage = Character("Merlin", 80, 7)
print(f"총 캐릭터 수: {Character.get_total_count()}")  # 2

# 최대 레벨 변경
Character.set_max_level(60)

# factory method를 이용하여 Character 생성
warrior = Character.create_character("전사", 200, 40)
wizard = Character.create_character("마법사", 80, 50)
print(warrior)
print(wizard)
print(f"총 캐릭터 수: {Character.get_total_count()}")  # 4
```

**출력:**
```
총 캐릭터 수: 0
총 캐릭터 수: 2
최대 레벨이 60로 변경되었습니다.
[Lv.40] 전사 (HP: 200)
[Lv.50] 마법사 (HP: 80)
총 캐릭터 수: 4
```

---
설명:
> `@classmethod` decorator를 이용하여 class method를 정의한다. 
> 첫 번째 parameter `cls`는 class를 가리키는 변수가 된다. (명시가 없으면 object로 인식하게 될 것이다.)  
>  
> class variable을 읽거나 수정할 때 사용한다.  
> 팩토리 메서드 정의에 사용된다.  
> instance 없이 `Class이름.method()`로 호출한다.

---

## 3. static method (@staticmethod) - decorator 사용

class나 instance의 내용과 별개인 독립적인 기능을 class 내부에 두고 관리하기 위한 문법이다.  
`self`, `cls`와 같은 parameter를 갖지 않는다.  
주로 관련은 있지만 class/instance data가 필요하지 않는 유틸리티 함수에 주로 사용한다.

class method나 instance method, 혹은 외부의 함수로 대체가 가능하지만 몇 가지 이유가 있다.

- 설계의 의도를 명확하게 한다. (이 함수는 class나 instance data를 변경하지 않는 그냥 유틸리티 함수!)
- 수천 개의 instance를 생성하더라도 staticmethod는 instance마다 별도의 바인딩 object를 생성하지 않는다. (memory 절약)
- 상속에서의 불필요한 간섭 방지

```python
class Character:
    total_count = 0
    max_level = 99

    def __init__(self, name, hp, level):
        self.name = name
        self.hp = hp
        self.level = level
        Character.total_count += 1

    def __str__(self):
        return f"[Lv.{self.level}] {self.name} (HP: {self.hp})"

    # is_valid_name = staticmethod(is_valid_name)
    @staticmethod
    def is_valid_name(name):
        if len(name) < 2:
            return False
        elif len(name) > 20:
            return False
        return True

    # calculate_damage = staticmethod(calculate_damage)
    @staticmethod
    def calculate_damage(attack, defense):
        damage = attack - defense
        if damage < 0:
            damage = 0
        return damage
```

```python
# static method는 class 이름으로 호출한다.
print(Character.is_valid_name("A"))          # False (너무 짧음)
print(Character.is_valid_name("Arthur"))     # True
print(Character.is_valid_name("A" * 21))     # False (너무 김)

print(Character.calculate_damage(50, 30))    # 20
print(Character.calculate_damage(10, 30))    # 0 (음수 방지)
```

**출력:**
```
False
True
False
20
0
```

---
설명: 
> `@staticmethod` decorator를 이용하여 static method를 정의한다.  
> `self`, `cls` 같은 parameter를 정의하지 않는다. (별도의 바인딩 object를 만들지 않는다.)  
> class/instance의 data에 접근할 필요가 없는 함수에 사용한다.  
> class 외부에 일반 함수로 만들어 사용할 수 있지만, class 안에 두고 관련 기능을 묶어서 관리할 수 있다.

### object에서 호출한다면?

```python
class Warrior(Character):
    @staticmethod
    def is_valid_name(name):
        return len(name) >= 3  # 전사는 3글자 이상

hero = Warrior("Arthur", 100, 5)

# 의도가 무엇인지 혼란스러울 수 있다.
hero.is_valid_name("Ab")       # False (Warrior의 것 호출)
Character.is_valid_name("Ab")  # True (Character의 것 호출)
```

> class 전역에서 사용하려는 목적에 맞게 사용하는 것이 원칙이다.  
> 미세한 탐색 차이도 있다. (override가 없다면 탐색 순서: object → class)  
> 또한 staticmethod에서 class member에 접근하면 (하드 코딩으로) 상속 대상이 불분명해질 수 있다.

---

## 세 가지 method 비교

| 구분 | decorator | 첫 번째 parameter | 접근 가능 대상 |
|------|-----------|-------------------|----------------|
| instance method | 없음 | `self` | instance variable, class variable |
| class method | `@classmethod` | `cls` | class variable만 |
| static method | `@staticmethod` | 없음 | 독립 함수 |

### 언제 사용하는가?

- **instance method**: 각 object의 data를 다룰 때
- **class method**: class 전체에 적용되는 data를 다루거나 factory method를 만들 때
- **staticmethod**: class와 관련된 유틸리티 함수를 묶어서 사용할 때

---

## 도전 과제 1 - 직원 관리 시스템 (Employee)

### 조건

**Employee class 만들기**
- class variable: `employee_count` (총 직원 수, 초기값 0), `company_name`
- instance variable: `name`, `position`, `salary`
- `__init__`: 직원 생성 시 `employee_count` 증가
- `__str__`: `"이름 (직책) - 연봉: 0원"` 형태로 출력
- `@classmethod get_employee_count(cls)`: 총 직원 수 반환
- `@classmethod set_company_name(cls, name)`: 회사명 변경
- `@classmethod create_intern(cls, name)`: 인턴 생성 (position="인턴", salary=24000000)
- `@staticmethod is_valid_salary(salary)`: 급여가 0 이상이면 True

**테스트:**
- 직원 3명을 생성하라. (1명은 create_intern으로)
- 총 직원 수를 출력하라.
- 회사명을 변경하고 확인하라.
- is_valid_salary로 유효성 검사를 테스트하라.

---

## 도전 과제 2 - 온도 변환기 (Temperature)

### 조건

**Temperature class 만들기**
- class variable: `conversion_count` (총 변환 횟수, 초기값 0)
- instance variable: `celsius` (섭씨 온도)
- `__str__`: `"현재 온도: 00°C"` 형태로 출력
- `to_fahrenheit()`: 화씨로 변환한 값 반환 (공식: celsius * 9/5 + 32)
- `@classmethod from_fahrenheit(cls, f)`: 화씨를 받아서 Temperature object 생성
- `@classmethod get_conversion_count(cls)`: 총 변환 횟수 반환
- `@staticmethod is_boiling(celsius)`: 100도 이상이면 True
- `@staticmethod is_freezing(celsius)`: 0도 이하이면 True

**테스트:**
- 섭씨 온도로 Temperature를 만들고 화씨로 변환하라.
- from_fahrenheit로 화씨에서 Temperature를 만들어라.
- is_boiling, is_freezing을 테스트하라.

---

**[Chapter 7 · 실전 프로젝트 + AI 바이브코딩 →](07_project_ai_vibe_coding.md)**
