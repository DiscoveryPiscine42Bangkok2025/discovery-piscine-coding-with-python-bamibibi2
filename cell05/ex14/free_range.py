import sys

my_array = []
if len(sys.argv) == 3:
    for i in range(int(sys.argv[1]), int(sys.argv[2])+ 1):
        my_array.append(i)
    print(my_array)
else:
    print("none")