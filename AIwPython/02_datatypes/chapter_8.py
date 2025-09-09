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