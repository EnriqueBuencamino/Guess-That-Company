'''
Class Definitions.py
Authors: Enrique Buencamino, Aleana Abon, Franzesca De Leon, Miguel Caeg, Amiel Basilla

This file contains the definition and initialization of all the classes used in the Main File.

Notes:
This program can currently only run in windows
Errors/Issues are only due to program being split into multiple files, there are no actual errors found yet
'''

#Imports the Library Functions/Mehtods needed for an Abstract Class
from abc import ABC, abstractmethod

#Defines all the classes used in the Program
#Company Classes
class Company(ABC):
  '''Abstract Class used by all the Company Topics'''
  def __init__(self, hints):
    '''Basic Initialization Method'''
    self.hints = hints

  @abstractmethod
  def hint(self, hintIndex):
    '''Abstract Method to reveal company hints'''
    pass
  
class Food(Company):
  '''Sub Class used by the Food Companies'''
  def __init__(self, hints):
    super().__init__(hints)

  def hint(self, hintIndex):
    assert hintIndex == 2 or hintIndex == 3 or hintIndex == 1, 'Incorrect Index'

    global logoImage
    if hintIndex == 1:
      logoImage = tk.PhotoImage(file = Guess.hints[1])
      logo = tk.Label(root, image = logoImage,  bg = '#ADABAB')
      logo.place(relx = 0.16, rely = 0.08 , anchor = 'nw')

    if hintIndex == 2:
      companyColor = tk.Label(root,
                              text=("This company's colors are " + Guess.hints[2]),
                              font=('Bookman Old Style', 26),
                              wraplength=500,
                              fg = '#FFECD9',
                              bg='#302532')
      companyColor.place(relx=0.93, rely=0.08, anchor='ne')

    elif hintIndex == 3:
      companyPurpose = tk.Label(root,
                                text=("This company " + Guess.hints[3]),
                                font=('Bookman Old Style', 20),
                                wraplength=500,
                                fg = '#FFECD9',
                                bg='#302532')
      companyPurpose.place(relx=0.93, rely=0.52, anchor='ne')

class Technology(Company):
  '''Sub Class used by the Technologies Companies'''
  def __init__(self, hints):
    super().__init__(hints)

  def hint(self, hintIndex):
    assert hintIndex == 2 or hintIndex == 3 or hintIndex == 1, 'Incorrect Index'

    global logoImage
    if hintIndex == 1:
      logoImage = tk.PhotoImage(file = Guess.hints[1])
      logo = tk.Label(root, image = logoImage,  bg = '#ADABAB')
      logo.place(relx = 0.16, rely = 0.08 , anchor = 'nw')

    if hintIndex == 2:
      companyColor = tk.Label(root,
                              text=("This company's colors are " + Guess.hints[2]),
                              font=('Bookman Old Style', 26),
                              wraplength=500,
                              fg = '#FFECD9',
                              bg='#302532')
      companyColor.place(relx=0.93, rely=0.08, anchor='ne')

    elif hintIndex == 3:
      companyPurpose = tk.Label(root,
                                text=("This company " + Guess.hints[3]),
                                font=('Bookman Old Style', 20),
                                wraplength=500,
                                fg = '#FFECD9',
                                bg='#302532')
      companyPurpose.place(relx=0.93, rely=0.52, anchor='ne')


class Clothing(Company):
  '''Sub Class used by the Clothing Companies'''
  def __init__(self, hints):
    super().__init__(hints)

  def hint(self, hintIndex):
    assert hintIndex == 2 or hintIndex == 3 or hintIndex == 1, 'Incorrect Index'

    global logoImage
    if hintIndex == 1:
      logoImage = tk.PhotoImage(file = Guess.hints[1])
      logo = tk.Label(root, image = logoImage,  bg = '#ADABAB')
      logo.place(relx = 0.16, rely = 0.08 , anchor = 'nw')

    if hintIndex == 2:
      companyColor = tk.Label(root,
                              text=("This company's colors are " + Guess.hints[2]),
                              font=('Bookman Old Style', 26),
                              wraplength=500,
                              fg = '#FFECD9',
                              bg='#302532')
      companyColor.place(relx=0.93, rely=0.08, anchor='ne')

    elif hintIndex == 3:
      companyPurpose = tk.Label(root,
                                text=("This company " + Guess.hints[3]),
                                font=('Bookman Old Style', 20),
                                wraplength=500,
                                fg = '#FFECD9',
                                bg='#302532')
      companyPurpose.place(relx=0.93, rely=0.52, anchor='ne')


class Automobile(Company):
  '''Sub Class used by the Automobile Companies'''
  def __init__(self, hints):
    super().__init__(hints)

  def hint(self, hintIndex):
    assert hintIndex == 2 or hintIndex == 3 or hintIndex == 1, 'Incorrect Index'

    global logoImage
    if hintIndex == 1:
      logoImage = tk.PhotoImage(file = Guess.hints[1])
      logo = tk.Label(root, image = logoImage,  bg = '#ADABAB')
      logo.place(relx = 0.16, rely = 0.08 , anchor = 'nw')

    if hintIndex == 2:
      companyColor = tk.Label(root,
                              text=("This company's colors are " + Guess.hints[2]),
                              font=('Bookman Old Style', 26),
                              wraplength=500,
                              fg = '#FFECD9',
                              bg='#302532')
      companyColor.place(relx=0.93, rely=0.08, anchor='ne')

    elif hintIndex == 3:
      companyPurpose = tk.Label(root,
                                text=("This company " + Guess.hints[3]),
                                font=('Bookman Old Style', 20),
                                wraplength=500,
                                fg = '#FFECD9',
                                bg='#302532')
      companyPurpose.place(relx=0.93, rely=0.52, anchor='ne')

class Medicine(Company):
  '''Sub Class used by the Medicine Companies'''
  def __init__(self, hints):
    super().__init__(hints)

  def hint(self, hintIndex):
    assert hintIndex == 2 or hintIndex == 3 or hintIndex == 1, 'Incorrect Index'

    global logoImage
    if hintIndex == 1:
      logoImage = tk.PhotoImage(file = Guess.hints[1])
      logo = tk.Label(root, image = logoImage,  bg = '#ADABAB')
      logo.place(relx = 0.16, rely = 0.08 , anchor = 'nw')

    if hintIndex == 2:
      companyColor = tk.Label(root,
                              text=("This company's colors are " + Guess.hints[2]),
                              font=('Bookman Old Style', 26),
                              wraplength=500,
                              fg = '#FFECD9',
                              bg='#302532')
      companyColor.place(relx=0.93, rely=0.08, anchor='ne')

    elif hintIndex == 3:
      companyPurpose = tk.Label(root,
                                text=("This company " + Guess.hints[3]),
                                font=('Bookman Old Style', 20),
                                wraplength=500,
                                fg = '#FFECD9',
                                bg='#302532')
      companyPurpose.place(relx=0.93, rely=0.52, anchor='ne')


class Personal_Care(Company):
  '''Sub Class used by the Personal Care Companies'''
  def __init__(self, hints):
    super().__init__(hints)

  def hint(self, hintIndex):
    assert hintIndex == 2 or hintIndex == 3 or hintIndex == 1, 'Incorrect Index'

    global logoImage
    if hintIndex == 1:
      logoImage = tk.PhotoImage(file = Guess.hints[1])
      logo = tk.Label(root, image = logoImage,  bg = '#ADABAB')
      logo.place(relx = 0.16, rely = 0.08 , anchor = 'nw')

    if hintIndex == 2:
      companyColor = tk.Label(root,
                              text=("This company's colors are " + Guess.hints[2]),
                              font=('Bookman Old Style', 26),
                              wraplength=500,
                              fg = '#FFECD9',
                              bg='#302532')
      companyColor.place(relx=0.93, rely=0.08, anchor='ne')

    elif hintIndex == 3:
      companyPurpose = tk.Label(root,
                                text=("This company " + Guess.hints[3]),
                                font=('Bookman Old Style', 20),
                                wraplength=500,
                                fg = '#FFECD9',
                                bg='#302532')
      companyPurpose.place(relx=0.93, rely=0.52, anchor='ne')

#Text Classes
class StoryLine(ABC):
  '''Abstract Class used by all the Text Classes'''
  def __init__(self, text):
    '''Basic Initializtion Method'''
    self.text = text

  @abstractmethod
  def displayText(self):
    '''Abstract Method which displays corresponding text'''
    pass

class Story(StoryLine):
  '''Sub Class used by the Story Texts'''
  def __init__(self, text):
    self.text = text

  def displayText(self, storyNumber, Image):
    storyNumber = tk.Label(root, text = self.text, font =("Courier", 12), fg = '#FFECD9', bg = '#302532')
    storyNumber.place(relx = 0.95, rely = 0.45, anchor = 'e')

    global artImage
    artImage = tk.PhotoImage(file = Images[Image])
    art = tk.Label(root, image = artImage, bg = '#452A49')
    art.place(relx = 0.2, rely = 0.45 , anchor = 'center')

class Title(StoryLine):
  '''Sub Class used by the Title Screen'''
  def __init__(self, text):
    self.text = text

  def displayText(self):
    Title = tk.Label(root, text = self.text, font = ("Dark Magic", 72), fg = '#FFECD9', bg = '#302532')
    Title.place(relx = 0.5, rely = 0.35, anchor = 'center')

    button = tk.Button(root, text = 'begin?', font=("Dark Magic", 32), bg='#452A49', fg = '#FFECD9', relief = 'sunken', 
                       activebackground = '#452A49', borderwidth = 0, command = storyScreen)
    button.place(relx = 0.5, rely = 0.67, anchor = 'center')

class Ending(StoryLine):
  '''Sub Class used by the Ending Texts'''
  def __init__(self, text):
    self.text = text

  def displayText(self, result):
    winStory = tk.Label(root, text = self.text, font =("Courier", 12), fg = '#FFECD9', bg = '#302532')
    winStory.place(relx = 0.3, rely = 0.5, anchor = 'center')

    winScreen = tk.Label(root, text = result, font = ('Dark Magic', 56), fg = '#FFECD9', bg = '#302532')
    winScreen.place(relx = 0.79, rely = 0.4, anchor = 'center')
  
#LifeSystem Class
class LifeSystem():
  '''Class for the Life System'''
  def __init__(self, healthPoints = 10, failCount = 0):
    self.healthPoints = healthPoints
    self.failCount = failCount

  def lifebar(self):
    '''Method that initializes the Health Bar'''
    global healthBar
    healthBar =  '\u2588' * self.healthPoints
    return healthBar

  def wrongAnswer(self):
    '''Method that adjusts lifebar and information whenever a wrong answer is given'''
    self.failCount += 1 
    self.healthPoints -= 2
    giveHint(self.failCount)
    self.lifebar()

  def reset(self):
    '''Method that resets the Life System variables to allow replayability'''
    self.healthPoints = 10
    self.failCount = 0