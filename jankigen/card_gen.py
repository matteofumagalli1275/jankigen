import genanki
import random

anki_kanji_card_model = genanki.Model(
    random.randrange(1 << 30, 1 << 31),
    'KanjiModel',
    fields=[
        {'name': 'Index'},
        {'name': 'Question'},
        {'name': 'Meanings'},
        {'name': 'KunReading'},
        {'name': 'OnReading'},
        {'name': 'JlptLevel'},
    ],
    templates=[
        {
            'name': 'Card Kanji',
            'qfmt': '<div class="style-front">{{Question}}</div>',
            'afmt': "{{FrontSide}}<hr id=\"answer\"> <div class=\"style-meaning\"> {{Meanings}} </div>"
                    "<div class=\"style-reading\">"
                    "<b>Kun: </b>{{KunReading}} <br/> "
                    "<b>On: </b>{{OnReading}} <br/> "
                    "<b>JLPT Level: </b>{{JlptLevel}}"
                    "</div>"
        }],
    css=".card { position: relative; text-align:center; color: #000000; background: #ffffff; margin: 0px auto; padding: 0px; }"
        ".style-front { font-size: 115px; margin: 0px auto; padding-top: 15px; }"
        ".style-meaning { font-size: 20px; margin: 0px auto; padding-top: 15px;}"
        ".style-reading { font-size: 25px; margin: 0px auto; padding: 15px 0px; display: inline-block; text-align: left;}",
)

anki_word_card_model = genanki.Model(
    random.randrange(1 << 30, 1 << 31),
    'WordModel',
    fields=[
        {'name': 'Index'},
        {'name': 'Question'},
        {'name': 'Meanings'},
        {'name': 'Reading'},
    ],
    templates=[
        {
            'name': 'Card Word',
            'qfmt': '<div class="style-front">{{Question}}</div>',
            'afmt': "<div class=\"style-reading\"> {{Reading}} </div> {{FrontSide}}"
                    "<hr id=\"answer\"><div class=\"style-meaning\"> {{Meanings}} </div>"
        }],
    css=".card { position: relative; text-align:center; color: #000000; background: #ffffff; margin: 0px auto; padding: 0px; }"
        ".style-front { font-size: 85px; margin: 0px auto; }"
        ".style-meaning { font-size: 20px; margin: 0px auto; padding-top: 15px;}"
        ".style-reading { font-size: 20px; margin: 0px auto; padding: 0px; padding-top: 20px; }",
)


def CardGen(token, dictionary_result, kanji_notes_dict, word_notes_dict):
    # Kanji
    for char in dictionary_result.chars:
        # Skip alternative writings (Ex. 迷う / 紕う)
        if char.literal not in token:
            continue
        literal = char.literal
        meanings = []
        readings_kun = []
        readings_on = []
        for rm in char.rm_groups:
            en_meanings = list(filter(lambda m: m.m_lang == '' or m.m_lang == 'en', rm.meanings))
            jp_readings = list(filter(lambda m: m.r_type == 'ja_kun' or m.r_type == 'ja_on', rm.readings))
            for en_m in en_meanings:
                meanings.append(en_m.value)
            for jp_r in jp_readings:
                if jp_r.r_type == 'ja_kun':
                    readings_kun.append(jp_r.value)
                else:
                    readings_on.append(jp_r.value)
        print("==== Single Kanji: " + literal + " ====")
        print(meanings)
        print(readings_kun)
        my_note = genanki.Note(
            model=anki_kanji_card_model,
            fields=["0", literal, ", ".join(meanings), ", ".join(readings_kun), ", ".join(readings_on), str(char.jlpt)])
        kanji_notes_dict[literal] = my_note

    # Words
    if len(dictionary_result.entries) > 0:
        entry = dictionary_result.entries[0]
        senses = []
        for sense in entry.senses:
            senses.append(", ".join(str(x) for x in sense.gloss))
        print("==== Word: " + token + " ====")
        print(entry.kana_forms[0].text)
        print(senses)
        if len(entry.kana_forms) > 0:
            my_note = genanki.Note(
                model=anki_word_card_model,
                fields=["0", token, "<br/>".join(senses), entry.kana_forms[0].text])
            word_notes_dict[token] = my_note
