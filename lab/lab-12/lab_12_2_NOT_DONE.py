##
# lab 12.2

# Bạn được tạo sẵn Class Pokemon được sử dụng để mô tả một Pokemon như đoạn code bên dưới.
# Bạn hãy bổ sung thêm các hàm như sau:

# update(): Thiết lập các chỉ số của Pokemon về như sau: health_boost = 5; attack_boost = 3; defense_boost = 2; evolve = 10.
# attack_up(): Tăng chỉ số attack của Pokemon = attack + attack_boost và trả về chỉ số attack mới.
# defense_up(): Tăng chỉ số defense của Pokemon = defense + defense_boost và trả về chỉ số defense mới.
# health_up(): Tăng chỉ số health của Pokemon = health + health_boost và trả về chỉ số health mới.

# Kiểm tra đoạn code đã hoạt động đúng chưa:
# pokemon = Pokemon('Alomomola', 9)
# print(pokemon)
# print('------')
# print('Traning: ', pokemon.train())
# print('------')
# print(pokemon)

# Expected Output:
# Pokemon name: Alomomola, Type: Normal, Level: 9
# Attack: 12, Defense: 10, Health: 15
# ------
# Traning:  (10, 'Evolved!')
# ------
# Pokemon name: Alomomola, Type: Normal, Level: 10
# Attack: 15, Defense: 12, Health: 20

# Tạo một Class Grass_Pokemon được kế thừa từ Pokemon với các thay đổi như sau:

# Các thuộc tính sẽ có giá trị ban đầu như sau attack = 15; defense = 14;
# health = 12; p_type = "Grass".
# Ghi đè lại hàm update để thay đôi các chỉ số như sau health_boost = 6;
# attack_boost = 2; defense_boost = 3; evolve = 12.
# Ghi đè lại hàm train để chỉ số attack chỉ tăng khi level > 10.
# Bổ sung thêm 2 thuộc tính là weak và strong.

# Kiểm tra đoạn code đã hoạt động đúng chưa:
# p1 = Grass_Pokemon('Petilil', 9)
# print(p1)
# print('------')
# print('Traning: ', p1.train())
# print('------')
# print(p1)
# print('------')
# print('Traning: ', p1.train())
# print('------')
# print(p1)

# Expected Output:
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

# Tạo thêm 3 Class mới được kế thừa từ Class Pokemon như sau:

# Class Ghost_Pokemon với p_type = "Ghost"; weak = "Dark"; strong = "Psychic".
# Class Fire_Pokemon với p_type = "Fire"; weak = "Water"; strong = "Grass".
# Class Flying_Pokemon với p_type = "Flying"; weak = "Electric"; strong = "Fighting".

# Kiểm tra đoạn code đã hoạt động đúng chưa:
# print(Ghost_Pokemon('Cofagrigus', 10))
# print(Fire_Pokemon('Reshiram', 12))
# print(Ghost_Pokemon('Zapdos', 9))

# Expected Output:
# Pokemon name: Cofagrigus, Type: Ghost, Level: 10
# Attack: 12, Defense: 10, Health: 15
# Pokemon name: Reshiram, Type: Fire, Level: 12
# Attack: 12, Defense: 10, Health: 15
# Pokemon name: Zapdos, Type: Ghost, Level: 9
# Attack: 12, Defense: 10, Health: 15
#


# class Pokemon(object):
#     attack = 12
#     defense = 10
#     health = 15
#     p_type = "Normal"

#     def __init__(self, name, level=5):
#         [...]

#     def train(self):
#         self.update()
#         self.attack_up()
#         self.defense_up()
#         self.health_up()
#         self.level = self.level + 1
#         if self.level % self.evolve == 0:
#             return self.level, "Evolved!"
#         else:
#             return self.level

#     def attack_up(self):
#         [...]

#     def defense_up(self):
#         [...]

#     def health_up(self):
#         [...]

#     def update(self):
#         [...]

#     def __str__(self):
#         self.update()
#         return "Pokemon name: {}, Type: {}, Level: {}\r\nAttack: {}, Defense: {}, Health: {}".format(self.name, self.p_type, self.level, self.attack, self.defense, self.health)

# --------------------------------------------------------------------------------------------

# class Grass_Pokemon(Pokemon):
#     [...]

#     def update(self):
#         [...]

#     def __init__(self, name,level = 5):
#         [...]
#         self.weak = "Dark"
#         self.strong = "Psychic"

#     def train(self):
#         [...]

#     def moves(self):
#         self.p_moves = ["razor leaf", "synthesis", "petal dance"]

#     def action(self):
#         return self.name + " knows a lot of different moves!"

# --------------------------------------------------------------------------------------------

# class Ghost_Pokemon(Pokemon):
#     [...]

# class Fire_Pokemon(Pokemon):
#     [...]

# class Flying_Pokemon(Pokemon):
#     [...]
