import kittypy as kp
import random
from threading import Thread
import os
import winsound
import scoreman as scmn
import time

didplayerwin=False
path,wall,unvisited='  ','██','x'
height,width=49,66
maze=[]
playarea=[]
elapsed_time=0
player_name=''
tst=True
kp.initialize(134,51)
def reiterateMaze(maze):
	#this function is used to convert the output of the RP algorithm into a kittypy readable format
	for i in range(0, height):
		playarea.append('')
		for j in range(0, width):
			playarea[i]+=maze[i][j]
def sCells(rand_wall):
	s_paths = 0
	if (maze[rand_wall[0]-1][rand_wall[1]] == '  '):
		s_paths += 1
	if (maze[rand_wall[0]+1][rand_wall[1]] == '  '):
		s_paths += 1
	if (maze[rand_wall[0]][rand_wall[1]-1] == '  '):
		s_paths +=1
	if (maze[rand_wall[0]][rand_wall[1]+1] == '  '):
		s_paths += 1
	return s_paths
#the following construct initializes the maze with given h,w
for i in range(0, height):
	line = []
	for j in range(0, width):
		line.append(unvisited)
	maze.append(line)
#the following constructs implements a starting position for the algorithm, and then checks to ensure it isnt on the border
starting_height = int(random.random()*height)
starting_width = int(random.random()*width)
if (starting_height == 0):
	starting_height += 1
if (starting_height == height-1):
	starting_height -= 1
if (starting_width == 0):
	starting_width += 1
if (starting_width == width-1):
	starting_width -= 1
#sets the current position of algorithm to a path block, and starts creating walls
maze[starting_height][starting_width] = path
walls = []
walls.append([starting_height - 1, starting_width])
walls.append([starting_height, starting_width - 1])
walls.append([starting_height, starting_width + 1])
walls.append([starting_height + 1, starting_width])
maze[starting_height-1][starting_width] = '██'
maze[starting_height][starting_width - 1] = '██'
maze[starting_height][starting_width + 1] = '██'
maze[starting_height + 1][starting_width] = '██'
while (walls):
	rand_wall = walls[int(random.random()*len(walls))-1]
	if (rand_wall[1] != 0):
		if (maze[rand_wall[0]][rand_wall[1]-1] == 'x' and maze[rand_wall[0]][rand_wall[1]+1] == '  '):
			s_paths = sCells(rand_wall)
			if (s_paths < 2):
				maze[rand_wall[0]][rand_wall[1]] = '  '
				if (rand_wall[0] != 0):
					if (maze[rand_wall[0]-1][rand_wall[1]] != '  '):
						maze[rand_wall[0]-1][rand_wall[1]] = '██'
					if ([rand_wall[0]-1, rand_wall[1]] not in walls):
						walls.append([rand_wall[0]-1, rand_wall[1]])
				if (rand_wall[0] != height-1):
					if (maze[rand_wall[0]+1][rand_wall[1]] != '  '):
						maze[rand_wall[0]+1][rand_wall[1]] = '██'
					if ([rand_wall[0]+1, rand_wall[1]] not in walls):
						walls.append([rand_wall[0]+1, rand_wall[1]])
				if (rand_wall[1] != 0):	
					if (maze[rand_wall[0]][rand_wall[1]-1] != '  '):
						maze[rand_wall[0]][rand_wall[1]-1] = '██'
					if ([rand_wall[0], rand_wall[1]-1] not in walls):
						walls.append([rand_wall[0], rand_wall[1]-1])			
			for wall in walls:
				if (wall[0] == rand_wall[0] and wall[1] == rand_wall[1]):
					walls.remove(wall)
			continue
	if (rand_wall[0] != 0):
		if (maze[rand_wall[0]-1][rand_wall[1]] == 'x' and maze[rand_wall[0]+1][rand_wall[1]] == '  '):
			s_paths = sCells(rand_wall)
			if (s_paths < 2):
				maze[rand_wall[0]][rand_wall[1]] = '  '
				if (rand_wall[0] != 0):
					if (maze[rand_wall[0]-1][rand_wall[1]] != '  '):
						maze[rand_wall[0]-1][rand_wall[1]] = '██'
					if ([rand_wall[0]-1, rand_wall[1]] not in walls):
						walls.append([rand_wall[0]-1, rand_wall[1]])
				if (rand_wall[1] != 0):
					if (maze[rand_wall[0]][rand_wall[1]-1] != '  '):
						maze[rand_wall[0]][rand_wall[1]-1] = '██'
					if ([rand_wall[0], rand_wall[1]-1] not in walls):
						walls.append([rand_wall[0], rand_wall[1]-1])
				if (rand_wall[1] != width-1):
					if (maze[rand_wall[0]][rand_wall[1]+1] != '  '):
						maze[rand_wall[0]][rand_wall[1]+1] = '██'
					if ([rand_wall[0], rand_wall[1]+1] not in walls):
						walls.append([rand_wall[0], rand_wall[1]+1])
			for wall in walls:
				if (wall[0] == rand_wall[0] and wall[1] == rand_wall[1]):
					walls.remove(wall)
			continue
	if (rand_wall[0] != height-1):
		if (maze[rand_wall[0]+1][rand_wall[1]] == 'x' and maze[rand_wall[0]-1][rand_wall[1]] == '  '):
			s_paths = sCells(rand_wall)
			if (s_paths < 2):
				maze[rand_wall[0]][rand_wall[1]] = '  '
				if (rand_wall[0] != height-1):
					if (maze[rand_wall[0]+1][rand_wall[1]] != '  '):
						maze[rand_wall[0]+1][rand_wall[1]] = '██'
					if ([rand_wall[0]+1, rand_wall[1]] not in walls):
						walls.append([rand_wall[0]+1, rand_wall[1]])
				if (rand_wall[1] != 0):
					if (maze[rand_wall[0]][rand_wall[1]-1] != '  '):
						maze[rand_wall[0]][rand_wall[1]-1] = '██'
					if ([rand_wall[0], rand_wall[1]-1] not in walls):
						walls.append([rand_wall[0], rand_wall[1]-1])
				if (rand_wall[1] != width-1):
					if (maze[rand_wall[0]][rand_wall[1]+1] != '  '):
						maze[rand_wall[0]][rand_wall[1]+1] = '██'
					if ([rand_wall[0], rand_wall[1]+1] not in walls):
						walls.append([rand_wall[0], rand_wall[1]+1])
			for wall in walls:
				if (wall[0] == rand_wall[0] and wall[1] == rand_wall[1]):
					walls.remove(wall)
			continue
	if (rand_wall[1] != width-1):
		if (maze[rand_wall[0]][rand_wall[1]+1] == 'x' and maze[rand_wall[0]][rand_wall[1]-1] == '  '):
			s_paths = sCells(rand_wall)
			if (s_paths < 2):
				maze[rand_wall[0]][rand_wall[1]] = '  '
				if (rand_wall[1] != width-1):
					if (maze[rand_wall[0]][rand_wall[1]+1] != '  '):
						maze[rand_wall[0]][rand_wall[1]+1] = '██'
					if ([rand_wall[0], rand_wall[1]+1] not in walls):
						walls.append([rand_wall[0], rand_wall[1]+1])
				if (rand_wall[0] != height-1):
					if (maze[rand_wall[0]+1][rand_wall[1]] != '  '):
						maze[rand_wall[0]+1][rand_wall[1]] = '██'
					if ([rand_wall[0]+1, rand_wall[1]] not in walls):
						walls.append([rand_wall[0]+1, rand_wall[1]])
				if (rand_wall[0] != 0):	
					if (maze[rand_wall[0]-1][rand_wall[1]] != '  '):
						maze[rand_wall[0]-1][rand_wall[1]] = '██'
					if ([rand_wall[0]-1, rand_wall[1]] not in walls):
						walls.append([rand_wall[0]-1, rand_wall[1]])
			for wall in walls:
				if (wall[0] == rand_wall[0] and wall[1] == rand_wall[1]):
					walls.remove(wall)
			continue
	for wall in walls:
		if (wall[0] == rand_wall[0] and wall[1] == rand_wall[1]):
			walls.remove(wall)
for i in range(0, height):
	for j in range(0, width):
		if (maze[i][j] == 'x'):
			maze[i][j] = '██'
for i in range(0, width):
	if (maze[1][i] == '  '):
		maze[0][i] = '  '
		break
for i in range(width-1, 0, -1):
	if (maze[height-2][i] == '  '):
		maze[height-1][i] = '  '
		break
reiterateMaze(maze)

g_stor=["HELLO. I AM DORIS, KEEPER OF THIS WORLD.",
"YOU HAVE STUMBLED ACROSS MY LAIR,...", "YOU MUST COMPLETE MY CHALLENGE!",
"I SHALL SET YOU DOWN IN A LABYRINTH MOST CRUEL", "DO YOU HAVE THE STRENGTH TO ESCAPE?",
"PROVE YOURSELF TO ME AND EXIT ALIVE.", "I SHALL THEN RETURN YOU TO YOUR WORLD.","EARN MY RESPECT! BEGIN!"
]
def game_story():
	for i in g_stor:
		os.system('cls')
		print('press enter to continue...')
		print('\n'*19)
		kp.print_center(kp.Fore.YELLOW + i+ kp.Style.RESET_ALL ,134)
		waiter=input()

name_enter_str=str('\n'*20 + ' '*55 + "ENTER YOUR NAME, TRESPASSER\n\n" + ' '*55)

kp.show_splash("assets\\splash.png",0.5,kp.Image.BOX)
os.system('cls')
print('\n'*20)
kp.print_center("made by Abhay Tripathi, Aditya Vikram and Indrajith Gopinathan",134)
kp.wait(1)
os.system('cls')
winsound.PlaySound('assets\\story.wav', winsound.SND_LOOP+winsound.SND_ASYNC)
player_name=input(name_enter_str)
game_story()

winsound.PlaySound(None, winsound.SND_ASYNC)
kp.backfore=kp.Fore.RED
kp.backback=kp.Back.BLACK
kp.chcolor=kp.Fore.CYAN+kp.Back.BLACK
kp.add_scene(playarea,"lst")
kp.add_character(['▓☻'],'lst')
kp.add_character(['☻▓'],'lst')
kp.teleport([2,0])
kp.draw_frame()

def gameterms():
	global elapsed_time
	global player_name
	global tst
	while tst:
		elapsed_time+=1
		ttod=str(str(elapsed_time)+' seconds | playing as '+player_name)
		if kp.cursp==0:
			kp.cursp=1
		else:
			kp.cursp=0
		kp.draw_frame(ttod)
		kp.wait(1)
t = Thread(target=gameterms, args=())
t.start()

def updateframe():
	os.system("cls")
	ttod=str(str(elapsed_time)+' seconds | playing as '+player_name)
	kp.draw_frame(ttod)

winsound.PlaySound('assets\\song.wav', winsound.SND_LOOP+winsound.SND_ASYNC)
while True:
	prevpos=[kp.location[0],kp.location[1]]
	ist = kp.await_get_input("\r")
	if kp.location[1]==48 or ist=='z':
		didplayerwin=True
		tst=False
		break
	if ist==kp.controls[0]:
		if playarea[kp.location[1]-1][kp.location[0]]==' ':
			kp.teleport([kp.location[0],kp.location[1]-1])
			updateframe()
	elif ist==kp.controls[2]:
		if playarea[kp.location[1]+1][kp.location[0]]==' ':
			kp.teleport([kp.location[0],kp.location[1]+1])
			updateframe()
	elif ist==kp.controls[1]:
		if playarea[kp.location[1]][kp.location[0]-2]==' ':
			kp.teleport([kp.location[0]-2,kp.location[1]])
			updateframe()
	elif ist==kp.controls[3]:
		if playarea[kp.location[1]][kp.location[0]+2]==' ':
			kp.teleport([kp.location[0]+2,kp.location[1]])
			updateframe()
	elif ist=='x':
		didplayerwin=False
		tst=False
		break
	ist=""
winsound.PlaySound(None, winsound.SND_ASYNC)
os.system('cls')
if didplayerwin:
	print('\n'*20)
	kp.print_center("excellent, you finished in "+str(elapsed_time)+" seconds!",134)
	try:
		scmn.update_score([str(player_name),str(elapsed_time),int(time.time())])
	except:
		print('err')
	kp.print_center("you may now leave, or... would you like to play again? (y/n)",134)
	ippt=kp.await_get_input("\r")
	if ippt=="y":
		os.system("cls")
		print('\n'*20)
		kp.print_center("Oh.",134)
		kp.wait(0.5)
		os.system("cls")
		print('\n'*20)
		kp.print_center("you are quite an interesting fellow :)",134)
		kp.wait(1)
		kp.full_restart()
	else:
		os.system('cls')
		print('\n'*20)
		kp.print_center('goodbye.',134)
		kp.wait(0.5)
else:
	os.system("cls")
	print('\n'*20)
	kp.print_center("Too bad. Do it again, then, or stay trapped FOREVER",134)
	kp.wait(2)
	kp.full_restart()
	xgg=input()
	