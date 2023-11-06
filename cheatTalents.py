import json
import pprint

FILENAME = "Characters.json"
TALENTS = "Talents"
ROW_NAME = "RowName"
RANK = "Rank"

path = "C:\\Users\\will\\AppData\\Local\\Icarus\\Saved\\PlayerData\\76561198004413179\\Characters.json"

with open(path) as f:
    data = json.load(f)

chars = [json.loads(char) for char in data[FILENAME]]
for char in chars:
    char["TalentNames"] = {talent[ROW_NAME]: talent["Rank"] for talent in char[TALENTS]}

missing_talents = {name: rank for name, rank in chars[1]["TalentNames"].items() if name not in chars[0]["TalentNames"]}
pprint.pprint(missing_talents)

for talent, rank in missing_talents.items():
    chars[0][TALENTS].append({RANK: rank, ROW_NAME: talent})

data[FILENAME][0] = json.dumps(chars[0])
with open(path, "w+") as f:
    json.dump(data, f)
