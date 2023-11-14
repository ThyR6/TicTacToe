from msvcrt import getch
from os import get_terminal_size, system
import numpy as np

class TicTacToe:

	def showGame(self,arr1=None,arr2=None,OX=False):
		for i in range(3):
			tmp=[]
			for j in range(3):
				tmp.append(self.ToOX(3*i+j+1))
			self.printOX(tmp)

			if(i!=2): print("\n"+ " "*((get_terminal_size().columns-27)//2),"---------------------------")

	def ToClassic(self,num):
		if num>6: return num-6
		if num<4: return num+6
		return num

	def Welcome(self):
		print(r"",
					r"+============================================================+",
					r"|    _____  _         _____              _____               |",
					r"|   |_   _|(_)  ___  |_   _|__ _   ___  |_   _|___    ___    |",
					r"|     | |  | | / __|   | | / _` | / __|   | | / _ \  / _ \   |",
					r"|     | |  | || (__    | || (_| || (__    | || (_) ||  __/   |",
					r"|     |_|  |_| \___|   |_| \__,_| \___|   |_| \___/  \___|   |",
					r"+============================================================+",sep="\n"+ " "*((get_terminal_size().columns-62)//2),end="\n\n")

	def GetOpts(self):
		self.P2="?"
		self.Mode="?"
		self.OX="?"
		while(self.P2=="?"):
			self.Welcome()
			print("\n\n",
			r"+==========================================================================+           +==================+",
			r"|    _____                      ____   _                                   |           |       _     _    |",
			r"|   |_   _|__      __ ___      |  _ \ | |  __ _  _   _   ___  _ __  ___    |           |      / \   (_)   |",
			r"|     | |  \ \ /\ / // _ \     | |_) || | / _` || | | | / _ \| '__|/ __|   |           |     / _ \  | |   |",
			r"|     | |   \ V  V /| (_) |    |  __/ | || (_| || |_| ||  __/| |   \__ \   |           |    / ___ \ | |   |",
			r"|     |_|    \_/\_/  \___/     |_|    |_| \__,_| \__, | \___||_|   |___/   |           |   /_/   \_\|_|   |",
			r"|    ~~~~~~~                                     |___/                     |           |   ~~~~~~~~~      |",
			r"+==========================================================================+           +==================+",sep="\n"+ " "*((get_terminal_size().columns-107)//2))
			self.P2=str(getch(),encoding="utf-8")
			if(self.P2 in ["T","t"]): self.P2="A"
			elif(self.P2 in ["A","a"]): self.P2="B"
			else: self.P2="?"
			system("cls")


		while(self.Mode=="?"):
			self.Welcome()
			# print("Which Mode Do You Want To Play: ")
			# self.showGame()
			print(r"",
			r"+==========================================+             +===============================================+",
			r"|     ____  _                   _          |             |    __  __             _                       |",
			r"|    / ___|| |  __ _  ___  ___ (_)  ___    |             |   |  \/  |  ___    __| |  ___  _ __  _ __     |",
			r"|   | |    | | / _` |/ __|/ __|| | / __|   |             |   | |\/| | / _ \  / _` | / _ \| '__|| '_ \    |",
			r"|   | |___ | || (_| |\__ \\__ \| || (__    |             |   | |  | || (_) || (_| ||  __/| |   | | | |   |",
			r"|    \____||_| \__,_||___/|___/|_| \___|   |             |   |_|  |_| \___/  \__,_| \___||_|   |_| |_|   |",
			r"|   ~~~~~~~                                |             |   ~~~~~~~~                                    |",
			r"+==========================================+             +===============================================+",sep="\n"+ " "*((get_terminal_size().columns-106)//2))
			self.Mode=str(getch(),encoding="utf-8")
			if(self.Mode in ["C","c"]): self.Mode="C"
			elif(self.Mode in ["M","m"]): self.Mode="M"
			else: self.Mode="?"
			system("cls")

		if(self.P2=="B"):
			while(self.OX=="?"):
				self.Welcome()
				print(r"",
						r"+=========+                          +===========+",
						r"|   ╔═╗   |                          |    ═╗ ╦   |",
						r"|   ║ ║   |                          |    ╔╩╦╝   |",
						r"|   ╚═╝   |                          |    ╩ ╚═   |",
						r"|   ~~~   |                          |    ~~~~   |",
						r"+=========+                          +===========+",sep="\n"+ " "*((get_terminal_size().columns-50)//2))
				self.OX=str(getch(),encoding="utf-8")
				if(self.OX in ["O","o"]): self.OX="O"
				elif(self.OX in ["X","x"]): self.OX="X"
				else: self.OX="?"
				system("cls")

	def Input(self):
		tmp=0
		i=0
		for index,num in enumerate(self.Game):
			if(num==0):
				i=index
				break
		if(self.P2=="B" and self.OX=="X" and self.Game[0]==0):
			tmp=[1,1,3,3,5,7,7,9,9][np.random.randint(0,9)]
		elif(self.P2=="B" and i%2==0 and self.OX=="X"):
			print("ThyR. AI is thinking about next move... ",end="")
			tmp=self._AI(self.Game)
		elif(self.P2=="B" and i%2==1 and self.OX=="O"):
			print("ThyR. AI is thinking about next move... ",end="")
			tmp=self._AI(self.Game)
		else:
			while(1):
				try:
					if(self.Mode=="M"): tmp=self.ToClassic(int(input("Which Maneuver You Want To Perform: ")))
					else: tmp=int(input("Which Maneuver You Want To Perform: "))
					break
				except:
					pass
		if(tmp not in self.Game and tmp in range(1,10)):
			self.Game[i]=tmp

	def _Status(self,GameL): # 	0 -> Ongoing;	1 -> X Wins;	2 -> O Wins;	3 -> Draw;
		Status=0
		if(GameL[8]!=0): Status=3
		G=[GameL[1::2],GameL[0::2]]
		for P in range(2):
			for i in range(3):
				if all(3*i+j in G[P] for j in range(1,4)): Status=P+1
				if all(i+j in G[P] for j in range(1,9,3)): Status=P+1
				if all(i in G[P] for i in [1,5,9]) or all(i in G[P] for i in [3,5,7]): Status=P+1
		return Status

	def UpdateStatus(self):
		self.Status=self._Status(self.Game)

	def StartGame(self):
		self.Game=[0,0,0,0,0,0,0,0,0]
		self.Status=0 # 	0 -> Ongoing;	1 -> X Wins;	2 -> O Wins;	3 -> Draw;
		system("cls")
		New="?"
		while(New=="?"):
			self.ThyR()
			New=str(getch(),encoding="utf-8")
			if New in ["N","n"]: New="N"
			# elif New in ["O","o"]: New="O"
			# elif New in ["H","h"]: New="H"
			else: New="?"
			system("cls")
		if(New=="N"): self.GetOpts()
		elif(New=="O"): self.Opts()
		elif(New=="H"): self.Help()
		while(self.Status==0):
			system("cls")
			self.Welcome()
			self.showGame(self.Game,OX=True)
			print("\n")
			self.Input()
			self.UpdateStatus()
		system("cls")
		self.Welcome()
		self.showGame(self.Game,OX=True)
		print("\n")
		if(self.P2=="B"):
			if(self.OX=="O"):
				match self.Status:
					case 1: self.Pprint(4)
					case 2: self.Pprint(5)
					case 3: self.Pprint(1)
			if(self.OX=="X"):
				match self.Status:
					case 1: self.Pprint(5)
					case 2: self.Pprint(4)
					case 3: self.Pprint(1)
		else:
			match self.Status:
				case 1: self.Pprint(3)
				case 2: self.Pprint(2)
				case 3: self.Pprint(1)

	def ToOX(self,index):
		for i in range(9):
			if (self.Game[i]==index):
				if(i%2): return "X"
				return "O"
		return " "
	
	def AI(self,GameAI):
		_0=0
		for i in range(9):
			if GameAI[i]==0:
				_0=i+1
				break
		if self._Status(GameAI)==1: return 1*(9-_0)
		if self._Status(GameAI)==2: return -1*(9-_0)
		if self._Status(GameAI)==3: return 0

		GameL=[]
		# tmp=[]
		for i in range(1,10):
			if i not in GameAI: 
				tmp=GameAI.copy()
				tmp[_0-1]=i
				GameL.append(self.AI(tmp))
				
		if(_0%2==0): return max(GameL)
		else: return min(GameL)

	def _AI(self,GameAI):
		_0=0
		for i in range(9):
			if GameAI[i]==0:
				_0=i+1
				break
		if self._Status(GameAI)!=0: return 0

		GameL=[[],[]]
		# tmp=[]
		for i in range(1,10):
			if i not in GameAI: 
				tmp=GameAI.copy()
				tmp[_0-1]=i
				GameL[0].append(i)
				GameL[1].append(self.AI(tmp))
		minimax=[GameL[1][0]]
		idx=[GameL[0][0]]
		for i in range(1,len(GameL[1])):
			if(_0%2==0 and GameL[1][i]>minimax[0]):
				minimax=[GameL[1][i]]
				idx=[GameL[0][i]]
			elif(_0%2==1 and GameL[1][i]<minimax[0]):
				minimax=[GameL[1][i]]
				idx=[GameL[0][i]]
			elif(_0%2==0 and GameL[1][i]==minimax[0]):
				minimax.append(GameL[1][i])
				idx.append(GameL[0][i])
			elif(_0%2==1 and GameL[1][i]==minimax[0]):
				minimax.append(GameL[1][i])
				idx.append(GameL[0][i])

		return idx[np.random.randint(0, len(idx))]

	def ThyR(self):
		print(r"",
			r" _____                                                                                                               _____ ",
			r"( ___ )                                                                                                             ( ___ )",
			r" |   |~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~|   | ",
			r" |   |                                                                                                               |   | ",
			r" |   |       _________   ___  ___       ___    ___  ________               ___  ___   ________   ________            |   | ",
			r" |   |      |\___   ___\|\  \|\  \     |\  \  /  /||\   __  \             |\  \|\  \ |\   __  \ |\   ___  \          |   | ",
			r" |   |      \|___ \  \_|\ \  \\\  \    \ \  \/  / /\ \  \|\  \            \ \  \\\  \\ \  \|\  \\ \  \\ \  \         |   | ",
			r" |   |           \ \  \  \ \   __  \    \ \    / /  \ \   _  _\            \ \   __  \\ \   __  \\ \  \\ \  \        |   | ",
			r" |   |            \ \  \  \ \  \ \  \    \/  /  /    \ \  \\  \|  ___       \ \  \ \  \\ \  \ \  \\ \  \\ \  \       |   | ",
			r" |   |             \ \__\  \ \__\ \__\ __/  / /       \ \__\\ _\ |\__\       \ \__\ \__\\ \__\ \__\\ \__\\ \__\      |   | ",
			r" |   |              \|__|   \|__|\|__||\___/ /         \|__|\|__|\|__|        \|__|\|__| \|__|\|__| \|__| \|__|      |   | ",
			r" |   |                                \|___|/                                                                        |   | ",
			r" |   |                                                                                                               |   | ",
			r" |___|~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~|___| ",
			r"(_____)                                                                                                             (_____)",sep="\n"+ " "*((get_terminal_size().columns-123)//2))
		print(r" ",
					r"+================================================================+",
					r"|    _   _                       ____                            |",
					r"|   | \ | |  ___ __      __     / ___|  __ _  _ __ ___    ___    |",
					r"|   |  \| | / _ \\ \ /\ / /    | |  _  / _` || '_ ` _ \  / _ \   |",
					r"|   | |\  ||  __/ \ V  V /     | |_| || (_| || | | | | ||  __/   |",
					r"|   |_| \_| \___|  \_/\_/       \____| \__,_||_| |_| |_| \___|   |",
					r"|   ~~~~~~~                                                      |",
					r"+================================================================+",sep="\n"+ " "*((get_terminal_size().columns-66)//2))
		print(r"",
		r"+===============================================+        +============================+",
		r"|     ___          _    _                       |        |     _   _      _           |",
		r"|    / _ \  _ __  | |_ (_)  ___   _ __   ___    |        |    | | | | ___| |_ __      |",
		r"|   | | | || '_ \ | __|| | / _ \ | '_ \ / __|   |        |    | |_| |/ _ \ | '_ \     |",
		r"|   | |_| || |_) || |_ | || (_) || | | |\__ \   |        |    |  _  |  __/ | |_) |    |",
		r"|    \___/ | .__/  \__||_| \___/ |_| |_||___/   |        |    |_| |_|\___|_| .__/     |",
		r"|          |_|                                  |        |                 |_|        |",
		r"|   ~~~~~~~                                     |        |    ~~~~~~~                 |",
		r"+===============================================+        +============================+",sep="\n"+ " "*((get_terminal_size().columns-87)//2))

	def printOX(self,OX):
		print("\n"+ " "*((get_terminal_size().columns-27)//2),end="")
		for i in range(3):
			if(i==2):
				if(OX[i]=="O"): print(r"╔═╗ ",end="",sep="")
				if(OX[i]=="X"): print(r"═╗ ╦",end="",sep="")
				if(OX[i]==" "): print(r"    ",end="",sep="")
			else:
				if(OX[i]=="O"): print(r"╔═╗ ",end="   |   ",sep="")
				if(OX[i]=="X"): print(r"═╗ ╦",end="   |   ",sep="")
				if(OX[i]==" "): print(r"    ",end="   |   ",sep="")
		print("\n"+ " "*((get_terminal_size().columns-27)//2),end="")
		for i in range(3):
			if(i==2):
				if(OX[i]=="O"): print(r"║ ║ ",end="",sep="")
				if(OX[i]=="X"): print(r"╔╩╦╝",end="",sep="")
				if(OX[i]==" "): print(r"    ",end="",sep="")
			else:
				if(OX[i]=="O"): print(r"║ ║ ",end="   |   ",sep="")
				if(OX[i]=="X"): print(r"╔╩╦╝",end="   |   ",sep="")
				if(OX[i]==" "): print(r"    ",end="   |   ",sep="")
		print("\n"+ " "*((get_terminal_size().columns-27)//2),end="")
		for i in range(3):
			if(i==2):
				if(OX[i]=="O"): print(r"╚═╝ ",end="",sep="")
				if(OX[i]=="X"): print(r"╩ ╚═",end="",sep="")
				if(OX[i]==" "): print(r"    ",end="",sep="")
			else:
				if(OX[i]=="O"): print(r"╚═╝ ",end="   |   ",sep="")
				if(OX[i]=="X"): print(r"╩ ╚═",end="   |   ",sep="")
				if(OX[i]==" "): print(r"    ",end="   |   ",sep="")

	def Pprint(self,strNo):
		match strNo:
			case 1: print(r"",
							r" _____                         _____ ",
							r"( ___ )                       ( ___ )",
							r" |   |~~~~~~~~~~~~~~~~~~~~~~~~~|   | ",
							r" |   |                         |   | ",
							r" |   |      ╔╦╗╦═╗╔═╗╦ ╦┬      |   | ",
							r" |   |       ║║╠╦╝╠═╣║║║│      |   | ",
							r" |   |      ═╩╝╩╚═╩ ╩╚╩╝o      |   | ",
							r" |   |                         |   | ",
							r" |___|~~~~~~~~~~~~~~~~~~~~~~~~~|___| ",
							r"(_____)                       (_____)",sep="\n"+ " "*((get_terminal_size().columns-37)//2))
			case 2: print(r"",
							r" _____                           _____ ",
							r"( ___ )                         ( ___ )",
							r" |   |~~~~~~~~~~~~~~~~~~~~~~~~~~~|   | ",
							r" |   |                           |   | ",
							r" |   |      ╔═╗  ╦ ╦╔═╗╔╗╔┬      |   | ",
							r" |   |      ║ ║  ║║║║ ║║║║│      |   | ",
							r" |   |      ╚═╝  ╚╩╝╚═╝╝╚╝o      |   | ",
							r" |   |                           |   | ",
							r" |___|~~~~~~~~~~~~~~~~~~~~~~~~~~~|___| ",
							r"(_____)                         (_____)",sep="\n"+ " "*((get_terminal_size().columns-39)//2))
			case 3: print(r"",
							r" _____                            _____ ",
							r"( ___ )                          ( ___ )",
							r" |   |~~~~~~~~~~~~~~~~~~~~~~~~~~~~|   | ",
							r" |   |                            |   | ",
							r" |   |      ═╗ ╦  ╦ ╦╔═╗╔╗╔┬      |   | ",
							r" |   |      ╔╩╦╝  ║║║║ ║║║║│      |   | ",
							r" |   |      ╩ ╚═  ╚╩╝╚═╝╝╚╝o      |   | ",
							r" |   |                            |   | ",
							r" |___|~~~~~~~~~~~~~~~~~~~~~~~~~~~~|___| ",
							r"(_____)                          (_____)",sep="\n"+ " "*((get_terminal_size().columns-40)//2))
			case 4: print(r"",
							r" _____                                    _____ ",
							r"( ___ )                                  ( ___ )",
							r" |   |~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~|   | ",
							r" |   |                                    |   | ",
							r" |   |      ╦ ╦╔═╗╦ ╦  ╦  ╔═╗╔═╗╔═╗┬      |   | ",
							r" |   |      ╚╦╝║ ║║ ║  ║  ║ ║╚═╗║╣ │      |   | ",
							r" |   |       ╩ ╚═╝╚═╝  ╩═╝╚═╝╚═╝╚═╝o      |   | ",
							r" |   |                                    |   | ",
							r" |___|~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~|___| ",
							r"(_____)                                  (_____)",sep="\n"+ " "*((get_terminal_size().columns-48)//2))
			case 5: print(r"",
							r" _____                                 _____ ",
							r"( ___ )                               ( ___ )",
							r" |   |~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~|   | ",
							r" |   |                                 |   | ",
							r" |   |      ╦ ╦╔═╗╦ ╦  ╦ ╦╔═╗╔╗╔┬      |   | ",
							r" |   |      ╚╦╝║ ║║ ║  ║║║║ ║║║║│      |   | ",
							r" |   |       ╩ ╚═╝╚═╝  ╚╩╝╚═╝╝╚╝o      |   | ",
							r" |   |                                 |   | ",
							r" |___|~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~|___| ",
							r"(_____)                               (_____)",sep="\n"+ " "*((get_terminal_size().columns-45)//2))

	def Opts(self):
		pass

	def Help(self):
		pass

TicTac = TicTacToe()
TicTac.StartGame()
