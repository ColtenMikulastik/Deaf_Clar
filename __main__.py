
from socket import *

def main():
    # ask for user input
    target = input("Enter the host to be scanned: ")
    print("starting scan on host: " + target)

    # loop through ports
    for i in range(1, 500):
        # create a socket object
        s = socket(AF_INET, SOCK_STREAM)
        # attempt to connect to target at i port
        conn = s.connect_ex((target, i))
        # print port number if found
        if conn == 0:
            print("Port " + str(i) + ": Open")
        s.close()


if __name__ == "__main__":
    main()
