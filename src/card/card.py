from typing import Set

from src.card.types import *


class Card:
    name: str = "Invalid"
    description: str = ""
    rules: str = ""

    cost: int = 0
    power: int = 0
    resolve: int = 0

    card_type: CardType = CardType.NONE
    subtypes: Set[CardSubtype] = set()
    faction: CardFaction = CardFaction.NONE
    rarity: CardRarity = CardRarity.NONE
    card_set: CardSet = CardSet.NONE
    keywords: Set[CardKeyword] = set()

    @staticmethod
    def on_card_played():
        pass

    @staticmethod
    def on_summon():
        pass

    @staticmethod
    def on_other_summon():
        pass

    @staticmethod
    def on_death():
        pass

    @staticmethod
    def on_discard():
        pass

    @staticmethod
    def on_other_death():
        pass

    @staticmethod
    def on_equip():
        pass

    @staticmethod
    def on_unequip():
        pass

    @staticmethod
    def on_tap():
        pass

    @staticmethod
    def on_sacrifice():
        pass
