import sys

if len(sys.argv) == 2:
    count_z = sys.argv[1].count("z")
    if count_z == 0:
        print("none")
    else:
        print("z" * count_z)
else:
    print("none")