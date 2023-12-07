import os
import random
d={}
max=0
print("!!WELCOME TO THE GUUESS A NUMBER CHALLENGE!!")
number=random.randint(1,1000)
n1,n2=random.randint(1,100),random.randint(1,100)
maxlim,minlim=number+n1,number-n2
while True:
    print("Number is between",maxlim,"and",minlim)
    name=input("Enter name of guesser and if no guessers left enter no:")
    if name=="no":
        break
    guess=int(input("Enter guess:"))
    d[name]=d.get(name,0)+guess
    os.system('cls')
bestguess=abs(number-list(d.values())[0])
guessname=list(d.keys())
j=0
bestguessname=list(d.keys())[0]
for i in d:
    guess2=d[i]
    guess1=abs(number-d[i])
    if guess1<bestguess:
        bestguess=guess2
        bestguessname=guessname[j]
    j+=1
print("The winner is",bestguessname,"with a guess of",bestguess,"to the number",number)
    