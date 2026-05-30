# Chapter 3 · Special Methods (Dunder Methods)

**소재:** 게임 캐릭터 시스템  
**핵심 질문:** "내가 만든 object를 print하면 왜 이상한 게 나올까?"

---

## Dunder Method란?

`__method__` 형태의 special method를 말한다. (double underscore method)  
Python이 특정 상황에서 자동으로 호출하는 method이다.

예: 
- `print(obj)` → `__str__()` 호출  
- `==` → `__eq__()` 호출

---

## 아래 코드에서 hero를 출력하면 무엇이 실행될까?

```python
class Character:
    def __init__(self, name, hp, level):
        self.namve = name
        self.hp = hp
        self.level = level

hero = Character("Arthur", 100, 5)
print(hero)  # <__main__.Character object at 0x...> ← 이게 뭐지?
```

Python에서 모든 class는 기본적으로 `object` class를 상속한다.  
따라서 이러한 dunder method는 `object` class에 정의된 method들이다.

```python
print(dir(object))  # object에 정의된 dunder method 목록을 확인할 수 있다.
```

---

## 1. `__str__()`과 `__repr__()` - 출력 관련

```python
class Character:
    def __init__(self, name, hp, level):
        self.name = name
        self.hp = hp
        self.level = level

    def __str__(self):
        return f"[Lv.{self.level}] {self.name} (HP: {self.hp})"

    def __repr__(self):
        return f"Character('{self.name}', {self.hp}, {self.level})"
```

```python
hero = Character("Arthur", 100, 5)
print(hero)         # __str__ 호출
print(repr(hero))   # __repr__ 호출
```

**출력:**
```
[Lv.5] Arthur (HP: 100)
Character('Arthur', 100, 5)
```

> `__str__`: 사용자에게 보여주는 읽기 쉬운 문자열로 사용 (print(), str()에서 호출)  
> `__repr__`: 개발자를 위한 정확한 문자열로 사용 (repr()에서 호출)

### 사용 예제: object를 list에 담아서 출력하는 경우

```python
party = [
    Character("Arthur", 100, 5),
    Character("Merlin", 80, 7),
    Character("Aria", 60, 3)
]

# __str__이 호출된다.
for member in party:
    print(member)       # print(f"{member!r}") __repr__() 호출

# __repr__이 호출된다.
print(party)
```

**출력:**
```
[Lv.5] Arthur (HP: 100)
[Lv.7] Merlin (HP: 80)
[Lv.3] Aria (HP: 60)
[Character('Arthur', 100, 5), Character('Merlin', 80, 7), Character('Aria', 60, 3)]
```

> `print(hero)` → hero의 `__str__` 호출  
> `print(party)` → 리스트의 `__str__` 호출 → 각 요소는 `__repr__` 호출
> 또는 f-string은 기본적으로 __str__을 호출하지만, 뒤에 !r을 붙이면 강제로 __repr__을 호출하게 할 수 있다.
---

## 2. `__eq__`, `__lt__` 등 - 비교 연산

아래와 같이 같은 속성을 갖는 object를 비교 연산한다면?

```python
hero1 = Character("Arthur", 100, 5)
hero2 = Character("Arthur", 100, 5)
print(hero1 == hero2)  # False ← 왜?
```

기본 `==` 비교는 메모리 주소를 비교한다 (같은 object인지 확인).  
만일 같은 속성의 object를 True로 평가하는 `==` 연산자를 만들려면 `__eq__` method를 override하면 된다.

### 사용 예제

요구 사항: name과 level이 같으면 같은 Character로 판단한다. `<` 연산은 level로 판단한다.

```python
class Character:
    def __init__(self, name, hp, level):
        self.name = name
        self.hp = hp
        self.level = level

    def __str__(self):
        return f"[Lv.{self.level}] {self.name} (HP: {self.hp})"

    def __repr__(self):
        return f"Character('{self.name}', {self.hp}, {self.level})"

    # 값의 비교(equality)로 override
    def __eq__(self, other):
        return self.name == other.name and self.level == other.level

    # less than의 override
    def __lt__(self, other):
        return self.level < other.level
```

```python
hero1 = Character("Arthur", 100, 5)
hero2 = Character("Arthur", 80, 5)
hero3 = Character("Merlin", 80, 7)

print(hero1 == hero2)   # True  ← 이름과 레벨이 같으므로
print(hero1 == hero3)   # False
print(hero1 < hero3)    # True  ← 레벨 5 < 레벨 7
print(hero3 < hero1)    # False
```

**출력:**
```
True
False
True
False
```

### Character를 level 순서로 정렬하기

```python
party = [hero1, hero2, hero3]
sorted_party = sorted(party)  # sorted()는 내부적으로 __lt__을 사용한다.

for member in sorted_party:
    print(member)
```

**출력:**
```
[Lv.5] Arthur (HP: 100)
[Lv.5] Arthur (HP: 80)
[Lv.7] Merlin (HP: 80)
```

### 참고

그런데 지금까지 사용했던 `==` 연산자는 어떻게 값을 비교하고 있었을까?  
이것은 Python 내부의 `int`, `float`, `str` 등의 class가 `__eq__` method를 override하고 있기 때문이다.

- 값의 비교: equality (동등성)
- 메모리 주소 비교: identity (동일성)

### 비교 연산자 method 정리

| 연산자 | method |
|--------|--------|
| `==` | `__eq__` |
| `!=` | `__ne__` |
| `<` | `__lt__` |
| `<=` | `__le__` |
| `>` | `__gt__` |
| `>=` | `__ge__` |

---

## 3. `__add__`, `__mul__` 등 - 산술 연산

Character의 `+` 연산을 통하여 HP가 더해진 새로운 Character 생성하기.  
Character의 `*` 연산을 통하여 HP가 몇 배 증가한 새로운 Character 생성하기.

```python
class Character:
    def __init__(self, name, hp, level):
        self.name = name
        self.hp = hp
        self.level = level

    def __str__(self):
        return f"[Lv.{self.level}] {self.name} (HP: {self.hp})"

    def __repr__(self):
        return f"Character('{self.name}', {self.hp}, {self.level})"

    def __eq__(self, other):
        return self.name == other.name and self.level == other.level

    def __lt__(self, other):
        return self.level < other.level

    # + 연산 override
    def __add__(self, other):
        new_name = f"{self.name}_{other.name}"
        new_hp = self.hp + other.hp
        new_level = self.level + other.level
        return Character(new_name, new_hp, new_level)

    # * 연산 override: HP n배 강화
    def __mul__(self, n):
        new_hp = self.hp * n
        return Character(self.name, new_hp, self.level)
```

```python
arthur = Character("Arthur", 100, 5)
mage = Character("Merlin", 80, 7)

# Character 합체
aurage = arthur + mage
print(aurage)

# HP 강화 Character 생성
super_arthur = arthur * 3
print(super_arthur)
```

**출력:**
```
[Lv.12] Arthur_Merlin (HP: 180)
[Lv.5] Arthur (HP: 300)
```

### 산술 연산자 method 정리

| 연산자 | method |
|--------|--------|
| `+` | `__add__` |
| `-` | `__sub__` |
| `*` | `__mul__` |
| `/` | `__truediv__` |

---

## 4. `__len__`, `__getitem__` - 내 object를 리스트처럼 사용하기

Python에서 컨테이너(container)란 `list`, `dict`, `tuple`처럼 여러 데이터를 담고 있는 object를 말한다.  
`__len__`, `__getitem__` 등을 정의하면 내 object도 리스트처럼 동작하게 만들 수 있다. (Emulating container types)

```python
class Inventory:
    def __init__(self, owner):
        self.owner = owner
        self.items = []

    def add(self, item):
        self.items.append(item)
        print(f"{self.owner}가 '{item}'을 획득하였습니다.")

    def __len__(self):
        return len(self.items)

    def __getitem__(self, index):
        if index < 0 or index >= len(self.items):
            print(f"{self.owner}의 인벤토리에 {index}칸은 없습니다.")
            return None
        return self.items[index]

    def __str__(self):
        return f"{self.owner}의 인벤토리 [{len(self)}칸]: {', '.join(self.items)}"
```

```python
# 인벤토리 사용
bag = Inventory("Arthur")
bag.add("롱소드")
bag.add("체력 포션")
bag.add("마법 방패")

# 소유한 아이템의 개수
print(f"보유 아이템 수: {len(bag)}")

# 소유한 아이템에 접근
print(f"첫 번째 아이템: {bag[0]}")
print(f"10 번째 아이템: {bag[10]}")
```

**출력:**
```
Arthur가 '롱소드'을 획득하였습니다.
Arthur가 '체력 포션'을 획득하였습니다.
Arthur가 '마법 방패'을 획득하였습니다.
보유 아이템 수: 3
첫 번째 아이템: 롱소드
Arthur의 인벤토리에 10칸은 없습니다.
10 번째 아이템: None
```

> `__getitem__`은 `[]` (subscript 연산자)를 사용할 때 호출되는 method이다.  
> `+`를 쓰면 `__add__`가 호출되는 것처럼, `[]`를 쓰면 `__getitem__`이 호출된다.

### 컨테이너 관련 method 정리

| 사용 방법 | method |
|-----------|--------|
| `len(obj)` | `__len__` |
| `obj[i]` | `__getitem__` |
| `x in obj` | `__contains__` |
| `for x in obj` | `__iter__` |

### 참고

컨테이너(container)란 다른 object를 포함할 수 있는 저장소 역할의 object이다. 여러 개의 data를 가질 수 있으며, `in` 연산자 동작을 정의하는 `__contains__(self, item)`가 포함되어 있다. `list`, `tuple`, `set`, `dict`, `str` 등이 해당된다.

---

## 전체 정리

Python은 상황에 맞는 dunder method를 자동으로 호출한다.

| 상황 | 호출되는 method |
|------|----------------|
| `print(obj)` | `__str__` |
| `repr(obj)` | `__repr__` |
| `obj1 == obj2` | `__eq__` |
| `obj1 < obj2` | `__lt__` |
| `sorted(list)` | `__lt__` |
| `obj1 + obj2` | `__add__` |
| `obj * n` | `__mul__` |
| `len(obj)` | `__len__` |
| `obj[i]` | `__getitem__` |

---

## 도전 과제 1 - 온라인 쇼핑몰 상품 (Product)

### 조건

**Product class 만들기**
- 속성: `name`, `price`, `quantity`
- `__str__`: `"상품명: 가격원 (재고: 수량개)"` 형태로 출력
- `__eq__`: 상품명과 가격이 같으면 같은 상품으로 판단
- `__lt__`: 가격 기준으로 비교 (sorted 가능하도록)
- `__add__`: 같은 상품이면 수량을 합친 새 Product 반환. 다른 상품이면 `"다른 상품은 합칠 수 없습니다"` 출력 후 self 반환

**테스트:**
- Product 3개를 만들어 리스트에 넣고 가격순으로 정렬해서 출력하라.
- 같은 상품 2개를 만들고 `+` 연산으로 새로운 상품을 만들어라.

---

## 도전 과제 2 - 음악 플레이리스트 (Playlist)

### 조건

**Song class 만들기**
- 속성: `title`, `artist`, `duration` (초 단위)
- `__str__`: `"아티스트 - 제목 (0분 00초)"` 형태로 반환
- `__eq__`: 제목과 아티스트가 같으면 같은 곡 (이미 포함된 곡 체크)

**Playlist class 만들기**
- 속성: `name`, `songs` (빈 리스트)
- `add(song)`: 곡 추가
- `__len__`: 곡 수 반환
- `__getitem__`: 인덱스로 곡 정보 반환
- `__str__`: `"플레이리스트명 (곡 수곡, 총 재생시간)"` 형태로 반환
- `__add__`: 두 플레이리스트를 합쳐서 새 Playlist 반환

**테스트:**
- Playlist 2개를 만들고 각각 곡을 2~3곡 추가하라. (중복 테스트)
- 두 플레이리스트를 `+` 연산으로 합쳐보라.
- 합쳐진 플레이리스트에서 `for` 문으로 모든 곡을 출력하라.
- running time 순으로 정렬하라.

---

**[Chapter 4 · 속성 숨기기와 캡슐화 →](04_encapsulation.md)**
