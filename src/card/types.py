from enum import Enum


class CardType(Enum):
    NONE = 0
    ARTIFACT = 1
    BATTLEFIELD = 2
    CREATURE = 3
    EVENT = 4
    EQUIPMENT = 5
    HUMAN = CREATURE  # Why does this exist...


class CardSubtype(Enum):
    NONE = 0
    ABOMINATION = 1
    ANOMALY = 2
    ARMOUR = 3
    ATMOSPHERICS = 4
    CAT = 5
    CLOWN = 6
    COMMANDER = 7
    CONSTRUCT = 8
    CORGI = 9
    DOCTOR = 10
    DRONE = 11
    EMPLOYEE = 12
    ENGINEER = 13
    EVENT = 14
    EXPLORER = 15
    HUMAN = 16
    INSTANT = 17
    LIZARD = 18
    MIME = 19
    MINER = 20
    MOTH = 21
    OFFICER = 22
    PLANT = 23
    PLASMAMAN = 24
    PRIMATE = 25
    RABBIT = 26
    ROBOT = 27
    SCIENTIST = 28
    SHUTTLE = 29
    SILICON = 30
    SLOTH = 31
    SOLDIER = 32
    SPIRIT = 33
    SYNDICATE = 34
    WEAPON = 35
    WORKER = 36
    XENOMORPH = 37


class CardFaction(Enum):
    NONE = 0
    CARGO = 1
    COMMAND = 2
    ENGINEERING = 3
    MEDICAL = 4
    SCIENCE = 5
    SECURITY = 6
    SERVICE = 7
    SILICON = 8
    SYNDICATE = 9
    XENO = 10


class CardRarity(Enum):
    NONE = 0
    COMMON = 0
    UNCOMMON = 1
    RARE = 2
    EPIC = 3
    LEGENDARY = 4
    MISPRINT = 5


class CardSet(Enum):
    NONE = 0
    CORESET2020 = 1
    RESINFRONT = 2


class CardKeyword(Enum):
    NONE = 0
    ASIMOV = 1
    BLOCKER = 2
    CHANGELING = 3
    CLOCKWORK = 4
    DEADEYE = 5
    FIRST_STRIKE = 6
    FURY = 7
    GRAYTIDE = 8
    HIVEMIND = 9
    HOLY = 10
    IMMUNITY_BATTLEFIELD = 11
    IMMUNITY_EFFECT = 12
    IMMUNITY_ENGINEERING_CREATURE = 13
    IMMUNITY_SPELL = 14
    IMMUNITY_XENO_CREATURE = 15
    SQUAD_TACTICS = 16
    TAUNT = 17

