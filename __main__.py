
from socket import *

def main():
    target = input("Enter the host to be scanned: ")
    print("starting scan on host: " + target)

    for i in range(1, 500):
        s = socket(AF_INET, SOCK_STREAM)
        conn = s.connect_ex((target, i))
        if conn == 0:
            print("Port " + str(i) + ": Open")
        s.close()


if __name__ == "__main__":
    main()
