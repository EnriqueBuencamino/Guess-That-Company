'''
Company Info.py
Authors: Enrique Buencamino, Aleana Abon, Franzesca De Leon, Miguel Caeg, Amiel Basilla

This file is the compilation of all the class instances and their appropriate information.
This includes texts, images, and company names and information.

Notes:
This program can currently only run in windows
Errors/Issues are only due to program being split into multiple files, there are no actual errors found yet
'''

#Executes the Class Definitions.py file to be used by the instances below
with open("Class Definitions.py") as f:
    exec(f.read())

#Initializes all the Company Information
#Food Companies
Nestle = Food([
    "Nestle", 'Company Logos/1.png', "Black and White",
    "This company's purpose is to enhance quality of life for all, now and for generations to come."])

Mcdonalds = Food([
    "McDonalds", 'Company Logos/2.png', "Red and Yellow",
    "This company's purpose is to feed and foster communities."])

Unilever = Food([
    "Unilever", 'Company Logos/3.png', "White and Blue",
    "This company's purpose is to make sustainable living commonplace."])

CocaCola = Food([
    "Coca-Cola", 'Company Logos/4.png', "White and Red",
    "This company's purpose is to refresh the world and make a difference."])

KraftHeinz = Food([
    "Kraft Heinz", 'Company Logos/5.png', "White, Blue, and Red",
    "This company's purpose is to provide consumers with products they know, love, and trust."])

Jollibee = Food([
    "Jollibee", 'Company Logos/6.png', "Red and White",
    "This company's purpose is to serve great-tasting food, bringing the joy of eating to everyone."])

FoodCompany = [Nestle, Mcdonalds, Unilever, CocaCola, KraftHeinz, Jollibee]

#Technology Companies
Apple = Technology([
    "Apple", 'Company Logos/7.png', "White and Black",
    "This company's purpose is to create technology that empowers people and enriches their lives."])

Microsoft = Technology([
    "Microsoft", 'Company Logos/8.png', "Orange, Green, Blue, and Yellow",
    "This company's purpose is to create technology that transforms the way people work, play, and communicate."])

Google = Technology([
    "Google", 'Company Logos/9.png', "Blue, Red, Yellow, and Green",
    "This company's purpose is to organize the world's information and make it universally accessible and useful."])

Lazada = Technology([
    "Lazada", 'Company Logos/10.png', "Orange, Blue, and Pink",
    "This company's purpose is to connect consumers to brands and create customized experiences for customers."])

ABSCBN = Technology([
    "ABS-CBN Corporation", 'Company Logos/11.png',
    "Red, Green, Blue, and Black",
    "This company's purpose is to inform, educate, and entertain through creative content for any platform."])

PLDT = Technology([
    "PLDT", 'Company Logos/12.png', "Red and White",
    "This company's purpose is to provide telecommunications and digital services across the wireless networks."])

TechnologyCompany = [Apple, Microsoft, Google, Lazada, ABSCBN, PLDT]

#Clothing Companies
Zara = Clothing([
    "Zara", 'Company Logos/13.png', "Black",
    "This company's purpose is to give customers what they want, and get it to them faster than anyone else."])

HM = Clothing([
    "H&M", 'Company Logos/14.png', "Red",
    "This company's purpose is to make fashion accessible and enjoyable for all."])

Kamiseta = Clothing([
    "Kamiseta", 'Company Logos/15.png', "Black",
    "This company's purpose is to give Kamiseta girls all over the world access to world-class products."])

Uniqlo = Clothing([
    "Uniqlo", 'Company Logos/16.png', "Red and White",
    "This company's purpose is to make clothing that innovate and bring warmth, lightness, and comfort ."])

Adidas = Clothing([
    "Adidas", 'Company Logos/17.png', "Black",
    "This company's purpose is to be the best sports brand in the world."])

Nike = Clothing([
    "Nike", 'Company Logos/18.png', "Black",
    "This company's purpose is to bring inspiration and innovation to every athlete in the world."])

ClothingCompany = [Zara, HM, Kamiseta, Uniqlo, Adidas, Nike]

#Automobile Companies
Toyota = Automobile([
    "Toyota", 'Company Logos/19.png', "White",
    "This company's purpose is to make ever-better cars, to build a future where all have the freedom to move."])

Honda = Automobile([
    "Honda", 'Company Logos/20.png', "Black",
    "This company's purpose is to put safe, efficient, and eco-friendly technology at the service of everyone."])

Tesla = Automobile([
    "Tesla", 'Company Logos/21.png', "Red",
    "This company's purpose is to hasten the move to sustainability with electric vehicles and renewable energy."])

Mercedes_Benz = Automobile([
    "Mercedes-Benz", 'Company Logos/22.png', "Silver",
    "This company's purpose is to build the most desirable cars in the world."])

Ford = Automobile([
    "Ford", 'Company Logos/23.png', "Blue and White",
    "This company's purpose is to build a better world, where all are free to move and pursue their dreams."])

Nissan = Automobile([
    "Nissan", 'Company Logos/24.png', "Black",
    "This company's purpose is to make innovative automotive products that delivers superior value to all."])

AutomobileCompany = [Toyota, Honda, Tesla, Mercedes_Benz, Ford, Nissan]

#Medicine Companies
Pfizer = Medicine([
    "Pfizer", 'Company Logos/25.png', "Blue",
    "This company's purpose is to deliver breakthroughs that change patients' lives."])

JJ = Medicine([
    "Johnson & Johnson", 'Company Logos/26.png', "Red",
    "This company's purpose is to build a world where complex diseases are treated and cured."])

Mercury_Drug = Medicine([
    "Mercury Drug", 'Company Logos/27.png', "Red and White",
    "This company's purpose is to provide the widest range of medicines, with care products and basic needs."])

AstraZeneca = Medicine([
    "AstraZeneca", 'Company Logos/28.png', "Purple and Yellow",
    "This company's purpose is to help people with rare diseases through innovative medicines, and healthcare."])

Unilab = Medicine([
    "Unilab", 'Company Logos/29.png', "Blue and White",
    "This company's purpose is to work towards a healthier Philippines, one quality medicine at a time."])

Interphil_Lab = Medicine([
    "Interphil Laboratories", 'Company Logos/30.png', "Red and White",
    "This company's purpose is to make pharmaceuticals, supplements, and cosmetics throughout Southeast Asia."])

MedicineCompany = [Pfizer, JJ, Mercury_Drug, AstraZeneca, Unilab, Interphil_Lab]

#Personal Care Companies
Colgate = Personal_Care([
    "Colgate", 'Company Logos/31.png', "Red and White",
    "This company's purpose is to provide hygiene products to enable family well-being and cleaner living."])

Shiseido = Personal_Care([
    "Shiseido", 'Company Logos/32.png', "White and Red",
    "This company's purpose is to strive to create a better, more sustainable world for all."])

Loreal = Personal_Care([
    "L'Oreal", 'Company Logos/33.png', "Black and White",
    "This company's purpose is to offer every person products to satisfy all beauty needs and desires."])

PersonalCareCompany = [Colgate, Shiseido, Loreal]

#Initializes all the text blocks and Title Screen
#Story Text
textOne = Story("""
    __| |___________________________________________________| |__
    (__   ___________________________________________________   __)
    | |                                                   | |
    | |                                                   | |
    | |                                                   | |
    | |                                                   | |
    | |     The wealthiest businessman in the land had    | |
    | | just passed away after the slow downfall of his   | |
    | | company due to its "unrecognizable" logo. His last| |
    | | speech to the public was about the importance of  | |
    | | businesses logos. "Stunning business logos draw   | |
    | | the attention of consumers!" and "A great business| |
    | | logo has the magical power to make customers      | |
    | | recognize your brand!" wera things he passionately| |
    | | preached to the public.                           | |
    | |                                                   | |
    | |                                                   | |
    | |                                                   | |
    | |                                                   | |
    __| |___________________________________________________| |__
    (__   ___________________________________________________   __)
    | |                                                   | |""")

textTwo = Story("""
    __| |___________________________________________________| |__
    (__   ___________________________________________________   __)
    | |                                                   | |
    | |      Soon after his death, news reports came out  | |
    | | saying that he hid his hard-earned treasures on a | |
    | | notorious mountain called Mt. A.I.M., A tall      | |
    | | mountain known for its treacherous lands,         | |
    | | ferocious beasts, and cruel terrain. However this | |
    | | didn't stop you and thousands of other explorers  | |
    | | from finding the great treasure. Fortunately, you | |
    | | found a map that guides you safely to the treasure| |
    | | at the bottom of the trail, ending up in front of | |
    | | a hidden gate after a long hike.                  | |
    | |                                                   | |
    | |      “Halt intruder!”                             | |
    | |                                                   | |
    | |      Suddenly, a mysterious figure holding a      | |
    | | strange weapon greets you with hostility.         | |
    | |                                                   | |
    __| |___________________________________________________| |__
    (__   ___________________________________________________   __)
     | |                                                   | | """)

textThree = Story("""
    __| |___________________________________________________| |__
    (__   ___________________________________________________   __)
    | |                                                   | |
    | |      “I am the wizard who guards the entrance of  | |
    | | this businessman's wealth. I cannot allow any     | |
    | | mortal man to enter lest you answer me these      | |
    | | questions three, 'ere the other side he sees.”    | |
    | |                                                   | |
    | |      “Ask your questions, I am not afraid!”       | |
    | |                                                   | |
    | |      You tell the wizard as your legs tremble and | |
    | | your teeth chatter.                               | |
    | |                                                   | |
    | |      “Name thy company using only the hints I     | |
    | | giveth. A hint is provided  for every wrong guess | |
    | | one shalt give thee. Fail to give the right answer| |
    | | five times, the consequences shall be grave! I    | |
    | | shall wipe your memory with my magic weapon and   | |
    | | transport you back to the bottom of the trail!”   | |
    __| |___________________________________________________| |__
    (__   ___________________________________________________   __)
    | |                                                   | |""")

textFour = Story("""
    __| |___________________________________________________| |__
    (__   ___________________________________________________   __)
    | |                                                   | |
    | |     Suddenly, a voice from the heavens whispers   | |
    | | into your ear.                                    | |
    | |                                                   | |
    | |                                                   | |
    | |                                                   | |
    | |                 “CHOOSE A TOPIC!"                 | |
    | |                                                   | |
    | |                                                   | |
    | |                                                   | |
    | |                                                   | |
    | |                                                   | |
    | |                                                   | |
    | |                                                   | |
    | |                                                   | |
    | |                                                   | |
    | |                                                   | |
    | |                                                   | |
    __| |___________________________________________________| |__
    (__   ___________________________________________________   __)
    | |                                                   | |""")

#List Containing all the Image Assets
global Images
Images = [r'Guess That Company Game Assets\IMG_0371.png', r'Guess That Company Game Assets\IMG_0372.png'
          , r'Guess That Company Game Assets\Untitled19_20231201003952.png']

#Ending Texts
textLose = Ending("""
    __| |___________________________________________________| |__
    (__   ___________________________________________________   __)
    | |                                                   | |
    | |    The wizard starts to grin maliciously as he    | |
    | | raises his wand, the last words you hear are:     | |
    | |                                                   | |
       | |                                                   | |   
    | |    “Foolish advneturer, you are wrong! Perhaps    | |
    | | the next person shall fare better."               | |
    | |                                                   | |
    __| |___________________________________________________| |__
    (__   ___________________________________________________   __)
    | |                                                   | |
    """)

textWin = Ending("""
    __| |___________________________________________________| |__
    (__   ___________________________________________________   __)
    | |                                                   | |
    | |     The wizard laughs as the door slowly begins to| |
    | | open.                                             | |
    | |                                                   | |
    | |                                                   | |
     | |     “Well done traveler! You are truly a master   | | 
         | | of the logos, worthy to possess my treasure.      | |     
    | |                                                   | |
    __| |___________________________________________________| |__
    (__   ___________________________________________________   __)
    | |                                                   | |
    """)

#Title Text
titleText = Title('GUESS THAT\n COMPANY')

#Initializes the Lifesystem
life = LifeSystem()