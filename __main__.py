
from socket import *
import queue
import threading


def fill_q(q, list_var):
    for i in list_var:
        q.put(i)

def scan_from_q(q, target):
    while not(q.empty()):
        i = q.get()
        
        s = socket(AF_INET, SOCK_STREAM)
         
        conn = s.connect_ex((target, i))
        if conn == 0:
            print(f"Port {i} is open")
        s.close()


def main():
    # ask for user input
    target = input("Enter the host to be scanned: ")
    print("starting scan on host: " + target)

    q = queue.Queue()

    list_var = [j for j in range(1,500)]
    
    fill_q(q, list_var)

    threads = []
    for i in range(0,10):
        thread = threading.Thread(target=scan_from_q, args=[q, target])
        threads.append(thread)

    for t in threads:
        t.start()

    for t in threads:
        t.join()

    print("finished")



if __name__ == "__main__":
    main()
