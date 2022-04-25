from random import shuffle
from typing import List
from random import randint

from src.card import CardInstance
from src.interrupt import *


class Player:
    def __init__(self, game):
        self.game = game
        self.hand: List[CardInstance] = list()
        self.board: List[CardInstance] = list()
        self.deck: List[CardInstance] = list()
        self.graveyard: List[CardInstance] = list()
        self.health: int = 20
        self.max_mana: int = 0
        self.mana: int = 0

    def __del__(self):
        self.game = None

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
            # Discard down to 7
            result = (yield ChooseMultipleFromListInterrupt(self.hand, len(self.hand) - 7))
            for card in result:
                self.discard_card(card)

    def shuffle_deck(self):
        shuffle(self.deck)

    def take_damage(self, amount):
        self.health -= amount

    def heal_all_cards(self):
        for card in self.deck:
            card.heal_to_full()

    def on_card_drawn(self, card):
        pass

    def draw_card(self):
        if len(self.deck):
            card = self.deck.pop()
            self.hand.append(card)
            self.on_card_drawn(card)
            return card
        self.take_damage(1)
        # TODO: Player may draw a chosen card from their graveyard
        result = (yield ChooseFromListInterrupt(self.graveyard, optional=True))
        if result is not None:
            self.add_card_to_hand(result)
            self.on_card_drawn(result)
            return result
        return None

    def play_card(self, card):
        if card in self.hand:
            self.hand.remove(card)
            self.board.append(card)
            self.enter_the_battlefield(card)
        elif card in self.deck:
            self.deck.remove(card)
            self.board.append(card)
            self.enter_the_battlefield(card)
        elif card in self.graveyard:
            self.graveyard.remove(card)
            self.board.append(card)
            self.enter_the_battlefield(card)
        elif card in self.board:
            pass
        # TODO: summon effects

    def add_card_to_hand(self, card):
        if card in self.deck:
            self.deck.remove(card)
            self.hand.append(card)
        elif card in self.graveyard:
            self.graveyard.remove(card)
            self.hand.append(card)
        elif card in self.board:
            card.reset()
            # TODO: Unequip all equipment etc.
            # TODO: split on_destroy to on_destroy and on_leave_board
            self.board.remove(card)
            self.hand.append(card)
        elif card in self.hand:
            pass

    def enter_the_battlefield(self, card):
        players = card.game.players
        for player in players:
            for c in player.board:
                if c is not card:
                    c.on_card_played(card)
        card.on_summon(card)
        for player in players:
            for c in player.board:
                if c is not card:
                    c.on_other_summon(card)

    def destroy_card(self, card):
        pass  # TODO

    def sacrifice_card(self, card):
        pass  # TODO

    def discard_card(self, card):
        pass  # TODO

    def flip_coin(self, amount=1):
        if amount == 1:
            return randint(0, 1) == 1
        elif amount > 1:
            return [randint(0, 1) == 1 for _ in range(amount)]
