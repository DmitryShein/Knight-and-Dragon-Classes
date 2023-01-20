from time import sleep
from random import randint

class Hero:
    def __init__(self, nickname, race, hp, armor, damage, weapon):
        self.nickname = nickname
        self.race = race
        self.hp = hp
        self.armor = armor
        self.damage = damage
        self.weapon = weapon

    def print_info(self):
        print('\nHero info: '+self.nickname+':\nRace: '+self.race+'\nHP: '+str(self.hp)+'\nArmor: '+str(self.armor)+'\nDamage: '+str(self.damage)+'\nWeapon: '+self.weapon)

    def strike(self, enemy):
        self.print_info()
        sleep(3)
        enemy.print_info()
        print('3..')
        sleep(1)
        print('2..')
        sleep(1)
        print('1..')
        sleep(1)
        print('\nLETS FIGHT!')
        play = True
        while play:
            sleep(3)
            who_is_attacked = randint(0,1)
            if who_is_attacked == 0:
                print(self.nickname+' atacked '+enemy.nickname+' get him '+str(self.damage)+' damage. ')
                enemy.armor -= self.damage
                if enemy.armor <= 0:
                    enemy.hp += enemy.armor
                    enemy.armor = 0 #возвращаем значение обратно на 0, т.к. уже вычли это значение из здоровья
                    print('Armor: '+str(enemy.armor))
                    if enemy.hp <= 0:
                        print('HP: 0')
                        print(enemy.nickname+' die from this battle...')
                        play = False
                    else:
                        print('HP: '+str(enemy.hp))
            else:
                print(enemy.nickname+' atacked '+self.nickname+' get him '+str(enemy.damage)+' damage. ')
                self.armor -= enemy.damage
                if self.armor <= 0:
                    self.hp += self.armor
                    self.armor = 0 #возвращаем значение обратно на 0, т.к. уже вычли это значение из здоровья
                    print('Armor: '+str(self.armor))
                    if self.hp <= 0:
                        print('HP: 0')
                        print(self.nickname+' die from this battle...')
                        play = False
                    else:
                        print('HP: '+str(self.hp))

def create_hero():
    race = ""
    hero_nick = ""
    hp = 0
    armor = 0
    damage = 0
    weapon = ""

    while (race != 1 and race != 2) and race != 3:
        race = int(input('Choose NUMBER of your charackter:\n\n1 - Human(HP: 100, Armor: 30, Damage: 25, Weapon: sword)\n\n2 - Elf(HP: 70, Armor: 10, Damage: 30, Weapon: stick + magic)\n\n3 - Demon(HP: 130, Armor: 20, Damage: 30, Weapon: axe -weakness for magic)\n'))
        #К сожалению в данном питоне алгоритмики нет match - case поэтому if
    match(race):
        case 1:
            hp = 100
            armor = 30
            damage = 25
            weapon = "Sword"
            race = "Human"
        case 2:
            hp = 70
            armor = 10
            damage = 30
            weapon = "Stick"
            race = "Elf"
        case 3:
            hp = 130
            armor = 20
            damage = 30
            weapon = "Axe"
            race = "Demon"

    while len(hero_nick) > 20 or len(hero_nick) <= 0:
        hero_nick = input('\nInput your hero name (under 20 symbols):')
    
    return hero_nick, race, hp, armor, damage, weapon

player_info = create_hero()
player = Hero(player_info[0], player_info[1], player_info[2], player_info[3], player_info[4], player_info[5])

#for all enemys
enemys = []
enemys.append(['Emil', 'Goblin', 50, 10, 20, 'Kitchen knife'])
# ... etc
goblin1 = Hero(enemys[0][0], enemys[0][1], enemys[0][2], enemys[0][3], enemys[0][4], enemys[0][5])

print('\nBefore starting your adventures, you decided to pick up equipment at the market, BUT SUDDENLY you were attacked by a strange green creature. Perhaps it did not see you as an armed hero and began to retreat.')
choose = 0
while choose != 1 and choose != 2:
    choose = int(input('\nWhat will you do?\n1 - spare\n2 - kill goblin!'))
if choose == 1:
    print('You turn away, letting the bastard leave in disgrace, BUT HE stabs you in the back..')
    goblin1.strike(player)
else:
    player.strike(goblin1)

