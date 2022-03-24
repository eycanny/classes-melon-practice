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
        "shaw",
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

    # Fill in the rest


############
# Part 2   #
############


class Melon:
    """A melon in a melon harvest."""

    # Fill in the rest
    # Needs __init__ and is_sellable methods


def make_melons(melon_types):
    """Returns a list of Melon objects."""

    # Fill in the rest


def get_sellability_report(melons):
    """Given a list of melon object, prints whether each one is sellable."""

    # Fill in the rest
