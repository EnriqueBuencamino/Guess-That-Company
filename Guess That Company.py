'''
Guess The Company LT10.py
Authors: Enrique Buencamino, Aleana Abon, Franzesca De Leon, Miguel Caeg, Amiel Basilla

This is the Main File of the program, which runs the actual game using information from the other two files

Notes:
This program can currently only run in windows
Please use Python 11.5 or lower to run latest Pygame (as of time of writing)
It is needed to have Pygame AND Numpy installed in computer for program to run
"Dark Magic" font may only work if your laptop has it installed, will default to Arial if it isn't
Errors/Issues are only due to program being split into multiple files, there are no actual errors found yet
'''

#imports all of the libraries used by the functions
import tkinter as tk
import numpy as np
import pygame

#Executes the Info.py file, containing all the text and company info
with open("Company Info.py", encoding="utf-8") as f:
    exec(f.read())

#Initializes all the functions
def giveHint(failCount):
  '''
  Function used when given a wrong answer (failCount).
  Displays new hints for the player if they answer incorrectly
  '''

  if failCount == 1:
    Guess.hint(2)
  elif failCount == 2:
    companyLength = tk.Label(root, text = ('This company has ' + str(len(Guess.hints[0])) + ' characters in its name.'), 
                             font = ('Bookman Old Style', 26), wraplength = 500, fg = '#FFECD9', bg = '#302532')
    companyLength.place(relx = 0.93, rely = 0.30, anchor = 'ne')
  elif failCount == 3:
    Guess.hint(3)

    #shifts music
    laugh = pygame.mixer.Sound('Sound Effects\Evil Laugh.mp3')
    laugh.set_volume(0.5)
    pygame.mixer.Channel(1).play(laugh)

    pygame.mixer_music.load('Sound Effects\Last Chance.mp3')
    pygame.mixer_music.play(loops=-1)
    pygame.mixer_music.set_volume(0.6)
  elif failCount == 4:
    #Company Name Part
    #Drills a random part of the company's name then prints it
    partLength = 0
    while partLength not in limits:
      x = np.random.randint(0, len(Guess.hints[0]) - 1)
      y = np.random.randint(x + 1, len(Guess.hints[0]))
      partLength = x + y

    companyPart = tk.Label(root, text = ("Part of the company's name is '" + Guess.hints[0][x:y] + "'"),
                            font = ('Bookman Old Style', 26), wraplength = 500, fg = '#FFECD9', bg = '#302532')
    companyPart.place(relx = 0.93, rely = 0.74, anchor = 'ne')

  else:
    return
  
def clearScreen():
    '''Clears Root window by destroying all currents widgets within it'''

    for widget in root.winfo_children():
      widget.destroy() 

def titleScreen(): 
    '''Function that displays the Title Screen'''
    clearScreen()
    #plays background music
    pygame.mixer_music.load('Sound Effects\Title Music.mp3')
    pygame.mixer_music.play(loops = -1)
    pygame.mixer_music.set_volume(0.6)

    titleText.displayText()

def storyScreen(): 
    '''Function that displays the Story Screen'''
    
    global textCheck
    textCheck = 0
    def textMove():
      '''Function that cycles the text in the Story Screen'''
      global textCheck
      textCheck += 1
      clearScreen()
      continueButton = tk.Button(root, text = '-->' , font =("Courier", 20), fg = '#FFECD9', bg = '#302532',
                                relief = 'sunken', activebackground = '#452A49', borderwidth = 0, 
                               command = textMove)
      continueButton.place(relx = 0.9, rely = 0.8, anchor = 'e')

      if textCheck == 1:
          textTwo.displayText('StoryTwo', 1)
          halt = pygame.mixer.Sound('Sound Effects\Halt!.mp3')
          halt.set_volume(0.7)
          pygame.mixer.Channel(1).play(halt)
          return
      if textCheck == 2:
          textThree.displayText('StoryThree', 2)
      if textCheck == 3:
          textFour.displayText('StoryFour', 2)
          continueButton.destroy()      

          #Topic Choice Buttons
          Food = tk.Button(root, text = 'Food' , font =('Bookman Old Style', 16), fg = '#FFECD9', bg = '#302532',
                              relief = 'sunken', activebackground = '#452A49', borderwidth = 0, 
                              command = FoodSet)
          Food.place(relx = 0.59, rely = 0.5, anchor = 'e')

          Technology = tk.Button(root, text = 'Technology' , font =('Bookman Old Style', 16), fg = '#FFECD9', bg = '#302532',
                              relief = 'sunken', activebackground = '#452A49', borderwidth = 0, 
                              command = TechSet)
          Technology.place(relx = 0.76, rely = 0.5, anchor = 'e')

          Clothing = tk.Button(root, text = 'Clothing' , font =('Bookman Old Style', 16), fg = '#FFECD9', bg = '#302532',
                              relief = 'sunken', activebackground = '#452A49', borderwidth = 0, 
                              command = ClothSet)
          Clothing.place(relx = 0.89, rely = 0.5, anchor = 'e')

          Automobile = tk.Button(root, text = 'Automobile' , font =('Bookman Old Style', 16), fg = '#FFECD9', bg = '#302532',
                              relief = 'sunken', activebackground = '#452A49', borderwidth = 0, 
                              command = CarSet)
          Automobile.place(relx = 0.68, rely = 0.58, anchor = 'e')

          Medicine = tk.Button(root, text = 'Medicine' , font =('Bookman Old Style', 16), fg = '#FFECD9', bg = '#302532',
                              relief = 'sunken', activebackground = '#452A49', borderwidth = 0, 
                              command = MedSet)
          Medicine.place(relx = 0.83, rely = 0.58, anchor = 'e')

          Personal_Care = tk.Button(root, text = 'Personal Care' , font =('Bookman Old Style', 16), fg = '#FFECD9', bg = '#302532',
                              relief = 'sunken', activebackground = '#452A49', borderwidth = 0, 
                              command = CareSet)
          Personal_Care.place(relx = 0.77, rely = 0.65, anchor = 'e')

    clearScreen()
    #plays background music
    pygame.mixer_music.load('Sound Effects\BGM.mp3')
    pygame.mixer_music.play(loops = -1)
    pygame.mixer_music.set_volume(0.6)

    textOne.displayText('StoryOne', 0)

    continueButton = tk.Button(root, text = '-->' , font =("Courier", 20), fg = '#FFECD9', bg = '#302532',
                                relief = 'sunken', activebackground = '#452A49', borderwidth = 0, 
                               command = textMove)
    continueButton.place(relx = 0.9, rely = 0.8, anchor = 'e')

#Functions that initialize the topic game loops
def FoodSet():
    '''Chooses a company from the Food topic list and sets corresponding limits'''
    clearScreen()
    global Guess
    Guess = ' '
    Guess = np.random.choice(FoodCompany)
    global limits
    limits = [1,2,3]
    gameScreen(Guess)

def TechSet():
    '''Chooses a company from the Technology topic list and sets corresponding limits'''
    clearScreen()
    global Guess
    Guess = ' '
    Guess = np.random.choice(TechnologyCompany)
    global limits
    limits = [1,2]
    gameScreen(Guess)

def ClothSet():
    '''Chooses a company from the Clothing topic list and sets corresponding limits'''
    clearScreen()
    global Guess
    Guess = ' '
    Guess = np.random.choice(ClothingCompany)
    global limits
    limits = [1,2]
    gameScreen(Guess)

def CarSet():
    '''Chooses a company from the Automobile topic list and sets corresponding limits'''
    clearScreen()
    global Guess
    Guess = ' '
    Guess = np.random.choice(AutomobileCompany)
    global limits
    limits = [1,2]
    gameScreen(Guess)

def MedSet():
    '''Chooses a company from the Medicine topic list and sets corresponding limits'''
    clearScreen()
    global Guess
    Guess = ' '
    Guess = np.random.choice(MedicineCompany)
    global limits
    limits = [2,3,4]
    gameScreen(Guess)

def CareSet():
    '''Chooses a company from the Personal Care topic list and sets corresponding limits'''
    clearScreen()
    global Guess
    Guess = ' '
    Guess = np.random.choice(PersonalCareCompany)
    global limits
    limits = [2,3,4]
    gameScreen(Guess)

def gameScreen(Guess):
    '''Function that shows the Game Screen which acts as the primary game loop'''

    def answerCheck():
      '''Function that checks if User input matches the correct Answer'''
      global failCount, healthPoints
      answer = userAnswer.get()
      if answer.upper() == Guess.hints[0].upper(): #if player gets the right answer
          clearScreen()   

          pygame.mixer_music.load('Sound Effects\Farewell.mp3')
          pygame.mixer_music.play(loops = -1)
          pygame.mixer_music.set_volume(0.6)
          door = pygame.mixer.Sound('Sound Effects\Door Opens.mp3')
          door.set_volume(0.5)
          pygame.mixer.Channel(1).play(door)

          #resets life system
          life.reset()
          textWin.displayText('YOU WIN')

          #buttons to either return to Title Screen or move to Story Screen
          Return = tk.Button(root, text = 'Exit' , font =('Bookman Old Style', 24), fg = '#FFECD9', bg = '#302532',
                              relief = 'sunken', activebackground = '#452A49', borderwidth = 0, 
                              command = titleScreen)
          Return.place(relx = 0.68, rely = 0.65, anchor = 'center')
      
          tryAgain = tk.Button(root, text = 'Try Again?' , font =('Bookman Old Style', 24), fg = '#FFECD9', bg = '#302532',
                              relief = 'sunken', activebackground = '#452A49', borderwidth = 0, 
                              command = storyScreen)
          tryAgain.place(relx = 0.88, rely = 0.65, anchor = 'center')

      elif life.failCount == 4: #if player loses the game
          clearScreen()
          pygame.mixer_music.unload()
          died = pygame.mixer.Sound('Sound Effects\You Died.mp3')
          died.set_volume(1)
          pygame.mixer.Channel(1).play(died)

          #resets global variables for replay
          life.reset()
          textLose.displayText('YOU LOSE')

          #buttons to either return to Title Screen or move to Story Screen
          Return = tk.Button(root, text = 'Exit' , font =('Bookman Old Style', 24), fg = '#FFECD9', bg = '#302532',
                              relief = 'sunken', activebackground = '#452A49', borderwidth = 0, 
                              command = titleScreen)
          Return.place(relx = 0.68, rely = 0.65, anchor = 'center')
      
          tryAgain = tk.Button(root, text = 'Try Again?' , font =('Bookman Old Style', 24), fg = '#FFECD9', bg = '#302532',
                              relief = 'sunken', activebackground = '#452A49', borderwidth = 0, 
                              command = storyScreen)
          tryAgain.place(relx = 0.88, rely = 0.65, anchor = 'center')

      else: #if player gave wrong answer but still has life left
          hurt = pygame.mixer.Sound('Sound Effects\Got Hurt.mp3')
          hurt.set_volume(1.5)
          pygame.mixer.Channel(2).play(hurt)
          life.wrongAnswer()
          lifeLeft.configure(text = ('Life: ' + healthBar))

    Guess.hint(1) #initializes the Company Logo

    #Sets up the Health Bar
    life.lifebar()
    lifeLeft = tk.Label(root, text = ('Life: ' + healthBar), font = ('Dark Magic', 28), fg = '#FFECD9', bg = '#302532')
    lifeLeft.place(relx = 0.10, rely = 0.62 , anchor = 'nw')

    #Sets up the input box for the player's guess
    Answer = tk.StringVar()
    Answer.set('')

    userAnswer = tk.Entry(root, font = ('Bookman Old Style', 32), fg = '#FFECD9', bg = '#302532', textvariable = Answer)
    userAnswer.place(relx = 0.08, rely = 0.77 , anchor = 'nw')

    submitAnswer = tk.Button(root, text = 'submit', font = ('Bookman Old Style', 20), fg = '#FFECD9', bg = '#302532',
                            relief = 'sunken', activebackground = '#452A49', borderwidth = 0, command = answerCheck)
    submitAnswer.place(relx = 0.25, rely = 0.85, anchor = 'nw')

#setting up the window proper and begin game
root = tk.Tk()
root.state('zoomed') 
root.title('Guess That Company')
root.configure(bg = '#452A49')
root.resizable(width=False, height=False)
pygame.mixer.init()

titleScreen()

root.mainloop()
