def make_coffee():
    if not kettle_has_water():
        fill_kettle()
    pulg_in_kettle()
    boil_water()
    if not is_cup_clean():
        wash_cup()
    pour("boild water")
    add_to_cup("coffee")
    add_to_cup("sugar")
    froth("cup")
    add_to_cup("milk")
    
make_coffee()