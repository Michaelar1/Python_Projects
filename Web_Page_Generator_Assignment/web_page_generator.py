

import tkinter as tk
from tkinter import *
import webbrowser

class ParentWindow(Frame):
    def __init__(self, master):
        Frame.__init__(self, master)
        self.master.title("Web Page Generator")

        #   Create a button that says "Default HTML Page"
        self.btn_default = Button(self.master, text="Default HTML Page", width=30, height=2, command=self.defaultHTML)
        self.btn_default.grid(row=2, column=1, padx=(10, 10), pady=(10, 10))

        #   Create input with label "Enter custom text or click the Default HTML page button"
        self.lbl_cust_txt = tk.Label(self.master, text="Enter custom text or click the Default HTML page button.")
        self.lbl_cust_txt.grid(row = 0, column=0, padx =(30, 10), pady = (10, 10))
        self.cust_txt = Entry(width = 125)
        self.cust_txt.grid(row=1, column=0, columnspan=4)

        #   Create "Submit custom text" button
        self.btn_submit = Button(self.master, text="Submit Custom Text", width = 30, height=2, command=self.customHTML)
        self.btn_submit.grid(row=2, column=2, padx=(10, 20), pady=(10, 10))
        


    def defaultHTML(self):
        htmlText= "Stay tuned for out amazing summer sale!"
        htmlFile = open("index.html", "w")
        htmlContent = "<html>\n<body>\n<h1>" + htmlText + "</h1>\n</body>\n</html>"
        htmlFile.write(htmlContent)
        htmlFile.close()
        webbrowser.open_new_tab("index.html")

    #   Create function that generates a web page with custom text
    def customHTML(self):
        cust_htmlText = self.cust_txt.get()
        htmlFile = open("index.html", "w")
        htmlContent = "<html>\n<body>\n<h1>" + cust_htmlText + "</h1>\n</body>\n</html>"
        htmlFile.write(htmlContent)
        htmlFile.close()
        webbrowser.open_new_tab("index.html")








if __name__ == "__main__":
    root = tk.Tk()
    App = ParentWindow(root)
    root.mainloop()
