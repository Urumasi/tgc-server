from json import loads

filename = 'set_one.json'

with open(filename, 'r') as f:
    data = loads(f.read())

card_set = data['templates'][0]['series'].upper()

for card in data['cards']:
    print(f'class Card_{card["id"]}(Card):')
    print(f'    name = "{card["name"]}"')
    print(f'    description = """{card["desc"]}"""')
    print(f'    rules = """{card["rules"]}"""\n')
    print(f'    cost = {card["summoncost"]}')
    if card["power"]:
        print(f'    power = {card["power"]}')
    if card["resolve"]:
        print(f'    resolve = {card["resolve"]}')
    print()
    print(f'    keywords = {{}}')
    print(f'    card_type = CardType.{card["cardtype"].upper()}')
    subtypes = ', '.join(('CardSubtype.' + x.upper()) for x in card["cardsubtype"].split(' '))
    if subtypes:
        print(f'    subtypes = {{{subtypes}}}')
    print(f'    rarity = CardRarity.{card["rarity"].upper()}')
    print(f'    faction = CardFaction.{card["faction"].upper()}')
    print(f'    card_set = CardSet.{card_set}')
    if card["rules"]:
        print(f'    """TODO:\n    {card["rules"]}\n    """')
    print('\n')
