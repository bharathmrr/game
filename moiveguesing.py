#movieguessinggame
import time as t
import random as r
print("the game is loading......")
t.sleep(2)
movie=["animal","leo",'rrr','bahubali','athadu','pushpa','sita ramam','arjun reddy']
a1=input("enter first person name")
a2=input("enter second person name")
i=0
j=0
def person1(name):
	
	print("welcome ",name,"the guess the below movie name puzzle>>")
	
def person2(name):
	
	print("welcome ",name,"the guess the below movie name puzzle >.")
	
game="not over"
a=r.choice(movie)
blo=[]
apl=[]
for i in a:
	apl.append(i)

for i in a:
	blo.append(' - ')

game="not over"
tst=apl.copy()

while game=="not over":
	def per():
		person1(a1)
		for i in blo:
			print(i,end="")
		print()
		submit=input("ENTER THE WORD OF MOVIE NAME:  " )
		if(submit in apl):
			b=apl.index(submit)
			
			blo[b]=submit
			apl[b]="#"
			per()
		else:
			if blo==tst:
				return True
			else:
				print(submit,"is not there in movie puzzle so,now ",a2,"turn")
				pass
	def per1():
		person2(a2)	
		for i in blo:
			print(i,end="")
		print()
		submit=input("ENTER THE WORD OF MOVIE NAME : ")
		if(submit in apl):
			b=apl.index(submit)
			blo[b]=submit
			apl[b]="#"
			
			
			
			
			
			per1()
				
				
		else:
			if blo==tst:
				return True
			else:
				print(submit,"is not there in movie puzzle so,now ",a1,"turn") 
				pass
	
	S=True		
	
	while S==True:
		if(per()==True or per1()==True):
			
			game="over"
			break
		else:
			S=True
			
						
	
	
	 
	



















