from src.card.types import *


class Interrupt:
    def __init__(self, optional=False):
        self.optional = optional

    def validate(self, value):
        return True


class PayManaInterrupt(Interrupt):
    def __init__(self, mana_cost, optional=False):
        super().__init__(optional)
        self.mana_cost = mana_cost


class ChooseFromListInterrupt(Interrupt):
    def __init__(self, cards, optional=False):
        super().__init__(optional)
        self.cards = cards


class ChooseMultipleFromListInterrupt(Interrupt):
    def __init__(self, cards, num, optional=False):
        super().__init__(optional)
        self.cards = cards
        self.num = num


class ChooseBoardCreatureInterrupt(Interrupt):
    def __init__(self, filter=None, optional=False):
        super().__init__(optional)
        self.filter = filter
        self.optional = optional

    def validate(self, instance):
        if instance.card.card_type != CardType.CREATURE:
            return False
        return self.filter(instance) if self.filter else True


class ChooseOwnerBoardCreatureInterrupt(ChooseBoardCreatureInterrupt):
    def __init__(self, owner, filter=None, optional=False):
        super().__init__(filter, optional)
        self.owner = owner

    def validate(self, instance):
        if instance.card.card_type != CardType.CREATURE:
            return False
        if instance.owner != self.owner:
            return False
        return self.filter(instance) if self.filter else True


class ChooseOpponentBoardCreatureInterrupt(ChooseBoardCreatureInterrupt):
    def __init__(self, owner, filter=None, optional=False):
        super().__init__(filter, optional)
        self.owner = owner

    def validate(self, instance):
        if instance.card.card_type != CardType.CREATURE:
            return False
        if instance.owner == self.owner:
            return False
        return self.filter(instance) if self.filter else True
