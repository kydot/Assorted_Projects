import tkinter as tk
import random
window = tk.Tk()
window.title('Literacy Test')
events_list = []
changed=False
def scramble(key):
    if key>96:
        caps=False
    else:
        caps=True
    key=random.randint(1,26)
    if caps==False:
        key+=96
    else:
        key+=64
    return key

def handle_keypress(event):
    key = event.char
    global changed
    if key == '\x08':
        label['text']=label['text'][:-1]
        changed=True
    else:
        if key.isalpha():
            key=ord(key)
            num = random.random()
            if changed==True:
                changed=False
                num+=.5
            if num>0.9:
                key=scramble(key)
            key=chr(key)
        label['text']+=key

window.bind('<Key>', handle_keypress)

text='Hello Australia! I can type words in the English Language!'
label = tk.Label(master=window, text=f'Type the following text:\n{text}\n-----\n')
label.pack()

window.mainloop()