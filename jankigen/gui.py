import tkinter as tk

class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        #self.hi_there["command"] = self.say_hi

        self.fleft = tk.Frame(self,  bg="red")
        self.fleft.pack(side=tk.LEFT, fill=tk.X, expand=True)

        self.fright = tk.Frame(self,  bg="yellow")
        self.fright.pack(side=tk.RIGHT, fill=tk.X, expand=True)

        self.text_area = tk.Text(self.fleft)
        self.text_area.pack(padx=10,pady=10)

        self.radio_shuffle = tk.Checkbutton(self.fright, text="Shuffle cards")
        self.radio_shuffle.pack(side="bottom", padx=10,pady=10)

        self.frame_user_dict = tk.Frame(self.fright)
        self.frame_user_dict.pack(side=tk.TOP, fill=tk.X, pady=10, expand=True)

        self.btn_user_dict = tk.Button(self.frame_user_dict, text="Select dictionary jp")
        self.btn_user_dict.pack(side=tk.TOP, padx=10, pady=5, fill=tk.X, expand=True)

        self.label_user_dict = tk.Label(self.frame_user_dict, text="None")
        self.label_user_dict.pack(side="left", fill=tk.X, expand=True)

        self.frame_user_dict_en = tk.Frame(self.fright)
        self.frame_user_dict_en.pack(side=tk.TOP, fill=tk.X, pady=10, expand=True)

        self.btn_user_dict_en = tk.Button(self.frame_user_dict_en, text="Select dictionary jp-en")
        self.btn_user_dict_en.pack(side=tk.TOP, padx=10, pady=5)

        self.label_user_dict_en = tk.Label(self.frame_user_dict_en, text="None")
        self.label_user_dict_en.pack(side="left", fill=tk.X, expand=True)

        self.btn_generate = tk.Button(self.fleft, text="Generate Anki deck")
        self.btn_generate.pack(side="bottom", padx=10)

        """
        self.quit = tk.Button(self, text="QUIT", fg="red",
                              command=self.master.destroy)
        self.quit.pack(side="bottom")


        self.radio_shuffle = tk.Checkbutton(self, text="Shuffle cards")
        self.radio_shuffle.pack(side="left", padx=10, pady=10)

        self.btn_user_dict = tk.Button(self, text="Choose")
        self.btn_user_dict.pack(side="left", padx=10, pady=10)


    def say_hi(self):
        print("hi there, everyone!")

"""
def do_gui():
    root = tk.Tk()
    app = Application(master=root)
    app.mainloop()