from tkinter import *
import tkinter
from tkinter import messagebox

height_w = 320
width_w = 250
    
window = Tk()
window.geometry(f'{height_w}x{width_w}')

def start_game():
    global btk_1
    btk_1 = Button(master=window, text=' Начать игру', command = lambda x = False: start_new_game(x))
    btk_1.place(relx =0.2, rely = 0.2, relheight=0.4, relwidth=0.5)


user_char = '0'
def click (index, button_list):
    global user_char

    button_list[index].configure(text = ['X' if user_char else '0'])
    button_list[index]['state'] = tkinter.DISABLED
    button_list[index]['relief'] = tkinter.SUNKEN
    user_char = not user_char
  

def start_new_game(player_start: int):
    btk_1.destroy()
    button_list = [0 for x in range(9)]
    index = 0
    for i in range(3):
        for j in range(3):
            frame = Frame(
                master = (window),
                relief = RAISED,
                borderwidth=1
                )
            frame.grid(row=i, column=j, padx=5, pady=5)
            button_list[index] = Button(master=frame, text='', height=4,width=12, command=lambda index = index:click(index, button_list))
            button_list[index].pack()
            index += 1

start_game()

window.mainloop()