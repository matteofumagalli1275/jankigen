## JANKIGEN

Generate anki decks from japanese text

#### Features
- Generate decks from directories
- Generate deck from single text file
- Card order is shuffled to prevent text understanding (enabled by default)
- Kanji card and Word cards
- Kanji cards are ordered to be before corresponding word cards
- Custom user dictionaries

#### Limitations/Known issues
- It is sloooow (some library i'm using don't fit this purpose, there is quite a work to do for this)
- CLI only for now

#### Install

```bash
pip install jankigen
```

#### Example commands:

```bash
# Decks are generated in the same folder of the parsed file/directory

# Generate one anki deck this file
jankigen text_file.txt

# Generate one anki deck for each file
jankigen directory_with_txts --disable_shuffle_card --deck_per_text_file --disable_gen_global_deck_for_all_files

```

```
jankigen --help

usage: jankigen [-h] [--disable_shuffle_card [DISABLE_SHUFFLE_CARD]] [--deck_per_text_file [DECK_PER_TEXT_FILE]]
                [--disable_gen_global_deck_for_all_files [DISABLE_GEN_GLOBAL_DECK_FOR_ALL_FILES]]
                [--user_dict USER_DICT] [--user_dict_en USER_DICT_EN]
                path

Generate anki deck from file

positional arguments:
  path                  File or directory with text files

optional arguments:
  -h, --help            show this help message and exit
  --disable_shuffle_card [DISABLE_SHUFFLE_CARD]
                        Shuffles cards to prevent text understanding/spoiler
  --deck_per_text_file [DECK_PER_TEXT_FILE]
                        If searching in a directory, create an anki file for each text file found
  --disable_gen_global_deck_for_all_files [DISABLE_GEN_GLOBAL_DECK_FOR_ALL_FILES]
                        Generate a global deck for all text files
  --user_dict USER_DICT
                        Simplified janome dictionary. A csv file as <surface form>,<part-of-speech>,<reading>
  --user_dict_en USER_DICT_EN
                        Match entries of user_dict with corresponding translations. <surface
                        form>,<reading>,<english_translation>

```
