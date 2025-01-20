import tkinter as tk

#inclut uniquement les fonctions :
'''
set_pixel
show_screen
clear_screen
'''

window = tk.Tk()
window.title("Calculette")
window.geometry("393x201")

canvas = tk.Canvas(window, width=383, height=191, bg='white')
# en haut au milieu :
canvas.pack()
# au centre :
#canvas.place(relx=0.5, rely=0.5, anchor="center")

def set_pixel(x,y,c):
  canvas.create_rectangle(x, y, x+1, y+1, fill=f'#{c[0]:02x}{c[1]:02x}{c[2]:02x}',outline="")

def show_screen():
  window.update()

def clear_screen():
  canvas.delete("all")
