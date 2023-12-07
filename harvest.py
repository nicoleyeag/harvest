############
# Part 1   #
############


class MelonType:
    """A species of melon at a melon farm."""
    
    def __init__(
        self, code, first_harvest, color, is_seedless, is_bestseller, name
    ):
        """Initialize a melon."""

        self.pairings = []
        self.code = code
        self.first_harvest = first_harvest
        self.color = color
        self.is_seedless = is_seedless
        self.is_bestseller = is_bestseller
        self.name = name

        # Fill in the rest

    def add_pairing(self, pairing):
        """Add a food pairing to the instance's pairings list."""
        #we need to replace pairing if someone adds into parameter
        self.pairings = [pairing]
        # print(pairing)

        # Fill in the rest

    def update_code(self, new_code):
        """Replace the reporting code with the new_code."""

    #make a function that returns the pairings data
    #return the pairings
    def pairings(self):
        return pairings


    # def __repr__(self):
    #     """Show info about cat."""

    #     return f"<melon type=>"



def make_melon_types():
    """Returns a list of current melon types."""

    all_melon_types = []

    #calling the class to create a list? of a type of melon
    #after each melon add pairing to list
    musk = MelonType("musk","1998","green",True,True,"Muskmelon")
    musk.add_pairing("mint")
    all_melon_types.append(musk)

    cas = MelonType("cas", 2003, "orange", True, False, "Casaba")
    cas.add_pairing("strawberries and mint")
    all_melon_types.append(cas)

    cren = MelonType("cren", 1996, "green", True, False, "Crenshaw")
    cren.add_pairing("prosciutto")
    all_melon_types.append(cren)

    yw = MelonType("yw", 2013, "yellow", True, True, "Yellow Watermelon")
    yw.add_pairing("ice cream")
    all_melon_types.append(yw)

    #we need to add each melon type
    #function should return a list of objects pertaining to specific melon

    #seedless/bestseller could be a boolean

    return all_melon_types


def print_pairing_info(melon_types):
    """Prints information about each melon type's pairings."""

    #if string = "musk"
      #print musk's pairing data

    #loop over each melon the print pairing
    for melon in melon_types:
        # print(melon.name)
        print(f"{melon.name} pairs with\n- {melon.pairings}")

#print(print_pairing_info(make_melon_types()))
    

def make_melon_type_lookup(melon_types):
    """Takes a list of MelonTypes and returns a dictionary of melon type by code."""

    #make a dictionary
    melons = {}

    #add melons to dictionary
    for melon in melon_types:
        #key is the code, value is the melon
        # key = (melon.code)
        melons[melon.code] = melon.name
    #use items() and sorted()
    sorted_melons = dict(sorted(melons.items()))
    #sorted() to sort by code?
    return sorted_melons
  

print(make_melon_type_lookup(make_melon_types()))
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


# musk = MelonType("cas", 2003, "orange", True, False, "Casaba")
# print(musk)
# # print(test)
# print(vars(musk))