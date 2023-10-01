"""lab 12.2"""

##
# Đề bài:
# Bạn được tạo sẵn Class Pokemon được sử dụng để mô tả một Pokemon như đoạn code bên dưới.
# Bạn hãy bổ sung thêm các hàm như sau:

# 1. update(): Thiết lập các chỉ số của Pokemon về như sau: health_boost = 5; attack_boost = 3; defense_boost = 2; evolve = 10.
# 2. attack_up(): Tăng chỉ số attack của Pokemon = attack + attack_boost và trả về chỉ số attack mới.
# 3. defense_up(): Tăng chỉ số defense của Pokemon = defense + defense_boost và trả về chỉ số defense mới.
# 4. health_up(): Tăng chỉ số health của Pokemon = health + health_boost và trả về chỉ số health mới.

# Tạo một Class Grass_Pokemon được kế thừa từ Pokemon với các thay đổi như sau:
# 1. Các thuộc tính sẽ có giá trị ban đầu như sau attack = 15; defense = 14; health = 12; p_type = "Grass".
# 2. Ghi đè lại hàm update để thay đôi các chỉ số như sau health_boost = 6; attack_boost = 2; defense_boost = 3; evolve = 12.
# 3. Ghi đè lại hàm train để chỉ số attack chỉ tăng khi level > 10.
# 4. Bổ sung thêm 2 thuộc tính là weak và strong.

# Tạo thêm 3 Class mới được kế thừa từ Class `Pokemon` như sau:

# 1. Class `Ghost_Pokemon` với `p_type = "Ghost"; weak = "Dark"; strong = "Psychic"`.
# 2. Class `Fire_Pokemon` với `p_type = "Fire"; weak = "Water"; strong = "Grass"`.
# 3. Class `Flying_Pokemon` với `p_type = "Flying"; weak = "Electric"; strong = "Fighting"`.
#


class Pokemon(object):
    attack = 12
    defense = 10
    health = 15
    p_type = "Normal"

    def __init__(self, name, level=5):
        self.name = name
        self.level = level

    def train(self):
        self.update()
        self.attack_up()
        self.defense_up()
        self.health_up()
        self.level = self.level + 1
        if self.level % self.evolve == 0:
            return self.level, "Evolved!"
        else:
            return self.level

    # Tăng chỉ số attack của Pokemon = attack + attack_boost và trả về chỉ số attack mới.
    def attack_up(self):
        self.attack += self.attack_boost
        return self.attack

    # Tăng chỉ số defense của Pokemon = defense + defense_boost và trả về chỉ số defense mới.
    def defense_up(self):
        self.defense += self.defense_boost
        return self.defense

    # Tăng chỉ số health của Pokemon = health + health_boost và trả về chỉ số health mới.
    def health_up(self):
        self.health += self.health_boost
        return self.health

    # Thiết lập các chỉ số của Pokemon về như sau:
    # health_boost = 5; attack_boost = 3; defense_boost = 2; evolve = 10.
    def update(self):
        self.health_boost = 5
        self.attack_boost = 3
        self.defense_boost = 2
        self.evolve = 10

    def __str__(self):
        self.update()
        return "Pokemon name: {}, Type: {}, Level: {}\r\nAttack: {}, Defense: {}, Health: {}".format(self.name, self.p_type, self.level, self.attack, self.defense, self.health)


# Tạo một Class Grass_Pokemon được kế thừa từ Pokemon với các thay đổi như sau:
# 1. Các thuộc tính sẽ có giá trị ban đầu như sau attack = 15; defense = 14; health = 12; p_type = "Grass".
# 2. Ghi đè lại hàm update để thay đôi các chỉ số như sau health_boost = 6; attack_boost = 2; defense_boost = 3; evolve = 12.
# 3. Ghi đè lại hàm train để chỉ số attack chỉ tăng khi level > 10.
# 4. Bổ sung thêm 2 thuộc tính là weak và strong.
class Grass_Pokemon(Pokemon):
    attack = 15
    defense = 14
    health = 12
    p_type = 'Grass'
    weak = ''
    strong = ''

    def update(self):
        self.health_boost = 6
        self.attack_boost = 2
        self.defense_boost = 3
        self.evolve = 12

    # Ghi đè lại hàm train để chỉ số attack chỉ tăng khi level > 10.
    def train(self):
        self.update()
        self.defense_up()
        self.health_up()
        if self.level > 10:
            self.attack_up()
        self.level = self.level + 1
        if self.level % self.evolve == 0:
            return self.level, "Evolved!"
        else:
            return self.level


class Ghost_Pokemon(Pokemon):
    p_type = 'Ghost'
    weak = 'Dark'
    strong = 'Psychic'


class Fire_Pokemon(Pokemon):
    p_type = 'Fire'
    weak = 'Water'
    strong = 'Grass'


class Flying_Pokemon(Pokemon):
    p_type = 'Flying'
    weak = 'Electric'
    strong = 'Fighting'


# Testing

# Required output:
# Pokemon name: Alomomola, Type: Normal, Level: 9
# Attack: 12, Defense: 10, Health: 15
# ------
# Traning:  (10, 'Evolved!')
# ------
# Pokemon name: Alomomola, Type: Normal, Level: 10
# Attack: 15, Defense: 12, Health: 20
def test_case_1():
    pokemon = Pokemon('Alomomola', 9)
    print(pokemon)
    print('------')
    print('Traning: ', pokemon.train())
    print('------')
    print(pokemon)


# Required output:
# Pokemon name: Petilil, Type: Grass, Level: 9
# Attack: 15, Defense: 14, Health: 12
# ------
# Traning:  10
# ------
# Pokemon name: Petilil, Type: Grass, Level: 10
# Attack: 15, Defense: 17, Health: 18
# ------
# Traning:  11
# ------
# Pokemon name: Petilil, Type: Grass, Level: 11
# Attack: 17, Defense: 20, Health: 24
def test_case_2():
    p1 = Grass_Pokemon('Petilil', 9)
    print(p1)
    print('------')
    print('Traning: ', p1.train())
    print('------')
    print(p1)
    print('------')
    print('Traning: ', p1.train())
    print('------')
    print(p1)


# Required output:
# Pokemon name: Cofagrigus, Type: Ghost, Level: 10
# Attack: 12, Defense: 10, Health: 15
# Pokemon name: Reshiram, Type: Fire, Level: 12
# Attack: 12, Defense: 10, Health: 15
# Pokemon name: Zapdos, Type: Ghost, Level: 9
# Attack: 12, Defense: 10, Health: 15
def test_case_3():
    print(Ghost_Pokemon('Cofagrigus', 10))
    print(Fire_Pokemon('Reshiram', 12))
    print(Ghost_Pokemon('Zapdos', 9))


def main():
    # test_case_1()
    # test_case_2()
    test_case_3()


if __name__ == '__main__':
    main()
