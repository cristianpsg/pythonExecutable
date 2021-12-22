from cryptography.fernet import Fernet
import base64

import tkinter as tk
import tkinter.ttk as ttk
import requests
from bs4 import BeautifulSoup

code = b"""

import tkinter as tk
import tkinter.ttk as ttk
import requests
from bs4 import BeautifulSoup


def helloCallBack():
    #tkMessageBox.showinfo( "Hello Python", "Hello World")
    combo.txt.delete("1.0",tk.END)
    response = requests.get("https://shubhamsayon.github.io/python/demo_html.html")
    webpage = response.content
    
    soup = BeautifulSoup(webpage, "html.parser")
    # 6. Implement the Logic.
    for tr in soup.find_all('tr'):
        topic = "TOPIC: "
        url = "URL: "
        values = [data for data in tr.find_all('td')]
        for value in values:
            combo.txt.insert(tk.INSERT,topic + value.text + "\\n" )
            topic = url
            combo.txt.insert(tk.INSERT, "\\n")

class TextScrollCombo(ttk.Frame):

    def __init__(self, *args, **kwargs):

        super().__init__(*args, **kwargs)

    # ensure a consistent GUI size
        self.grid_propagate(False)
    # implement stretchability
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)

    # create a Text widget
        self.txt = tk.Text(self)
        self.txt.grid(row=0, column=0, sticky="nsew", padx=2, pady=2)

    # create a Scrollbar and associate it with txt
        scrollb = ttk.Scrollbar(self, command=self.txt.yview)
        scrollb.grid(row=0, column=1, sticky='nsew')
        self.txt['yscrollcommand'] = scrollb.set

main_window = tk.Tk()

combo = TextScrollCombo(main_window)
combo.pack(fill="both", expand=True)
combo.config(width=600, height=400)

combo.txt.config(font=("consolas", 10), undo=True, wrap='word')
combo.txt.config(borderwidth=2, relief="sunken")

combo.txt.insert(tk.INSERT,"HELOOO\\n" )

#style = ttk.Style()
#style.theme_use('clam')

b=tk.Button(main_window, text ="Run Test", command = helloCallBack)
b.pack()

main_window.mainloop()

"""

key = Fernet.generate_key()
encryption_type = Fernet(key)
encrypted_message = encryption_type.encrypt(code)

decrypted_message = encryption_type.decrypt(encrypted_message)

exec(decrypted_message)