from Pig import Pig
from tkinter import *
from tkinter.ttk import Combobox

def input_action():
    bot_number.set(int(bot_number_combo.get()))
    move_number.set(int(move_number_input.get()))


window = Tk()
window.title('Pig game')
window.geometry('800x250')
input_label1 = Label(window, text='Input bots number')
input_label1.grid(column=0, row=0)
bot_number_combo = Combobox(window)
bot_number_combo.grid(column=1, row=0)
bot_number_combo['values'] = (0, 1, 2, 3, 4, 5)
bot_number_combo.current(1)
input_label2 = Label(window, text='Input moves number')
input_label2.grid(column=0, row=1)
move_number_input = Entry(window, width=10)
move_number_input.grid(column=1, row=1)

bot_number = IntVar()
move_number = IntVar()
input_button = Button(window, text='Confirm', command=input_action)
input_button.grid(column=0, row=2)
window.wait_variable(move_number)
pig = Pig(bot_number.get(), move_number.get(), window)
pig.play()
#arguments = tuple(map(int, input('Input bots number (0-5) and moves number: ').split()))
window.mainloop()