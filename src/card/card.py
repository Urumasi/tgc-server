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

    # Return True to cancel something, for example destruction

    @classmethod
    def on_card_played(cls, instance, other):
        """
        When any card is played in the game
        """
        return False

    @classmethod
    def on_summon(cls, instance):
        """
        When the current creature card is summoned
        """
        return False

    @classmethod
    def on_other_summon(cls, instance, other):
        """
        When any creature card is summoned in the game
        """
        return False

    @classmethod
    def on_death(cls, instance):
        """
        When the current card dies
        """
        return False

    @classmethod
    def on_discard(cls, instance):
        """
        When the current card is discarded
        """
        return False

    @classmethod
    def on_other_death(cls, instance, other, source):
        """
        When another card dies
        """
        return False

    @classmethod
    def on_equip(cls, instance, target):
        """
        When the current equipment card is equipped onto a target creature
        """
        return False

    @classmethod
    def on_unequip(cls, instance, target):
        """
        When the current equipment card is unequipped from a target creature
        """
        return False

    @classmethod
    def on_tap(cls, instance):
        """
        When the current card is tapped for an ability
        """
        return False

    @classmethod
    def on_untap(cls, instance):
        """
        When the current card is untapped
        """
        return False

    @classmethod
    def on_sacrifice(cls, instance):
        """
        When the current card is sacrificed
        """
        return False

    @classmethod
    def on_gain_buff(cls, instance, amount):
        """
        When the current card gains a buff, return modified amount or None for no change
        """
        return amount

    @classmethod
    def on_other_gain_buff(cls, instance, other, source, amount):
        """
        When another card in the game gains a buff, return modified amount or None for no change
        """
        return amount
