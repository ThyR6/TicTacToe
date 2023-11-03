from os import system

class TicTacToe:

	def showGame(self,arr1=None,arr2=None,OX=False):
		n=int(self.Level)
		for i in range(n):
			for j in range(n):
				if(arr1!=None):
					if j%n==n-1: print(self.ToOX(n*i+j+1),end=" ")
					else: print(self.ToOX(n*i+j+1),end=" | ")
				elif OX==True: pass
				else:
					if self.Level=="3":
						if j%n==n-1: print(n*i+j+1,end=" ")
						else: print(n*i+j+1,end=" | ")
					else:
						if j%n==n-1: print(i+1,j+1,end=" ",sep="")
						else: print(i+1,j+1,end=" | ",sep="")
			print("\t\t\t",end="")

			for j in range(n):
				if(arr2!=None):
					if j%n==n-1: print(self.ToOX(n*i+j+1),end=" ")
					else: print(self.ToOX(n*i+j+1),end=" | ")
				elif OX==True: pass
				else:
					if self.Level=="3":
						if j%n==n-1: print(n*i+j+1,end=" ")
						else: print(n*i+j+1,end=" | ")
					else:
						if j%n==n-1: print(i+1,j+1,end=" ",sep="")
						else: print(i+1,j+1,end=" | ",sep="")

			if i%n!=n-1:
				if OX==False and self.Level!="3": print("\n","-----"*n,"\b\b\b\t\t\t","-----"*n,sep="")
				else: print("\n","----"*n,"\b\b\b   ",sep="")

	def ToClassic(self,num):
		if num>6: return num-6
		if num<4: return num+6
		return num

	def Welcome(self):
		print("*"*100,"\n\tWelcome To ThyR. Han's implementation of TicTacToe.\n","*"*100,sep="",end="\n\n")

	def GetOpts(self):
		self.P2="?"
		self.Level="?"
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

		while(self.Level=="?"):
			self.Welcome()
			self.Level=input("Which Difficulty Level Do You Want To Play: \nA: Basic(3x3)\nB: Advanced(4x4)\nC: Custom\nEnter Your Choice: ")
			if(self.Level in ["A","a","3"]): self.Level="3"
			elif(self.Level in ["B","b","4"]): self.Level="4"
			elif(self.Level in ["C","c","3"]): self.Level="C"
			else: self.Level="?"
			system("cls")

		while(self.Level=="C"):
			self.Welcome()
			self.Level=input("How Many Rows/Columns Do You Want To Have: \nEnter Your Choice: ")
			if(self.Level not in ["3","4","5","6","7","8","9"]): self.Level="C"
			system("cls")

		if self.Level =="3":
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
		while(1):
			try:
				tmp=int(input("Which Maneuver You Want To Perform: "))
				break
			except: 
				pass
		if(tmp not in self.Game):
			if(self.Mode=="M"): self.Game[i]=self.ToClassic(tmp)
			else: self.Game[i]=tmp

	def UpdateStatus(self):
		self.G=[self.Game[1::2],self.Game[0::2]]
		for P in range(2):
			for i in range(3):
				if all(3*i+j in self.G[P] for j in range(1,4)): self.Status=P+1
				if all(i+j in self.G[P] for j in range(1,9,3)): self.Status=P+1
				if all(i in self.G[P] for i in [1,5,9]) or all(i in self.G[P] for i in [3,5,7]): self.Status=P+1
		if(self.Game[8]!=0): self.Status=3

	def StartGame(self):
		self.Game=[0,0,0,0,0,0,0,0,0]
		self.Status=0 # 	0 -> Ongoing;	1 -> X Wins;	2 -> O Wins;	3 -> Draw;
		system("cls")
		self.GetOpts()
		while(self.Status==0):
			self.Welcome()
			self.showGame(self.Game,OX=True)
			print("\n")
			self.Input()
			self.UpdateStatus()
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
	



TicTac = TicTacToe()
# TicTac.GetOpts()
# TicTac.showGame([7,8,9,4,5,6,1,2,3],[1,2,3,4,5,6,7,8,9])
# TicTac.showGame([7,8,9,4,5,6,1,2,3])
TicTac.StartGame()
