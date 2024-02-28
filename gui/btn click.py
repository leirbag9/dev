from tkinter import *
click_count = 0
def btn_click():
    print("men")



window = Tk()

btn= Button(window, text="click for men", command=btn_click)

btn.pack()


window.mainloop()
