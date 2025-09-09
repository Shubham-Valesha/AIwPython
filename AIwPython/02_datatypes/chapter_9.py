essential_spices = {"cardamom", "ginger", "cinnamon"}
optional_spices = {"cloves", "ginger", "black pepper"}

# | pipe operator - union
all_spices = essential_spices | optional_spices
print(f"All spices: {all_spices}")
# union - no repeatation

# Intersection - &
common_spices = essential_spices & optional_spices
print(f"common spices: {common_spices}")

# Differences - '-'
only_in_essential = essential_spices - optional_spices
print(f"Only in essential spices: {only_in_essential}")

# membership test
print(f"Is 'cloves' in optional spices? {'cloves' in optional_spices}")