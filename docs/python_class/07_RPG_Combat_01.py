
# 프로젝트 1: 텍스트 RPG 전투 게임

# 핵심 class 구현

# 주요 내용

    # class Character에서 ===================================
    # 모든 Charater(Monster 포함)의 parents class
    # 공통 속성: 
        # name: 이름, public - 외부(child class 포함)에서 자유롭게 접근
        # __HP: 현재 HP, private - property로만 접근 가능(읽기, 쓰기)
        # __max_hp: 최대 HP, private - 레벨업 시에 증가 시킴
        # __attack_power: 공격력, private - 읽기 전용
        # __defense: 방어력, private - 읽기 전용
        # __exp: 경험치, private - gain_exp()로만 증가
        # __level: 레벨,  private - 읽기 전용, 레벨업 시 자동증가
        # Character.total_count: Character 생성 시 +1 

    # 출력 관련

        # __str__(self)
        # __repr__(self)
    
    # 상태 정보

        # is_alive(self): 생존 여부, property로 읽기 전용
        
    # 공통 기능:
        # take_damage(self, damage): 피격, 실제 적용 damage return(현재는 필요 없음)
        # attack(self, other): 공격, 주로 child character에서 override
        # special(self): 특수 능력, 주로 child character에서 override
        # gain_exp(self, amount): 경험 획득(레벨업 판단하여 실행)
        # __level_up(self): 레벨업 class, name mangling으로 현재 class에서만 접근 가능(현재 class의 gain_exp()에서만 접근 가능하게 한다.)

    # classmethod:
        # get_total_count(cls): 
    # staticmethod:
        # calculate_damage(attack, defense): 공격량과 방어량을 계산해서 실제 적용되는 damage를 return하는 utility
    # ==================================================== 

    # class Warrior에서 ===================================
    # 특징: HP와 방어력이 높음
    # self.__rage = 0 분노 게이지가 축척되면 강력한 특수 능력을 할 수 있다.
    # special(self, other): 분노가 30이상이면 special 공격을 할 수 있다.
    # ====================================================

    # class Wizard에서 ====================================
    # 특징: 공격력은 높고 HP와 방어력은 낮음
    # self.__mana: private - 공격 시 mana 시스템을 사용한다.
    # attack(self, other): mana가 10이상이면 강력한 화살 마법(마법 손실 10), 아니면 약한 지팡이 마법(마법 손실 없음)
    # special(self, other): mana가 40이상이면 fire ball(공격력의 3배)
    # =====================================================

    # class Healer에서 =====================================
    # 특징: 균형잡힌 stats, 치유 능력으로 character(자신 포함)의 hp를 회복
    # self.__mana: 80, private - 치유 능력에서 사용한다.

    # class Monster에서 ====================================
    # 특징: 속성을 character마다 다르게 적용하여 여러 종류의 Monster를 만들 수 있게 한다 
    # self.__exp_reward: private - Monster를 물리치면 Character에게 부여되는 경험치
    # create_random(): difficulty에 따라 랜덤으로 monster가 생성(factory method)
    # difficulty 1: 슬라임만 등장
    # difficulty 2: 슬라임 고블린 중 랜덤
    # difficulty 3: 슬라임, 고블린, 오크 중 랜덤
    # difficulty 4: 슬라임, 고블린, 오크, 드래곤 중 랜덤
    # ========================================================

import random

class Character:

    total_count = 0     # 생성된 전체 Character 수(class variable)

    def __init__(self, name, hp, attack_power, defense):
        
        self.name = name                    # public
        self.__max_hp = hp                  # private - 최대 hp
        self.hp = hp                        # setter를 통해 유효성 검사 통과하여 self.__hp 설정, property에 self.__max_hp가 언급되어 있어서 아래 정의해야 한다.
        self.__attack_power = attack_power  # private - 공격력
        self.__defense = defense            # private - 방어력
        self.__exp = 0                      # private - 경험치 값
        self.__level = 1                    # private - 레벨
        Character.total_count += 1          # Character 수 증가

    # --- 출력 관련 ---
    def __str__(self):      # 사용자에게 보여주는 Character의 상태

        return f"[Lv.{self.__level}] {self.name} (HP: {self.__hp}/{self.__max_hp})"
    
    def __repr__(self):     # debugging용 상세 정보

        return f"Character('{self.name}', {self.__hp}, {self.__attack_power}, {self.__defense})"
    
    # --- property: 외부에서 변수처럼 접근 ---
    @property
    def hp(self):
        return self.__hp
    @hp.setter
    def hp(self, value):
        
        # 유효성 검사
        if value < 0:
            self.__hp = 0
        elif value > self.__max_hp:
            self.__hp = self.__max_hp
        else:
            self.__hp = value
    
    @property
    def attack_power(self):
        return self.__attack_power

    @property
    def defense(self):
        return self.__defense

    @property
    def level(self):
        return self.__level

    @property
    def is_alive(self):
        # 생존 여부 return
        return self.__hp > 0

    # --- 전투 관련 method ---
    # 피격
    def take_damage(self, damage):
        
        # 실제 damage는 받은 damage에서 방어력을 뺀 값이다.
        actual_damage = Character.calculate_damage(damage, self.__defense)
        # setter를 통해 유효성 검사 통과
        self.hp = self.__hp - actual_damage
        print(f"    {self.name}이 {actual_damage}의 데미지를 받았다! (남은 HP: {self.__hp})")
        return actual_damage

    # 공격 - 자신의 공격력으로 상대에게 damage를 준다.
    def attack(self, other):
        # 각 character에서 override하여 다른 공격 방식을 구현할 수 있다.
        print(f"\n⚔ {self.name}이 {other.name}을 공격!")
        other.take_damage(self.__attack_power)

    def special(self):
        # 각 character마다 override하여 특수한 능력을 수행한다.
        return f"{self.name}: 특수 능력 없음"

    # --- 성장 관련 method ---
    def gain_exp(self, amount):
    
        # 경험치 획득 후 조건에 맞는 레벨업 실행
        self.__exp += amount
        print(f"    {self.name}이 경험치 {amount}를 획득! (총 경험치: {self.__exp})")

        while self.__exp >= self.level * 100: # 레벨이 두 단계 올라갈 수도 있다.
            self.__level_up()


    def __level_up(self):

        self.__level += 1
        self.__max_hp += 20
        self.__hp = self.__max_hp   # 최대치로 회복
        self.__attack_power += 5
        self.__defense += 3
        print(f"    🎉 레벨 업! {self.name} → Lv.{self.__level}!")


    # --- class method / static method ---
    @classmethod
    def get_total_count(cls):
        return cls.total_count

    @staticmethod
    def calculate_damage(attack, defense):
        damage = attack - defense
        if damage < 1:     # 방어력이 아무리 높아도 1의 damage는 받는다.
            damage = 1
        return damage     

# --- 직업 class 구현 (inheritance + override) ---

class Warrior(Character):

    def __init__(self, name):
        super().__init__(name, hp=150, attack_power=25, defense=15)
        self.__rage = 0     # private - 분노 게이지
    
    # Warrior의 일반 공격, 분노값 축척
    def attack(self, other):

        print(f"\n⚔ {self.name}이 {other.name}에게 강력한 검 베기!")
        self.__rage += 10
        other.take_damage(self.attack_power)
    
    # 전사의 special 공격: 분노 폭발(분노 30 이상 필요)
    def special(self, other):

        if self.__rage >= 30:
            print(f"\n🔥 {self.name}의 분노 폭발!")
            self.__rage = 0
            # self.__attack_power는 parents의 name mangling이기 때문에 child에서는 property로 접근
            other.take_damage(self.attack_power * 2)
        else:
            print(f"    분노가 부족합니다. (현재: {self.__rage}/30)")
    
    # Warrior의 상태 출력
    def __str__(self):
        return f"[Lv.{self.level}] ⚔ 전사 {self.name} (HP: {self.hp}) [분노: {self.__rage}]"

class Wizard(Character):

    def __init__(self, name):
        super().__init__(name, hp=80, attack_power=35, defense=8)
        self.__mana = 100       # private - 공격 능력치
    
    # Wizard의 일반 공격: 마나에 따라 다른 공격
    def attack(self, other):

        if self.__mana >= 10:
            print(f"\n🔮 {self.name}이 {other.name}에게 마법 화살 발사!")
            self.__mana -= 10
            other.take_damage(self.attack_power)
        else:
            print(f"\n👊 {self.name}이 {other.name}을 지팡이로 때린다! (마나 부족)")
            other.take_damage(5)

    # Wizard의 특수 능력: Fire Ball(마나 40 소모)
    def special(self, other):
        
        if self.__mana >= 40:
            print(f"\n🌋 {self.name}의 파이어볼!")
            self.__mana -= 40
            other.take_damage(self.attack_power * 3)
        else:
            print(f"    마나가 부족합니다! (현재: {self.__mana}/40)")

    # Wizard의 상태 출력
    def __str__(self):
        return f"[Lv.{self.level}] 🔮 마법사 {self.name} (HP: {self.hp}) [마나: {self.__mana}]"

class Healer(Character):

    def __init__(self, name):
        
        super().__init__(name, hp=100, attack_power=15, defense=10)
        self.__mana = 80            # private - 치유능력에 사용
    
    # Healer의 일반 공격: 빛의 화살
    def attack(self, other):

        print(f"\n✨ {self.name}이 {other.name}에게 빛의 화살!")
        other.take_damage(self.attack_power)
    
    # Healer의 특수 능력: 치유 40(마나 30 소모)
    def special(self, target=None):

        # target이 None이면 자신을 치유한다.
        if self.__mana >= 30:
            if target is None:
                target = self
            heal_amount = 40
            print(f"\n💚 {self.name}의 치유! {target.name}의 HP +{heal_amount}")
            self.__mana -= 30           # 마나 소모
            target.hp += heal_amount    # Character의 setter를 호출한다.(유효성 검사 통과)
            print(f"    {target.name}의 현재 HP: {target.hp}")
        else:
            print(f"    마나가 부족합니다! (현재: {self.__mana}/30)")
    
    # Healer의 상태 출력
    def __str__(self):
        return f"[Lv.{self.level}] 💚 힐러 {self.name} (HP: {self.hp}) [마나: {self.__mana}]"
    

# --- Monster class 구현 ---

class Monster(Character):

    monster_count = 0       # 생성된 전체 Monster 수, class variable)

    def __init__(self, name, hp, attack_power, defense, exp_reward):

        super().__init__(name, hp, attack_power, defense)
        self.__exp_reward = exp_reward
        Monster.monster_count += 1
    
    @property
    def exp_reward(self):
        return self.__exp_reward
    
    # Monster의 상태 출력
    def __str__(self):
        return f"👾 {self.name} (HP: {self.hp})"
    
    @classmethod
    def create_random(cls, difficulty=2):
        
        # difficulty에 따라 등장 가능한 Monster의 범위를 제한하여 random 생성
        # Monster의 종류(name, HP, attack_power, defense, exp_reward)
        monsters = [
            ("슬라임", 40, 20, 3, 30), # Warrior에게 5 damage
            ("고블린", 70, 30, 5, 50),
            ("오크", 120, 40, 12, 80), 
            ("드래곤", 200, 55, 25, 200),
        ]

        available = monsters[:min(difficulty, len(monsters))]
        data = random.choice(available)
        return cls(*data)


# --- 핵심 class 동작 테스트 ---
# AI에게 전달하기 전에 직접 만든 class가 정상 동작하는지 확인한다.

# 1. Character 생성 테스트
warrior = Warrior("Arthur")
wizard = Wizard("Merlin")
healer = Healer("Aria")
print(warrior)
print(wizard)
print(healer)

# 2. 공격 테스트
warrior.attack(wizard)
wizard.attack(warrior)
healer.attack(warrior)

# 3. 특수 능력 테스트
warrior.attack(wizard)   # 분노 축적
warrior.attack(wizard)   # 분노 축적
warrior.special(wizard)  # 분노 30 → 특수 공격 가능
wizard.special(warrior)  # 파이어볼
healer.special()         # 자기 자신 치유

# 4. 몬스터 생성 테스트
monster = Monster.create_random(difficulty=2)
print(monster)

# 5. 경험치 / 레벨업 테스트
warrior.gain_exp(250)    # 레벨 2단계 상승 확인

# 6. 생성된 Character 수 확인
print(f"총 Character 수: {Character.get_total_count()}")



# Game Loop 예제

def select_class(name):
    print("\n=== 캐릭터를 선택하세요. ===")
    print("1. ⚔ 전사  (HP 높음, 분노 시스템)")
    print("2. 🔮 마법사 (공격력 높음, 마나 시스템)")
    print("3. 💚 힐러  (치유 능력, 균형형)")

    while True:
        choice = input("선택: (1, 2, 3): ")
        if choice == "1":
                return Warrior(name)
        elif choice == "2":
            return Wizard(name)
        elif choice == "3":
            return Healer(name)
        else:
            print("잘못된 입력입니다. 다시 선택하세요.")

def battle_turn(player, monster):

    print(f"\n--- {player.name}의 턴 ---")
    print(player)
    print(monster)
    print("\n1. 공격  2. 특수 능력  3. 회복 아이템")

    choice = input("행동 선택: ")
    if choice == "1":
        player.attack(monster)
    elif choice == "2":
        if isinstance(player, Healer):
            player.special()  # 힐러는 자기 자신을 치유
        else:
            player.special(monster)
    elif choice == "3":
        print("  🧪 회복 아이템 사용! HP +50")
        player.hp = player.hp + 50
    else:
        print("  잘못된 입력! 턴을 낭비했다...")

    # 몬스터 턴
    if monster.is_alive:
        print(f"\n--- {monster.name}의 턴 ---")
        monster.attack(player)

def game():

    Character.total_count = 0   # 현재 file에서 먼저 생성한 test code가 있을 수 있다.

    print("=" * 40)
    print("  텍스트 RPG  ")
    print("=" * 40)

    name = input("\n Player 이름을 입력하세요: ")
    player = select_class(name)
    print(f"\n{player.name}이(가) 모험을 시작합니다!")
    print(player)

    monsters_defeated = 0   # 물리친 monster 수
    difficulty = 8          # monster 난이도 

    while player.is_alive and monsters_defeated < 3: # game 진행
        # monster 등장
        monster = Monster.create_random(difficulty)
        print(f"\n{'='*40}")
        print(f"  👾 {monster.name}이 나타났다!")
        print(f"{'='*40}")

        # 전투 루프(player와 monster가 살아있으면)
        while player.is_alive and monster.is_alive:
            battle_turn(player, monster)

        # 전투 결과
        if player.is_alive:
            monsters_defeated += 1
            difficulty += 1
            print(f"\n🎉 {monster.name}을 물리쳤다!")
            player.gain_exp(monster.exp_reward)
            print(f"  물리친 몬스터: {monsters_defeated}/3")
            print(player)

    # 게임 종료
    print(f"\n{'='*40}")
    if player.is_alive:
        print("  🏆 승리! 모든 몬스터를 처치했다!")
    else:
        print("  💀 게임 오버...")
    print(f"  최종 상태: {player}")
    print(f"  총 생성된 캐릭터 수: {Character.get_total_count()}")
    print(f"{'='*40}")

game()