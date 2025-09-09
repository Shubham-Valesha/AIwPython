# Dictionary
# Insted of your [0] to call, it has names to call.(named argument)
# this concept gives us power to call data through specified names, Key - Value pair.

# create a Dictionary
chai_order = dict(type="Masala Chai", size="Large", sugar=2)
print(f"Chai order: {chai_order}")

# another way to create a Dictionary
chai_recipe = {}
# adding more data:
chai_recipe["base"] = "black tea"
chai_recipe["liquid"] = "milk"

print(f"Recipe base: {chai_recipe['base']}")
# delete 