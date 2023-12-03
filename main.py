import tkinter as tk 
from tkinter import PhotoImage
import winsound 
import time
import os 


W = 600
H = 800

win = tk.Tk()
win.title('DRUM')
win.geometry(f'{W}x{H}')
win.configure(bg='#FFFFFF')
win.resizable(width=False, height=False)

notes_list = []

NOTES_PATH = os.getcwd() +'/notes'

# Function
def click_play():
    for note in notes_list:        
        winsound.PlaySound(f'{NOTES_PATH}/{note}.wav', winsound.SND_ASYNC)    
        time.sleep(0.30)
    
   
def click_delete_all():
    notes_list.clear()
    

def click_add_note(note):
    if note == 'do':
        note1 = tk.Button(image=notett, bg='#FFFFFF')
        note1.pack(anchor="nw", padx=20, pady=250, side='left')
        notes_list.append(note)
    if note == 're':
        note1 = tk.Button(image=notett, bg='#FFFFFF')
        note1.pack(anchor="nw", padx=20, pady=235, side='left')
        notes_list.append(note)
    if note == 'mi':
        note1 = tk.Button(image=notett, bg='#FFFFFF')
        note1.pack(anchor="nw", padx=20, pady=210, side='left')
        notes_list.append(note)
    if note == 'fa':
        note1 = tk.Button(image=notett, bg='#FFFFFF')
        note1.pack(anchor="nw", padx=20, pady=190, side='left')
        notes_list.append(note)
    if note == 'sol':
        note1 = tk.Button(image=notett, bg='#FFFFFF')
        note1.pack(anchor="nw", padx=20, pady=175, side='left')
        notes_list.append(note)
    if note == 'lya':
        note1 = tk.Button(image=notett, bg='#FFFFFF')
        note1.pack(anchor="nw", padx=20, pady=150, side='left')
        notes_list.append(note)
    if note == 'si':
        note1 = tk.Button(image=notett, bg='#FFFFFF')
        note1.pack(anchor="nw", padx=20, pady=135, side='left')
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

note_SI_button = tk.Button(text='si', bg='#FFFFFF', command=lambda: click_add_note('si'))
note_SI_button.place(x=490, y=120, height=40, width=70)




delete_button = tk.Button(text='Удалить всё', bg='#FFFFFF', command=lambda: click_delete_all())
delete_button.place(x=500, y=120, height=40, width=70)














win.mainloop()

print(notes_list)










