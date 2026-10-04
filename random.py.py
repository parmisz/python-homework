


import random
while True:
    list_bazikon=[]
    bazikonan=["messi","ronaldo","mbappe","neymar"]
    teamha=["barsa","real","psg","alhilal"]
    entekhab_1_1=random.choice(bazikonan)
    entekhab_1_2=random.choice(teamha)
    bazikonan.remove(entekhab_1_1)
    teamha.remove(entekhab_1_2)

    entekhab_2_1=random.choice(bazikonan)
    bazikonan.remove(entekhab_2_1)
    entekhab_2_2=random.choice(teamha)
    teamha.remove(entekhab_2_2)

    entekhab_3_1=random.choice(bazikonan)
    entekhab_3_2=random.choice(teamha)
    bazikonan.remove(entekhab_3_1)
    teamha.remove(entekhab_3_2)

    entekhab_4_1=random.choice(bazikonan)
    bazikonan.remove(entekhab_4_1)
    entekhab_4_2=random.choice(teamha)
    teamha.remove(entekhab_4_2)

    list_bazikon.append(entekhab_1_1)
    list_bazikon.append(entekhab_1_2)
    list_bazikon.append(entekhab_2_1)
    list_bazikon.append(entekhab_2_2)
    list_bazikon.append(entekhab_3_1)
    list_bazikon.append(entekhab_3_2)
    list_bazikon.append(entekhab_4_1)
    list_bazikon.append(entekhab_4_2)
    print(list_bazikon)