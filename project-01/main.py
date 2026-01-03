from tkinter import *
from tkinter import colorchooser
from tkinter import filedialog
from tkinter import ttk
from PIL import ImageTk, Image, ImageChops

# ------------- #
# --- LOGIC --- #
# ------------- #

def show_info(original, inverted, mode):
  left_text = Label(
    root,
    text=None
  )
  left_text.grid(row=2, column=0)
  left_output = Label(
    root,
    text=None
  )
  left_output.grid(row=3, column=0)

  right_text = Label(
    root,
    text=None
  )
  right_text.grid(row=2, column=2)
  right_output = Label(
    root,
    text=None
  )
  right_output.grid(row=3, column=2)

  if mode == 'color':
    pass
  elif mode == 'image':
    tk_image = ImageTk.PhotoImage(original)
    tk_inverted = ImageTk.PhotoImage(inverted)

def invert_color(color):
  print(f"User is now inverting color ({color})")
  inverted_r = 255 - color[0]
  inverted_g = 255 - color[1]
  inverted_b = 255 - color[2]
  inverted_color = (inverted_r, inverted_g, inverted_b)
  print(f"Color has now been converted ({inverted_color}).")
  return inverted_color

def pick_color():
  print("User is selecting color.")
  selected_color = colorchooser.askcolor(title="Color to be Inverted")[0]
  print(f"User selected color {selected_color}.")
  inverted_color = invert_color(selected_color)
  show_info(selected_color, inverted_color, 'color')

def invert_image(image):
  print(f"Image is now being inverted ({image}).")
  opened_image = Image.open(image)
  print(f"Image has now been opened ({opened_image}).")
  inverted_image = ImageChops.invert(opened_image)
  print(f"Image has now been inverted ({inverted_image}).")

  return inverted_image

def get_image():
  print(f"User chose to send image.")
  filetypes = (
    ('.PNG Image', '*.png'),
    ('.JPEG Image', '*.jpeg'),
    ('.WEBP Image', '*.webp') # fuck you webp is ass
  )

  image = filedialog.askopenfilename(
    title='Image to be inverted',
    initialdir='/',
    filetypes=filetypes
  )
  print(f"User picked image {image}")
  inverted_image = invert_image(image)
  show_info(image, inverted_image, 'image')

# -------------- #
# --- WINDOW --- #
# -------------- #

root = Tk()
root.title("Color Picker")

title = Label(
  root,
  text='Color Picker'
)
title.grid(row=0, column=1)

color_button = ttk.Button(
  root,
  text='Pick Color',
  command=pick_color
)
color_button.grid(row=1, column=0)

or_label = Label(
  root,
  text='or'
)
or_label.grid(row=1, column=1)

image_button = ttk.Button(
  root,
  text='Upload Image',
  command=get_image
)
image_button.grid(row=1, column=2)


root.mainloop()