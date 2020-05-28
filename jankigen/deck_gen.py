import genanki
import random


def DeckGen(name, file_path, shuffle_card, word_notes, kanji_notes):
    my_deck = genanki.Deck(
        random.randrange(1 << 30, 1 << 31),
        name)

    if shuffle_card:
        def shuffle_dict(dictionary):
            tmp = list(dictionary.items())
            random.shuffle(tmp)
            return dict(tmp)
        word_notes = shuffle_dict(word_notes)
        kanji_notes = shuffle_dict(kanji_notes)

    notes = []
    for word_note in word_notes:
        for c in word_note:
            if c in kanji_notes:
                notes.append(kanji_notes.pop(c))
        notes.append(word_notes[word_note])

    # Remaining kanji
    for kanji_note in kanji_notes:
        notes.insert(random.randrange(0, len(notes)), kanji_notes[kanji_note])

    counter = 0
    for note in notes:
        note.fields[0] = str(counter)
        counter = counter + 1
        my_deck.add_note(note)
    if len(notes) > 0:
        genanki.Package(my_deck).write_to_file(file_path)