import random
def out(inp):
    if inp=="rock" or inp==1:
        print("""
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
""")
    elif inp=="paper" or inp==2:
        print("""
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
""")
    elif inp=="scissors" or inp==3:
        print("""
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
""")
def process(G):
    if G==1:
        print("Rock Paper or Scissors? ")
        rps=input()
        inp=rps.lower()
        out(inp)
        print("\nComputer plays:\n")
        R=random.randint(1,3)
        out(R)
        L=["rock","paper","scissors"]
        if inp==L[R-1]:
            print("DRAW!! 🤠")
        elif (inp=="rock" and R==2) or (inp=="paper" and R==3) or (inp=="scissors" and R==1):
            print("COMPUTER WINS!! 😎")
        elif (inp=="scissors" and R==2) or (inp=="rock" and R==3) or (inp=="paper" and R==1):
            print("YOU WIN!! 🎊")
        X=input("\nDo you want to continue? (Enter 1 to continue or any other key to quit)\nEnter your choice: ")
        Y=int(X)
        process(Y)
    else:
        return 0
process(1)
