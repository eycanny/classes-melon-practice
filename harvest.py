############
# Part 1   #
############


class MelonType:
    """A species of melon at a melon farm."""

    def __init__(
        self, name, code, first_harvest, color, is_seedless, is_bestseller 
    ):
        """Initialize a melon."""
        self.name = name
        self.code = code
        self.first_harvest = first_harvest
        self.color = color
        self.pairings = []
        self.is_seedless = is_seedless
        self.is_bestseller = is_bestseller
        

    def add_pairing(self, pairing):
        """Add a food pairing to the instance's pairings list."""

        self.pairings.append(pairing)

    def update_code(self, new_code):
        """Replace the reporting code with the new_code."""

        self.code = new_code

    def __repr__(self):

        return f"{self.name}"


def make_melon_types():
    """Returns a list of current melon types."""

    all_melon_types = []

    musk = MelonType(
        "Muskmelon",
        "musk",
        1998,
        "green",
        True,
        True
    )
    musk.add_pairing("mint")
    
    cas = MelonType(
        "Casaba",
        "cas",
        2003,
        "orange",
        True,
        False
    )
    
    cas.add_pairing("strawberries")
    cas.add_pairing("mint")


    crenshaw = MelonType(
        "Crenshaw",
        "cren",
        1996,
        "green",
        True,
        False
    )
    crenshaw.add_pairing("proscuitto")
    

    yellow_watermelon = MelonType(
        "Yellow Watermelon",
        "yw",
        2013,
        "yellow",
        True,
        True
    )
    yellow_watermelon.add_pairing("ice cream")

    # all_melon_types.append(musk)
    # all_melon_types.append(cas)
    # all_melon_types.append(crenshaw)
    # all_melon_types.append(yellow_watermelon)

    all_melon_types.extend([musk, cas, crenshaw, yellow_watermelon])

    return all_melon_types

def print_pairing_info(melon_types):
    """Prints information about each melon type's pairings."""

    for melon in melon_types:
        print(f"{melon.name} pairs with:")
        for item in melon.pairings:
            print(f"- {item}")
        if melon != melon_types[-1]:
            print()

    

def make_melon_type_lookup(melon_types):
    """Takes a list of MelonTypes and returns a dictionary of melon type by code."""

    melon_codes = {}

    for melon in melon_types:
        melon_codes[melon.code] = melon

    return melon_codes


############
# Part 2   #
############


class Melon:
    """A melon in a melon harvest."""

    def __init__(self, melon_types, shape_rating, color_rating, harvested_field, harvester_name):
        self.melon_types = melon_types
        self.shape_rating = shape_rating
        self.color_rating = color_rating
        self.harvested_field = harvested_field
        self.harvester_name = harvester_name
    
    def is_sellable(self):
        if self.shape_rating > 5 and self.color_rating > 5 and self.harvested_field != 3:
            return True
        else:
            return False

    def __repr__(self):

        return f"<Melon type={self.melon_types}>"


def make_melons(melon_types):
    """Returns a list of Melon objects."""

    melons = []

    melons_by_id = make_melon_type_lookup(melon_types)

    melon1 = Melon(melons_by_id['yw'], 8, 7, 2, 'Sheila')
    melon2 = Melon(melons_by_id['yw'], 3, 4, 2, 'Sheila')
    melon3 = Melon(melons_by_id['yw'], 9, 8, 3, 'Sheila')
    melon4 = Melon(melons_by_id['cas'], 10, 6, 35, 'Sheila')
    melon5 = Melon(melons_by_id['cren'], 8, 9, 35, 'Michael')
    melon6 = Melon(melons_by_id['cren'], 8, 2, 35, 'Michael')
    melon7 = Melon(melons_by_id['cren'], 2, 3, 4, 'Michael')
    melon8 = Melon(melons_by_id['musk'], 6, 7, 4, 'Michael')
    melon9 = Melon(melons_by_id['yw'], 7, 10, 3, 'Michael')

    melons.extend([melon1, melon2, melon3, melon4, melon5, melon6, melon7, melon8, melon9])

    return melons


def get_sellability_report(melons):
    """Given a list of melon object, prints whether each one is sellable."""

    for melon in melons:
        if melon.is_sellable() == True:
            print(f"Harvested by {melon.harvester_name} from Field {melon.harvested_field} (CAN BE SOLD)")
        elif melon.is_sellable() == False:
            print(f"Harvested by {melon.harvester_name} from Field {melon.harvested_field} (NOT SELLABLE)")