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

    @classmethod
    def on_card_played(cls, instance):
        return True

    @classmethod
    def on_summon(cls, instance):
        return True

    @classmethod
    def on_other_summon(cls, instance):
        return True

    @classmethod
    def on_death(cls, instance):
        return True

    @classmethod
    def on_discard(cls, instance):
        return True

    @classmethod
    def on_other_death(cls, instance):
        return True

    @classmethod
    def on_equip(cls, instance):
        return True

    @classmethod
    def on_unequip(cls, instance):
        return True

    @classmethod
    def on_tap(cls, instance):
        return True

    @classmethod
    def on_untap(cls, instance):
        return True

    @classmethod
    def on_sacrifice(cls, instance):
        return True
