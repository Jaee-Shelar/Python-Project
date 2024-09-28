#PRINCESS GAME
name=input("Enter your name:")
print("welcome",name,"to this  amazing game .")

print("Let's see which kind of princess are you.")

questions=(("1. choose any one of the following:"),
           ("2. what is your nature:"),
           ("3.Your proffesion would be :"),
           ("4.How you spent your free time:"),
           ("5. What is your soul element?"))

options= (("A.Dancing","B.Adventure","C.Sport","D.Singing"),
         ("A.Be kind", "B.Caring", "C.Disciplined", "D.Curious"),
         ("A.Curious,intelligent,outgoing","B.Intuitive,romantic,caring","C.kind,deligent,hopeful","D.Brave,selfless,tough"),
         ("A.helping parents", "B.Reading book",  "C.Playing Games", "D.Painting"),
         ("A.earth", "B.Air", "C.Water" , "D.Fire"))
score=0
question_num=0

for question in questions:
    print("-------------------------------------------")
    print(questions)
    for option in options[question_num]:
        print(option)