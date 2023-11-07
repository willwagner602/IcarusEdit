from typing import Dict, List
import os
import json
import pprint
from datetime import datetime
import shutil
import copy

# all known talents formatted by name: max level

resource_talents: Dict[str, int] = {
    "Resources_Increased_Wood": 3,
    "Gathering_Meat_Yield": 1,
    "Produce_Food_Decay": 3,
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
}
hunting_talents: Dict[str, int] = {
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
}
cooking_farming_talents: Dict[str, int] = {
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
exploration_talents: Dict[str, int] = {
    "Exploration_Base_Health": 3,
    "Exploration_Base_Movement": 3,
    "Exploration_Storm_Regen": 3,
    "Exploration_Reduced_Hunger": 3,
    "Exploration_Reduced_Oxygen": 3,
    "Exploration_Reduced_Thirst": 3,
    "Exploration_Reduced_Exposure": 3,
    "Exploration_Jump_Stamina": 3,
    "Exploration_Healing_Revive": 2,
    "Exploration_Weight_Capacity": 3,
    "Exploration_Aura_Oxygen_Consumption": 1,
    "Exploration_Swim_Speed": 2,
    "Exploration_Increased_Exposure_Decay": 3,
    "Exploration_Fall_Damage": 3,
    "Exploration_Swim_Oxygen": 1,
    "Exploration_Nocturnal1": 2,
    "Exploration_Revive_Regeneration": 1,
    "Exploration_Movespeed_End_Drop": 1,
    "Exploration_Nocturnal2": 1,
    "Exploration_Sprain_Chance": 2,
    "Exploration_Sprain_Recovery": 3,
    "Exploration_Forest_Hero": 1,
    "Exploration_Arctic_Hero": 1,
    "Exploration_Desert_Hero": 1,
    "Exploration_Party_Xp": 1,
}
husbandry_talents: Dict[str, int] = {
    "Husbandry_TamingCosts": 2,
    "Husbandry_ForagingYield": 3,
    "Husbandry_SaddleCost": 2,
    "Husbandry_TameUpkeep": 2,
    "Husbandry_ParentDamage": 1,
    "Husbandry_StaminaRecharge": 2,
    "Husbandry_TameTempTolerance": 2,
    "Husbandry_RidingEfficiency": 2,
    "Husbandry_TameHealth": 3,
    "Husbandry_Threat": 3,
    "Husbandry_TameSpeedAura": 1,
    "Husbandry_TameCarryingCapacity": 3,
    "Husbandry_Stamina": 2,
    "Husbandry_MountSpeed": 1,
    "Husbandry_JuvenileThreat": 1,
    "Husbandry_TameHeatTolerance": 1,
    "Husbandry_TameColdTolerance": 1,
    "Husbandry_RidingExposureResist": 2,
}
fishing_talents: Dict[str, int] = {
    "Fishing_Rod_Crafting_Cost": 2,
    "Fishing_Golden_Zone_Size": 2,
    "Fishing_Minigame_Speed": 2,
    "Fishing_Lure_wear_Rate": 3,
    "Fishing_Damage_Reduction": 1,
    "Fishing_Fish_Weight": 1,
    "Fishing_Fish_Length": 1,
    "Fishing_Exposure_Resistance": 2,
    "Fishing_Fish_Carry_Weight": 1,
    "Fishing_Oxygen_Consumption": 2,
    "Fishing_Water_Comsumption": 2,
    "Fishing_Saltwater_Quaility": 1,
    "Fishing_Freshwater_Quality": 1,
    "Fishing_Fish_Food_Buff": 1,
    "Fishing_Quaility_In_Storm": 1,
    "Fishing_Golden_Zone_Size_2": 3,
    "Fishing_Rare_Unique_Chance": 2,
    "Fishing_Uncommon_Chance": 2,
}
repair_talents: Dict[str, int] = {
    "Repair_Stamina_Regen": 3,
    "Repair_Hammer_Speed": 3,
    "Repair_Flapper_Movement": 1,
    "Repair_Extinguish_Speed": 3,
    "Repair_Flapper_Durability": 3,
    "Repair_Flapper_Stamina_Regen": 2,
    "Repair_Hammer_Durability": 2,
    "Repair_Storm_Resistant": 1,
    "Repair_Instant_Repair_Building": 1,
    "Repair_Fire_Resistance": 1,
    "Repair_Throw_Flapper": 1,
    "Repair_Hammer_Speed_0": 2,
}
tool_talents: Dict[str, int] = {
    "Tools_Pickaxe_Durability": 3,
    "Tools_Cheaper_Pickaxe1_0": 1,
    "Tools_Axe_Crafting_0": 1,
    "Tools_Axe_Durability": 3,
    "Tools_Axe_Swing_Speed": 3,
    "Tools_Pickaxe_Swing_Speed": 3,
    "Tools_Pickaxe_Melee_Damage": 3,
    "Tools_Pickaxe_Radius": 2,
    "Tools_Pickaxe_Stamina_Usage": 3,
    "Tools_Axe_Stamina_Usage": 3,
    "Tools_Axe_Felling_Damage": 3,
    "Tools_Sickle_Durability": 2,
    "Tools_Axe_Crafting": 1,
    "Tools_Combat_Axes": 1,
    "Tools_Combat_Axes2": 1,
    "Tools_Axe_Crafting2": 2,
    "Tools_Axe_Durability_0": 3,
    "Tools_Cheaper_Pickaxe1": 1,
    "Tools_Cheaper_Pickaxe2": 2,
    "Tools_Pickaxe_Durability_0": 3,
    "Tools_Pickaxe_Stamina_Usage_0": 3,
    "Tools_Pickaxe_Free_Durability": 1,
}
building_talents: Dict[str, int] = {
    "Building_Wood_Cost_0": 2,
    "Building_Wood_Cost": 2,
    "Building_Wood_Health": 2,
    "Building_Wood_Weight": 3,
    "Building_Wood_Weight_0": 3,
    "Building_Stone_Weight": 3,
    "Building_Stone_Weight_0": 3,
    "Building_Concrete_Weight": 3,
    "Building_Concrete_Weight_0": 3,
    "Building_Stone_Cost": 2,
    "Building_Wood_Storm_Resistance": 1,
    "Building_Concrete_Cost": 2,
    "Building_Wood_Fire_Resist": 1,
    "Building_Concrete_Cost_0": 2,
    "Building_Storage_Increase": 2,
    "Building_Stone_Furnace_Smelting": 2,
    "Building_Deployable_Crafting": 1,
    "Building_Lightning_Rod_Crafting": 1,
    "Building_Lightning_Rod_Health": 3,
    "Building_Hedgehog_Damage": 1,
    "Building_Storage_Increase_0": 2,
}
bow_talents: Dict[str, int] = {
    "Bow_Movement_Speed1": 3,
    "Bow_Craft_Master_0": 1,
    "Bow_Reduced_Stamina_Usage": 3,
    "Bow_Reduced_Reload_Speed": 3,
    "Bow_Arrow_Speed": 3,
    "Bow_Increase_Aim_Speed": 3,
    "Bow_Projectile_Damage1": 3,
    "Bow_Projectile_Damage2": 3,
    "Bow_Cheap_Arrows1": 1,
    "Bow_Durability_Usage": 3,
    "Bow_Accuracy": 2,
    "Bow_Critical_Multiplier1": 2,
    "Bow_Arrow_Double_Craft": 1,
    "Bow_Craft_Master": 1,
    "Bow_Double_Arrows": 2,
    "Bow_Slowing_Shot": 3,
    "Bow_Crafted_Arrow_Damage": 3,
    "Bow_Bleed_Arrows_0": 3,
    "Bow_Critical_Multiplier2": 2,
    "Bow_Pinning_Shot": 1,
    "Bow_Homing_Arrow": 1,
}
spear_talents: Dict[str, int] = {
    "Spear_Melee_Damage1": 3,
    "Spear_Cheap_Crafting1_0": 1,
    "Spear_Stamina_Usage": 3,
    "Spear_Fast_Aim": 3,
    "Spear_Range_Damage1": 2,
    "Spear_Faster_Melee": 3,
    "Spear_Melee_Damage2": 3,
    "Spear_Critical_Multiplier1": 2,
    "Spear_Range_Damage2": 2,
    "Spear_Aim_Movement": 3,
    "Spear_Critical_Damage2": 2,
    "Spear_Stamina_Battery": 2,
    "Spear_Cheap_Crafting1": 1,
    "Spear_Damage_Reduction": 2,
    "Spear_Cheap_Crafting2": 1,
    "Spear_Highlight": 1,
    "Spear_Range_Distance1": 2,
    "Spear_Cheap_Crafting2_0": 1,
    "Spear_Bleed_Hits": 3,
    "Spear_Range_Distance2": 2,
}
knife_talents: Dict[str, int] = {
    "Knife_Fast_Aim": 3,
    "Knife_Increased_Movement": 3,
    "Knife_Faster_Melee": 3,
    "Knife_Melee_Damage": 3,
    "Knife_Use_Durability": 3,
    "Knife_Smith2": 1,
    "Knife_Stamina_Usage": 3,
    "Knife_Smith1": 1,
    "Knife_Highlight": 1,
    "Knife_Range_Damage": 3,
    "Knife_Skin_Durability": 3,
    "Knife_Critical_Multiplier": 3,
    "Knife_Felling_Damage": 1,
    "Knife_Range_Damage2": 3,
    "Knife_Range_Distance": 3,
    "Knife_Smith1_0": 1,
    "Knife_Instant_Skin": 3,
    "Knife_Increased_Sneak": 3,
    "Knife_Instant_Kill": 1,
    "Knife_Pin_Throw": 1,
    "Knife_Range_Distance2": 3,
}
firearm_talents: Dict[str, int] = {
    "Firearm_Cheap_Pistol_Ammo": 1,
    "Firearm_Cheap_Shotgun_Ammo": 1,
    "Firearm_Cheap_Rifle_Ammo": 1,
    "Firearm_Gun_Weight": 1,
    "Firearm_Reload_Pistol": 3,
    "Firearm_Reload_Shotgun": 3,
    "Firearm_Reload_Rifle": 3,
    "Firearm_Damage_Pistol": 3,
    "Firearm_Damage_Shotgun": 3,
    "Firearm_Damage_Rifle": 3,
    "Firearm_Gun_Movement": 2,
    "Firearm_Double_Ammo": 1,
    "Firearm_Gun_Durability": 3,
    "Firearm_Bullet_Spread": 2,
    "Firearm_Gun_Critical_Multiplier": 3,
    "Firearm_No_Consume": 2,
    "Firearm_Second_Wind": 1,
}

all_talents: Dict[str, int] = {
    **resource_talents,
    **hunting_talents,
    **cooking_farming_talents,
    **exploration_talents,
    **husbandry_talents,
    **fishing_talents,
    **repair_talents,
    **tool_talents,
    **building_talents,
    **bow_talents,
    **spear_talents,
    **knife_talents,
    **firearm_talents,
}

player_data_path: str = f"C:\\Users\\{os.getlogin()}\\AppData\\Local\\Icarus\\Saved\\PlayerData"


def get_player_id() -> str:
    player_ids = os.listdir(player_data_path)
    if len(player_ids) != 1:
        raise NotImplementedError(f"Found more than one Player ID: {player_ids}")
    return player_ids[0]


player_id = get_player_id()
data_path = f"{player_data_path}\\{player_id}\\Characters.json"


class Talent(object):

    def __init__(self, data: Dict):
        self.RowName = data["RowName"]
        self.Rank = data["Rank"]

    def __str__(self):
        return f"\"{self.RowName}\": {self.Rank},"


def get_max_talents() -> List[Talent]:
    return [Talent({"RowName": talent, "Rank": rank}) for talent, rank in all_talents.items()]


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


class CharacterEncoder(json.JSONEncoder):
    def default(self, o: Character) -> str:
        char = copy.deepcopy(o)
        char.Talents = [{"Rank": talent.Rank, "RowName": talent.RowName} for talent in char.Talents]
        return char.__dict__


def get_characters() -> List[Character]:
    with open(data_path) as f:
        data = json.load(f)

    return [Character(json.loads(char)) for char in data["Characters.json"]]


def find_character_index_by_name(target_name: str, characters: List[Character]) -> int:
    for i, char in enumerate(characters):
        if char.CharacterName == target_name.upper():
            return i

    raise RuntimeError(f"Couldn't find character {target_name}")


def backup_characters():
    target_path = f"{player_data_path}\\{player_id}\\Characters-{datetime.now():%d-%m-%Y-%H_%M_%S}.json"

    print(f"Copying\n{data_path}\n\tto\n{target_path}")

    if input("Look good? ").lower() != "y":
        if input("Okay, should I exit this run? ").lower() != "no":
            exit(1)
        return

    shutil.copy(data_path, target_path)
    print("Copied")


def save_characters(characters: List[Character]):
    backup_characters()
    encoder = CharacterEncoder()
    with open(data_path, "w+") as f:
        json.dump({"Characters.json": [encoder.encode(char) for char in characters]}, f)
