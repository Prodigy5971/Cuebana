from pathlib import Path
import tkinter as tk
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage, Frame, ttk


OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path("./assets")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


def mainPage(frame):
    #tree_view = ttk.Treeview()
    #item = tree_view.insert("", tk.END, text="Elemento 1")
    #tree_view.insert(item, tk.END, text="Sub-elemento 1")
    #tree_view.pack()
    frame.pack(fill="x")
    frame.config(bg="blue", width="400", height="200",
                 bd="24", relief="sunken", cursor="heart")
    

def secondPage(frame):
    frame.pack(fill="x")
    frame.config(bg="red", width="400", height="200",
                 bd="24", relief="sunken", cursor="")


def switchFrame(frame, number):
    if (number == 0): 
        mainPage(frame)
    elif (number == 1):
        secondPage(frame)


def main():
    root = Tk()
    root.title("Tkinter Test")
    root.config(width="500", height="500")
    frame = Frame()

    button = Button(root, text="frame 0",
                    command=lambda: switchFrame(frame, 0))
    button.place(x=50, y=50)

    button_1 = Button(root, text="frame 1",
                      command=lambda: switchFrame(frame, 1))
    button_1.place(x=120, y=50)

    root.mainloop()


if __name__ == "__main__":
    main()