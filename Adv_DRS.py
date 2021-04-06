# imported the libraries needed(modules)
import tkinter
from PIL import Image, ImageTk
import random

# top-level widget which represents the main window of an application
root = tkinter.Tk()
root.geometry('400x400')
root.title('DearSaurav Roll the Dice')
# above code will generate a blank window of  dice rolling simulator

# Adding label into the frame
BlankLine = tkinter.Label(root, text="")
BlankLine.pack()

# Adding label with different font and format
HeadingLabel = tkinter.Label(root, text="Hello, from !!Saurav_Kashyap!!", fg="light green", bg="dark green", font= "Helvetica 16 bold italic")
HeadingLabel.pack()

'''...........formatting a list of images to be randomly displayed....'''
# images
# dice is the list of the names of the image kept in same folder
dice = ['die1.png', 'die2.png', 'die3.png',
        'die4.png', 'die5.png', 'die6.png']

# simulating the dice with random numbers between
# 0 to 6 and generating image
DiceImage = ImageTk.PhotoImage(Image.open(random.choice(dice)))
# aboveLine is used to store an image of dice which is
# chosen by randomly generated numbers.
'''.....till here,.......'''

# constructing a label widget for the image
ImageLabel = tkinter.Label(root, image=DiceImage)
ImageLabel.image = DiceImage

# packing a widget in the parent widget
ImageLabel.pack(expand=True)

'''here we arrange \"pack()\" to arrange our widgets in rows
    and column form.
     \'Blackline\' label is to skip a line.
      \'HeadingLabel\' label is to give a heading'''
# root – the name by which we refer to the main window of the application
# text – text to be displayed in the HeadingLabel
# fg– the colour of the font used in HeadingLabel
# bg – background colour of the HeadingLabel
# font – used to give customised fonts to the HeadingLabel text
# .pack() – Used to pack the widget onto the root window

# function activated by button

def rolling_dice():
    DiceImage = ImageTk.PhotoImage(Image.open(random.choice(dice)))
    # update image
    ImageLabel.configure(image=DiceImage)
    # keeping a reference
    ImageLabel.image = DiceImage

# adding button, and command will use rolling_function
button = tkinter.Button(root, text='Roll the Dice', fg='blue', command=rolling_dice)
button.pack(expand=True)

# call the main loop of TK
# keeps the windows open
root.mainloop()