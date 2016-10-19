import time
import player
from game import end
dragon = [
"################################################################ ###################################",
"#############################################################W D####################################",
"############################################################   #####################################",
"###############################################j##########  #  #####################################",
"########################################:  #### ########f ,##  #####################################",
"#######################################  ###### #######  W###  #####################################",
"######################################  ####### ######  #####  #####################################",
"#####################################  .######  ####K  ######i #####################################",
"################### #########G   j##,  ######   ###j t########  #####E f############################",
"##################  ########     ##K   #####,  ###; L##########     ################################",
"##################   ##Ej    ##        ####    ##; f##########t  j##################################",
"#################              #        #f    ##E .#########   # ###################################",
"################                             ###  ########j  W## ###################################",
"################                            ###  ########  ,#### ###################################",
"#################      #####.             W###  #######,  ###### ###################################",
"#################    ####   ##          #####f t######   #######  ##################################",
"#################: E##L       .#    #   #####  ######  #########W W##########W######################",
"################## ##   K####. #    ;    ###  ######  ###########j ;##   E##########################",
"################### i :########:    L    ###  #####  #############    ##############################",
"###################t # ####:        #    ##  #####  ###########      ###############################",
"##################  ###           .#     ##  ###G  #########.   ### ,###############################",
"###############.  ####t      ####D       #  ###W  ########   t##### W###############################",
"##############D#######     ######        #  ###  #######   D####### ################################",
"####################### ########   #    #  ##   #####   ########### E###############################",
"####################### #######         #  #;  ####  .#############  ###############################",
"########################W#####         W#     t###  .##############W ###############################",
"###############################        #K     ##   #################j ##############################",
"############################    j      #      ,   ######;                 K#########################",
"###########################           ##   D:    ##L       f#########:.#############################",
"##########################            ##  ###:       :############### ##############################",
"##########################            ## W# ##    ################## ###############################",
"#########################   DD        ####  ##  ###################,;###############################",
"########################                    #    ################## ################################",
"### .##################                    ##      :############## W##########K#####################",
"#j##   ## ############W                   ##j           ########## ########### #####################",
"#####   # ############                 #####  W####L          D## f##########; #####################",
"#####D  # E###########W##f;,          ####:   ###############f:       #######  #####################",
"######K   ###########W                 ##i                      ###########W  ######################",
"####  #    ##########                   K#################################    ######################",
"###        ##########                         .                      ###     ### ;##################",
"## ###     #########f                                                       j    ###################",
"######    ##########E   ##t                                                     W###################",
"#######    ######   #                                                             ##################",
"##########  ###t    ;                                                            ###################",
"##########.          W                                  ,##GE##                  ###################",
"##########   E       #     ,#                          EG      #E                 ##################",
"##########  ,##D      #   #                            #        #     #           ##################",
"#########    ####     ###:                            #          #   ###t          #################",
"#########;  W#####.  ####                             #          #   ####E         #################",
"##########  #######  ##### .                      jt  #          #  ######         #################",
"##########  ####### #######j                   ##.   ##          Wf########        #################",
"########## ######## #######           t       #      ##          ##########;       #################",
"#########t########W########           K     #K      ####         ###########       #################",
"###########################W         #    ###       #####        ###########       #################",
"############################        :#L######       ######       ###########      ##################",
"############################       ###########t     #######      j### #####       ##################",
"############################    :#############G      #######W         #####       ##################",
"###########################f   ###############         f######      i######       ##################",
"###########################   G##############   ,###############    ######:       ##################",
"###########################E  ##############  ##################W   D#####        ##################",
"############################  ############## ####################    #####         L################",
"###########################j E#############  #####################  G#####            ##############",
"###########################  ##############. E####################  #######              ###########",
"##################### ####   ########jE#W     Di##################  ## ######              ;########",
"###################           ######j           #############K ###      ii######              ######",
"################## ##         f####f      ###:  ############           L###########K           .####",
"########################    .  #### #L#   ####  ###########  #      E##################          ###",
"#####################   #:   ######K#    i#####################   D  #######################       #",
"####################  ####  #########  f#######################  ##. ########################      K",
"#################### ##### ########################, D########  :##D #########################      ",
"####################j#### ##########L############   ########## #####Df########################:     ",
"######################### ###########L#########    ###########f################################     ",
"##############################################    j###########K################################     ",
"############################################f     ########EE##################################      ",
"###########################################      W#                   j#######################      ",
"##########################################      #      jEEE;                 W###############      t",
"#########################################     #   ################                  iE###D         #",
"########################################    D   j#####################.                           E#",
"######################################        #G##########################                       :##",
"####################################              fWEi  #####################G                  G###",
"############################j                         W##########################             .#####",
"##############################                      ;################################,     .########",
"################################W                 ##################################################",
"######################################D;. ,tE#######################################################",
"####################################################################################################"]
welcome = [
" __     __     ______     __         ______     ______     __    __     ______              ______   ______    ",
"/\ \  _ \ \   /\  ___\   /\ \       /\  ___\   /\  __ \   /\ '-./  \   /\  ___\            /\__  _\ /\  __ \   ",
"\ \ \/ '.\ \  \ \  __\   \ \ \____  \ \ \____  \ \ \/\ \  \ \ \-./\ \  \ \  __\            \/_/\ \/ \ \ \/\ \  ",
" \ \__/'.~\_\  \ \_____\  \ \_____\  \ \_____\  \ \_____\  \ \_\ \ \_\  \ \_____\             \ \_\  \ \_____\ ",
"  \/_/   \/_/   \/_____/   \/_____/   \/_____/   \/_____/   \/_/  \/_/   \/_____/              \/_/   \/_____/ ",
"  				  _   _   _   _   _   _   _   _   _   _   _   _  ",
" 				 / \ / \ / \ / \ / \ / \ / \ / \ / \ / \ / \ / \ ",
" 				( M ) i ) s ) a ) d ) v ) e ) n ) t ) u ) r ) e )",
" 				 \_/ \_/ \_/ \_/ \_/ \_/ \_/ \_/ \_/ \_/ \_/ \_/ "]

def generate_kirill(r_num):
    r_string = ""
    for num in range(0, r_num):
        r_string = r_string + "r"
    name = "Ki{}ill".format(r_string)
    return name

def print_intro():
    try:
        print("\n")
        for line in dragon:
            print(line)
            time.sleep(0.03)
        time.sleep(1)
        for line in welcome:
            print(line)
            time.sleep(0.01)
        time.sleep(1)
        print("""\
            \n\nYou find yourself in a cluttered office, seated on a small chair screwed to the floor. Overlooking you are the backs of several
            monitors, and behind them a vague figure. You notice a whiteboard to your right, but you can't read any of the gibberish written on it.
            The figure prompts you to drink the tea in front of you. You lift it to your face, and smell sweet mushrooms and vanilla. As you drink, 
            your mind clears, and the gibberish on the board makes sense to you, taking the form of some kind of rune. Your vision fails you as your 
            head drops to desk.""")
        input("\n\nPress enter to start the game... ")
        print("\n-----------------------------------------------------------\n")

        gave_name = True
        # while loop ensures player eventually gives a name
        while True:
            player.name = input("WHAT is your name?: ").lower()
            if player.name != "":
                break
            gave_name = False # If player doesn't give a name, set to false for getting quest
            print("Oh come on, it's not exactly difficult.") # Maybe add some catch for multiple empty responses?
            time.sleep(1)

        if player.name == "kirill":
            r_count = 2
            while True:
                player.name = generate_kirill(r_count)
                player_input = str(input("Ah, so your name is " + player.name + "? ")).lower()
                if player_input == "y" or player_input == "yes":
                    r_count = r_count * 2
                    player.name = generate_kirill(r_count)
                    print("I think I got it. I'll call you " + player.name)
                    time.sleep(1.5)
                    print("Actually that's pretty hard to remember, too many Ls. I'll stick to Player 1.")
                    time.sleep(1)
                    break
                r_count = r_count + 2
        else:
            print("Great, I'll call you Player 1. That's right isn't it?")
            time.sleep(1.5)
        
        # Loops until player gives a quest
        while True:
            player.quest = str(input("WHAT is your quest?: ")).lower()
            if player.quest != "":
                break
            if gave_name == False: # If player at first did not give a name
                print("Christ. I struggle to get a name out of you, and now you're not answering this?? Work with me here.")
            else:
                print("It would be great if you could just cooperate here. Not that it matters.")
            time.sleep(1)

        if "holy" in player.quest:
            time.sleep(0.3)
            player.answer = input("WHAT is the air speed velocity of an unladen swallow?: ")
            if "african" in player.answer:
                time.sleep(0.1)
                print("What?!? I DON'T KNOW THAT!")
                time.sleep(1)
                print("The narrator falls with a cry into the valley below.")
                time.sleep(2)
                print("Anyway, on with the story. . .")
                time.sleep(1)
            else:
                time.sleep(0.1)
                print("The narrator cackles as your thrown into the valley below.")
                end()

        elif len(player.quest) < 4:
            print("You are a special snowflake arn't you? This IS a game you know, try to have some fun with it you dull witted sloth")
            time.sleep(1.5)
        else:
            print("We actually considered that for the plot of this game, but decided it wasn't good enough. You tried.")
            time.sleep(1.5)
            print("And so your (our) quest begins. . .")
            time.sleep(0.7)
    except KeyboardInterrupt:
        print("Exited game.")
        exit()
    except:
        print("Ah, an error. How unfortunate.")

