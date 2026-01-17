# Project 01: Color Inverter
**Description**: The user will place down RGB values. After submitting the values, a new color value will be returned, with this new value being the inverted version of the color you placed.

**What I'm Testing**: I've never made a full-blown GUI before. After all my time of using Python, I've been using the console, and those weren't cool CLI apps either. So, I'll be _experimenting with Tkinter_. I'll be using it for a few projects while I learn the ropes of the module, starting with this.

**Due Date**: 1/17/26
## Reflection
1. **Problem Summary**: This project was meant to just invert the RGB values of whatever the user placed, but after having completed that rather easily, I chose to add onto the project by inverting the image sent by the user. 

2. **My Approach**: I would have a unique function handling the logic. A function would handle the color inversion, another would handle the image inversion, one function would handle the color input and another function would handle the image input.

3. **Challenges Faced**: Eventually, I had trouble finding out _where_ an error came from, even after reading the error message where it leads me to the source of the error. Furthermore, I learned that I was passing variables while not quite knowing what type it is. What I mean bu this is:
	- I thought the image path (in the `get_image()` function) was the image itself and not the _path_ to the image. This had taken me a while to find out. And stuff like this occurred semi-frequently throughout the project.

4. **Key Learnings**: Printing every single action that has been performed has helped me during the debugging process massively. By printing out _every_ single thing that the code is doing, I was able to tell just where the errors had spawned from. It was also thanks to printing everything that I found out that I had to keep track of the variable types.

5. **Future Applications**: I need to pay attention to the data types of the variables so that I’m not passing a variable with a data type that just doesn’t work. I’ll be sure to read a lot more on the documentation of the modules I’m using too, as I had simply looked up how to do things like image conversion without truly understanding what’s going on.

6. **Areas for Improvement**: My **consistency** throughout the first project has been very poor. as you can see by the commit history from January 3 to the day of writing (January 17), I’ve made about five commits (some not even related to the code but the Markdown files). And, while the image inversion part “works”, the user needs to close the app and reopen it to place another image. Some other images simply just turn into a solid color when trying to invert it.

**Overall**: I could’ve done much better. I’m left with a semi-functional color inverting app. I’ll focus on paying attention to what I’m doing to data types, pseudo-code and plan out what I want to write first, and actually remain dedicated to the craft of coding.