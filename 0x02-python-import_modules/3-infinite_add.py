#!/usr/bin/python3
<<<<<<< HEAD

=======
>>>>>>> 88c1345aaebccb5e0c5c05aae7878062d51c361d
if __name__ == "__main__":
    import sys

<<<<<<< HEAD
    total = 0

    for i in range(len(sys.argv) - 1):

        total += int(sys.argv[i + 1])

    print("{}".format(total))
=======
    count = len(sys.argv) - 1
    if count == 0:
        print("0 arguments.")
    elif count == 1:
        print("1 argument:")
    else:
        print("{} arguments:".format(count))
    for i in range(1, count + 1):
        print("{}: {}".format(i, sys.argv[i]))
>>>>>>> 88c1345aaebccb5e0c5c05aae7878062d51c361d
