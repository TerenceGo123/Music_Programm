import tkinter as tk 
from tkinter import PhotoImage
import winsound 
import time

W = 600
H = 800

win = tk.Tk()
win.title('DRUM')
win.geometry(f'{W}x{H}')
win.configure(bg='#FFFFFF')
win.resizable(width=False, height=False)

notes_str = []

# Function
def click_play():
    if notes_str[0] == '1':
        winsound.PlaySound('C:/Users/User/Documents/My Games/test/do.wav', winsound.SND_ASYNC)
    elif notes_str[0] == '2':
        winsound.PlaySound('C:/Users/User/Documents/My Games/test/mi.wav', winsound.SND_ASYNC)
    time.sleep(0.30)
    if notes_str[1] == '1':
        winsound.PlaySound('C:/Users/User/Documents/My Games/test/do.wav', winsound.SND_ASYNC)
    elif notes_str[1] == '2':
        winsound.PlaySound('C:/Users/User/Documents/My Games/test/mi.wav', winsound.SND_ASYNC)
    time.sleep(0.30)
    if notes_str[2] == '1':
        winsound.PlaySound('C:/Users/User/Documents/My Games/test/do.wav', winsound.SND_ASYNC)
    elif notes_str[2] == '2':
        winsound.PlaySound('C:/Users/User/Documents/My Games/test/mi.wav', winsound.SND_ASYNC)
    time.sleep(0.30)
    if notes_str[3] == '1':
        winsound.PlaySound('C:/Users/User/Documents/My Games/test/do.wav', winsound.SND_ASYNC)
    elif notes_str[3] == '2':
        winsound.PlaySound('C:/Users/User/Documents/My Games/test/mi.wav', winsound.SND_ASYNC)
    time.sleep(0.30)
    if notes_str[4] == '1':
        winsound.PlaySound('C:/Users/User/Documents/My Games/test/do.wav', winsound.SND_ASYNC)
    elif notes_str[4] == '2':
        winsound.PlaySound('C:/Users/User/Documents/My Games/test/mi.wav', winsound.SND_ASYNC)
    time.sleep(0.30)
    if notes_str[5] == '1':
        winsound.PlaySound('C:/Users/User/Documents/My Games/test/do.wav', winsound.SND_ASYNC)
    elif notes_str[5] == '2':
        winsound.PlaySound('C:/Users/User/Documents/My Games/test/mi.wav', winsound.SND_ASYNC)
    time.sleep(0.30)
    if notes_str[6] == '1':
        winsound.PlaySound('C:/Users/User/Documents/My Games/test/do.wav', winsound.SND_ASYNC)
    elif notes_str[6] == '2':
        winsound.PlaySound('C:/Users/User/Documents/My Games/test/mi.wav', winsound.SND_ASYNC)
    time.sleep(0.30)
    if notes_str[7] == '1':
        winsound.PlaySound('C:/Users/User/Documents/My Games/test/do.wav', winsound.SND_ASYNC)
    elif notes_str[7] == '2':
        winsound.PlaySound('C:/Users/User/Documents/My Games/test/mi.wav', winsound.SND_ASYNC)
    time.sleep(0.30)
    if notes_str[8] == '1':
        winsound.PlaySound('C:/Users/User/Documents/My Games/test/do.wav', winsound.SND_ASYNC)
    elif notes_str[8] == '2':
        winsound.PlaySound('C:/Users/User/Documents/My Games/test/mi.wav', winsound.SND_ASYNC)
    time.sleep(0.30)
    
def click_do():
    note1 = tk.Button(image=note, bg='#FFFFFF')
    note1.pack(anchor="nw", padx=20, pady=170, side='left')
    notes_str.append('1')

    
def click2_mi():
    note1 = tk.Button(image=note, bg='#FFFFFF')
    note1.pack(anchor="nw", padx=20, pady=170, side='left')
    notes_str.append('2')



# images
play_image = PhotoImage(file='C:/Users/User/Documents/My Games/test/play_button.png')
notes_list = PhotoImage(file='C:/Users/User/Documents/My Games/test/notes.png')
note = PhotoImage(file='C:/Users/User/Documents/My Games/test/note.png')


# Labels
welcome_label = tk.Label(text='Напиши свою музыку прямо здесь!', bg='#FFFFFF', )
welcome_label.pack()

notes_label = tk.Label(image=notes_list, bg='#FFFFFF')
notes_label.place(x=1, y=300) 

notes_label = tk.Label(text='Выберите ноту', bg='#FFFFFF', )
notes_label.pack()

# Buttons
play_button = tk.Button(image=play_image, bg='#FFFFFF', command=lambda: click_play())
play_button.pack()

note_DO_button = tk.Button(text='До', bg='#FFFFFF', command=lambda: click_do())
note_DO_button.place(x=20, y=120, height=40, width=70)

note_MI_button = tk.Button(text='Ми', bg='#FFFFFF', command=lambda: click2_mi())
note_MI_button.place(x=80, y=120, height=40, width=70)














win.mainloop()

print(notes_str)





