# Integer 

black_tea_grams = 14
ginger_grams = 3

total = (black_tea_grams + ginger_grams)
print(f"total grams of base tea is {total}.")

remaining_tea = black_tea_grams - ginger_grams
print(f"total grams of remaining tea is {remaining_tea}.")

milk_liters = 7
servings = 4
milk_per_serving = milk_liters/ servings
print(f"Milk per serving is {milk_per_serving}.")

total_tea_bags = 7
pots = 4
bags_per_pot = total_tea_bags // pots
print(f"Whole tea bags per pot: {bags_per_pot}")

total_cadamom_pods = 10
pods_per_cup = 3
leftover_pods = total_cadamom_pods % pods_per_cup
print(f"Leftover C pods {leftover_pods}")

base_flavor_strength = 2
scale_factor = 3
powerful_flavour = base_flavor_strength ** scale_factor
print(f"Scaled Flavour strength {powerful_flavour}")
# 2 * 2 * 2

total_tea_leaves_harvested = 1_000_000_000
print(f"tea leaves: {total_tea_leaves_harvested}")