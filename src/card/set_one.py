# Set one: "Core Set 2020"
from src.card.card import Card
from src.card.types import *


class Card_AI(Card):
    name = "AI"
    description = """The latest generation of NT's top secret artificial intelligence project, this time with actual human brains in a jar! Don't tell the press though."""
    rules = """{$Asimov}"""

    cost = 5
    power = 3
    resolve = 6

    keywords = {CardKeyword.ASIMOV}
    card_type = CardType.CREATURE
    subtypes = {CardSubtype.SILICON}
    rarity = CardRarity.UNCOMMON
    faction = CardFaction.SCIENCE
    card_set = CardSet.CORESET2020


class Card_stickman(Card):
    name = "Angry Stickman"
    description = """Sure, he's flat and crudely drawn, but watch out! He's a menace!"""
    rules = """{$On Summon}: If another 'Angry Stickman' card has been destroyed, you may summon it for at double cost. This ability may be activated only once per turn."""

    cost = 1
    power = 1
    resolve = 1

    keywords = {}
    card_type = CardType.CREATURE
    subtypes = {CardSubtype.CONSTRUCT}
    rarity = CardRarity.UNCOMMON
    faction = CardFaction.XENO
    card_set = CardSet.CORESET2020
    """TODO:
    {$On Summon}: If another 'Angry Stickman' card has been destroyed, you may summon it for at double cost. This ability may be activated only once per turn.
    """


class Card_changeling(Card):
    name = "Armoured Changeling"
    description = """The strange creatures known as changelings have been known to develop natural armour as a defense mechanism when in combat."""
    rules = """{$Changeling}"""

    cost = 6
    power = 2
    resolve = 8

    keywords = {CardKeyword.CHANGELING}
    card_type = CardType.CREATURE
    subtypes = {CardSubtype.ABOMINATION}
    rarity = CardRarity.RARE
    faction = CardFaction.SYNDICATE
    card_set = CardSet.CORESET2020


class Card_assistant(Card):
    name = "Staff Assistant"
    description = """The lowest ladder on the Nanotrasen Employment Ladder, Staff Assistants are employed to help out with tasks deemed 'too menial for robots'."""
    rules = """{$Graytide}, for every card with '{$Graytide}', this card has +1/+1 on the field."""

    cost = 1
    power = 1
    resolve = 1

    keywords = {CardKeyword.GRAYTIDE}
    card_type = CardType.CREATURE
    subtypes = {CardSubtype.HUMAN, CardSubtype.EMPLOYEE}
    rarity = CardRarity.COMMON
    faction = CardFaction.SERVICE
    card_set = CardSet.CORESET2020
    """TODO:
    {$Graytide}, for every card with '{$Graytide}', this card has +1/+1 on the field.
    """


class Card_atmos_tech(Card):
    name = "Atmospheric Technician"
    description = """The Atmospheric Technicians are tasked with keeping the station's air clean, breathable, and, most importantly, devoid of plasma."""
    rules = """{$On Summon}: Search your deck for an Atmospherics Battlefield card, and add it to your hand. Shuffle your deck afterward."""

    cost = 4
    power = 2
    resolve = 3

    keywords = {}
    card_type = CardType.CREATURE
    subtypes = {CardSubtype.HUMAN, CardSubtype.ENGINEER}
    rarity = CardRarity.COMMON
    faction = CardFaction.ENGINEERING
    card_set = CardSet.CORESET2020
    """TODO:
    {$On Summon}: Search your deck for an Atmospherics Battlefield card, and add it to your hand. Shuffle your deck afterward.
    """


class Card_bartender(Card):
    name = "Bartender"
    description = """Prior to the introduction of on-station psychologists, the Bartender served to alleviate many employees' woes and fears. Remember, always drink responsibly."""
    rules = """"""

    cost = 3
    power = 3
    resolve = 2

    keywords = {}
    card_type = CardType.CREATURE
    subtypes = {CardSubtype.HUMAN, CardSubtype.EMPLOYEE}
    rarity = CardRarity.COMMON
    faction = CardFaction.SERVICE
    card_set = CardSet.CORESET2020


class Card_botanist(Card):
    name = "Botanist"
    description = """The Botanist is in charge of keeping the station's food supply happy, healthy, and preferably not laced with hallucinogens."""
    rules = """"""

    cost = 1
    power = 1
    resolve = 4

    keywords = {}
    card_type = CardType.CREATURE
    subtypes = {CardSubtype.HUMAN, CardSubtype.EMPLOYEE}
    rarity = CardRarity.COMMON
    faction = CardFaction.SERVICE
    card_set = CardSet.CORESET2020


class Card_captain(Card):
    name = "Captain"
    description = """Every Captain is expected to lay down their life for their assigned station. Any Captain who returns to Centcom alive without permission is ceremonially executed before being cloned and stripped of rank."""
    rules = """Tap this card: inflict -1/-1 to an opposing creature card."""

    cost = 7
    power = 5
    resolve = 5

    keywords = {}
    card_type = CardType.CREATURE
    subtypes = {CardSubtype.HUMAN, CardSubtype.COMMANDER}
    rarity = CardRarity.RARE
    faction = CardFaction.COMMAND
    card_set = CardSet.CORESET2020
    """TODO:
    Tap this card: inflict -1/-1 to an opposing creature card.
    """


class Card_caps_suit(Card):
    name = "Apadyne Technologies Mk.2 R.I.O.T. Suit (Captain's Version)"
    description = """A heavily customised Apadyne Technologies Mk.2 R.I.O.T. Suit, rebuilt and refitted to Nanotrasen's highest standards for issue to Station Captains."""
    rules = """{$On Equip}: tap the equipped card for 2 turns, without triggering the target card's effects."""

    cost = 3
    power = -1
    resolve = 5

    keywords = {}
    card_type = CardType.EQUIPMENT
    subtypes = {CardSubtype.ARMOUR}
    rarity = CardRarity.EPIC
    faction = CardFaction.COMMAND
    card_set = CardSet.CORESET2020
    """TODO:
    {$On Equip}: tap the equipped card for 2 turns, without triggering the target card's effects.
    """


class Card_cargo_tech(Card):
    name = "Cargo Technician"
    description = """The grunts of Cargo. Any reports that Cargo Technicians are frequently overcome by revolutionary fervour are exaggerated."""
    rules = """Once per turn, you may give 'Cargo Technician' -1/0 until the start of your next turn and gain 1 mana."""

    cost = 2
    power = 3
    resolve = 1

    keywords = {}
    card_type = CardType.CREATURE
    subtypes = {CardSubtype.HUMAN, CardSubtype.EMPLOYEE}
    rarity = CardRarity.COMMON
    faction = CardFaction.CARGO
    card_set = CardSet.CORESET2020
    """TODO:
    Once per turn, you may give 'Cargo Technician' -1/0 until the start of your next turn and gain 1 mana.
    """


class Card_chap_plate(Card):
    name = "Crusader Armour"
    description = """The common war attire of chaplains. Mostly ceremonial."""
    rules = """{$Holy}"""

    cost = 2
    power = 2
    resolve = 2

    keywords = {CardKeyword.HOLY}
    card_type = CardType.EQUIPMENT
    subtypes = {CardSubtype.ARMOUR}
    rarity = CardRarity.COMMON
    faction = CardFaction.SERVICE
    card_set = CardSet.CORESET2020


class Card_chemist(Card):
    name = "Chemist"
    description = """Chemists are encouraged to not set up illicit methamphetamine factories on the company's dime."""
    rules = """Tap this card: flip a coin. If heads: a friendly Medical {$Faction} card gains 0/+2. If tails, an opponents creature of your choice gains +2/0."""

    cost = 2
    power = 0
    resolve = 3

    keywords = {}
    card_type = CardType.CREATURE
    subtypes = {CardSubtype.HUMAN, CardSubtype.DOCTOR}
    rarity = CardRarity.COMMON
    faction = CardFaction.MEDICAL
    card_set = CardSet.CORESET2020
    """TODO:
    Tap this card: flip a coin. If heads: a friendly Medical {$Faction} card gains 0/+2. If tails, an opponents creature of your choice gains +2/0.
    """


class Card_CE(Card):
    name = "Chief Engineer"
    description = """The Chief Engineer is in charge of keeping the station powered and intact."""
    rules = """If a battlefield card would otherwise be destroyed by an opponent's card effect, you may sacrifice an Engineering faction card of yours in play to negate the battlefield's destruction."""

    cost = 5
    power = 3
    resolve = 6

    keywords = {}
    card_type = CardType.CREATURE
    subtypes = {CardSubtype.HUMAN, CardSubtype.ENGINEER}
    rarity = CardRarity.UNCOMMON
    faction = CardFaction.ENGINEERING
    card_set = CardSet.CORESET2020
    """TODO:
    If a battlefield card would otherwise be destroyed by an opponent's card effect, you may sacrifice an Engineering faction card of yours in play to negate the battlefield's destruction.
    """


class Card_ce_suit(Card):
    name = "Nakamura Engineering R.I.G.Suit (Advanced)"
    description = """An updated version of Nakamura Engineering's R.I.G.Suit, fitted with advanced radiation shielding and extra armour."""
    rules = """Tap this card: tap the equipped creature. The equipped creature avoids the effects of the active battlefield until removed from the field."""

    cost = 3
    power = 0
    resolve = 3

    keywords = {}
    card_type = CardType.EQUIPMENT
    subtypes = {CardSubtype.ARMOUR}
    rarity = CardRarity.RARE
    faction = CardFaction.ENGINEERING
    card_set = CardSet.CORESET2020
    """TODO:
    Tap this card: tap the equipped creature. The equipped creature avoids the effects of the active battlefield until removed from the field.
    """


class Card_CMO(Card):
    name = "Chief Medical Officer"
    description = """Head of the medical department, the CMO is expected to maintain the standards of his underlings."""
    rules = """If a Medical faction card on your side of the field would gain power or resolve from an event, equipment, or card effect, it gains +1 more."""

    cost = 5
    power = 4
    resolve = 5

    keywords = {}
    card_type = CardType.CREATURE
    subtypes = {CardSubtype.HUMAN, CardSubtype.DOCTOR}
    rarity = CardRarity.COMMON
    faction = CardFaction.MEDICAL
    card_set = CardSet.CORESET2020
    """TODO:
    If a Medical faction card on your side of the field would gain power or resolve from an event, equipment, or card effect, it gains +1 more.
    """


class Card_cmo_suit(Card):
    name = "DeForest Medical Corporation 'Lifesaver' Carapace"
    description = """An advanced voidsuit designed for emergency medical personnel. Features include a built-in medical HUD and advanced medical gauntlets."""
    rules = """Tap this card: tap the equipped creature and re-equip 'DeForest Medical Corporation 'Lifesaver' Carapace' on a different creature on your side of the field. This effect may be activated once per turn."""

    cost = 3
    power = 1
    resolve = 3

    keywords = {}
    card_type = CardType.EQUIPMENT
    subtypes = {CardSubtype.ARMOUR}
    rarity = CardRarity.UNCOMMON
    faction = CardFaction.MEDICAL
    card_set = CardSet.CORESET2020
    """TODO:
    Tap this card: tap the equipped creature and re-equip 'DeForest Medical Corporation 'Lifesaver' Carapace' on a different creature on your side of the field. This effect may be activated once per turn.
    """


class Card_chrono(Card):
    name = "Chrono Legionnaire"
    description = """Currently in the earliest stages of development, the Chrono Legionnaire project is expected to weaponise time itself."""
    rules = """If this card is destroyed or discarded, flip 3 coins. If the result has 2 or more heads, add this card back to your hand. Otherwise, send it to your graveyard."""

    cost = 4
    power = 6
    resolve = 2

    keywords = {}
    card_type = CardType.CREATURE
    subtypes = {CardSubtype.HUMAN, CardSubtype.SOLDIER}
    rarity = CardRarity.EPIC
    faction = CardFaction.SECURITY
    card_set = CardSet.CORESET2020
    """TODO:
    If this card is destroyed or discarded, flip 3 coins. If the result has 2 or more heads, add this card back to your hand. Otherwise, send it to your graveyard.
    """


class Card_sloth(Card):
    name = "Citrus"
    description = """Cargo's happy sloth pal. Known for his cute sweater and always getting in the way."""
    rules = """Tap this card: Tap an opponent's card until the start of your next turn"""

    cost = 2
    power = 0
    resolve = 3

    keywords = {}
    card_type = CardType.CREATURE
    subtypes = {CardSubtype.SLOTH}
    rarity = CardRarity.COMMON
    faction = CardFaction.CARGO
    card_set = CardSet.CORESET2020
    """TODO:
    Tap this card: Tap an opponent's card until the start of your next turn
    """


class Card_clown(Card):
    name = "Clown"
    description = """Every Nanotrasen station has a clown on board, as high command believes that a source of entertainment will reduce instances of murder-suicide on board Spinward Stations. The results of this hypothesis are, as of yet, unproven."""
    rules = """{$Taunt}"""

    cost = 2
    power = 2
    resolve = 4

    keywords = {CardKeyword.TAUNT}
    card_type = CardType.CREATURE
    subtypes = {CardSubtype.CLOWN}
    rarity = CardRarity.COMMON
    faction = CardFaction.SERVICE
    card_set = CardSet.CORESET2020


class Card_clownborg(Card):
    name = "Cyborg (Clown Shell)"
    description = """The clown shell is a new development in cyborg technology, designed to capture the joyous hijinks of the station clown in a notably more macabre and disturbing fashion."""
    rules = """{$Taunt}, {$Asimov}"""

    cost = 2
    power = 2
    resolve = 4

    keywords = {CardKeyword.TAUNT, CardKeyword.ASIMOV}
    card_type = CardType.CREATURE
    subtypes = {CardSubtype.SILICON, CardSubtype.CLOWN}
    rarity = CardRarity.UNCOMMON
    faction = CardFaction.SERVICE
    card_set = CardSet.CORESET2020


class Card_clown_suit(Card):
    name = "HONK Ltd. Entertainment Voidsuit"
    description = """The most advanced clown suit produced by HONK Ltd. the Entertainment Voidsuit is designed to withstand extreme conditions while still maintaining the aesthetic expected of clowns."""
    rules = """{$On Equip}: give the equipped unit {$Taunt}."""

    cost = 1
    power = 0
    resolve = 0

    keywords = {}
    card_type = CardType.EQUIPMENT
    subtypes = {CardSubtype.ARMOUR}
    rarity = CardRarity.EPIC
    faction = CardFaction.SERVICE
    card_set = CardSet.CORESET2020
    """TODO:
    {$On Equip}: give the equipped unit {$Taunt}.
    """


class Card_abductor_armour(Card):
    name = "Abductor Combat Armour"
    description = """Recovered from the strange alien species known as the Abductors, this armour is made from an extremely tough yet flexible material that has been dubbed as Alien Alloy by researchers."""
    rules = """{$On Equip}: give the equipped unit Effect {$Immunity} and Spell {$Immunity}."""

    cost = 4
    power = 1
    resolve = 3

    keywords = {}
    card_type = CardType.EQUIPMENT
    subtypes = {CardSubtype.ARMOUR}
    rarity = CardRarity.UNCOMMON
    faction = CardFaction.SYNDICATE
    card_set = CardSet.CORESET2020
    """TODO:
    {$On Equip}: give the equipped unit Effect {$Immunity} and Spell {$Immunity}.
    """


class Card_chef(Card):
    name = "Cook"
    description = """Every Nanotrasen chef is trained in 3 cuisines of their choosing upon being hired, alongside the closely guarded secret of Close Quarters Cooking."""
    rules = """{$First Strike}"""

    cost = 3
    power = 3
    resolve = 2

    keywords = {CardKeyword.FIRST_STRIKE}
    card_type = CardType.CREATURE
    subtypes = {CardSubtype.HUMAN, CardSubtype.EMPLOYEE}
    rarity = CardRarity.COMMON
    faction = CardFaction.SERVICE
    card_set = CardSet.CORESET2020


class Card_wiz_suit(Card):
    name = "Wizard Federation Standard Issue Hardsuit"
    description = """Seemingly reverse engineered from captured engineering hardsuits, the iconic Wizard Federation Hardsuit is a spectacular melding of technology and magic."""
    rules = """{$On Equip}: The equipped creature cannot attack targets with {$Holy}."""

    cost = 1
    power = 3
    resolve = 1

    keywords = {}
    card_type = CardType.EQUIPMENT
    subtypes = {CardSubtype.ARMOUR}
    rarity = CardRarity.RARE
    faction = CardFaction.SYNDICATE
    card_set = CardSet.CORESET2020
    """TODO:
    {$On Equip}: The equipped creature cannot attack targets with {$Holy}.
    """


class Card_curator(Card):
    name = "Curator"
    description = """In Nanotrasen polls, the Curator has ranked as the most pointless job on station, much to the ire of the Curator's union. Thankfully, we don't have to listen to them."""
    rules = """{$On Summon}: Draw 1 card: if it's an event card, discard it."""

    cost = 2
    power = 1
    resolve = 1

    keywords = {}
    card_type = CardType.CREATURE
    subtypes = {CardSubtype.HUMAN, CardSubtype.WORKER}
    rarity = CardRarity.COMMON
    faction = CardFaction.SERVICE
    card_set = CardSet.CORESET2020
    """TODO:
    {$On Summon}: Draw 1 card: if it's an event card, discard it.
    """


class Card_ianborg(Card):
    name = "Borgi Ian"
    description = """While Ian's cyborg costume is very convincing, we at the NTED would like to remind all employees that Ian has not been experimented on."""
    rules = """{$Asimov}. You may sacrifice this card in play: Summon a Silicon type card from your hand worth up to double this card's cost."""

    cost = 2
    power = 0
    resolve = 3

    keywords = {CardKeyword.ASIMOV}
    card_type = CardType.CREATURE
    subtypes = {CardSubtype.SILICON, CardSubtype.CORGI}
    rarity = CardRarity.RARE
    faction = CardFaction.SCIENCE
    card_set = CardSet.CORESET2020
    """TODO:
    {$Asimov}. You may sacrifice this card in play: Summon a Silicon type card from your hand worth up to double this card's cost.
    """


class Card_deathsquad_armour(Card):
    name = "Apadyne Technologies Mk.3 R.I.O.T. Carapace"
    description = """The most advanced set of armour available for purchase from Apadyne Technologies, the Mk.3 R.I.O.T. Carapace is issued to Nanotrasen's most elite forces."""
    rules = """{$On Equip}: if the equipped creature is of the Security faction, it gains {$Taunt}."""

    cost = 1
    power = 3
    resolve = 3

    keywords = {}
    card_type = CardType.EQUIPMENT
    subtypes = {CardSubtype.ARMOUR}
    rarity = CardRarity.EPIC
    faction = CardFaction.SECURITY
    card_set = CardSet.CORESET2020
    """TODO:
    {$On Equip}: if the equipped creature is of the Security faction, it gains {$Taunt}.
    """


class Card_det(Card):
    name = "Detective"
    description = """Nanotrasen hires nothing but the best detectives to investigate crime on our stations. A penchant for cigarettes and outdated fashion isn't mandatory, but is appreciated."""
    rules = """{$Deadeye}"""

    cost = 5
    power = 3
    resolve = 2

    keywords = {CardKeyword.DEADEYE}
    card_type = CardType.CREATURE
    subtypes = {CardSubtype.HUMAN, CardSubtype.OFFICER}
    rarity = CardRarity.UNCOMMON
    faction = CardFaction.SECURITY
    card_set = CardSet.CORESET2020


class Card_nukie_elite(Card):
    name = "Elite Syndicate Nuclear Stormtrooper"
    description = """The best of the best of the syndicate troops, elite stormtroopers can be distinguished by their black armour. Shoot on sight, ask questions later!"""
    rules = """{$Fury}"""

    cost = 7
    power = 5
    resolve = 5

    keywords = {CardKeyword.FURY}
    card_type = CardType.CREATURE
    subtypes = {CardSubtype.SYNDICATE, CardSubtype.SOLDIER}
    rarity = CardRarity.RARE
    faction = CardFaction.SYNDICATE
    card_set = CardSet.CORESET2020


class Card_engiborg(Card):
    name = "Cyborg (Engineering Shell)"
    description = """A common sight on Nanotrasen Stations, Engineering Shells maintain critical station systems in hazardous conditions."""
    rules = """{$Asimov}"""

    cost = 2
    power = 2
    resolve = 2

    keywords = {CardKeyword.ASIMOV}
    card_type = CardType.CREATURE
    subtypes = {CardSubtype.SILICON}
    rarity = CardRarity.COMMON
    faction = CardFaction.ENGINEERING
    card_set = CardSet.CORESET2020


class Card_ert_command(Card):
    name = "NT P.A.V. Suit (Command)"
    description = """Issued to members of Emergency Response Teams, the P.A.V. Suit gives superior protection from any threat the galaxy can throw at it. This particular model is outfitted with a sidearm holster and a sleek blue finish."""
    rules = """While equipped, give the equipped unit {$Squad Tactics} and {$First Strike}."""

    cost = 2
    power = 2
    resolve = 2

    keywords = {}
    card_type = CardType.EQUIPMENT
    subtypes = {CardSubtype.ARMOUR}
    rarity = CardRarity.RARE
    faction = CardFaction.COMMAND
    card_set = CardSet.CORESET2020
    """TODO:
    While equipped, give the equipped unit {$Squad Tactics} and {$First Strike}.
    """


class Card_ert_engi(Card):
    name = "NT P.A.V. Suit (Engineering)"
    description = """Issued to members of Emergency Response Teams, the P.A.V. Suit gives superior protection from any threat the galaxy can throw at it. This particular model is outfitted with a welding screen and a flashy yellow finish."""
    rules = """While equipped, give the equipped unit {$Squad Tactics}."""

    cost = 1
    power = 1
    resolve = 1

    keywords = {}
    card_type = CardType.EQUIPMENT
    subtypes = {CardSubtype.ARMOUR}
    rarity = CardRarity.UNCOMMON
    faction = CardFaction.ENGINEERING
    card_set = CardSet.CORESET2020
    """TODO:
    While equipped, give the equipped unit {$Squad Tactics}.
    """


class Card_ert_med(Card):
    name = "NT P.A.V. Suit (Medical)"
    description = """Issued to members of Emergency Response Teams, the P.A.V. Suit gives superior protection from any threat the galaxy can throw at it. This particular model is outfitted with a sterile coating and a calming white finish."""
    rules = """While equipped, give the equipped unit {$Squad Tactics}."""

    cost = 2
    power = 1
    resolve = 2

    keywords = {}
    card_type = CardType.EQUIPMENT
    subtypes = {CardSubtype.ARMOUR}
    rarity = CardRarity.UNCOMMON
    faction = CardFaction.MEDICAL
    card_set = CardSet.CORESET2020
    """TODO:
    While equipped, give the equipped unit {$Squad Tactics}.
    """


class Card_ert_sec(Card):
    name = "NT P.A.V. Suit (Security)"
    description = """Issued to members of Emergency Response Teams, the P.A.V. Suit gives superior protection from any threat the galaxy can throw at it. This particular model is outfitted with bulletproof padding and an intimidating red finish."""
    rules = """While equipped, give the equipped unit {$Squad Tactics}."""

    cost = 2
    power = 2
    resolve = 1

    keywords = {}
    card_type = CardType.EQUIPMENT
    subtypes = {CardSubtype.ARMOUR}
    rarity = CardRarity.UNCOMMON
    faction = CardFaction.SECURITY
    card_set = CardSet.CORESET2020
    """TODO:
    While equipped, give the equipped unit {$Squad Tactics}.
    """


class Card_explorer(Card):
    name = "Explorer"
    description = """The Nanotrasen Explorers Corps boldly goes where humanity has never gone before. Or would, if they weren't buried under mounds of bureaucracy."""
    rules = """You may tap this card: Flip a coin, if heads, gain 4 mana this turn, if tails, tap this card for 2 turns."""

    cost = 2
    power = 2
    resolve = 2

    keywords = {}
    card_type = CardType.CREATURE
    subtypes = {CardSubtype.HUMAN, CardSubtype.EXPLORER}
    rarity = CardRarity.LEGENDARY
    faction = CardFaction.CARGO
    card_set = CardSet.CORESET2020
    """TODO:
    You may tap this card: Flip a coin, if heads, gain 4 mana this turn, if tails, tap this card for 2 turns.
    """


class Card_borg(Card):
    name = "Cyborg"
    description = """Created as part of humanity's first foray into artificial intelligence, the original cyborg models used organic parts in lieu of sophisticated artificial brains."""
    rules = """{$Asimov}"""

    cost = 2
    power = 3
    resolve = 3

    keywords = {CardKeyword.ASIMOV}
    card_type = CardType.CREATURE
    subtypes = {CardSubtype.SILICON}
    rarity = CardRarity.COMMON
    faction = CardFaction.SCIENCE
    card_set = CardSet.CORESET2020


class Card_geneticist(Card):
    name = "Geneticist"
    description = """Geneticists are tasked with manipulating human DNA to produce special effects. Nanotrasen maintains a strict 'no superhero' policy for mutations, following the Superhero Civil War of 2150."""
    rules = """You may tap this card and pay 3 mana: Give a friendly creature {$Hivemind} until this card leaves the field."""

    cost = 3
    power = 3
    resolve = 4

    keywords = {}
    card_type = CardType.CREATURE
    subtypes = {CardSubtype.HUMAN, CardSubtype.SCIENTIST}
    rarity = CardRarity.COMMON
    faction = CardFaction.SCIENCE
    card_set = CardSet.CORESET2020
    """TODO:
    You may tap this card and pay 3 mana: Give a friendly creature {$Hivemind} until this card leaves the field.
    """


class Card_med_geneticist(Card):
    name = "Geneticist"
    description = """Geneticists are tasked with manipulating human DNA to produce special effects. Nanotrasen maintains a strict 'no superhero' policy for mutations, following the Superhero Civil War of 2150."""
    rules = """{$Graytide}, {$Hivemind}"""

    cost = 8
    power = 3
    resolve = 6

    keywords = {CardKeyword.GRAYTIDE, CardKeyword.HIVEMIND}
    card_type = CardType.CREATURE
    subtypes = {CardSubtype.HUMAN, CardSubtype.DOCTOR}
    rarity = CardRarity.MISPRINT
    faction = CardFaction.MEDICAL
    card_set = CardSet.CORESET2020


class Card_spookian(Card):
    name = "Ghost Ian"
    description = """Oh my god! Ian's dead!"""
    rules = """{$On Summon}: Search your deck for a battlefield, and add it to your hand. Shuffle your deck afterwards."""

    cost = 3
    power = 1
    resolve = 1

    keywords = {}
    card_type = CardType.CREATURE
    subtypes = {CardSubtype.SPIRIT, CardSubtype.CORGI}
    rarity = CardRarity.EPIC
    faction = CardFaction.SERVICE
    card_set = CardSet.CORESET2020
    """TODO:
    {$On Summon}: Search your deck for a battlefield, and add it to your hand. Shuffle your deck afterwards.
    """


class Card_HOP(Card):
    name = "Head of Personnel"
    description = """The head of the Cargo and Service Departments, guardian of all access, and Ian's lovable, yet dumb, sidekick."""
    rules = """Once per turn: Select a friendly creature card. That card gains {$Changeling}."""

    cost = 7
    power = 4
    resolve = 3

    keywords = {}
    card_type = CardType.CREATURE
    subtypes = {CardSubtype.HUMAN, CardSubtype.COMMANDER}
    rarity = CardRarity.UNCOMMON
    faction = CardFaction.SERVICE
    card_set = CardSet.CORESET2020
    """TODO:
    Once per turn: Select a friendly creature card. That card gains {$Changeling}.
    """


class Card_HOS(Card):
    name = "Head of Security"
    description = """Nanotrasen hires most heads of staff based on their qualifications as being amicable, good at conflict resolution, ability to handle high-stakes situations, humanity, and desire to learn. Heads of Security only need a highschool degree."""
    rules = """{$On Summon}: Select a card type. That card type now costs 1 extra mana to summon. This effect persists until Head of Security is removed from the battlefield."""

    cost = 7
    power = 4
    resolve = 4

    keywords = {}
    card_type = CardType.CREATURE
    subtypes = {CardSubtype.HUMAN, CardSubtype.OFFICER}
    rarity = CardRarity.UNCOMMON
    faction = CardFaction.SECURITY
    card_set = CardSet.CORESET2020
    """TODO:
    {$On Summon}: Select a card type. That card type now costs 1 extra mana to summon. This effect persists until Head of Security is removed from the battlefield.
    """


class Card_hos_suit(Card):
    name = "Apadyne Technologies 'Tyrant' Class Hardshell"
    description = """The distinctive shape of the Tyrant Class Hardshell is caused, in part, by the large amount of kevlar reinforcement and the ablative armour layer. Perhaps more importantly, it also looks rad."""
    rules = """Grant the equip card {$Fury} until this card is removed from play."""

    cost = 5
    power = 4
    resolve = 2

    keywords = {}
    card_type = CardType.EQUIPMENT
    subtypes = {CardSubtype.ARMOUR}
    rarity = CardRarity.RARE
    faction = CardFaction.SECURITY
    card_set = CardSet.CORESET2020
    """TODO:
    Grant the equip card {$Fury} until this card is removed from play.
    """


class Card_ian(Card):
    name = "Ian"
    description = """This adorable corgi has become the defacto mascot of the Spinward Stations to many. He comes in many forms, many sizes, and many shapes, but he's still just as lovable. Hand wash only."""
    rules = """{$Holy}, You may Sacrifice this card on the field: Play a Command card from your hand for free."""

    cost = 4
    power = 0
    resolve = 3

    keywords = {CardKeyword.HOLY}
    card_type = CardType.CREATURE
    subtypes = {CardSubtype.CORGI}
    rarity = CardRarity.COMMON
    faction = CardFaction.SERVICE
    card_set = CardSet.CORESET2020
    """TODO:
    {$Holy}, You may Sacrifice this card on the field: Play a Command card from your hand for free.
    """


class Card_inquisitor_suit(Card):
    name = "Inquisitor's Hardsuit"
    description = """Nanotrasen officially doesn't believe in ghosts, magic, or anything that can't be solved with science. When you see someone show up in one of these, let that remind you of that fact."""
    rules = """Apply {$First Strike} to the equip creature."""

    cost = 4
    power = 2
    resolve = 2

    keywords = {}
    card_type = CardType.EQUIPMENT
    subtypes = {CardSubtype.ARMOUR}
    rarity = CardRarity.EPIC
    faction = CardFaction.SERVICE
    card_set = CardSet.CORESET2020
    """TODO:
    Apply {$First Strike} to the equip creature.
    """


class Card_intern(Card):
    name = "Intern"
    description = """All Nanotrasen interns come with 3 things: A resume, a desire to learn, and vague promises that they're getting paid at some point. So don't be too rough on them."""
    rules = """{$First Strike}"""

    cost = 1
    power = 1
    resolve = 1

    keywords = {CardKeyword.FIRST_STRIKE}
    card_type = CardType.HUMAN
    subtypes = {CardSubtype.HUMAN, CardSubtype.EMPLOYEE}
    rarity = CardRarity.COMMON
    faction = CardFaction.COMMAND
    card_set = CardSet.CORESET2020


class Card_jannie(Card):
    name = "Janitor"
    description = """A true testament to futility, they clean and they clean and they clean, knowing that there's no way they can clean it all. Yet, they perservere, knowing that without them, the crew would simply give in to their base animalistic nature."""
    rules = """{$Taunt}"""

    cost = 1
    power = 1
    resolve = 1

    keywords = {CardKeyword.TAUNT}
    card_type = CardType.HUMAN
    subtypes = {CardSubtype.HUMAN, CardSubtype.EMPLOYEE}
    rarity = CardRarity.COMMON
    faction = CardFaction.SERVICE
    card_set = CardSet.CORESET2020


class Card_jannieborg(Card):
    name = "Cyborg (Custodial Shell)"
    description = """A powerful, state of the act cleaning machine. They exist to eradicate stains, snag garbage, and replace lights, forever. We are legally obligated by the Janitor's Union to state that these machines are no replacement for a flesh-and-blood janitor."""
    rules = """{$Asimov}, you may tap this card: Tap an opponent's Human Creature as well."""

    cost = 2
    power = 1
    resolve = 3

    keywords = {CardKeyword.ASIMOV}
    card_type = CardType.CREATURE
    subtypes = {CardSubtype.SILICON}
    rarity = CardRarity.COMMON
    faction = CardFaction.SERVICE
    card_set = CardSet.CORESET2020
    """TODO:
    {$Asimov}, you may tap this card: Tap an opponent's Human Creature as well.
    """


class Card_lawyer(Card):
    name = "Lawyer"
    description = """Nanotrasen knows the value of a good lawyer. That's why they're all working hard at our home offices defending us from frivolous labor suits from lazy no-good employees who should be working hard instead of slacking off reading trading cards."""
    rules = """When an opponent attacks with a creature with 3 or more power, this card gains {$Taunt}."""

    cost = 2
    power = 0
    resolve = 4

    keywords = {}
    card_type = CardType.CREATURE
    subtypes = {CardSubtype.HUMAN, CardSubtype.EMPLOYEE}
    rarity = CardRarity.COMMON
    faction = CardFaction.SERVICE
    card_set = CardSet.CORESET2020
    """TODO:
    When an opponent attacks with a creature with 3 or more power, this card gains {$Taunt}.
    """


class Card_legion(Card):
    name = "Legion"
    description = """They are the cursed, damned souls of civilizations born and lost in the flames of Indecipheres, conglomerated into a lump of emaciated bodies, wandering the realms they used to rule... or something along those lines, anyway."""
    rules = """When Legion is destroyed, search your deck for a human card, and summon it to the battlefield. Shuffle your deck afterward."""

    cost = 3
    power = 2
    resolve = 1

    keywords = {}
    card_type = CardType.CREATURE
    subtypes = {CardSubtype.ABOMINATION}
    rarity = CardRarity.UNCOMMON
    faction = CardFaction.XENO
    card_set = CardSet.CORESET2020
    """TODO:
    When Legion is destroyed, search your deck for a human card, and summon it to the battlefield. Shuffle your deck afterward.
    """


class Card_medborg(Card):
    name = "Cyborg (Medical Shell)"
    description = """A state of the art medical shell, for when biological life just can't take care of itself. Comes equipped with built-in surgical equipment and all the medicated lollipops you could ever want."""
    rules = """{$Asimov}, you may tap this card and pay 2 mana: Reset a card's resolve to it's original value."""

    cost = 4
    power = 2
    resolve = 3

    keywords = {CardKeyword.ASIMOV}
    card_type = CardType.CREATURE
    subtypes = {CardSubtype.SILICON, CardSubtype.DOCTOR}
    rarity = CardRarity.UNCOMMON
    faction = CardFaction.MEDICAL
    card_set = CardSet.CORESET2020
    """TODO:
    {$Asimov}, you may tap this card and pay 2 mana: Reset a card's resolve to it's original value.
    """


class Card_doc(Card):
    name = "Medical Doctor"
    description = """Nanotrasen's doctors are well known for their ability to treat almost any ailment known to mankind... as well as causing a fair few in the process."""
    rules = """You may tap this card: Select a card that has less attack than this card from your graveyard, and summon it to your side of the field."""

    cost = 3
    power = 2
    resolve = 3

    keywords = {}
    card_type = CardType.CREATURE
    subtypes = {CardSubtype.HUMAN, CardSubtype.DOCTOR}
    rarity = CardRarity.COMMON
    faction = CardFaction.MEDICAL
    card_set = CardSet.CORESET2020
    """TODO:
    You may tap this card: Select a card that has less attack than this card from your graveyard, and summon it to your side of the field.
    """


class Card_mime(Card):
    name = "Mime"
    description = """Si vous regardez attentivement dans les yeux d'un mime, vous pouvez voir le tourment sans fin derrière leur façade silencieuse. C'est vraiment tragique."""
    rules = """You may tap this card: Pick an opponent's card and nullify it's effect until it leaves play."""

    cost = 1
    power = 2
    resolve = 1

    keywords = {}
    card_type = CardType.CREATURE
    subtypes = {CardSubtype.MIME}
    rarity = CardRarity.UNCOMMON
    faction = CardFaction.SERVICE
    card_set = CardSet.CORESET2020
    """TODO:
    You may tap this card: Pick an opponent's card and nullify it's effect until it leaves play.
    """


class Card_miningborg(Card):
    name = "Cyborg (Mining Shell)"
    description = """Fitted with a drill and tracks, the Mining Shell is designed to hold up to the rigours of mining, be that on the hellish surface of Indecipheres, or in the silent vacuum of the asteroid belt."""
    rules = """{$Asimov}, at the end of your turn, if this card is not tapped, you may tap this card at the start of your next turn to gain 1 mana."""

    cost = 2
    power = 3
    resolve = 1

    keywords = {CardKeyword.ASIMOV}
    card_type = CardType.CREATURE
    subtypes = {CardSubtype.SILICON, CardSubtype.MINER}
    rarity = CardRarity.COMMON
    faction = CardFaction.CARGO
    card_set = CardSet.CORESET2020
    """TODO:
    {$Asimov}, at the end of your turn, if this card is not tapped, you may tap this card at the start of your next turn to gain 1 mana.
    """


class Card_monkey(Card):
    name = "Monkey"
    description = """Nanotrasen seeks to phase out animal testing by 2570, in accordance with new TerraGov legislation. This will be replaced with more ethical solutions, such as computer simulations, or experimentation on Staff Assistants."""
    rules = """{$Graytide}, this card is considered Human with a Geneticist on your side of the field."""

    cost = 1
    power = 1
    resolve = 1

    keywords = {CardKeyword.GRAYTIDE}
    card_type = CardType.CREATURE
    subtypes = {CardSubtype.PRIMATE}
    rarity = CardRarity.COMMON
    faction = CardFaction.SCIENCE
    card_set = CardSet.CORESET2020
    """TODO:
    {$Graytide}, this card is considered Human with a Geneticist on your side of the field.
    """


class Card_nukeop(Card):
    name = "Nuclear Operative"
    description = """The frontline grunts of the syndicate army, Nuclear Operatives are typically well trained and equipped for their grim duty."""
    rules = """{$Squad Tactics}"""

    cost = 4
    power = 4
    resolve = 2

    keywords = {CardKeyword.SQUAD_TACTICS}
    card_type = CardType.CREATURE
    subtypes = {CardSubtype.SYNDICATE, CardSubtype.SOLDIER}
    rarity = CardRarity.RARE
    faction = CardFaction.SYNDICATE
    card_set = CardSet.CORESET2020


class Card_paramed(Card):
    name = "Paramedic"
    description = """Nanotrasen encourages all paramedics to think of others before themselves- if this means running through a plasma fire to save a colleague, so be it."""
    rules = """{$Taunt}, {$First Strike}"""

    cost = 3
    power = 2
    resolve = 3

    keywords = {CardKeyword.TAUNT, CardKeyword.FIRST_STRIKE}
    card_type = CardType.CREATURE
    subtypes = {CardSubtype.HUMAN, CardSubtype.DOCTOR}
    rarity = CardRarity.COMMON
    faction = CardFaction.MEDICAL
    card_set = CardSet.CORESET2020


class Card_peaceborg(Card):
    name = "Cyborg (Peacekeeper Shell)"
    description = """After the unilateral phasing out of Security Shells in 2554 following mass reports of cyborg-on-human violence, the Peacekeeper Shell was introduced as a stopgap solution until the problems could be resolved."""
    rules = """{$Asimov}, this card loses -1 power for every creature on your opponent's side of the field"""

    cost = 2
    power = 3
    resolve = 3

    keywords = {CardKeyword.ASIMOV}
    card_type = CardType.CREATURE
    subtypes = {CardSubtype.SILICON, CardSubtype.OFFICER}
    rarity = CardRarity.UNCOMMON
    faction = CardFaction.SECURITY
    card_set = CardSet.CORESET2020
    """TODO:
    {$Asimov}, this card loses -1 power for every creature on your opponent's side of the field
    """


class Card_plasma_engi(Card):
    name = "Station Engineer (Plasmaman)"
    description = """The ever industrious plasmamen are well suited to engineering work, due to their natural radiation resistance."""
    rules = """{$Immunity} to Battlefields"""

    cost = 5
    power = 2
    resolve = 4

    keywords = {CardKeyword.IMMUNITY_BATTLEFIELD}
    card_type = CardType.CREATURE
    subtypes = {CardSubtype.PLASMAMAN, CardSubtype.ENGINEER}
    rarity = CardRarity.COMMON
    faction = CardFaction.ENGINEERING
    card_set = CardSet.CORESET2020


class Card_QM(Card):
    name = "Quartermaster"
    description = """Every Nanotrasen station has a Quartermaster, who controls the flow of cargo to and from the station, and by extension to and from the hands of the crew. He's not given the distinction of being a head, though. His job isn't hard enough."""
    rules = """Pay 3 mana and tap this card: All card cards on your side of the field gain +1/+1 until the end of this turn."""

    cost = 6
    power = 3
    resolve = 3

    keywords = {}
    card_type = CardType.CREATURE
    subtypes = {CardSubtype.HUMAN, CardSubtype.EMPLOYEE}
    rarity = CardRarity.UNCOMMON
    faction = CardFaction.CARGO
    card_set = CardSet.CORESET2020
    """TODO:
    Pay 3 mana and tap this card: All card cards on your side of the field gain +1/+1 until the end of this turn.
    """


class Card_qm_head(Card):
    name = "Quartermaster"
    description = """Every Nanotrasen station has a Quartermaster, who controls the flow of cargo to and from the station, and by extension to and from the hands of the crew."""
    rules = """Pay 8 mana and permanantly tap this card: All cargo cards on your side of the field gain +2/+2 until this card leaves play."""

    cost = 10
    power = 6
    resolve = 6

    keywords = {}
    card_type = CardType.CREATURE
    subtypes = {CardSubtype.HUMAN, CardSubtype.EMPLOYEE}
    rarity = CardRarity.MISPRINT
    faction = CardFaction.CARGO
    card_set = CardSet.CORESET2020
    """TODO:
    Pay 8 mana and permanantly tap this card: All cargo cards on your side of the field gain +2/+2 until this card leaves play.
    """


class Card_rabbit_pai(Card):
    name = "Personal AI Device (Rabbit Shell)"
    description = """Personal AI Devices are able to take the form of many household pets, to provide a homely sense of comfort and companionship to their owners."""
    rules = """This card may steal the {$Asimov} keyword off of another friendly silicon creature."""

    cost = 2
    power = 0
    resolve = 1

    keywords = {}
    card_type = CardType.CREATURE
    subtypes = {CardSubtype.SILICON, CardSubtype.RABBIT}
    rarity = CardRarity.COMMON
    faction = CardFaction.SCIENCE
    card_set = CardSet.CORESET2020
    """TODO:
    This card may steal the {$Asimov} keyword off of another friendly silicon creature.
    """


class Card_drone_pai(Card):
    name = "Personal AI Device (Drone Shell)"
    description = """The most basic Personal AI shell, the Drone Shell resembles the old maintainance drones used on Nanotrasen Stations prior to 'the incident', and is perfect for the tech-savvy AI-owner."""
    rules = """You may pay 1 mana and tap this card: a silicon card may attack one additional time this turn."""

    cost = 5
    power = 2
    resolve = 4

    keywords = {}
    card_type = CardType.CREATURE
    subtypes = {CardSubtype.SILICON, CardSubtype.DRONE}
    rarity = CardRarity.COMMON
    faction = CardFaction.SCIENCE
    card_set = CardSet.CORESET2020
    """TODO:
    You may pay 1 mana and tap this card: a silicon card may attack one additional time this turn.
    """


class Card_RD(Card):
    name = "Research Director"
    description = """The Research Director is the head of the Science Division, and is responsible for, shockingly, directing research."""
    rules = """Once per turn, you may tap all Science faction cards in play, activate the effect of an event card twice."""

    cost = 7
    power = 2
    resolve = 5

    keywords = {}
    card_type = CardType.CREATURE
    subtypes = {CardSubtype.HUMAN, CardSubtype.SCIENTIST}
    rarity = CardRarity.UNCOMMON
    faction = CardFaction.SCIENCE
    card_set = CardSet.CORESET2020
    """TODO:
    Once per turn, you may tap all Science faction cards in play, activate the effect of an event card twice.
    """


class Card_rd_suit(Card):
    name = "Nakamura Engineering B.O.M.B.Suit"
    description = """The Nakamura Engineering B.O.M.B.Suit is an innovative combination of a R.I.G.Suit and a bomb suit, perfect for toxins research."""
    rules = """Reduces all battlefield damage to the equipped creature by 2."""

    cost = 1
    power = 0
    resolve = 0

    keywords = {}
    card_type = CardType.EQUIPMENT
    subtypes = {CardSubtype.ARMOUR}
    rarity = CardRarity.RARE
    faction = CardFaction.SCIENCE
    card_set = CardSet.CORESET2020
    """TODO:
    Reduces all battlefield damage to the equipped creature by 2.
    """


class Card_roboticist(Card):
    name = "Roboticist"
    description = """The roboticist's work is as close as Nanotrasen legally allows its employees to come to necromancy."""
    rules = """If a {$Asimov} card on your side of the field is destroyed, you may pay 2 mana and tap this card: Return that card to your hand."""

    cost = 3
    power = 2
    resolve = 2

    keywords = {}
    card_type = CardType.CREATURE
    subtypes = {CardSubtype.HUMAN, CardSubtype.SCIENTIST}
    rarity = CardRarity.UNCOMMON
    faction = CardFaction.SCIENCE
    card_set = CardSet.CORESET2020
    """TODO:
    If a {$Asimov} card on your side of the field is destroyed, you may pay 2 mana and tap this card: Return that card to your hand.
    """


class Card_runtime(Card):
    name = "Runtime"
    description = """Runtime is the CMO's personal feline companion, and is well known for her laziness. It's said that opening a tin of tuna anywhere on the station will bring her running."""
    rules = """You may sacrifice this card: reduce the cost of summoning a medical faction card this turn by 2 mana."""

    cost = 3
    power = 0
    resolve = 1

    keywords = {}
    card_type = CardType.CREATURE
    subtypes = {CardSubtype.CAT}
    rarity = CardRarity.UNCOMMON
    faction = CardFaction.MEDICAL
    card_set = CardSet.CORESET2020
    """TODO:
    You may sacrifice this card: reduce the cost of summoning a medical faction card this turn by 2 mana.
    """


class Card_scientist(Card):
    name = "Scientist"
    description = """Rumours that Nanotrasen hires 'mad scientists' are greatly exaggerated. Scientists are regularly screened to ensure that their insanity remains within acceptable limits."""
    rules = """When this card is targeted by an opponent's single target event, you gain 1 lifeshard."""

    cost = 4
    power = 1
    resolve = 2

    keywords = {}
    card_type = CardType.CREATURE
    subtypes = {CardSubtype.HUMAN, CardSubtype.SCIENTIST}
    rarity = CardRarity.COMMON
    faction = CardFaction.SCIENCE
    card_set = CardSet.CORESET2020
    """TODO:
    When this card is targeted by an opponent's single target event, you gain 1 lifeshard.
    """


class Card_secborg(Card):
    name = "Cyborg (Security Shell)"
    description = """Following an incident in 2554, the Security Cyborg Shell was unilaterally phased out and replaced by the Peacekeeper. Nonetheless, many units remain in service with various other organisations such as private militaries."""
    rules = """{$Asimov}, when this card targets a human creature, deal 1 damage to it after the battle resolves."""

    cost = 6
    power = 4
    resolve = 2

    keywords = {CardKeyword.ASIMOV}
    card_type = CardType.CREATURE
    subtypes = {CardSubtype.SILICON, CardSubtype.OFFICER}
    rarity = CardRarity.EPIC
    faction = CardFaction.SECURITY
    card_set = CardSet.CORESET2020
    """TODO:
    {$Asimov}, when this card targets a human creature, deal 1 damage to it after the battle resolves.
    """


class Card_sec_officer(Card):
    name = "Security Officer"
    description = """Nanotrasen would like to remind all employees to support their station security team; remember, the boys in red keep you safe!"""
    rules = """{$Squad Tactics}"""

    cost = 3
    power = 2
    resolve = 2

    keywords = {CardKeyword.SQUAD_TACTICS}
    card_type = CardType.CREATURE
    subtypes = {CardSubtype.HUMAN, CardSubtype.OFFICER}
    rarity = CardRarity.COMMON
    faction = CardFaction.SECURITY
    card_set = CardSet.CORESET2020


class Card_ratvar_armor(Card):
    name = "Ratvarian Clockwork Cuirass"
    description = """Fashioned from paranormally reinforced brass, the Ratvar Cult's clockwork armour is as beautiful as it is heretical."""
    rules = """While equipped, give the equipped unit {$Clockwork}."""

    cost = 4
    power = 2
    resolve = 2

    keywords = {}
    card_type = CardType.EQUIPMENT
    subtypes = {CardSubtype.ARMOUR}
    rarity = CardRarity.EPIC
    faction = CardFaction.SYNDICATE
    card_set = CardSet.CORESET2020
    """TODO:
    While equipped, give the equipped unit {$Clockwork}.
    """


class Card_beercanborg(Card):
    name = "Cyborg (Service Shell- Beercan)"
    description = """Despite being based on the Medical Shell, this particular Service Shell is tasked with destroying livers, rather than healing them."""
    rules = """{$Asimov}, you may discard this card: draw one Service {$Faction} card from your deck, then shuffle."""

    cost = 1
    power = 1
    resolve = 1

    keywords = {CardKeyword.ASIMOV}
    card_type = CardType.CREATURE
    subtypes = {CardSubtype.SILICON}
    rarity = CardRarity.UNCOMMON
    faction = CardFaction.SERVICE
    card_set = CardSet.CORESET2020
    """TODO:
    {$Asimov}, you may discard this card: draw one Service {$Faction} card from your deck, then shuffle.
    """


class Card_flamboyantborg(Card):
    name = "Cyborg (Service Shell- Flamboyant)"
    description = """Sometimes a cyborg just needs to show a bit of flamboyance, you know?"""
    rules = """{$Asimov}, gains +2/+2 when it's the only card on your side of the field."""

    cost = 1
    power = 0
    resolve = 1

    keywords = {CardKeyword.ASIMOV}
    card_type = CardType.CREATURE
    subtypes = {CardSubtype.SILICON}
    rarity = CardRarity.COMMON
    faction = CardFaction.SERVICE
    card_set = CardSet.CORESET2020
    """TODO:
    {$Asimov}, gains +2/+2 when it's the only card on your side of the field.
    """


class Card_skirtborg(Card):
    name = "Cyborg (Service Shell- Skirted)"
    description = """The Service Shell is intended to be the most human of the Cyborg Shells, due to its outwardly social role- none exemplify this better than the Skirted Shell, showing that even robots can't escape fashion norms."""
    rules = """{$Asimov}"""

    cost = 1
    power = 0
    resolve = 3

    keywords = {CardKeyword.ASIMOV}
    card_type = CardType.CREATURE
    subtypes = {CardSubtype.SILICON}
    rarity = CardRarity.COMMON
    faction = CardFaction.SERVICE
    card_set = CardSet.CORESET2020


class Card_classicborg(Card):
    name = "Cyborg (Service Shell- Classic)"
    description = """The classic Service Shell, the Classic Shell is what most crewmembers think of when they think of a 'useless robot that serves drinks'."""
    rules = """{$Asimov}, for every piece of equipment in play, gain +1 temporary resolve during the opponent's turn. That temporary resolve is lost at the start of your turn."""

    cost = 2
    power = 1
    resolve = 1

    keywords = {CardKeyword.ASIMOV}
    card_type = CardType.CREATURE
    subtypes = {CardSubtype.SILICON}
    rarity = CardRarity.COMMON
    faction = CardFaction.SERVICE
    card_set = CardSet.CORESET2020
    """TODO:
    {$Asimov}, for every piece of equipment in play, gain +1 temporary resolve during the opponent's turn. That temporary resolve is lost at the start of your turn.
    """


class Card_stylinborg(Card):
    name = "Cyborg (Service Shell- Ritzy)"
    description = """Ooh, isn't this robot one cool cat?"""
    rules = """{$Asimov}"""

    cost = 1
    power = 1
    resolve = 2

    keywords = {CardKeyword.ASIMOV}
    card_type = CardType.CREATURE
    subtypes = {CardSubtype.SILICON}
    rarity = CardRarity.COMMON
    faction = CardFaction.SERVICE
    card_set = CardSet.CORESET2020


class Card_miner(Card):
    name = "Shaft Miner"
    description = """When the station needs materials, these are the guys who risk their lives, bravely pioneering the wastes of Indecipheres, to bring them in."""
    rules = """Once per turn, you may pay 1 mana and tap this card: Draw one card from your deck, and either discard it, or send it to the bottom of your deck."""

    cost = 5
    power = 5
    resolve = 3

    keywords = {}
    card_type = CardType.CREATURE
    subtypes = {CardSubtype.HUMAN, CardSubtype.MINER}
    rarity = CardRarity.RARE
    faction = CardFaction.CARGO
    card_set = CardSet.CORESET2020
    """TODO:
    Once per turn, you may pay 1 mana and tap this card: Draw one card from your deck, and either discard it, or send it to the bottom of your deck.
    """


class Card_engi(Card):
    name = "Station Engineer"
    description = """Station Engineers maintain the intricate and delicate web of machinery that keeps you, and everyone else aboard your station, alive. No pressure there, then."""
    rules = """Tap this card: Reduce the damage a card would take this turn from a battlefield to zero."""

    cost = 4
    power = 2
    resolve = 2

    keywords = {}
    card_type = CardType.CREATURE
    subtypes = {CardSubtype.HUMAN, CardSubtype.ENGINEER}
    rarity = CardRarity.COMMON
    faction = CardFaction.ENGINEERING
    card_set = CardSet.CORESET2020
    """TODO:
    Tap this card: Reduce the damage a card would take this turn from a battlefield to zero.
    """


class Card_swarmer(Card):
    name = "Swarmer"
    description = """Leading researchers theorise that Swarmers were designed as some kind of vanguard for an alien invasion force, which seemingly has never materialised."""
    rules = """{$Graytide}, {$Immunity} to Engineering creature cards."""

    cost = 1
    power = 0
    resolve = 1

    keywords = {CardKeyword.GRAYTIDE, CardKeyword.IMMUNITY_ENGINEERING_CREATURE}
    card_type = CardType.CREATURE
    subtypes = {CardSubtype.ROBOT}
    rarity = CardRarity.RARE
    faction = CardFaction.SYNDICATE
    card_set = CardSet.CORESET2020


class Card_viro(Card):
    name = "Virologist"
    description = """Officially, the virologist is present on station to deal with novel diseases and ailments that originate from deep space. As everyone knows, this is not what the virologist actually does."""
    rules = """"""

    cost = 3
    power = 5
    resolve = 1

    keywords = {}
    card_type = CardType.CREATURE
    subtypes = {CardSubtype.HUMAN, CardSubtype.DOCTOR}
    rarity = CardRarity.COMMON
    faction = CardFaction.MEDICAL
    card_set = CardSet.CORESET2020


class Card_warden(Card):
    name = "Warden"
    description = """The Warden is tasked with the herculean (and futile) feat of defending the armory and brig, and never leaving his post, no matter the situation."""
    rules = """{$Squad Tactics}, {$Blocker}"""

    cost = 4
    power = 2
    resolve = 4

    keywords = {CardKeyword.SQUAD_TACTICS, CardKeyword.BLOCKER}
    card_type = CardType.CREATURE
    subtypes = {CardSubtype.HUMAN, CardSubtype.OFFICER}
    rarity = CardRarity.UNCOMMON
    faction = CardFaction.SECURITY
    card_set = CardSet.CORESET2020


class Card_xeno(Card):
    name = "Xenomorph Hunter (2560 Core Set)"
    description = """This particular strain of Xenomorph is capable of semi-transparency, allowing it to strike from the shadows."""
    rules = """{$Hivemind}"""

    cost = 4
    power = 2
    resolve = 3

    keywords = {CardKeyword.HIVEMIND}
    card_type = CardType.CREATURE
    subtypes = {CardSubtype.XENOMORPH}
    rarity = CardRarity.RARE
    faction = CardFaction.XENO
    card_set = CardSet.CORESET2020


class Card_tough_choices(Card):
    name = "Tough Choices"
    description = """Every Nanotrasen employee will, at some point, be forced to make a tough choice. Make sure you make the right one!"""
    rules = """Draw the top three cards from your deck. Summon one at no cost, and discard the other two."""

    cost = 2
    power = 0
    resolve = 0

    keywords = {}
    card_type = CardType.EVENT
    subtypes = {CardSubtype.INSTANT}
    rarity = CardRarity.COMMON
    faction = CardFaction.SYNDICATE
    card_set = CardSet.CORESET2020
    """TODO:
    Draw the top three cards from your deck. Summon one at no cost, and discard the other two.
    """


class Card_bsa_barrage(Card):
    name = "Bluespace Barrage"
    description = """The officers at Centcom are well known for their ability to hit targets extremely accurately with their bluespace artillery, especially when stupid pictures show up at their fax machine."""
    rules = """Destroy any creature on the opponent's battlefield. If your opponent has no creatures, deal 2 damage directly to them."""

    cost = 3
    power = 0
    resolve = 0

    keywords = {}
    card_type = CardType.EVENT
    subtypes = {CardSubtype.INSTANT}
    rarity = CardRarity.UNCOMMON
    faction = CardFaction.SECURITY
    card_set = CardSet.CORESET2020
    """TODO:
    Destroy any creature on the opponent's battlefield. If your opponent has no creatures, deal 2 damage directly to them.
    """


class Card_glitch_system(Card):
    name = "Glitch in the System"
    description = """Even a meticulously maintained AI system will eventually develop errors. Many are benign, but some may cause unforeseen problems..."""
    rules = """Select a Creature with {$Asimov} that you control. Remove the {$Asimov} trait from it."""

    cost = 1
    power = 0
    resolve = 0

    keywords = {}
    card_type = CardType.EVENT
    subtypes = {CardSubtype.INSTANT}
    rarity = CardRarity.COMMON
    faction = CardFaction.SCIENCE
    card_set = CardSet.CORESET2020
    """TODO:
    Select a Creature with {$Asimov} that you control. Remove the {$Asimov} trait from it.
    """


class Card_adrenals(Card):
    name = "Adrenals"
    description = """A potent mixture of stimulants, designed to enhance a soldier's ability in the field. Technically illegal in Terragov territory, but since when has that stopped anyone?"""
    rules = """Grant +2/+1 to a Creature card that you control."""

    cost = 1
    power = +2
    resolve = +1

    keywords = {}
    card_type = CardType.EVENT
    subtypes = {CardSubtype.INSTANT}
    rarity = CardRarity.COMMON
    faction = CardFaction.MEDICAL
    card_set = CardSet.CORESET2020
    """TODO:
    Grant +2/+1 to a Creature card that you control.
    """


class Card_plasmafire(Card):
    name = "Atmospherics Incident"
    description = """Accidents happen."""
    rules = """While this card is active, deal 1/1 to every creature during the First Effect Phase."""

    cost = 3
    power = 0
    resolve = 0

    keywords = {}
    card_type = CardType.BATTLEFIELD
    subtypes = {CardSubtype.ATMOSPHERICS}
    rarity = CardRarity.RARE
    faction = CardFaction.ENGINEERING
    card_set = CardSet.CORESET2020
    """TODO:
    While this card is active, deal 1/1 to every creature during the First Effect Phase.
    """


class Card_psych(Card):
    name = "Psychologist"
    description = """The psychologist is the newest addition to Nanotrasen's medical workforce, quickly settling into their role as the job that does nothing valuable."""
    rules = """"""

    cost = 1
    power = 1
    resolve = 1

    keywords = {}
    card_type = CardType.CREATURE
    subtypes = {CardSubtype.HUMAN, CardSubtype.DOCTOR}
    rarity = CardRarity.COMMON
    faction = CardFaction.MEDICAL
    card_set = CardSet.CORESET2020


class Card_just_losses(Card):
    name = "Justifiable Casualties"
    description = """The beat is hell. Officers die. The strongest, they live."""
    rules = """Sacrifice two friendly creatures from the battlefield, then summon a creature from your hand at no mana cost."""

    cost = 2
    power = 0
    resolve = 0

    keywords = {}
    card_type = CardType.EVENT
    subtypes = {CardSubtype.INSTANT}
    rarity = CardRarity.UNCOMMON
    faction = CardFaction.SECURITY
    card_set = CardSet.CORESET2020
    """TODO:
    Sacrifice two friendly creatures from the battlefield, then summon a creature from your hand at no mana cost.
    """


class Card_blue_warp(Card):
    name = "Bluespace Flux"
    description = """Despite being a revolutionary new technology, bluespace still has some... kinks that need sorted out."""
    rules = """While this card is active, once a round during the play phase each player may pay 2 mana to summon the top card from their deck."""

    cost = 3
    power = 0
    resolve = 0

    keywords = {}
    card_type = CardType.BATTLEFIELD
    subtypes = {CardSubtype.ANOMALY}
    rarity = CardRarity.COMMON
    faction = CardFaction.SCIENCE
    card_set = CardSet.CORESET2020
    """TODO:
    While this card is active, once a round during the play phase each player may pay 2 mana to summon the top card from their deck.
    """


class Card_bag_greed(Card):
    name = "Bag of Greed"
    description = """BAG OF GREED ALLOWS ME TO DRAW TWO MORE CARDS. I WILL START MY TURN BY PLAYING BAG OF GREED WHICH ALLOWS ME TO DRAW TWO MORE CARDS. I WILL PLAY THE EVENT CARD, BAG OF GREED, WHICH ALLOWS ME TO DRAW TWO NEW CARDS."""
    rules = """Draw two cards from your deck."""

    cost = 3
    power = 0
    resolve = 0

    keywords = {}
    card_type = CardType.EVENT
    subtypes = {CardSubtype.INSTANT}
    rarity = CardRarity.UNCOMMON
    faction = CardFaction.SCIENCE
    card_set = CardSet.CORESET2020
    """TODO:
    Draw two cards from your deck.
    """


class Card_eco_crash(Card):
    name = "Economy Crash"
    description = """So cargo sold 20 canisters of miasma, and now the galactic economy is experiencing what's known as 'a catastrophic collapse'."""
    rules = """All cards cost 1 extra mana to summon."""

    cost = 2
    power = 0
    resolve = 0

    keywords = {}
    card_type = CardType.BATTLEFIELD
    subtypes = {CardSubtype.EVENT}
    rarity = CardRarity.COMMON
    faction = CardFaction.CARGO
    card_set = CardSet.CORESET2020
    """TODO:
    All cards cost 1 extra mana to summon.
    """


class Card_black_gaia(Card):
    name = "Black Ambrosia Gaia"
    description = """If Ambrosia Gaia is the gold of Botany, the rare black variety is the platinum. Almost nobody has seen this illusive plant with their own eyes."""
    rules = """During the draw phase, you may sacrifice Ambrosia Gaia to gain 3 mana."""

    cost = 0
    power = 0
    resolve = 0

    keywords = {}
    card_type = CardType.ARTIFACT
    subtypes = {CardSubtype.PLANT}
    rarity = CardRarity.LEGENDARY
    faction = CardFaction.SERVICE
    card_set = CardSet.CORESET2020
    """TODO:
    During the draw phase, you may sacrifice Ambrosia Gaia to gain 3 mana.
    """


class Card_good_planning(Card):
    name = "Good Planning"
    description = """Always prepare for the worst."""
    rules = """Search your deck for an equipment card. Add it to your hand, then shuffle your deck."""

    cost = 2
    power = 0
    resolve = 0

    keywords = {}
    card_type = CardType.EVENT
    subtypes = {CardSubtype.INSTANT}
    rarity = CardRarity.COMMON
    faction = CardFaction.SECURITY
    card_set = CardSet.CORESET2020
    """TODO:
    Search your deck for an equipment card. Add it to your hand, then shuffle your deck.
    """


class Card_revenant(Card):
    name = "Revenant"
    description = """The revenant is a spirit of pure hatred, kept alive by drawing the life force of its enemies."""
    rules = """When a creature on your battlefield dies, Revenant gains 1/0."""

    cost = 3
    power = 2
    resolve = 3

    keywords = {}
    card_type = CardType.CREATURE
    subtypes = {CardSubtype.SPIRIT}
    rarity = CardRarity.RARE
    faction = CardFaction.SYNDICATE
    card_set = CardSet.CORESET2020
    """TODO:
    When a creature on your battlefield dies, Revenant gains 1/0.
    """


class Card_re_education(Card):
    name = "Re-Education"
    description = """Nobody ever seems to return from re-education. Probably best not to question it."""
    rules = """Destroy any creature on the opponent's battlefield."""

    cost = 2
    power = 0
    resolve = 0

    keywords = {}
    card_type = CardType.EVENT
    subtypes = {CardSubtype.INSTANT}
    rarity = CardRarity.UNCOMMON
    faction = CardFaction.SECURITY
    card_set = CardSet.CORESET2020
    """TODO:
    Destroy any creature on the opponent's battlefield.
    """


class Card_immoral_surgeon(Card):
    name = "Immoral Surgeon"
    description = """Remember, the Hippocratic oath is only a suggestion."""
    rules = """2 Mana- You may tap Immoral Surgeon and give a creature +1/+1."""

    cost = 4
    power = 2
    resolve = 4

    keywords = {}
    card_type = CardType.CREATURE
    subtypes = {CardSubtype.LIZARD, CardSubtype.DOCTOR}
    rarity = CardRarity.UNCOMMON
    faction = CardFaction.MEDICAL
    card_set = CardSet.CORESET2020
    """TODO:
    2 Mana- You may tap Immoral Surgeon and give a creature +1/+1.
    """


class Card_botanist_plant(Card):
    name = "Committed Botanist"
    description = """When you've grown the plants, nurtured the plants, and harvested the plants, there's only one place to go from there... becoming the plant."""
    rules = """While Committed Botanist is on your battlefield, you can play Plant and Service cards at half their cost, rounded up."""

    cost = 4
    power = 2
    resolve = 3

    keywords = {}
    card_type = CardType.CREATURE
    subtypes = {CardSubtype.PLANT, CardSubtype.WORKER}
    rarity = CardRarity.RARE
    faction = CardFaction.SERVICE
    card_set = CardSet.CORESET2020
    """TODO:
    While Committed Botanist is on your battlefield, you can play Plant and Service cards at half their cost, rounded up.
    """


class Card_scientist_moth(Card):
    name = "Scientist (Moth)"
    description = """Moths are a common sight in Nanotrasen research departments, acting as integral ideas guys for new clothing designs and lighting innovations."""
    rules = """"""

    cost = 1
    power = 2
    resolve = 2

    keywords = {}
    card_type = CardType.CREATURE
    subtypes = {CardSubtype.MOTH, CardSubtype.SCIENTIST}
    rarity = CardRarity.COMMON
    faction = CardFaction.SCIENCE
    card_set = CardSet.CORESET2020


class Card_inducer(Card):
    name = "Inducer"
    description = """The inducer is a marvelous piece of tech, allowing the recharging of an internal cell without opening a machine."""
    rules = """Pay 3 lifeshards: Gain 3 mana this turn."""

    cost = 0
    power = 0
    resolve = 0

    keywords = {}
    card_type = CardType.EVENT
    subtypes = {CardSubtype.INSTANT}
    rarity = CardRarity.COMMON
    faction = CardFaction.ENGINEERING
    card_set = CardSet.CORESET2020
    """TODO:
    Pay 3 lifeshards: Gain 3 mana this turn.
    """


class Card_fryer(Card):
    name = "Deep Fryer"
    description = """God bless the United States of Space America."""
    rules = """For 2 mana: Tap this card and destroy an opposing equipment card."""

    cost = 2
    power = 0
    resolve = 0

    keywords = {}
    card_type = CardType.EVENT
    subtypes = {CardSubtype.INSTANT}
    rarity = CardRarity.UNCOMMON
    faction = CardFaction.SERVICE
    card_set = CardSet.CORESET2020
    """TODO:
    For 2 mana: Tap this card and destroy an opposing equipment card.
    """


class Card_sleeping_carp(Card):
    name = "Scroll of the Sleeping Carp"
    description = """Created by the long-extinct Carp Monks of Space Tibet, the Sleeping Carp style has been kept alive by dedicated practitioners, and even found its way into the Syndicate's training regime."""
    rules = """{$On Equip}: Your opponent must show you one card in their hand of their choice."""

    cost = 3
    power = 3
    resolve = 1

    keywords = {}
    card_type = CardType.EQUIPMENT
    subtypes = {CardSubtype.WEAPON}
    rarity = CardRarity.EPIC
    faction = CardFaction.SYNDICATE
    card_set = CardSet.CORESET2020
    """TODO:
    {$On Equip}: Your opponent must show you one card in their hand of their choice.
    """


class Card_nuclear_option(Card):
    name = "The Nuclear Option"
    description = """The Gorlex Marauders are well known for their nuclear weapons, and their nuke first, second, third and fourth policy with regards to deploying them."""
    rules = """Destroy the active battlefield card. Deal 2 damage to all creatures on both battlefields."""

    cost = 3
    power = 0
    resolve = 0

    keywords = {}
    card_type = CardType.EVENT
    subtypes = {CardSubtype.INSTANT}
    rarity = CardRarity.RARE
    faction = CardFaction.SYNDICATE
    card_set = CardSet.CORESET2020
    """TODO:
    Destroy the active battlefield card. Deal 2 damage to all creatures on both battlefields.
    """


class Card_bepis(Card):
    name = "B.E.P.I.S. Chamber"
    description = """Created as an automated investment machine for a venture capitalism company, the B.E.P.I.S. ended up in the hands of Nanotrasen's research division after bankrupting the original creators... and 27 other corporations."""
    rules = """Flip a coin. If heads, gain 2 mana. If tails, lose up to 2 mana."""

    cost = 0
    power = 0
    resolve = 0

    keywords = {}
    card_type = CardType.EVENT
    subtypes = {CardSubtype.INSTANT}
    rarity = CardRarity.COMMON
    faction = CardFaction.SCIENCE
    card_set = CardSet.CORESET2020
    """TODO:
    Flip a coin. If heads, gain 2 mana. If tails, lose up to 2 mana.
    """


class Card_weekend_at_bernies(Card):
    name = "Weekend at Nanotrasen's"
    description = """Holy shit! We just accidentally killed the Captain! Here, uhh... oh god, stuff him in that wheelchair over there, before anyone comes in. Yeah, yeah! Get his sunglasses, cover his face. Oh my god, oh my god, oh my god. No one will be able to tell, he looks sorta fine, right? Right?"""
    rules = """Return a creature card from your graveyard to the battlefield."""

    cost = 3
    power = 0
    resolve = 0

    keywords = {}
    card_type = CardType.EVENT
    subtypes = {CardSubtype.INSTANT}
    rarity = CardRarity.UNCOMMON
    faction = CardFaction.MEDICAL
    card_set = CardSet.CORESET2020
    """TODO:
    Return a creature card from your graveyard to the battlefield.
    """


class Card_disco_inferno(Card):
    name = "Disco Inferno"
    description = """(Burn baby burn) burn that mother down y'all
(Burn baby burn) Disco Inferno
(Burn baby burn) burn that mother down"""
    rules = """For 2 mana: Tap this card permanantly. While tapped, all active creatures take 3 damage during the first play phase of each turn. This card is destroyed after 2 turns of being tapped."""

    cost = 4
    power = 0
    resolve = 0

    keywords = {}
    card_type = CardType.BATTLEFIELD
    subtypes = {CardSubtype.SHUTTLE}
    rarity = CardRarity.UNCOMMON
    faction = CardFaction.SCIENCE
    card_set = CardSet.CORESET2020
    """TODO:
    For 2 mana: Tap this card permanantly. While tapped, all active creatures take 3 damage during the first play phase of each turn. This card is destroyed after 2 turns of being tapped.
    """
