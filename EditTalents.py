from IcarusEdit import get_characters

FILENAME = "Characters.json"
TALENTS = "Talents"
ROW_NAME = "RowName"
RANK = "Rank"

path = "C:\\Users\\will\\AppData\\Local\\Icarus\\Saved\\PlayerData\\76561198004413179\\Characters.json"

target_talents = [
    {'Rank': 1, 'RowName': 'Resources_Increased_Wood'},
    {'Rank': 1, 'RowName': 'Gathering_Meat_Yield'},
    {'Rank': 1, 'RowName': 'Produce_Food_Decay'},
    {'Rank': 1, 'RowName': 'Exploration_Base_Health'},
    {'Rank': 1, 'RowName': 'Husbandry_TamingCosts'},
    {'Rank': 1, 'RowName': 'Fishing_Rod_Crafting_Cost'},
    {'Rank': 1, 'RowName': 'Repair_Stamina_Regen'},
    {'Rank': 1, 'RowName': 'Tools_Pickaxe_Durability'},
    {'Rank': 1, 'RowName': 'Building_Wood_Cost_0'},
    {'Rank': 1, 'RowName': 'Bow_Movement_Speed1'},
    {'Rank': 1, 'RowName': 'Spear_Melee_Damage1'},
    {'Rank': 1, 'RowName': 'Knife_Fast_Aim'},
    {'Rank': 1, 'RowName': 'Firearm_Cheap_Pistol_Ammo'},
    {'Rank': 1, 'RowName': 'Solo_Stamina'}
]

chars = get_characters()
print(chars)

# target_char = find_character_index_by_name("TEMPLATE", chars)
#
# data[FILENAME][0] = json.dumps(chars[0])
# with open(path, "w+") as f:
#     json.dump(data, f)
