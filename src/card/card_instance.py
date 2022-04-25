from src.card.card import Card
from src.card.types import *


class CardInstance:
    def __init__(self, card: Card, game, owner):
        self.owner = owner
        self.game = game
        self.equipped_to = None
        self.card = card
        self.max_resolve = self.card.resolve
        self.resolve = self.max_resolve
        self.max_power = self.card.power
        self.power = self.max_power
        self.added_subtypes = set()
        self.removed_subtypes = set()
        self.added_keywords = set()
        self.removed_keywords = set()
        self.tapped = False
        self.buffs = dict()
        self.temp_buffs = list()

    def __del__(self):
        self.owner = None

    def reset(self):
        self.equipped_to = None
        self.max_resolve = self.card.resolve
        self.resolve = self.max_resolve
        self.max_power = self.card.power
        self.power = self.max_power
        self.added_subtypes = set()
        self.removed_subtypes = set()
        self.added_keywords = set()
        self.removed_keywords = set()
        self.tapped = False
        self.buffs = dict()
        self.temp_buffs = list()

    def add_buff(self, name, amount):
        if name is not None:
            self.remove_buff(name)
            if amount == (0, 0):
                return
            self.buffs[name] = amount
        self.max_power += amount[0]
        self.power += amount[0]
        self.max_resolve += amount[1]
        self.resolve += amount[1]

    def remove_buff(self, name):
        if name not in self.buffs:
            return
        self.max_power -= self.buffs[name][0]
        self.power -= self.buffs[name][0]
        self.max_resolve -= self.buffs[name][1]
        self.resolve -= self.buffs[name][1]
        del self.buffs[name]

    def add_temporary_buff(self, amount):
        self.temp_buffs.append(amount)
        self.max_power += amount[0]
        self.power += amount[0]
        self.max_resolve += amount[1]
        self.resolve += amount[1]

    def clear_temporary_buffs(self):
        for amount in self.temp_buffs:
            self.max_power -= amount[0]
            self.power -= amount[0]
            self.max_resolve -= amount[1]
            self.resolve -= amount[1]
        self.temp_buffs = list()

    def heal_to_full(self):
        self.resolve = self.max_resolve

    def has_keyword(self, keyword: CardKeyword):
        return keyword in self.get_keywords()

    def get_keywords(self):
        return (self.card.keywords | self.added_keywords) - self.removed_keywords

    def add_keyword(self, keyword: CardKeyword):
        if keyword in self.removed_keywords:
            self.removed_keywords.remove(keyword)
        self.added_keywords.add(keyword)

    def remove_keyword(self, keyword: CardKeyword):
        if keyword in self.added_keywords:
            self.added_keywords.remove(keyword)
        self.removed_keywords.add(keyword)

    def has_subtype(self, subtype: CardSubtype):
        return subtype in self.get_subtypes()

    def get_subtypes(self):
        return (self.card.subtypes | self.added_subtypes) - self.removed_subtypes

    def add_subtype(self, subtype: CardSubtype):
        if subtype in self.removed_subtypes:
            self.removed_subtypes.remove(subtype)
        self.added_subtypes.add(subtype)

    def remove_subtype(self, subtype: CardSubtype):
        if subtype in self.added_subtypes:
            self.added_subtypes.remove(subtype)
        self.removed_subtypes.add(subtype)

    def tap(self):
        if not self.tapped:
            if self.card.on_tapped(self):
                self.tapped = True

    def untap(self):
        if self.tapped:
            if self.card.on_untapped(self):
                self.tapped = False
