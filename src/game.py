from datetime import datetime
from enum import Enum

from src.player import Player


class GameState(Enum):
    NONE = 0
    DRAW = 1
    FIRST_EFFECT = 2
    PLAY = 3
    BATTLE = 4
    END = 5


class Game:
    def __init__(self):
        self.created_time = datetime.now()
        self.interacted_time = self.created_time
        self.turn_player = 0
        self.phase = GameState.NONE
        self.players = [Player(self), Player(self)]
        self.log = list()

    def __del__(self):
        pass

    def main(self):
        while True:
            yield 123
            self.turn_player = (self.turn_player + 1) % len(self.players)

    def phase_draw(self):
        ply = self.players[self.turn_player]
        ply.phase_draw(self)
        for player in self.players:
            player.heal_all_cards()

    def phase_first_effect(self):
        for i, player in enumerate(self.players):
            if i == self.turn_player:
                continue
            player.phase_first_effect(self)
        ply = self.players[self.turn_player]
        ply.phase_first_effect(self)

    def phase_play(self):
        ply = self.players[self.turn_player]
        ply.phase_play(self)

    def phase_battle(self):
        ply = self.players[self.turn_player]
        ply.phase_battle(self)

    def phase_end(self):
        ply = self.players[self.turn_player]
        ply.phase_end(self)
