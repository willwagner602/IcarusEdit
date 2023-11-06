from typing import Dict, List
import os
import json
import pprint

# all known talents formatted by name: max level
Talents: Dict[str, int] = {
    "Resources_Increased_Wood": 3,
    "Gathering_Meat_Yield": 1,
    "Produce_Food_Decay": 3,
    "Exploration_Base_Health": 3,
    "Husbandry_TamingCosts": 2,
    "Fishing_Rod_Crafting_Cost": 2,
    "Repair_Stamina_Regen": 3,
    "Tools_Pickaxe_Durability": 3,
    "Building_Wood_Cost_0": 2,
    "Bow_Movement_Speed1": 3,
    "Spear_Melee_Damage1": 3,
    "Knife_Fast_Aim": 3,
    "Firearm_Cheap_Pistol_Ammo": 1,
    "Solo_Stamina": 2,
    "Resources_Increased_Harvesting": 4,
    "Resources_Increased_Stone": 3,
    "Resources_Inventory_Capacity": 3,
    "Resources_Increased_Wood_0": 1,
    "Resources_Secondary_Fibre": 3,
    "Resources_Encumbrance_Penalty": 4,
    "Resources_Exotic_Weight": 4,
    "Resources_Secondary_Voxel": 3,
    "Resources_Oxite_Miner": 3,
    "Resources_Wood_Weight": 4,
    "Resources_Stone_Weight": 4,
    "Resources_Inventory_Capacity_0": 3,
    "Resources_Exotic_Movement": 3,
    "Resources_Increased_Metals": 3,
    "Resources_Metal_Weight": 4,
    "Resources_Voxel_Instant": 1,
    "Resources_Wood_Pickup": 1,
    "Resources_Instant_Tree": 1,
    "Exploration_Reduced_Tree_Damage": 1,
    "Stalking_Base_Stamina": 3,
    "Stalking_Sneak_Speed": 3,
    "Gathering_Bone_Yield": 1,
    "Stalking_Damage_Stamina_Regen": 1,
    "Talent_Leather_Breakdown": 1,
    "Gathering_Corpse_Movement": 1,
    "Gathering_Corpse_Movement_0": 1,
    "Stalking_Detection_Range": 3,
    "Hunting_Knife_Skinning_Durability": 3,
    "Stalking_Small_Highlight": 1,
    "Gathering_Leather_Yield": 2,
    "Stalking_Storm_Stealth": 1,
    "Stalking_Blueprint_Ghillie": 1,
    "Hunting_See_World_Boss": 1,
    "Stalking_Base_Stamina_0": 3,
    "Gathering_Meat_Yield_0": 2,
    "Gathering_Bone_Yield_0": 2,
    "Stalking_Medium_Highlight": 1,
    "Hunting_Cold_Hearted": 1,
    "Gathering_Polarbear_Recipe": 1,
    "Stalking_Large_Highlight": 1,
    "Resources_Food_Hunger": 2,
    "Resources_Crop_Grow_Speed": 2,
    "Produce_Campfire_Fuel": 2,
    "Produce_Crops_Yield": 2,
    "Produce_Food_Buff_Duration": 3,
    "Produce_Dried_Meat_Buff_Food": 2,
    "Produce_FruitAndVege_Buff_Food": 2,
    "Produce_Max_Stamina": 3,
    "Produce_CropPlot_Fertilizer_Consumption": 1,
    "Produce_Melee_Damage": 3,
    "Produce_Gunpowder_Recipe": 1,
    "Produce_CropPlot_Growth_Speed": 2,
    "Produce_Foraging_Buff": 3,
    "Resources_Food_Benefit": 2,
    "Produce_Shotgun_Recipe": 1,
    "Produce_Food_Rotten": 1,
    "Produce_Food_Rotten2": 2,
    "Produce_CropPlot_Crop_Yield": 2,
    "Resources_Crop_Decay": 1,
    "Resources_Food_Buff_Slot": 1,
    "Produce_CropPlot_Item_Spoil_Time": 2,
}
playerdata_path: str = f"C:\\Users\\{os.getlogin()}\\AppData\\Local\\Icarus\\Saved\\PlayerData"


def get_player_id() -> str:
    player_ids = os.listdir(playerdata_path)
    if len(player_ids) != 1:
        raise NotImplementedError(f"Found more than one Player ID: {player_ids}")
    return player_ids[0]


data_path = f"{playerdata_path}\\{get_player_id()}\\Characters.json"


class Talent(object):

    def __init__(self, data: Dict):
        self.RowName = data["RowName"]
        self.Rank = data["Rank"]

    def __str__(self):
        return f"\"{self.RowName}\": {self.Rank},"


class Character(object):
    CharacterName: str = ""
    ChrSlot: int = -1
    XP: int = -1
    XP_Debt: int = -1
    IsDead: bool = False
    IsAbandoned: bool = False
    LastProspectId: str = ""
    Location: str = ""
    UnlockedFlags: List[int] = []
    MetaResources: List = []
    Cosmetic: Dict = {}
    Talents: List[Talent] = []

    expected_keys = [
        'CharacterName',
        'ChrSlot',
        'XP',
        'XP_Debt',
        'IsDead',
        'IsAbandoned',
        'LastProspectId',
        'Location',
        'UnlockedFlags',
        'MetaResources',
        'Cosmetic',
        'Talents'
    ]

    def __init__(self, data: Dict):
        self.__dict__.update(data)
        missing_keys = [key for key in self.expected_keys if key not in self.__dict__]
        self.Talents = self.generate_talents()
        if missing_keys:
            print(f"Missing keys {missing_keys}")
        extra_keys = [key for key in self.__dict__ if key not in self.expected_keys]
        if extra_keys:
            print(f"Found extra keys {extra_keys}")

    def __str__(self):
        return pprint.pformat(self.__dict__)

    def __repr__(self):
        return self.__str__()

    def generate_talents(self) -> List[Talent]:
        return [Talent(item) for item in self.Talents]


def get_characters() -> [Character]:
    with open(data_path) as f:
        data = json.load(f)

    return [Character(json.loads(char)) for char in data["Characters.json"]]


def find_character_index_by_name(target_name: str, characters: List[Character]) -> int:
    for i, char in enumerate(characters):
        if char.CharacterName == target_name.upper():
            return i

    raise RuntimeError(f"Couldn't find character {target_name}")
