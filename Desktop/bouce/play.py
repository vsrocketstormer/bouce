from tkinter import*
#from winsound import*
#tk=Tk()

#play = lambda: PlaySound("ved.mp3",SND_FILENAME)
#button = Button(tk, text = 'Play', command = play)

#button.pack()
#tk.mainloop()

from mp3play import *

root = Tk()

f = mp3play.load('ved.mp3'); play = lambda: f.play()
button = Button(root, text = 'Play', command = play)

button.pack()
root.mainloop()
