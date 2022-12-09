"""
Author: Samit Singhvi
Submission Date: December 9, 2022
Task: To create a rabit game, in which a track is displayed on screen, a user can move rabit forward and backward
and pick up carrot present on the way, and later put up it in a hole ending the game
Modules Used: random, sys, tty, termios
"""

import tty, sys, termios,random

#globally declared values so that they can be later changed and used accordingly
#c represent the character of rabit, it is "r" if rabit has not pick up the carrot, and "R" if it has picked
#if the carrot has been picked, the carrot_pick variable will be given True value
c="r"
carrot_pick=False

'''
function: print_there(x,y,text)

description: Used to print a particular text at a given coordinate
arguments: x,y = coordinates where the text is to be printed
		   text = text which has to be printed
return : nothing

remarks: I have used this so that the track is always present at the same location, and whenever the user updates
anything, so updated track is printed on the same place, giving an illusion that the track is being upadated,
i.e the rabit is moving
'''

def print_there(x, y, text):
	sys.stdout.write("\x1b7\x1b[%d;%df%s\x1b8" % (x, y, text))
	sys.stdout.flush()

'''
function: left_move(track)

description: Used to move the rabit to the left of current position by updating the index of it in the list
arguments: track = the list which include rabit, path , carrot and the hole
return : track(updated list after moving one position to left)

remarks: 1. Here rabit will move one step to left whenever user press "a" button on the keyboard
		 2. If the next step to left is a carrot, it will call pick_carrot function ( where we will decide
		 whether to pick carrot or not)
		 3. Similarly if next step has hole it will call jump_hole function.
		 4. After the updation list is printed
'''

def left_move(track):
	global c
	i=track.index(c)
	if (i>0):
		next=i-1
	if (track[next]=="c"):
	    track = pick_carrot(track, next, i)
	    return track
	if (track[next]=="O"):
	    track=jump_hole(track, next-1, "a", i)    
	    return track
	track[next]=c
	track[i]="-"
	print_there(0,0,string_track(track))
	return track

'''
function: right_move(track)

remarks: Same as left_move(track) function defined above, just it is called whenever user press "d"
and it helps to move to tight(forward)
'''

def right_move(track):
	global c
	i=track.index(c)
	if (i<50):
	    next=i+1
	    if (track[next]=="c"):
	        track = pick_carrot(track, next, i)
	        return track
	    if (track[next]=="O"):
	        track=jump_hole(track, next+1, "d", i)
	        return track
	    track[next]=c
	    track[i]="-"
	    print_there(0,0,string_track(track))
	    return track

'''
function: string_track(track)

description: Used to convert a given list to a string
arguments: track = the list which include rabit, path , carrot and the hole
return : track_as_string, which is a string

remarks: I have used so that we can print track on screen without comma, quotes and spaces
'''  

def string_track(track):
	track_as_string = '[' + ' '.join(track) + ']'
	return(track_as_string)

'''
function: pick_carrot(track, carrot, rabit)

description: Used to pick the carrot if the user allows
arguments: track = the list which include rabit, path , carrot and the hole
		   carrot = index of the carrot
		   rabit = index of the current position of the rabit
return : track(updated list after picking up the carrot)

remarks: 1. When the user moves forward or backward and the next step has carrot this function is called
		 2. It will change the symbol of rabit from "r" to "R" symbolising that it has pick up the carrot
		 and then rabit can move wherever user want.
		 3. Once the function is called, if the user doesn't want to pick, it will return the previous track
		 4. After the updation list is printed
'''

def pick_carrot(track, carrot, rabit):
	print("Enter p to pick the carrot")
	val = 0
	val=sys. stdin. read(1)[0]
	if val=="p":
	    global carrot_pick
	    global c
	    c="R"
	    carrot_pick=True
	    track[carrot]="R"
	    track[rabit]="-"
	else:
	    return track
	print_there(0,0,string_track(track))
	return track

'''
function: jump_hole(track, hole, direction, current)

description: Used to jump a hole if it comes , and also to put the carrot in it which finishes the game
arguments: track = the list which include rabit, path , carrot and the hole
		   hole = index of the hole
		   direction = direction in which rabit has to jump, if "a" jump to backward and if "d" jump to forward
		   it will depend on whether it has been called by left_move() or right_move
		   current = 
return : track(updated list after picking up the carrot)

remarks: 1. When the user moves forward or backward and the next step has hole this function is called
		 2. It will move rabit one step forward or backward to hole, and the hole remain unchanged
		 3. Once this is called, if the rabit has earlier pick up the call and user press "p" then the carrot
		 is put in hole and game ends
		 4. And if user enter j, the rabit jumps and the game continues
'''

def jump_hole(track, hole, direction, current):
	global c
	global carrot_pick
	print("Enter j to jump and p to put the carrot in the hole")
	val = 0
	val=sys. stdin. read(1)[0]   
	if val=="p":
	    if (carrot_pick==True):
	        exit()
	elif val=="j":
	    track[hole]=c
	    track[current]="-"
	else:
	    return track
	print_there(0,0,string_track(track))
	return track

'''
function: begin()

description: The main function which is executed first just after importing modules and declaring global variables
arguments: none 
return : nothing

remarks: 1. It is the main body of the game, includes the track, command to reshuffle it etc.
		 2. It will print the track on the screen at the given (x,y) using print_there() function and then
		 takes the input from the user
		 3. Depending on the input it calls left_move and right_move function
		 4. If user press enter, the function begin is called again recursively with new track
		 5. And if the key which user pressed, doesn't match with any of the allowed input, "INVALID" is printed.
'''

def begin():
	track=["-","-","-","-","-","-","r","-","-","-","-","c","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","O"]
	random.shuffle(track)
	print("Began")
	global c
	c="r"
	random.shuffle(track)
	print_there(0,0,string_track(track))
	filedescriptors = termios. tcgetattr(sys. stdin)
	tty. setcbreak(sys. stdin)
	val = 0.
	while 1:
		val=sys. stdin. read(1)[0]
		if val=="a":	
		    track=left_move(track)
		elif val=="d":
		    track=right_move(track)
		elif val=="\n":
			begin()
		else:
			print("Invalid")
	print_there(0,0,string_track(track))
	

'''
The below three lines has been used so that we can take input from user using keystrokes and need not press enter
Suppose user press d the rabit move forward, without enter key
This has been done to increase convenience and east to play the game
'''

begin()