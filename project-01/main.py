from tkinter import *
from tkinter import colorchooser

selected_color = ()
inverted_color = ()

def get_color():
  global selected_color
  color_code = colorchooser.askcolor(title='Color to be inverted')
  print(color_code[0])
  selected_color = color_code[0]
  show_color.config(text=f'Selected Color: {selected_color}')

def invert_color():
  global selected_color
  global inverted_color
  inverted_r = 255 - selected_color[0]
  inverted_g = 255 - selected_color[1]
  inverted_b = 255 - selected_color[2]
  inverted_color = (inverted_r, inverted_g, inverted_b)
  show_invert.config(text=f"Inverted Color: {inverted_color}")

root = Tk()

### COLUMN 0 ###
l1 = Label(
  root,
  text='Enter your color of choice'
)
l1.grid(row=0, column=0)

color_button = Button(
  root,
  text='Select Color',
  command=get_color
)
color_button.grid(row=1, column=0)

show_color = Label(
  root,
  text="Select a color!"
)
show_color.grid(row=2, column=0)

### COLUMN 1 ###
l2 = Label(
  root,
  text='Below is the inverted color'
)
l2.grid(row=0, column=1)

invert_button = Button(
  root,
  text='Get Inverted Color',
  command=invert_color
)
invert_button.grid(row=1, column=1)

show_invert = Label(
  root,
  text='Pick the color first!'
)
show_invert.grid(row=2, column=1)

root.mainloop()