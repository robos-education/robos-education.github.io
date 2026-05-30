

# ### 조건

# 각 몬스터는 기본 Monster와 다른 고유한 공격 방식을 가지고 있다.
# 기본 공격이 맞지 않는 몬스터는 완전히 새로 쓰고,
# 기본 공격에 추가 동작이 필요한 몬스터는 super()를 활용하라.

# **Monster 클래스 만들기**
# - 속성: `name`, `hp`, `attack_power`
# - 메서드: `attack()` → `"{name} Attacks!! Deals {attack_power} damage"` 반환

# **Monster를 상속받아 3종류의 몬스터 만들기**
# - `Slime` : 기본 공격과 완전히 다름(공격력이 1/2) → attack override → `"{name} Sticks!! Deals {damage} damage"` 반환
# - `Dragon` : 기본 공격과 완전히 다름(공격력이 x2) → attack override → `"{name} Breathes fire!! Deals {damage} damage"` 반환
# - `Mimic` : 기본 공격 앞에 추가 대사 → attack override → `"Thought it was a treasure chest, didn't you?"` + 기본 공격(super() 활용) 반환

# **몬스터 리스트를 만들고 `for` 문으로 전부 `attack()`을 실행하라.**

# **(추가)** 새로운 몬스터 `Ghost`를 추가하라. (`attack_power` → 5)
# - 기본 공격 앞에 추가 대사 → attack override → `"유령이라 공격이 매우 약해"` + 기본 공격(super() 활용)
# - `for` 문을 수정하지 않고 동작하는지 확인하라. (Polymorphism)

class Monster:

    def __init__(self, name, hp, attack_power=30):
        self.name = name
        self.hp = hp
        self.attack_power = attack_power
    
    def attack(self):

        return  f"{self.name} Attack!! Deals {self.attack_power} damage!!"

class Slime(Monster):

    def attack(self):
        damage = self.attack_power * 0.5
        return f"{self.name} Sticks!! Deals {damage} damage"

class Dragon(Monster):

    def attack(self):
        damage = self.attack_power * 2
        return f"{self.name} Breathes!! Deals {damage} damage"

class Mimic(Monster):

    def attack(self):
        return f"Thought it was a treasure chest, did't you?" + super().attack()

class Ghost(Monster):
    
    def attack(self):
        return f"{self.name}'s Attack Power is very low. " + super().attack()

# test
monsters = [Slime("슬라임", 100, 50), Dragon("드래곤", 50, 150), Mimic("미믹", 60, 10)]
monsters.append(Ghost("유령", 20, 5))

for member in monsters:
    print(member.attack())


# 출력
    # 슬라임 Sticks!! Deals 25.0 damage
    # 드래곤 Breathes!! Deals 300 damage
    # Thought it was a treasure chest, did't you?미믹 Attack!! Deals 10 damage!!
    # 유령's Attack Power is very low. 유령 Attack!! Deals 5 damage!!

# 설명: Ghost를 추가 했지만 for 문은 한 줄도 수정하지 않았다. Polymerphism이라고 한다.