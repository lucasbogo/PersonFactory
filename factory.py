from enum import Enum


class NPC:

    # definir construtor; é possível passar os atributos dentro do contrutor (self , ...)
    def __init__(self, name, strenght, health):
        # incializa os atributos:
        self.name = name
        self.strenght = strenght
        self.health = health

    # definir uma função: método abstrato pois nem todo NPC ataca
    def attack():
        pass


class NpcType(Enum):
    DRAGON = 1
    JOKER = 2
    HOST = 3


class NpcFactory:
    @staticmethod
    def create(npc_type):
        if npc_type == NpcType.DRAGON:
            return Dragon('Blue Eyes White Dragon', 30, 200)

        if npc_type == NpcType.JOKER:
            return Joker('Killing Laughter', 10, 155)


# Classe DRAGON herda de NPC
class Dragon(NPC):
    def attack(self, opponent: NPC):
        print(f'{self.name} Dragon Attack. Hit Points: {self.strenght}')
        #opponent.health -= self.strenght
        opponent.health = opponent.health - self.strenght

# Classe JOKER herda de NPC
class Joker(NPC):
    def attack(self, opponent: NPC):
        print(f'{self.name} Joker Attack. Hit Points: {self.strenght}')
        #opponent.health -= self.strenght
        opponent.health = opponent.health - self.strenght


# main...
if __name__ == '__main__':

    """  # Python: dragao é o objeto. o Python deduz que dragão é NPC
     dragon = NPC('Blue Eyes White Dragon', 100, 50)

     # Python: joker é o objeto. o Python deduz que joker é NPC
     joker = NPC('Killing Laughter', 75, 45)

     # Python: host é o objeto. o Python deduz que joker é NPC
     host = NPC('Mr. Crowley', 45, 35) """

    # Criar os NPCs antes de chamar abstract method attack
    dragon = NpcFactory.create(NpcType.DRAGON)
    joker = NpcFactory.create(NpcType.JOKER)

    dragon.attack(opponent=joker)
    joker.attack(opponent=dragon)

    print(f'{dragon.name}health: ', dragon.health)
    print(f'{joker.name}health: ', joker.health)