# Mutables: 
# List (you say this is a array, in python we call it a list.)

ingredients = ["water", "milk", "black tea"]
#let's say you forgot to add sugar, if it would have been a tuple i would had no choice but come to line 4 and add "sugar", but as we are using list to store which is mutable(can be changed) that's not the case.
ingredients.append("sugar")
print(f"Ingredients are: {ingredients}")
ingredients.remove("water")
print(f"Ingredients are: {ingredients}")

spice_options = ["ginger", "cardamom"]
chai_ingredients = ["water", "milk"]

chai_ingredients.extend(spice_options)
print(f"chai: {chai_ingredients}")
# .append() always adds the to end to a list.
# .insert() you have to provide what prosition you want to add.
chai_ingredients.insert(2, "black tea")
print(f"chai: {chai_ingredients}")
# remove something from list
last_added = chai_ingredients.pop()
print(f"{last_added}")
print(f"chai: {chai_ingredients}")
chai_ingredients.reverse()
print(f"chai: {chai_ingredients}")
chai_ingredients.sort()
print(f"chai: {chai_ingredients}")

sugar_levels = [1, 2, 3, 4, 5]
print(f"Maximum sugar level: {max(sugar_levels)}")
print(f"Minimum sugar level: {min(sugar_levels)}")

base_liquid = ["water", "milk"]
extra_flavor = ["ginger"]

# operator overloading
full_liquid_mix = base_liquid + extra_flavor
print(f"Liquid mix: {full_liquid_mix}")

strong_brew = ["black tea", "water"] * 3
print(f"String brew: {strong_brew}")

# bytearray
raw_spice_data = bytearray(b"CINNAMON")
raw_spice_data = raw_spice_data.replace(b"CINNA", b"CARD")
print(f"Bytes: {raw_spice_data}")