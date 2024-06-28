
class Game:
    def __init__(self):
        self.player = Hero('player', 100, 20)
        self.computer = Hero('computer', 100, 20)

    def start(self):
        while self.player.is_alive() and self.computer.is_alive():
            self.player.attack(self.computer)
            self.computer.attack(self.player)