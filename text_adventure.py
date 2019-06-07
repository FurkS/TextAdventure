import time #Imports a module to add a pause

#Figuring out how users might respond
answer_A = ["A", "a"]
answer_B = ["B", "b"]
answer_C = ["C", "c"]
yes = ["Y", "y", "yes"]
no = ["N", "n", "no"]
back = ["Back", "back"]
shoot = ["Shoot", "shoot"]

#Grabbing objects
key = 0
torch = 0
knife = 0
gun = 0


required = ("\nYou can only choose option A, B, or C\n") #Cutting down on duplication
required2 = ("\nYou can only choose option A or B\n")
required3 = ("\nThere is nowhere to go from here- type 'back' to return to the previous decision\n")

print("""Welcome to Abstergo Enterprises. You may not remember who or where you are. But that does not matter- what matters is where you were. We have the technology to transport you into the body of Edward Kenway,
infamous pirate in the 1800's. You will spend your time sailing the seas, finding gold, facing adversity from Templars and the law alike. But you will have an ulterior motive- your task will be to find a device called 'The Observatory'. This device is used to track and monitor anyone, anywhere in the world using a
DNA sample. When you find it, you will bring it back to us. However, if you die, you will be transported back to our facility.\n\n""")


#The story is broken into sections, starting with "intro"
#When you see def name() it means you are defining a function which you will later call
def intro():
    choice = input("Do you accept your fate?\n >>> ")
    time.sleep(1) #this just means you are including a pause
    print("\n")
    if choice in yes: #see arrays above
        print("Try to relax. You'll wake up shortly, but we have no way of knowing where or when you'll wake up aside from the year and month, so be prepared.\n")
    elif choice in no:
        print ("\n Very well. We will put you back to sleep now, but you will have no memory of this place or us. "
        "\n\nThere comes a time in every man's life where he decides to be something, or nothing.")
        raise SystemExit #This will exit the program and bring you back to command line

def learn_more():
  print ("""'Sir?' You snap awake, and take a rapid reality check, taking into account your surroundings while remembering the conversation at Abstergo.
  Your name is Edward Kenway. You are a pirate in the 1800's, with holstered guns and swords decorating your dirty white hooded robe to match. There's a shore off in the distance to your left;
  to your right, nothing but ocean blue, clouds and a schooner off in the distance that looks similar to the one you are steering. 'Captain', your first mate says, '
  They're manning their cannons. What say you?' Do you: """)
  time.sleep(1)
  choice2 = input("""
    A. Arm your cannons and get ready to board
    B. Retreat and sail to the next island
    C. Decide this isn't worth your time\n
    >>> """)
  print("\n")
  if choice2 in answer_A:
        print("Your first mate shoots you a wild grin, then turns around and addresses the crew. 'Raise the mainsail, man the cannons! Prepare to board!'.")
  elif choice2 in answer_B:
        print("Your first mate, albeit disappointed, signals the crew. You whip the steering wheel around as fast as possible until the ship is on a steady pace heading towards the horizon.\n")
        raise SystemExit
  elif choice2 in answer_C:
        print ("\nYou remember being told that if you die, you will wake up in the present day. "
        "\n\n You look down at the pistol holstered to your chest and know exactly what to do.\n")
        raise SystemExit
  else:
        print(required)
        time.sleep(0.5)
        learn_more()
    #option_rock()

def appointment():
    print("""  \nYour men are bloody and battered. After a week on the seas, you spot the shore of a small, uncharted island even though you expected to be sailing
    for weeks more at the minimum. As you and your men struggle onshore, a small, hunchbacked lady comes out of the woodwork to greet you. She is elderly, but walks with a strong pace; and has a piercing stare, with one eye blue and the other green.
    She looks unfazed by your rough appearance or your weaponry as she addresses you.'Greetings. I am Circe, golden witch of Aiaia. What brings you to my island?'""")
    time.sleep(1)
    choice3 = input("""
    A. We are but weary travelers, hoping to take shelter on your humble abode.
    B. We are pirates, however battered and bloody, and hope that you can trust us to behave ourselves if you give us sanctuary.
    C. We are pirates and conquerors, and now you, this island and everything on it is ours.\n
    >>> """)
    print("\n")
    if choice3 in answer_A:
          print("The witch says to you: I shall shelter you for exactly one night, and you will be on your way.\n")
          time.sleep(0.5)
          print("""You and your men eat like kings that night, and thank the witch profusely the next morning. She whispers a spell into a jar that, when you open it, harnesses the power of the winds to blow you wherever you want to go.\n""")
          key()
    elif choice3 in answer_B:
          print("""I will not provide sanctuary to the likes of thugs and criminals. Leave me, before I capsize your ship with a single word.\n""")
          raise SystemExit
    elif choice3 in answer_C:
          print("You're delusional to believe that I will stand meekly while you violate me so. I will allow you and your men one chance to leave me; it would be a grave mistake not to take it.\n")
          time.sleep(1)
          terrestrial()
          raise SystemExit
    else:
          print(required)
          time.sleep(1)
          appointment()

def key():
    print("Pssssst...\n")
    time.sleep(0.75)
    print("After leaving the witch's island, you spet weeks getting back to your hometown on the Cote d'Azur. It is a raw hour of night, and you and your men are sitting in a bar raucously drinking the night away. You decide to break away to study the vaguely detailed map that leads you to the Observatory when you hear a meek voice behind you. \n")
    time.sleep(0.75)
    print("""You turn around and find a young boy barely over the age of 7 or maybe 8 staring at you with steely eyes.\n""")
    time.sleep(0.75)
    print("What is it, boy?, you ask.\n")
    time.sleep(0.75)
    print("""The boy manages to push out a weak "He told me to give you this" before yanking a rusty looking pendant out of his pocket. Before you could ask who "he" was or what this is, the boy takes off busting out of the coffeeshop and disappearing down the street
    You hardly get a moment to study the pendant and find out it opens up to reveal a small key before you notice the foorsteps approaching your behind.
    You turn around to find two burly men in Britian's royal guard uniforms staring at you. In a rough, unfriendly voice, one of them says, "That does not belong to you. Give it to me".\n""")
    choice4 = input("""Do you give up the key, or defy them?\n
    A. Give them the key; you don't need the heat it will bring
    B. Keep the key- it has piqued your curiosity, and for them to want it so bad it must be important to some very powerful people.\n
    >>> """)
    print("\n")
    if choice4 in answer_A:
        print("Good choice. We've stumbled across a sensible one, haven't we?\n")
        raise SystemExit
    elif choice4 in answer_B:
        print("One of the guards leans in close. 'This key should not matter to you. If you part with it now, you will be handsomely rewarded, if you don't? Well, we are on orders to do whatever is necessary to retrieve it, and that includes the death of a rather unruly looking civilian.\n")
    else:
          print(required2)
          key()

def coffeeshop():
    print("""You lean in so close to the guard that you could smell the sweat on his brow and grin. "You say this doesn't belong to me, but I don't see anyone's
    name on it". Both of the guards grab their guns, but you are quicker than both. A spring loaded knife leaps from the wrist on your right hand while your left flashes to the handle of the guard's pistol,
    and both are dead in a matter of seconds. You draw the hood over your face so as to stay concealed to the crowd of onlookers, leap through the window and make your way over the rooftops to a coffeeshop miles away.\n""")
    time.sleep(0.75)
    print("""Two hours later, as the sun cracks over the horizon, you are sitting in a coffeeshop studying the key. It is incredibly ancient looking, rusted and worn down, with a symbol you do not recognize
    etched into the back. You are aware of a man sitting in the back watching you, but you become incredibly alarmed when you look up to check on him
     and see that he has somehow, without getting up, changed into an assassins robe with red accents and a hood that looks identical to yours.\n""")
    time.sleep(0.75)
    print("""You pretend to study the key for a second longer, debating on what to do. When you get up and turn around to confront him, he is no longer there. Before
    you can take a precursory look around, you hear a raspy voice directly behind you "Beautiful morning, isn't it?" In less than a half a second, you are holding your gun an inch from his nose, but he does not bat an eyelash.\n""")
    time.sleep(0.75)
    print("""He has taken his hood off and is grinning at you, and when you look down at his hands he is holding the pendant and key in his hands as if he himself were studying them.\n""")
    time.sleep(0.75)
    print("""You keep the gun shoved in his face. 'Who are you, and what business do you have with me?' .\n""")
    time.sleep(0.75)
    print("""'You can relax, boy', he says in a disarming voice, 'for those questions do not matter. This symbol represents a clocktower built hundreds of years ago, in the center of town. Go there to find the answers you seek.'\n""")

def keyclue ():
    print("""He gestures at a tall, majestic structure visible from the window of the coffeeshop. You turn to look to see that it is a clocktower, but when you look back down you see that you now have your gun pointed at an empty seat, as the mysterious man has disappeared without a trace.""")

def terrestrial():
    print("""Behind a painting at the top of the clocktower, you find a mysterious safe, the front of which is filled with a myriad of dials and false keyholes. You spot the true keyhole after a minute of searching- this one is small, inconspicuous, and looks as old as the key. You carefully insert the key into the keyhole.
    You turn it, and hear a series of clicks and gears turning as if the safe is some sort of ancient clocktower. The safe doors part open to reveal a small, boxed shape device. You know what it is as soon as you look at it- you have completed your quest and found the Observatory.\n""")

#This is where you call all the functions so they run
intro()
learn_more()
appointment()
coffeeshop()
