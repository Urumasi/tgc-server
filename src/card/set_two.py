# Set two: "Resin Frontier"
from src.card.card import Card
from src.card.types import *


class Card_xenoborg(Card):
    name = "Xenoborg"
    description = """With a mini-gun in one hand and a rocket launcher in the other, the Xenoborg is a failed hybridization of a Xenomorph and a cyborg."""
    rules = """{$Asimov}. Once per turn, you may sacrifice a silicon card, and pay the difference between that card's summon cost and this card's summon cost to summon this card from your hand."""

    cost = 6
    power = 7
    resolve = 5

    keywords = {CardKeyword.ASIMOV}
    card_type = CardType.CREATURE
    subtypes = {CardSubtype.SILICON, CardSubtype.XENOMORPH}
    rarity = CardRarity.EPIC
    faction = CardFaction.SCIENCE
    card_set = CardSet.RESINFRONT
    """TODO:
    {$Asimov}. Once per turn, you may sacrifice a silicon card, and pay the difference between that card's summon cost and this card's summon cost to summon this card from your hand.
    """


class Card_sentinel(Card):
    name = "Xenomorph Sentinel"
    description = """The juices from a Sentinel's neurotoxin gland pair brilliantly with a Pan-Galactic Gargle Blaster."""
    rules = """{$Hivemind}"""

    cost = 4
    power = 5
    resolve = 3

    keywords = {CardKeyword.HIVEMIND}
    card_type = CardType.CREATURE
    subtypes = {CardSubtype.XENOMORPH}
    rarity = CardRarity.COMMON
    faction = CardFaction.XENO
    card_set = CardSet.RESINFRONT


class Card_drone(Card):
    name = "Xenomorph Drone"
    description = """Rarely seen on the frontlines, the Drone is your average worker that lays the foundation of the hive."""
    rules = """{$Hivemind}. Tap this card: you may summon a Xeno faction creature for 1 less mana this turn."""

    cost = 2
    power = 1
    resolve = 1

    keywords = {CardKeyword.HIVEMIND}
    card_type = CardType.CREATURE
    subtypes = {CardSubtype.XENOMORPH}
    rarity = CardRarity.COMMON
    faction = CardFaction.XENO
    card_set = CardSet.RESINFRONT
    """TODO:
    {$Hivemind}. Tap this card: you may summon a Xeno faction creature for 1 less mana this turn.
    """


class Card_hunter(Card):
    name = "Xenomorph Hunter (Resin Frontier)"
    description = """A rare strain of Hunter that prioritizes slaying prey over infecting them."""
    rules = """If this card destroys a creature via combat, you may discard a card in your hand to add a card from your discard pile to your hand, whose summon cost is 2 or less."""

    cost = 5
    power = 6
    resolve = 3

    keywords = {}
    card_type = CardType.CREATURE
    subtypes = {CardSubtype.XENOMORPH}
    rarity = CardRarity.UNCOMMON
    faction = CardFaction.XENO
    card_set = CardSet.RESINFRONT
    """TODO:
    If this card destroys a creature via combat, you may discard a card in your hand to add a card from your discard pile to your hand, whose summon cost is 2 or less.
    """


class Card_spitter(Card):
    name = "Xenomorph Spitter"
    description = """While their acid gland is too dangerous to mix with alcohol (not that it stops the marines), a Spitter's acid is useful for industry as it can melt almost anything with ease."""
    rules = """{$Hivemind}. Tap this card: draw the top 2 cards of your deck, you may re-arrange their order, then return them to the top of your deck."""

    cost = 3
    power = 3
    resolve = 3

    keywords = {CardKeyword.HIVEMIND}
    card_type = CardType.CREATURE
    subtypes = {CardSubtype.XENOMORPH}
    rarity = CardRarity.UNCOMMON
    faction = CardFaction.XENO
    card_set = CardSet.RESINFRONT
    """TODO:
    {$Hivemind}. Tap this card: draw the top 2 cards of your deck, you may re-arrange their order, then return them to the top of your deck.
    """


class Card_runner(Card):
    name = "Xenomorph Runner"
    description = """Running fast and dying faster, the sheer number of Runner corpses from a battle are enough to keep a research facility busy for years."""
    rules = """{$First Strike}, {$Hivemind}"""

    cost = 3
    power = 2
    resolve = 3

    keywords = {CardKeyword.FIRST_STRIKE, CardKeyword.HIVEMIND}
    card_type = CardType.CREATURE
    subtypes = {CardSubtype.XENOMORPH}
    rarity = CardRarity.COMMON
    faction = CardFaction.XENO
    card_set = CardSet.RESINFRONT
    """TODO:
    {$First Strike}, {$Hivemind}
    """


class Card_praetorian(Card):
    name = "Xenomorph Praetorian"
    description = """The Praetorian is the Queen's royal guard, never seen far from the Queen's chambers."""
    rules = """{$Hivemind}. If you have 2 or more other Xeno cards on your field alongside this card, you may sacrifice 3 Xeno cards and add Xenomorph Queen to your hand from your deck."""

    cost = 5
    power = 3
    resolve = 6

    keywords = {CardKeyword.HIVEMIND}
    card_type = CardType.CREATURE
    subtypes = {CardSubtype.XENOMORPH}
    rarity = CardRarity.RARE
    faction = CardFaction.XENO
    card_set = CardSet.RESINFRONT
    """TODO:
    {$Hivemind}. If you have 2 or more other Xeno cards on your field alongside this card, you may sacrifice 3 Xeno cards and add Xenomorph Queen to your hand from your deck.
    """


class Card_hivelord(Card):
    name = "Xenomorph Hivelord"
    description = """The Hivelord is the last word in construction, capable of building entire hives in a matter of seconds."""
    rules = """{$Hivemind}. For two mana, tap this card and summon a 0/2 Resin Wall counter creature. Each Resin Wall has {$Blocker}."""

    cost = 3
    power = 1
    resolve = 3

    keywords = {CardKeyword.HIVEMIND}
    card_type = CardType.CREATURE
    subtypes = {CardSubtype.XENOMORPH}
    rarity = CardRarity.RARE
    faction = CardFaction.XENO
    card_set = CardSet.RESINFRONT
    """TODO:
    {$Hivemind}. For two mana, tap this card and summon a 0/2 Resin Wall counter creature. Each Resin Wall has {$Blocker}.
    """


class Card_boiler(Card):
    name = "Xenomorph Boiler"
    description = """The Boiler is a long-range artillery machine, capable of spewing clouds of acid that melt everything in seconds."""
    rules = """{$Hivemind}. If this card attacks, it is tapped for an additional turn before it is untapped."""

    cost = 4
    power = 6
    resolve = 2

    keywords = {CardKeyword.HIVEMIND}
    card_type = CardType.CREATURE
    subtypes = {CardSubtype.XENOMORPH}
    rarity = CardRarity.RARE
    faction = CardFaction.XENO
    card_set = CardSet.RESINFRONT
    """TODO:
    {$Hivemind}. If this card attacks, it is tapped for an additional turn before it is untapped.
    """


class Card_ravager(Card):
    name = "Xenomorph Ravager"
    description = """With large scythe claws for hands, the furious Ravager goes berserk at the sight of fire."""
    rules = """{$Hivemind}, {$Fury}"""

    cost = 3
    power = 4
    resolve = 2

    keywords = {CardKeyword.HIVEMIND, CardKeyword.FURY}
    card_type = CardType.CREATURE
    subtypes = {CardSubtype.XENOMORPH}
    rarity = CardRarity.RARE
    faction = CardFaction.XENO
    card_set = CardSet.RESINFRONT
    """TODO:
    {$Hivemind}, {$Fury}
    """


class Card_crusher(Card):
    name = "Xenomorph Crusher"
    description = """Extensive testing has revealed that a pulse rifle is unable to penetrate a Crusher's thick armored head."""
    rules = """{$Hivemind}, {$Blocker}"""

    cost = 3
    power = 1
    resolve = 6

    keywords = {CardKeyword.HIVEMIND, CardKeyword.BLOCKER}
    card_type = CardType.CREATURE
    subtypes = {CardSubtype.XENOMORPH}
    rarity = CardRarity.RARE
    faction = CardFaction.XENO
    card_set = CardSet.RESINFRONT
    """TODO:
    {$Hivemind}, {$Blocker}
    """


class Card_defender(Card):
    name = "Xenomorph Defender"
    description = """The Defender's armored head crest makes an excellent makeshift shield."""
    rules = """{$Hivemind}, {$Blocker}"""

    cost = 2
    power = 1
    resolve = 2

    keywords = {CardKeyword.HIVEMIND, CardKeyword.BLOCKER}
    card_type = CardType.CREATURE
    subtypes = {CardSubtype.XENOMORPH}
    rarity = CardRarity.COMMON
    faction = CardFaction.XENO
    card_set = CardSet.RESINFRONT
    """TODO:
    {$Hivemind}, {$Blocker}
    """


class Card_warrior(Card):
    name = "Xenomorph Warrior"
    description = """Warriors exhibit greater cruelty than other Xeno strains, enjoying snapping a victim's limbs before finishing them off."""
    rules = """{$Hivemind}"""

    cost = 4
    power = 4
    resolve = 4

    keywords = {CardKeyword.HIVEMIND}
    card_type = CardType.CREATURE
    subtypes = {CardSubtype.XENOMORPH}
    rarity = CardRarity.UNCOMMON
    faction = CardFaction.XENO
    card_set = CardSet.RESINFRONT
    """TODO:
    {$Hivemind}
    """


class Card_queen(Card):
    name = "Xenomorph Queen (Resin Frontier)"
    description = """The ruler of the hive. Organs from a Queen fetch a high price amongst researchers and less-than-moral surgeons."""
    rules = """For 2 mana, tap the equipped creature and summon a 1/1 Xenomorph Brood counter creature, with {$Hivemind}."""

    cost = 5
    power = 5
    resolve = 5

    keywords = {}
    card_type = CardType.EQUIPMENT
    subtypes = {CardSubtype.ARMOUR}
    rarity = CardRarity.EPIC
    faction = CardFaction.XENO
    card_set = CardSet.RESINFRONT
    """TODO:
    For 2 mana, tap the equipped creature and summon a 1/1 Xenomorph Brood counter creature, with {$Hivemind}.
    """


class Card_carrier(Card):
    name = "Xenomorph Carrier"
    description = """Carriers are like the Easter Bunny except the eggs they hide will kill you."""
    rules = """{$Hivemind}, {$Squad Tactics}"""

    cost = 3
    power = 2
    resolve = 2

    keywords = {CardKeyword.HIVEMIND, CardKeyword.SQUAD_TACTICS}
    card_type = CardType.CREATURE
    subtypes = {CardSubtype.XENOMORPH}
    rarity = CardRarity.UNCOMMON
    faction = CardFaction.XENO
    card_set = CardSet.RESINFRONT
    """TODO:
    {$Hivemind}, {$Squad Tactics}
    """


class Card_defiler(Card):
    name = "Xenomorph Defiler"
    description = """Instead of utilizing eggs, the Defiler prefers to inject an unknown chemical in their victim, causing a devastating infection."""
    rules = """{$Hivemind}. When this card attacks a target enemy creature, calculate damage as though the target creature has this card's power subtracted from it first."""

    cost = 3
    power = 1
    resolve = 3

    keywords = {CardKeyword.HIVEMIND}
    card_type = CardType.CREATURE
    subtypes = {CardSubtype.XENOMORPH}
    rarity = CardRarity.RARE
    faction = CardFaction.XENO
    card_set = CardSet.RESINFRONT
    """TODO:
    {$Hivemind}. When this card attacks a target enemy creature, calculate damage as though the target creature has this card's power subtracted from it first.
    """


class Card_predalien(Card):
    name = "Predalien"
    description = """No concrete information is available on this elusive creature as no one that has seen it has lived to tell the tale."""
    rules = """{$Hivemind}, {$Changeling}"""

    cost = 3
    power = 4
    resolve = 3

    keywords = {CardKeyword.HIVEMIND, CardKeyword.CHANGELING}
    card_type = CardType.CREATURE
    subtypes = {CardSubtype.XENOMORPH, CardSubtype.SOLDIER}
    rarity = CardRarity.LEGENDARY
    faction = CardFaction.XENO
    card_set = CardSet.RESINFRONT
    """TODO:
    {$Hivemind}, {$Changeling}
    """


class Card_shrike(Card):
    name = "Xenomorph Shrike"
    description = """It is unknown why Shrikes are able to lead a Hive, but their hives are always much smaller than a Queen's."""
    rules = """{$Hivemind}. If Xenomorph Queen would be destroyed, you may re-equip Xenomorph Queen on this card instead, once per game."""

    cost = 2
    power = 3
    resolve = 1

    keywords = {CardKeyword.HIVEMIND}
    card_type = CardType.CREATURE
    subtypes = {CardSubtype.XENOMORPH}
    rarity = CardRarity.RARE
    faction = CardFaction.XENO
    card_set = CardSet.RESINFRONT
    """TODO:
    {$Hivemind}. If Xenomorph Queen would be destroyed, you may re-equip Xenomorph Queen on this card instead, once per game.
    """


class Card_bull(Card):
    name = "Xenomorph Bull"
    description = """Popular in illegal rodeos, a Bull's horn can pierce a reinforced wall with ease."""
    rules = """{$First Strike}, {$Hivemind}"""

    cost = 6
    power = 5
    resolve = 3

    keywords = {CardKeyword.FIRST_STRIKE, CardKeyword.HIVEMIND}
    card_type = CardType.CREATURE
    subtypes = {CardSubtype.XENOMORPH}
    rarity = CardRarity.UNCOMMON
    faction = CardFaction.XENO
    card_set = CardSet.RESINFRONT
    """TODO:
    {$First Strike}, {$Hivemind}
    """


class Card_hivemind(Card):
    name = "Xenomorph Hivemind"
    description = """Recently discovered to have sapience, this pulsating orb will dig into the earth and rapidly spread resin throughout planets."""
    rules = """{$Blocker}"""

    cost = 1
    resolve = 1

    keywords = {CardKeyword.BLOCKER}
    card_type = CardType.CREATURE
    subtypes = {CardSubtype.XENOMORPH}
    rarity = CardRarity.UNCOMMON
    faction = CardFaction.XENO
    card_set = CardSet.RESINFRONT


class Card_screecher(Card):
    name = "Xenomorph Screecher"
    description = """The Screecher's screeches are more psychologically damaging than the resulting hearing damage."""
    rules = """{$Deadeye}"""

    cost = 2
    power = 3
    resolve = 2

    keywords = {CardKeyword.DEADEYE}
    card_type = CardType.CREATURE
    subtypes = {CardSubtype.XENOMORPH}
    rarity = CardRarity.EPIC
    faction = CardFaction.XENO
    card_set = CardSet.RESINFRONT


class Card_creep(Card):
    name = "Xenomorph Creep"
    description = """This special Hunter strain prioritizes stalking its target. It evolves into a strain of Hunter that is (mercifully) rarely seen aboard space stations."""
    rules = """Tap this card: Until the start of your next turn, this card has immunity to Xeno Creatures."""

    cost = 5
    power = 4
    resolve = 3

    keywords = {}
    card_type = CardType.CREATURE
    subtypes = {CardSubtype.XENOMORPH}
    rarity = CardRarity.COMMON
    faction = CardFaction.XENO
    card_set = CardSet.RESINFRONT
    """TODO:
    Tap this card: Until the start of your next turn, this card has immunity to Xeno Creatures.
    """
