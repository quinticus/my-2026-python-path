from tkinter import *
from tkinter import colorchooser

selected_color = ()
inverted_color = ()

def invert_color():
  global selected_color
  global inverted_color
  inverted_r = 255 - selected_color[0]
  inverted_g = 255 - selected_color[1]
  inverted_b = 255 - selected_color[2]
  inverted_color = (inverted_r, inverted_g, inverted_b)
  show_invert.config(text=f"Inverted Color: {inverted_color}")

def get_color():
  global selected_color
  color_code = colorchooser.askcolor(title='Color to be inverted')
  selected_color = color_code[0]
  show_color.config(text=f'Selected Color: {selected_color}')
  invert_color()

root = Tk()
root.title("Color Inverter")

label = Label(
  root,
  text='Use the buttton below to pick a color.'
)
label.grid(row=0, column=0)

color_button = Button(
  root,
  text='Select Color',
  command=get_color
)
color_button.grid(row=1, column=0)

show_color = Label(
  root,
  text=None
)
show_color.grid(row=2, column=0)

show_invert = Label(
  root,
  text=None
)
show_invert.grid(row=3, column=0)

root.mainloop()