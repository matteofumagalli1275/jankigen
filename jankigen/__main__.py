import os
import argparse
from jankigen.cli_utils import CliUtils
from jankigen.gui import do_gui


def main(args=None):
    """The main routine."""
    path = ""
    user_dict = ""
    user_dict_en = ""
    shuffle_card = True
    deck_per_text_file = False
    gen_global_deck_for_all_files = True

    parser = argparse.ArgumentParser(description='Generate anki deck from file')
    parser.add_argument('path', type=str, nargs='?',
                        help='File or directory with text files')
    parser.add_argument('--disable_shuffle_card', action='store_true',
                        help='Shuffles cards to prevent text understanding/spoiler')
    parser.add_argument('--enable_deck_per_text_file', action='store_true',
                        help='If searching in a directory, create an anki file for each text file found')
    parser.add_argument('--disable_gen_global_deck_for_all_files', action='store_true',
                        help='Generate a global deck for all text files')
    parser.add_argument('--user_dict', type=str,
                        help='Simplified janome dictionary. A csv file as <surface form>,<part-of-speech>,<reading>')
    parser.add_argument('--user_dict_en', type=str,
                        help='Match entries of user_dict with corresponding translations. <surface form>,<reading>,<english_translation>')

    args = parser.parse_args()

    print("Wait initialization...")

    if args.path:
        path = args.path
        if args.disable_shuffle_card:
            shuffle_card = False

        if args.enable_deck_per_text_file:
            deck_per_text_file = True

        if args.disable_gen_global_deck_for_all_files:
            gen_global_deck_for_all_files = False

        if args.user_dict:
            user_dict = args.user_dict

        if args.user_dict_en:
            user_dict_en = args.user_dict_en

        def normalize_path(path):
            if path == "" or os.path.isabs(path):
                return path
            else:
                return os.path.relpath(path)

        path = normalize_path(path)
        user_dict = normalize_path(user_dict)
        user_dict_en = normalize_path(user_dict_en)

        cli = CliUtils(path=path,
                       shuffle_card=shuffle_card,
                       deck_per_text_file=deck_per_text_file,
                       gen_global_deck_for_all_files=gen_global_deck_for_all_files,
                       user_dict=user_dict,
                       user_dict_en=user_dict_en)

        cli.run()
    else:
        do_gui()

if __name__ == "__main__":
    main()