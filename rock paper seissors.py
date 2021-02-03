import random
Cchoice=["Rock","Paper","Scissors"]
while True:
    print("Rock Paper scissors game:")
    youwin,computerwin=0,0
    for i in range (1,4):
        print(f"Round {i} start:")
        print("Please select any option:")
        print("1.ROCK 2.PAPER 3.SCISSORS".split(" "))
        yourchoice=int(input("Enter any number:"))
        if yourchoice==1:
            print("You choose Rock")
            yourchoice="Rock"
        elif yourchoice==2:
            print("You choose Paper")
            yourchoice="Paper"
        elif yourchoice==3:
            print("You choose Scissors")
            yourchoice="Scissors"
        else:
            print("you have entered wrong choice")
            break
        computerchoice=random.choice(Cchoice)
        print(f"computer choose:{computerchoice}")
        if yourchoice==computerchoice:
            youwin+=1
            computerwin+=1
            print("Your match tied")
        elif (yourchoice=="Paper" and computerchoice=="Rock") or (yourchoice=="Rock" and computerchoice=="Scissors") or (yourchoice=="Scissors" and computerchoice=="Paper"):
            youwin+=1
            print("You won")
        else:
            computerwin+=1
            print("computer won")
        if youwin>computerwin:
            print(f"Your score:{youwin},computer score:{computerwin}")
            print("you have won it")
        elif computerwin>youwin:
            print(f"Your score:{youwin},computer score:{computerwin}")
            print("computer have won it")
        else:
            print("Match drawn")
            print(f"Your score:{youwin},computer score:{computerwin}")
    userchoice=input("Enter you want to continue (YEs/NO)")
    if userchoice=="YES" or userchoice=="Yes" or userchoice=="yes":
        continue
    else:
        break