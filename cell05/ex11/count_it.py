import sys

if len(sys.argv) < 2:
    print("none")

else:
    print("parameters: "+ str(len(sys.argv)-1))
    for i in sys.argv[1:]:
        print(i + ": " + str(len(i)))