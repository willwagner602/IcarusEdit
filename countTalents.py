from IcarusEdit import get_characters, find_character_index_by_name, Character
from typing import List

TALENTS = "Talents"
ROW_NAME = "RowName"
RANK = "Rank"

CHAR_NAME = "TEMPLATE"

chars: List[Character] = get_characters()
target = find_character_index_by_name(CHAR_NAME, chars)

talentCount = sum([talent.Rank for talent in chars[target].Talents])

print(f"Found {talentCount} talents")

for talent in chars[target].Talents:
    print(talent)
