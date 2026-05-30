

#  Encapsulation: 캡슐화


class Character:
    def __init__(self, name, hp, level):
        self.name = name        # 자유
        self._hp = hp           #  하지 말기로 해요
        self.__level = level      # 말 안듣네... 

    def __str__(self):
        return f"[Lv.{self.level}] {self.name} (HP: {self._hp})"

hero = Character("Arthur", 100, 5)
print(hero)  # [Lv.5] Arthur (HP: 100)

# 어떻 속성(attribute)을 가지고 있는가? name, hp, level
hero._hp = -2
hero.__level = 30
print(hero)  # [Lv.5] Arthur (HP: 100)


