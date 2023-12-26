import tkinter as tk 
from tkinter import PhotoImage
import winsound 
import time
import os 
import sys

W = 600
H = 800

win = tk.Tk()
win.title('DRUM')
win.geometry(f'{W}x{H}')
win.configure(bg='#FFFFFF')
# win.resizable(width=False, height=False)

notes_list = []

NOTES_PATH = os.getcwd() +'/notes'

# Function
def click_play():
    for note in notes_list:        
        winsound.PlaySound(f'{NOTES_PATH}/{note}.wav', winsound.SND_ASYNC)    
        time.sleep(0.30)
    
   
def restart_program():
    python = sys.executable
    os.execl(python, python, * sys.argv)


def click_add_note(note):
        if note == 'do':
            note1 = tk.Button(image=notett, bg='#FFFFFF')
            note1.place(x=(len(notes_list)+1) * 50 % 600, y= 320 + ((len(notes_list)+1) * 50 // 600) * 118)
            notes_list.append(note)
        if note == 're':
            note1 = tk.Button(image=notett, bg='#FFFFFF')
            note1.place(x=(len(notes_list)+1) * 50 % 600, y= 310 + ((len(notes_list)+1) * 50 // 600) * 118)
            notes_list.append(note)
        if note == 'mi':
            note1 = tk.Button(image=notett, bg='#FFFFFF')
            note1.place(x=(len(notes_list)+1) * 50 % 600, y= 300 + ((len(notes_list)+1) * 50 // 600) * 118)
            notes_list.append(note)
        if note == 'fa':
            note1 = tk.Button(image=notett, bg='#FFFFFF')
            note1.place(x=(len(notes_list)+1) * 50 % 600, y= 290 + ((len(notes_list)+1) * 50 // 600) * 118)
            notes_list.append(note)
        if note == 'sol':
            note1 = tk.Button(image=notett, bg='#FFFFFF')
            note1.place(x=(len(notes_list)+1) * 50 % 600, y= 280 + ((len(notes_list)+1) * 50 // 600) * 118)
            notes_list.append(note)
        if note == 'lya':
            note1 = tk.Button(image=notett, bg='#FFFFFF')
            note1.place(x=(len(notes_list)+1) * 50 % 600, y= 270 + ((len(notes_list)+1) * 50 // 600) * 118)
            notes_list.append(note)
        if note == 'si':
            note1 = tk.Button(image=notett, bg='#FFFFFF')
            note1.place(x=(len(notes_list)+1) * 50 % 600, y= 260 + ((len(notes_list)+1) * 50 // 600) * 118)
            notes_list.append(note)
        if note == 'pause':
            note1 = tk.Button(image=notett, bg='#FFFFFF')
            note1.place(x=(len(notes_list)+1) * 50 % 600, y= 290 + ((len(notes_list)+1) * 50 // 600) * 118)
            notes_list.append(note)
    
    


    


# images
play_image = PhotoImage(file=os.getcwd() + '/notes/play_button.png')
notes_lis = PhotoImage(file=os.getcwd() + '/notes/notes.png')
notett = PhotoImage(file=os.getcwd() + '/notes/note.png')


# Labels
welcome_label = tk.Label(text='Напиши свою музыку прямо здесь!', bg='#FFFFFF', )
welcome_label.pack()

notes_label = tk.Label(image=notes_lis, bg='#FFFFFF')
notes_label.place(x=1, y=300) 

notes_label = tk.Label(text='Выберите ноту', bg='#FFFFFF', )
notes_label.pack()

# Buttons
play_button = tk.Button(image=play_image, bg='#FFFFFF', command=lambda: click_play())
play_button.pack()

note_DO_button = tk.Button(text='До', bg='#FFFFFF', command=lambda: click_add_note('do')) #, command=lambda: click_add_note2('do'))
note_DO_button.place(x=20, y=120, height=40, width=70)

note_RE_button = tk.Button(text='Ре', bg='#FFFFFF', command=lambda: click_add_note('re'))
note_RE_button.place(x=100, y=120, height=40, width=70)

note_MI_button = tk.Button(text='Ми', bg='#FFFFFF', command=lambda: click_add_note('mi'))
note_MI_button.place(x=180, y=120, height=40, width=70)

note_FA_button = tk.Button(text='Фа', bg='#FFFFFF', command=lambda: click_add_note('fa'))
note_FA_button.place(x=260, y=120, height=40, width=70)

note_SOL_button = tk.Button(text='Соль', bg='#FFFFFF', command=lambda: click_add_note('sol'))
note_SOL_button.place(x=340, y=120, height=40, width=70)

note_LYA_button = tk.Button(text='Ля', bg='#FFFFFF', command=lambda: click_add_note('lya'))
note_LYA_button.place(x=420, y=120, height=40, width=70)

note_SI_button = tk.Button(text='Си', bg='#FFFFFF', command=lambda: click_add_note('si'))
note_SI_button.place(x=500, y=120, height=40, width=70)

note_pause_button = tk.Button(text='Пауза', bg='#FFFFFF', command=lambda: click_add_note('pause'))
note_pause_button.place(x=20, y=170, height=40, width=70)




delete_button = tk.Button(text='Перезапуск', bg='#FFFFFF', command=lambda:restart_program())
delete_button.place(x=500, y=70, height=40, width=70)


win.mainloop()












