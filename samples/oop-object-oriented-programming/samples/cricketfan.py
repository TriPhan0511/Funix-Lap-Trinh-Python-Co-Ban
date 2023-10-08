from party import PartyAnimal


class CricketFan(PartyAnimal):
    points = 0

    def six(self):
        self.points += 6
        self.party()
        print(f'{self.name} points {self.points}')


s = PartyAnimal('Sally')
s.party()
j = CricketFan('Jim')
j.six()

# Sally constructed.
# Sally count 1
# Jim constructed.
# Jim count 1
# Jim points 6

print(dir(j))
# [... 'name', 'party', 'points', 'six', 'x']
