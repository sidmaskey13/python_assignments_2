# Imagine you are creating a Super Mario game. You need to define
# a class to represent Mario. What would it look like? If you aren't
# familiar with SuperMario, use your own favorite video or board game
# to model a player.
GIVEN_STRING = input('Enter your name: ')


class SuperMario:
    def __init__(self, name):
        self.name = name
        self.lives = 10
        self.level = 1
        self.coin = 0
        self.highscore = 0

    def display_info(self):
        return f"""
        Name: {self.name}
-----------------------------------------
        Lives: {self.lives}
        Level: {self.level}
        Coin: {self.coin}
        Highscore: {self.highscore}
-----------------------------------------
        """

    def next_level(self):
        self.level += 1
        self.increase_highscore(5000)
        return self.level

    def get_coin(self):
        self.coin += 1
        self.increase_highscore(10)
        return self.coin

    def kill_enemy(self):
        self.increase_highscore(50)

    def die(self):
        self.lives -= 1
        return self.lives

    def get_health(self):
        self.lives += 1
        self.increase_highscore(100)
        return self.lives

    def increase_highscore(self,x):
        self.highscore += x
        return self.highscore

    def decrease_highscore(self,x):
        self.highscore -= x
        return self.highscore


mario = SuperMario(GIVEN_STRING)

mario.get_coin()
mario.get_coin()
mario.get_coin()
mario.get_coin()
mario.get_coin()
mario.kill_enemy()
mario.kill_enemy()
mario.get_coin()
mario.get_coin()
mario.get_coin()
mario.get_health()
mario.die()
mario.get_coin()
mario.die()
mario.die()
mario.kill_enemy()
mario.die()
mario.kill_enemy()
mario.die()
mario.get_coin()
mario.get_coin()
mario.next_level()

print(mario.display_info())

