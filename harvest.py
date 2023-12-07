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
        """"returns pairings outside of the class"""
        return self.pairings


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
    def __init__(
        self, melon_type, shape, color, field_name, harvester_name, melon_num, 
    ):
        """Initialize a melon."""
        
        self.type = melon_type
        self.shape = shape
        self.color = color
        self.harvest_field = field_name
        self.harvester = harvester_name
        self.num = melon_num
        # self.sellable = status
        #ex of harvester name is "michael"

    # def sellable(self):

            #if the melon is in the list it is sellable

            #self.pairings = [pairing]


    # Fill in the rest
    # Needs __init__ and is_sellable methods


def make_melons():
    """Returns a list of Melon objects."""
    melon_list = []
    #melon1 = Melon("things") <- instance
    melon1 = Melon("yw", 8, 7, 2, "Sheila", 1, )
    melon2 = Melon("yw", 3, 4, 2, "Sheila", 2)
    melon3 = Melon("yw", 9, 8, 2, "Sheila", 3)
    melon4 = Melon("cas", 10, 6, 35, "Sheila", 4)
    melon5 = Melon("cren", 8, 9, 35, "Michael", 5)
    melon6 = Melon("cren", 8, 2, 35, "Michael", 6)
    melon7 = Melon("cren", 2, 3, 4, "Michael", 7)
    melon8 = Melon("musk", 6, 7, 4, "Michael", 8)
    melon9 = Melon("yw", 7, 10, 3, "Sheila", 9)

    melon_list.extend([melon1, melon2, melon3, melon4, melon5, melon6, melon7, melon8, melon9] )

    #from the list print each melon
    for melon in melon_list:
        print(f"Melon{melon.num}\n- Melon Type: {melon.type}\n- Shape rating: {melon.shape}\n- Color rating: {melon.color}\n- Harvested from field {melon.harvest_field}\n- Harvested by {melon.harvester}")

    #return a list of objects in Melon
    return melon_list

    # for melon in melon_types:
    #     # print(melon.name)
    #     print(f"{melon.name} pairs with\n- {melon.pairings}")

# print(make_melons())

def get_sellability_report(melons):
    """Given a list of melon object, prints whether each one is sellable."""
    #
    #check: shape rating is over 5
    #check: color rating is over 5
    #check: did NOT come from field 3

    sellable_melons = []
    notsellable_melons = []

    for melon in melons:
        if melon.shape > 5 and melon.color > 5 and melon.harvest_field != 3:
            sellable_melons.append(melon)
            # sellable_melons.append(melon.harvest_field)
        else:
            notsellable_melons.append(melon)
            # notsellable_melons.append(melon.harvest_field)

    for melon in sellable_melons:
        print(f"Harvested by {melon.harvester} from field {melon.harvest_field} (CAN BE SOLD)")
    for melon in notsellable_melons:
        print(f"Harvested by {melon.harvester} from field {melon.harvest_field} (NOT SELLABLE)")

    return None

print(get_sellability_report(make_melons()))

# musk = MelonType("cas", 2003, "orange", True, False, "Casaba")
# print(musk)
# # print(test)
# print(vars(musk))