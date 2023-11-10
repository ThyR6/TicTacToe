from os import system
import numpy as np

class TicTacToe:

	def showGame(self,arr1=None,arr2=None,OX=False):
		for i in range(3):
			for j in range(3):
				if(arr1!=None):
					if j%3==2: print(self.ToOX(3*i+j+1),end=" ")
					else: print(self.ToOX(3*i+j+1),end=" | ")
				elif OX==True: pass
				else:
					if j%3==2: print(3*i+j+1,end=" ")
					else: print(3*i+j+1,end=" | ")
			print("\t\t\t",end="")

			for j in range(3):
				if(arr2!=None):
					if j%3==2: print(self.ToOX(3*i+j+1),end=" ")
					else: print(self.ToOX(3*i+j+1),end=" | ")
				elif OX==True: pass
				else:
					if j%3==2: print(self.ToClassic(3*i+j+1),end=" ")
					else: print(self.ToClassic(3*i+j+1),end=" | ")

			if i%3!=3-1:
				if OX==False: print("\n----------\t\t\t----------",sep="")
				else: print("\n----------",sep="")

	def ToClassic(self,num):
		if num>6: return num-6
		if num<4: return num+6
		return num

	def Welcome(self):
		print("*"*100,"\n\tWelcome To ThyR. Han's implementation of TicTacToe.\n","*"*100,sep="",end="\n\n")

	def GetOpts(self):
		self.P2="?"
		self.Mode="?"
		self.OX="?"
		while(self.P2=="?"):
			self.Welcome()
			self.P2=input("Which Game Do You Want To Play: \nA: Two Player\nB: Against AI\nC: Online\nEnter Your Choice: ")
			if(self.P2 in ["A","a","1"]): self.P2="A"
			elif(self.P2 in ["B","b","2"]): self.P2="B"
			elif(self.P2 in ["C","c","3"]): self.P2="C"
			else: self.P2="?"
			system("cls")


		while(self.Mode=="?"):
			self.Welcome()
			print("Which Mode Do You Want To Play: ")
			self.showGame()
			self.Mode=input("\nA: Classic\t\t\tB: Modern\nEnter Your Choice: ")
			if(self.Mode in ["A","a","C","c","1"]): self.Mode="C"
			elif(self.Mode in ["B","b","M","m","2"]): self.Mode="M"
			else: self.Mode="?"
			system("cls")

		if(self.P2=="B"):
			while(self.OX=="?"):
				self.Welcome()
				self.OX=input("Which Symbol Do You Want To Use: \nA: O\nB: X\nEnter Your Choice: ")
				if(self.OX in ["A","a","O","o","1"]): self.OX="O"
				elif(self.OX in ["B","b","X","x","2"]): self.OX="X"
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
		if(tmp not in self.Game):
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
		self.GetOpts()
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
		match self.Status:
			case 1: print("\n\n'X' has Won The Game")
			case 2: print("\n\n'O' has Won The Game")
			case 3: print("\n\nThe Game Has Ended In Draw")

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



TicTac = TicTacToe()
TicTac.StartGame()
