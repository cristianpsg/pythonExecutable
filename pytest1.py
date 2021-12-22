import tkinter as tk

import requests
from bs4 import BeautifulSoup


def helloCallBack():
    #tkMessageBox.showinfo( "Hello Python", "Hello World")
    response = requests.get("https://shubhamsayon.github.io/python/demo_html.html")
    webpage = response.content
    # 4. Check Status Code (Optional)
    # print(response.status_code)
    # 5. Create a Beautiful Soup Object
    soup = BeautifulSoup(webpage, "html.parser")
    # 6. Implement the Logic.
    for tr in soup.find_all('tr'):
        topic = "TOPIC: "
        url = "URL: "
        values = [data for data in tr.find_all('td')]
        for value in values:
            text.insert(tk.INSERT,topic + value.text + "\n" )
            topic = url
            text.insert(tk.INSERT, "\n")
    #print()
 
    #for x in range(1,10):
    #     text.insert(tk.INSERT, "Hello.....\n")
    #     #text.insert(tk.END, "Bye Bye.....")
   



root= tk.Tk()

b=tk.Button(root, text ="Hello", command = helloCallBack)
b.pack()

text = tk.Text(root)
text.pack()

root.mainloop()