import tkinter as tk
import tkinter.ttk as ttk
import tkinter.scrolledtext as tkscrolled
from tkinter import filedialog
from tkinter import simpledialog
from tkinter import StringVar
from ttkthemes import ThemedTk
from jankigen.card_gen import CardGen
from jankigen.deck_gen import DeckGen
from jankigen.learning_material_getter import LearningMaterialGetter
from jankigen.version import version_string
import os
import sys


class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.shuffle_bool = tk.BooleanVar(value=True)
        self.label_user_dict_full_path = ""
        self.label_user_dict_en_full_path = ""
        self.master = master
        self.pack()
        self.create_widgets()

    def create_widgets(self):

        self.fleft = ttk.Frame(self)
        self.fleft.pack(side=tk.LEFT, fill=tk.X, expand=True, pady=5, padx=5)

        self.fright = ttk.Frame(self)
        self.fright.pack(side=tk.RIGHT, fill=tk.X, expand=True)

        self.btn_generate = ttk.Label(self.fleft, text="Insert Japanese text for deck generation", font=("Arial", 20))
        self.btn_generate.pack(side="top", padx=10, pady=5)

        self.text_area = tkscrolled.ScrolledText(self.fleft, font=("Times New Roman", 12))
        self.text_area.pack()

        self.check_shuffle = ttk.Checkbutton(self.fright, text="Shuffle cards", takefocus=False,
                                             variable=self.shuffle_bool)
        self.check_shuffle.grid(row=0, column=0, padx=(0, 20), pady=5)

        self.btn_user_dict = ttk.Button(self.fright, text="Select dictionary jp", takefocus=False,
                                        command=self.select_ditionary_jp)
        self.btn_user_dict.grid(row=1, column=0, padx=(0, 20), pady=5)

        self.label_user_dict = ttk.Label(self.fright, text="None")
        self.label_user_dict.grid(row=2, column=0, padx=(0, 20), pady=5)
        self.label_user_dict_full_path = ""

        self.btn_user_dict_en = ttk.Button(self.fright, text="Select dictionary jp-en", takefocus=False,
                                           command=self.select_ditionary_en)
        self.btn_user_dict_en.grid(row=3, column=0, padx=(0, 20), pady=5)

        self.label_user_dict_en = ttk.Label(self.fright, text="None")
        self.label_user_dict_en.grid(row=4, column=0, padx=(0, 20), pady=5)
        self.label_user_dict_en_full_path = ""

        self.btn_generate = ttk.Button(self.fleft, text="Generate Anki deck", takefocus=False,
                                       command=self.generate_deck)
        self.btn_generate.pack(side="bottom", padx=10, pady=5)

    def select_ditionary_jp(self):
        filename = tk.filedialog.askopenfilename(initialdir=".", title="Select file",
                                                 filetypes=[("csv files", "*.csv")])
        if len(filename) > 0:
            self.label_user_dict['text'] = os.path.basename(filename)
            self.label_user_dict_full_path = filename

    def select_ditionary_en(self):
        filename = tk.filedialog.askopenfilename(initialdir=".", title="Select file",
                                                 filetypes=[("csv files", "*.csv")])
        if len(filename) > 0:
            self.label_user_dict_en['text'] = os.path.basename(filename)
            self.label_user_dict_en_full_path = filename

    def generate_deck(self):
        shuffle = self.shuffle_bool.get()
        self.btn_generate.config(text="Wait...")
        self.btn_generate.configure(state=tk.DISABLED)

        name = tk.simpledialog.askstring("Enter deck name", "Enter deck name")
        if not name == "" and name:

            text = self.text_area.get("1.0", "end-1c")

            learning_material_getter = LearningMaterialGetter(self.label_user_dict_full_path,
                                                              self.label_user_dict_en_full_path)

            pairs = learning_material_getter.tokenize(text)
            dic_infos = learning_material_getter.getDictionaryInfos(pairs)
            kanji_notes = {}
            word_notes = {}
            for token, dic_info in dic_infos:
                CardGen(token, dic_info, kanji_notes, word_notes)

            savepath = filedialog.asksaveasfilename(initialdir=".", title="Select file destination",
                                                    filetypes=[("Anki deck", "*.apkg")])

            if not savepath == "":
                if not savepath.endswith(".apkg"):
                    savepath = savepath + ".apkg"

                DeckGen(os.path.basename(name),
                        savepath,
                        shuffle,
                        word_notes,
                        kanji_notes)

        self.btn_generate.config(text="Generate Anki deck")
        self.btn_generate.configure(state=tk.NORMAL)


def do_gui():
    root = ThemedTk(theme="plastik")
    root.title('JANKIGEN - ' + version_string)

    favicon_path = '/res/favicon.ico'
    if os.path.isfile(os.path.dirname(__file__) + favicon_path):
        root.iconbitmap(os.path.dirname(__file__) + favicon_path)
    else:
        root.iconbitmap(os.path.dirname(sys.argv[0]) + favicon_path)
    app = Application(master=root)
    app.mainloop()
