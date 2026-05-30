# Chapter 5 · @property와 Decorator

**소재:** 게임 캐릭터 시스템  
**핵심 질문:** "hero.get_hp() 매번 쓰기 귀찮은데, hero.hp처럼 쓸 수는 없을까?"

---

## 학습 내용

- Chapter 4의 불편함 되돌아보기
- property class - attribute처럼 쓰는 getter, setter
- decorator @property
- Chapter 4 전투 시스템을 @property로 개선
- decorator란 무엇인가? (@의 정체)
- nested function, closure
- decorator 실전 예제
- 도전 과제

---

## 1. Chapter 4의 불편함 되돌아보기

아래는 Chapter 4에서 안전하게 instance variable에 접근하는 방식으로 학습했던 방식이다.

```python
class Character:
    def __init__(self, name, hp):
        self.name = name
        self.__hp = hp

    def get_hp(self):
        return self.__hp

    def set_hp(self, value):
        if value < 0:
            self.__hp = 0
        else:
            self.__hp = value

hero = Character("Arthur", 100)

# 매번 이렇게 써야 한다
print(hero.get_hp())     # 읽기
hero.set_hp(150)         # 쓰기
```

하지만 우리는 변수에 값을 직접 할당하는 아래와 같은 방식에 익숙하다. (또한 code도 훨씬 간결해 보일 수 있다.)

```python
# hero.hp = 150
# print(hero.hp)
```

> 그래서 Python은 변수에 접근하는 method를 값을 직접 전달하는 형식으로 변형해서 사용할 수 있는 문법을 제공한다.

---

## 2. property class - attribute처럼 쓰는 getter, setter

Python의 `property`는 object에서 일반 변수처럼 직관적으로 접근할 수 있게 해주는 내장 class이다.  
getter, setter, deleter로 사용할 method를 등록하여 instance를 생성하면 object에서 변수처럼 사용할 수 있다.

```python
class Character:
    def __init__(self, name, hp):
        self.name = name
        self.__hp = hp

    def get_hp(self):
        return self.__hp

    def set_hp(self, hp):
        self.__hp = hp

    hp = property(get_hp, set_hp)  # getter와 setter 등록
```

```python
hero = Character("Arthur", 100)
hero.hp = 200
print(hero.hp)  # 200
```

> `get_hp(self)`와 `set_hp(self, hp)`를 `hp`라는 이름의 property object로 생성하여 hero object에서 마치 변수처럼 사용한다.  
> Python에서는 이러한 문법을 좀 더 간결하게 사용할 수 있는 `@property` 문법을 제공한다.

---

## 3. decorator @property

decorator를 사용하면 위 code를 훨씬 간결하게 사용할 수 있다.

```python
class Character:
    def __init__(self, name, hp):
        self.name = name
        self.__hp = hp

    @property               # getter 등록
    def hp(self):
        return self.__hp

    @hp.setter              # setter 등록
    def hp(self, hp):
        self.__hp = hp
```

```python
hero = Character("Arthur", 100)
hero.hp = 200
print(hero.hp)  # 200
```

> getter, setter, deleter로 사용할 method의 앞에 `@~~`를 붙이고 method 이름을 변수처럼 사용할 이름으로 통일하면 된다.  
> 이러한 문법을 decorator라고 한다.  
> 만일 setter를 정의하지 않으면 읽기 전용 attribute가 된다.

---

## 4. Chapter 4 전투 시스템을 @property로 개선

```python
class Character:
    def __init__(self, name, hp, attack_power):
        self.name = name
        self.hp = hp                       # hp.setter 사용
        self.__attack_power = attack_power  # setter가 없으므로 직접 할당

    def __str__(self):
        return f"{self.name} (HP:{self.hp})"

    @property               # self.__hp의 getter
    def hp(self):
        return self.__hp

    @hp.setter              # self.__hp의 setter
    def hp(self, hp):
        # 유효성 검사
        if hp < 0:
            self.__hp = 0
        elif hp > 999:
            self.__hp = 999
        else:
            self.__hp = hp

    @property               # 읽기 전용
    def attack_power(self):
        return self.__attack_power

    @property               # 읽기 전용
    def is_alive(self):
        return self.hp > 0

    def take_damage(self, damage):
        if damage < 0:
            print("Damage는 음수일 수 없습니다.")
            return
        # setter를 통해서 자동 유효성 검사를 할 수 있다.
        self.hp = self.hp - damage
        print(f"{self.name}이 {damage}의 Damage를 받았습니다! (남은 HP: {self.hp})")

    def attack(self, other):
        print(f"{self.name}이 {other.name}을 공격합니다.")
        other.take_damage(self.attack_power)
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
print(f"Goblin 생존 여부: {monster.is_alive}")  # 변수처럼 사용
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

> encapsulation을 위해 내부 instance variable에 접근하는 method를 property를 이용하여 마치 일반 변수처럼 접근할 수 있다.  
> 그 과정에서 값의 유효성 같은 필요한 code 역시 그대로 적용할 수 있으며 필요에 따라 읽기 전용으로 설정할 수도 있다.  
> `attack_power`와 `is_alive`는 읽기 전용이 되었다.

---

## 5. Decorator란 무엇인가? (@의 정체)

위에 살펴본 것처럼 `@property`는 `hp = property(hp)`와 같은 의미이다.  
여기서 `@property`는 `hp(self)`를 property로 감싼다는 의미이다.  
이러한 문법을 decorator라고 한다.

함수를 감싸서 기능을 추가하는 패턴은 이전부터 있었지만 함수의 정의와 함수를 감싸는 부분의 code가 분리되어 있어 코드가 길어지면 가독성이 떨어지게 된다.  
`@decorator`는 함수 바로 위에 명시하여 간결하고 가독성을 높여준다.

만일 여러 가지 인사말을 return하는 함수가 있는 경우, 모두 대문자 형태로 return 되어야 한다고 가정해 보자.  
그러면 대문자로 return하는 함수를 아래와 같이 구성할 수 있다.

```python
def shout(func):
    def wrapper():
        result = func()
        return result.upper()
    return wrapper
```

> shout에 인사말을 return하는 함수를 인자로 전달하면 인사말이 어떤 문자이던지 대문자로 바뀌어 return되는 함수를 만들 수 있다.  
> 함수가 return된다는 것에 주의하자.

### decorator 없이 사용

```python
def greet():
    return "hello world"

def greet_night():
    return "good night"

greet = shout(greet)                # greet를 shout로 감싼다.
greet_night = shout(greet_night)    # greet_night를 shout로 감싼다.

print(greet())
print(greet_night())
```

**출력:**
```
HELLO WORLD
GOOD NIGHT
```

> 여러 가지 필요한 함수들을 `shout(함수명)`으로 통과시키면 공통된 형식을 만들어 주는 함수로 포장할 수 있다.  
> 또한, 이것은 간결한 표현법인 decorator로 작성할 수 있다.

### decorator로 작성

```python
@shout
def greet_morning():
    return "good morning"

print(greet_morning())
```

**출력:**
```
GOOD MORNING
```

> `@shout`는 `greet_morning = shout(greet_morning)`과 같은 의미이다.  
> 함수를 인자로 받아서 새로운 함수를 return하고 있으며 decorator는 이 과정을 간결하게 해주는 문법이다. (Syntactic Sugar라고 한다.)

---

## 6. nested function, closure

decorator의 원리를 조금 더 이해하려면 함수 안에 다른 함수를 정의하는 패턴을 이해해야 한다.

### nested function (중첩 함수)

```python
def order_coffee(size):
    def calculate_price(base):
        if size == "tall":
            return base
        elif size == "grande":
            return base + 500
        elif size == "venti":
            return base + 1000
        return base

    price = calculate_price(4500)
    print(f"{size} 사이즈: {price}원")

order_coffee("tall")      # tall 사이즈: 4500원
order_coffee("grande")    # grande 사이즈: 5000원
order_coffee("venti")     # venti 사이즈: 5500원
# calculate_price("tall") # NameError! 외부에서 직접 호출 불가
```

> 내부(inner) 함수는 외부 함수 안에서만 사용 가능하다.  
> 내부 함수는 외부(outer) 함수의 변수에 접근할 수 있다. (local variable인데 이상하지 않은가?)

### closure

그렇다면 내부 함수에서 어떻게 외부 함수의 parameter나 local variable을 기억할 수 있을까?  
Python은 함수 자체도 class의 object라고 했으니 내부를 파헤쳐 보자.

```python
def order_coffee(size):
    def calculate_price(base):  # 내부 함수는 필요할 때 __closure__ 속성을 갖게 된다.
        if size == "tall":
            return base
        elif size == "grande":
            return base + 500
        elif size == "venti":
            return base + 1000
        return base

    # calculate_price를 정의한 후
    print(dir(calculate_price.__closure__[0]))
    print(calculate_price.__closure__[0].cell_contents)
    price = calculate_price(4500)
    print(f"{size} 사이즈: {price}원")

order_coffee("venti")
```

**출력:**
```
['__class__', '__delattr__', '__dir__', ..., 'cell_contents']
venti
venti 사이즈: 5500원
```

> `__closure__`가 외부 함수의 변수를 저장하면서 만들어진다.  
> `__closure__`는 이렇게 외부 함수의 변수를 사용하고 있을 때 생성되는 속성이다.

### 참고

만일 내부 함수에서 외부 함수의 변수에 쓰기 기능을 부여하려면 `nonlocal` 키워드로 선언한다. (일반 함수의 `global`과 같은 기능)

---

## 7. decorator 실전 예제 - 실행 시간 측정하는 함수

```python
import time

def timer(func):
    def wrapper(n1, n2):        # 모든 parameter 전달받기 위해 *args, **kwargs로 표현할 수 있다.
        start = time.time()
        result = func(n1, n2)   # 모든 parameter 전달받기 위해 *args, **kwargs로 표현할 수 있다.
        end = time.time()
        print(f"{func.__name__}의 실행 시간: {end-start:.4f}초")
        return result
    return wrapper
```

### 명시적 호출 방식 (manual decorator)

```python
def slow_add(a, b):
    time.sleep(3)
    return a + b

slow_add = timer(slow_add)
print(slow_add(3, 7))
```

### decorator 문법 방식

```python
@timer
def slow_add(a, b):
    time.sleep(3)
    return a + b

print(slow_add(3, 7))
```

**출력:**
```
slow_add의 실행 시간: 3.0008초
10
```

> 어떤 함수라도 `@timer`를 붙이면 함수가 실행되면서 시간도 측정된다.  
> 함수 자체와는 상관없이 기능을 추가할 수 있다.  
> parameter의 전달 방식에 유의해야 한다.

---

## 전체 정리

`property` class를 이용하면 class 내부의 method를 attribute처럼 읽기(getter), 쓰기(setter), 삭제(deleter) 기능을 만들 수 있다.

**Decorator:** 함수를 감싸서 기능을 추가하는 문법
- nested function: 중첩 함수
- closure 문법으로 nested의 내부 함수에서 외부 함수의 변수에 접근할 수 있다.
- syntactic sugar 문법으로 `@decorator` 형식으로 간결하게 사용할 수 있다.

이러한 decorator 문법으로 property class를 이용할 수 있다.
- `@property`, `@이름.setter`, `@이름.deleter`

---

## 도전 과제 1 - 은행 계좌 개선 (BankAccount)

### 조건

Chapter 4의 BankAccount를 가져와 `@property`로 개선하라.

**BankAccount class 만들기**
- 속성: `owner` (public), `__balance` (private, 초기값 0)
- `@property balance`: 잔액 읽기
- `@balance.setter`: 음수면 0으로 설정
- `deposit(amount)`: 입금. 0 이하면 `"입금액은 0보다 커야 합니다"` 출력
- `withdraw(amount)`: 출금. 잔액보다 크면 `"잔액이 부족합니다"` 출력
- `__str__`: `"소유자님의 계좌 (잔액: 0원)"` 형태로 출력

**테스트:**
- `account.balance`로 잔액을 읽어라. (`get_balance()`가 아닌!)
- 입금, 출금 후 balance를 확인하라.
- 잔액보다 큰 금액을 출금 시도하라.

---

## 도전 과제 2 - 학생 성적 개선 (Student)

### 조건

Chapter 4의 Student를 `@property`로 개선하라.

**Student class 만들기**
- 속성: `name` (public), `__scores` (private, 빈 리스트)
- `add_score(score)`: 점수 추가. 0~100 범위가 아니면 `"유효하지 않은 점수입니다"` 출력
- `@property average`: 평균 점수 반환 (읽기 전용). 점수가 없으면 0 반환
- `@property highest`: 최고 점수 반환 (읽기 전용)
- `@property scores`: 전체 점수 리스트 반환 (읽기 전용)
- `__str__`: `"이름 (평균: 00.0점, 최고: 00점)"` 형태로 출력

**테스트:**
- `student.average`로 평균을 읽어라. (`get_average()`가 아닌!)
- `student.scores`로 점수 리스트를 읽어라.
- `student.average = 100`을 시도하라. (읽기 전용 에러 확인)

---

**[Chapter 6 · class variable, class method, staticmethod →](06_class_variable_class_method_staticmethod.md)**
