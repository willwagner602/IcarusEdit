from IcarusEdit import get_characters, find_character_index_by_name, save_characters, get_max_talents

CHARACTER_NAME = "BODICUS"

chars = get_characters()
target_char = find_character_index_by_name(CHARACTER_NAME, chars)
chars[target_char].Talents = get_max_talents()
save_characters(chars)
