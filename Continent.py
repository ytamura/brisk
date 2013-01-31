from Player import Player

class Continent():

    def __init__(self, id, bonus, name, territories):
        self.id = id
        self.bonus = bonus
        self.name = name
        self.territories = territories
        pass

    def __repr__(self):
        return str(self.id) + ',' + str(self.name)

    @property
    def player(self):
        player_ids_in_continent = set()
        for territory in self.territories:
            player_ids_in_continent.add(territory.player.id)
        
        if len(player_ids_in_continent) == 1:
            return Player.get(player_ids_in_continent.pop())

        return None