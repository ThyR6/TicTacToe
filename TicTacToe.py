from os import system

class TicTacToe:
	def showGame(self):
		for i in range(3):
			for j in range(3):
				if j%3==2: print(3*i+j+1,end=" ")
				else: print(3*i+j+1,end=" | ")
			if i%3!=2: print("\n---------")

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

		while(self.Mode=="?"):
			self.Welcome()
			self.Mode=input("Which Mode Do You Want To Play: \nA: Classic\nB: Modern\nEnter Your Choice: ")
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


TicTac = TicTacToe()
TicTac.GetOpts()
TicTac.showGame()
