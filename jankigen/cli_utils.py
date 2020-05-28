import os
import io
from jankigen.card_gen import CardGen
from jankigen.deck_gen import DeckGen
from jankigen.learning_material_getter import LearningMaterialGetter


class CliUtils:
    def __init__(self, path, shuffle_card=True, deck_per_text_file=False, gen_global_deck_for_all_files=True,
                 user_dict="", user_dict_en=""):
        self.learning_material_getter = LearningMaterialGetter(user_dict, user_dict_en)
        self.path = path
        self.kanji_notes = {}
        self.word_notes = {}
        self.shuffle_card = shuffle_card
        self.anki_per_text_file = deck_per_text_file
        self.gen_global_anki_for_all_files = gen_global_deck_for_all_files

    def run(self):
        if os.path.isdir(self.path):
            self.__handle_dir(self.path)
        else:
            self.__handle_file(self.path)

        if self.gen_global_anki_for_all_files:
            DeckGen(os.path.basename(self.path),
                    os.path.splitext(self.path)[0] + '.apkg',
                    self.shuffle_card,
                    self.word_notes,
                    self.kanji_notes)

    def __handle_file(self, full_a):
        if full_a.endswith(".apkg") or full_a.endswith(".csv"):
            return
        print("Handling file " + full_a)
        f = io.open(full_a, mode="r", encoding="utf-8")
        text = f.read()
        f.close()
        pairs = self.learning_material_getter.tokenize(text)
        dic_infos = self.learning_material_getter.getDictionaryInfos(pairs)
        kanji_notes = {}
        word_notes = {}
        for token, dic_info in dic_infos:
            CardGen(token, dic_info, kanji_notes, word_notes)

        if self.gen_global_anki_for_all_files:
            self.kanji_notes = {**kanji_notes, **self.kanji_notes}
            self.word_notes = {**word_notes, **self.word_notes}

        if self.anki_per_text_file:
            DeckGen(os.path.basename(full_a),
                    os.path.splitext(full_a)[0] + '.apkg',
                    self.shuffle_card,
                    word_notes,
                    kanji_notes)

    def __handle_dir(self, path):
        arr = os.listdir(path)
        for a in arr:
            full_a = os.path.join(path, a)
            if os.path.isdir(full_a):
                self.__handle_dir(os.path.join(path, full_a))
            else:
                self.__handle_file(full_a)
