#Original game by HalloSpaceBoy "Minefield" PicoBoy SDK Demo

#Program Setup:
from PicoBoySDK import PicoBoySDK, PlayerObject, MusicBoxObject #This brings code for functions used in this program from the PicoBoy SDK
from random import randint #This brings the random function used for generating random numbers
from time import sleep #This brings in a function that is used for making the program wait

PicoBoy=PicoBoySDK(namespace="Minefield SDK Demo", tick_time=0) #This is the "PicoBoySDK" object. This is an object that represents the PicoBoy that allows you to control the PicoBoy's hardware
Player=PlayerObject(PicoBoy, initx=112, inity=0, width=16, height=16, sprite=PicoBoy.Load_Sprite("detector.sprt",16,16), speed=16) #This creates the "PlayerObject" Object. This is an object you can create to have a moveable player without any code
MusicBox=MusicBoxObject(PicoBoy, 1) # Initialize the MusicBox Object
MusicBox.Play_Song("Minefield Song.pbs") # Play the song file "Minefield Song.pbs"

#Declared Variables:
minesprite=PicoBoy.Load_Sprite("mine.sprt",16,16) #Set the variable minesprite to the sprite in the file "mine.sprt"
flagsprite=PicoBoy.Load_Sprite("flag.sprt",16,16) #Set the variable flagsprite to the sprite in the file "flag.sprt"
score=0 #This is the current score
enemylocations=[] #This is the list of locations of all of the mines
winlocation=() #This is the location of the win spot


#Utilized Functions:
#This is the function that creates new locations for the mines and the win spot
def new_locations():
    global enemylocations
    global winlocation
    Player.x=randint(0,14)*16 #Generates random x location for the player
    Player.y=randint(0,14)*16 #Generates random y location for the player
    enemylocations=[] #Clears out the old locations
    for number in range(45): #Opens a loop for generating locations that will loop 45 times
        while True: #Starts an infinite loop
            location=(randint(0,14)*16, randint(0,14)*16) #Generates a random location
            if not (Player.x, Player.y) == location: #Checks if the generated location is the player location
                #Generated location is not the player location
                enemylocations.append(location) #Adds randomized location to enemy list
                break #Exits the infinite loop
    while True: #Starts an infinite loop
        location=(randint(0,14)*16, randint(0,14)*16) #Generates a random location
        if not location in enemylocations and (not (location[0]+16,location[1]) in enemylocations or not (location[0]-16,location[1]) in enemylocations or not (location[0],location[1]+16) in enemylocations or not (location[0],location[1]-16) in enemylocations): #Checks if location and sides are within the enemy location list
            #Generated location is not within list
            winlocation=location #Sets randomized location to win location
            break #Exits the infinite loop

#Start Functions:
new_locations() #Generates the initial locations

#Main Game Loop:
while True:
    PicoBoy.Fill_Screen(color=(0,0,0)) #Fills the PicoBoy's Screen with the color Black
    for location in enemylocations: #Iterates through the enemy list
        PicoBoy.Render_Sprite(minesprite,location[0],location[1]) #Draws the mine sprite
        if PicoBoy.Check_Collision(x=Player.x, y=Player.y, width=Player.width, height=Player.height, x2=location[0], y2=location[1], width2=16, height2=16, speed=4, mode=1): #Checks if there is a collision between the player and the enemy
            #Player collided with enemy "Game Over"
            MusicBox.Stop_Song() #Stop the song
            PicoBoy.Play_Sound(100, 4) #Play game over sound on channel 4
            sleep(0.1)
            PicoBoy.Stop_Sound()
            sleep(0.05)
            PicoBoy.Play_Sound(100, 4)
            sleep(0.1)
            PicoBoy.Stop_Sound()
            new_locations() #Generate new locations
            PicoBoy.Save_Score(score) #Save the score to the high score leaderboard
            sleep(0.5) #Wait half a second
            while True: #Start infinite loop
                #Game Over Screen
                PicoBoy.Fill_Screen((255,0,0)) #Fill the screen with red
                PicoBoy.Create_Text("Game Over!", -1, -1, (0,0,0)) #Draws the text "Game Over"
                PicoBoy.Create_Text("Your score is "+str(score), -1, 130, (0,0,0)) #Draws the score on screen
                PicoBoy.Create_Text("Press the A button", -1, 150, (0,0,0)) #Draws the text "Press the A button to play again."
                PicoBoy.Create_Text("to play again.", -1, 160, (0,0,0)) #The text was split in two to fit the screen
                PicoBoy.Create_Text("Press start to", -1, 180, (0,0,0)) #Draws the text "Press start to view top scores."
                PicoBoy.Create_Text("view top scores.", -1, 190, (0,0,0)) #The text was split in two to fit the screen
                if PicoBoy.Button("Start"): #Check for the start button
                    PicoBoy.Show_Scores() #Display saved scores
                PicoBoy.Update() #Updates the PicoBoy. Displays the screen, checks system controls, etc.
                if PicoBoy.Button("A"): #Checks for the A button press on the PicoBoy
                    #Button was pressed
                    score=0 #Reset the score
                    sleep(0.2) # Wait .2 seconds to account for button holding
                    MusicBox.Play_Song("Minefield Song.pbs") # Play the song file "Minefield Song.pbs"
                    break #Exit the infinite loop
            break
    PicoBoy.Render_Sprite(flagsprite,winlocation[0],winlocation[1]) #Draws the win flag
    if PicoBoy.Check_Collision(x=Player.x, y=Player.y, width=Player.width, height=Player.height, x2=winlocation[0], y2=winlocation[1], width2=16, height2=16, speed=4, mode=1): #Checks if there is a collision between the player and the win spot
        score+=1 #Add one to the score
        new_locations() #Generate new locations
        MusicBox.Stop_Song() #Stop the song
        PicoBoy.Play_Sound(200, 4) #Play victory sound on channel 4
        sleep(0.1)
        PicoBoy.Stop_Sound()
        sleep(0.05)
        PicoBoy.Play_Sound(200, 4)
        sleep(0.1)
        PicoBoy.Stop_Sound()
        sleep(0.5) #Wait half a second
        while True: #Start infinite loop
            #Win Screen
            PicoBoy.Fill_Screen((0,240,0)) #Fill the screen with green
            PicoBoy.Create_Text("Level Clear!", -1, -1, (0,0,0)) #Draws the text "Level Clear"
            PicoBoy.Create_Text("Score:"+str(score), -1, 130, (0,0,0)) #Draws the score on screen
            PicoBoy.Create_Text("Press any button", -1, 150, (0,0,0)) #Draws the text "Press any button to play again."
            PicoBoy.Create_Text("to play again.", -1, 160, (0,0,0)) #The text was split in two to fit the screen
            PicoBoy.Update(score) #Updates the PicoBoy. Displays the screen, checks system controls, etc. Score is passed in to autosave if home is pressed.
            if PicoBoy.Button("Any"): #Checks for any button press on the PicoBoy
                #Button was pressed
                sleep(0.2) # Wait .2 seconds to account for button holding
                MusicBox.Play_Song("Minefield Song.pbs") # Play the song file "Minefield Song.pbs"
                break #Exit the infinite loop
    PicoBoy.Create_Text("Score: "+str(score), -1, 5, (255,255,255)) #Displays the score onscreen
    Player.Update() #Updates the player. Checks for movement, renders the player, etc.
    if PicoBoy.Button("Start"): #Check for the start button
        MusicBox.Stop_Song() #Stop the song
        PicoBoy.Pause_Screen() #Enter a pause screen
        MusicBox.Play_Song("Minefield Song.pbs") # Play the song file "Minefield Song.pbs"
    if PicoBoy.Button("Any"): #If any button is pressed
        sleep(0.1) #Wait 0.1 seconds
    PicoBoy.Update(score) #Updates the PicoBoy. Displays the screen, checks system controls, etc. Score is passed in to autosave if home is pressed.