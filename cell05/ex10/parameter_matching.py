import sys

if len(sys.argv) == 2:
    word = input("What was the parameter? ")
    if sys.argv[1] == word:
        print("Good job!")
    else:
        print("Nope, sorry...")
else: 
    print ("none")