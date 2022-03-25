from random import shuffle
from typing import List

from src.card import CardInstance


class Player:
    def __init__(self):
        self.hand: List[CardInstance] = list()
        self.board: List[CardInstance] = list()
        self.deck: List[CardInstance] = list()
        self.graveyard: List[CardInstance] = list()
        self.health: int = 20
        self.max_mana: int = 0
        self.mana: int = 0

    def phase_draw(self, game):
        for card in self.board:
            card.untap()
        self.draw_card()
        self.max_mana += 1
        self.mana = self.max_mana

    def phase_first_effect(self, game):
        pass

    def phase_play(self, game):
        pass

    def phase_battle(self, game):
        pass

    def phase_end(self, game):
        if len(self.hand) > 7:
            pass  # TODO: Discard down to 7

    def shuffle_deck(self):
        shuffle(self.deck)

    def take_damage(self, amount):
        self.health -= amount

    def heal_all_cards(self):
        for card in self.deck:
            card.heal_to_full()

    def draw_card(self):
        if len(self.deck):
            self.hand.append(self.deck.pop())
            return
        self.take_damage(1)
        # TODO: Player may draw a chosen card from their graveyard
