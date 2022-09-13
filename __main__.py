
from socket import *
import queue
import threading


# function used to write to a file
def write_to_file(file_name, lst_info):
    with open(file_name, 'w') as f:
        for line in lst_info:
            f.write(str(line))


def fill_q(q, list_var):
    for i in list_var:
        q.put(i)

def scan_from_q(q, target, open_ports):
    # loop throught the q 
    while not(q.empty()):
        # pull element from q
        i = q.get()
        
        # create a socket for a regular ip addess
        s = socket(AF_INET, SOCK_STREAM)
        
        # use the connect_ex func to attemp to connecto to a port
        # the member function will return a 0 if the connection succeeded
        conn = s.connect_ex((target, i))
        if conn == 0:
            # print the result only if success
            print(f"Port {i} is open")
            open_ports.append(i)
        s.close()


def main():
    # ask for user input
    print("---------------------------------------") 
    target = input("Enter the host to be scanned: ")
    print("starting scan on host: " + target)
    min_port = input("what starting port would you would like to scan: ")
    max_port = input("what is the last port you would like to scan: ")
    common_port_flag = input("Would you like to scan all common ports?: ")
    write_to_file_flag = input("Would you like to write output to a file?: ")
    print("---------------------------------------")
    print("beginning scan...")

    # common ports const
    common_ports = 1023
    # create queue
    q = queue.Queue()

    if common_port_flag == 'y':
        list_var = [j for j in range(1,common_ports)]
    else:
        # create list, with ports based on user input
        list_var = [j for j in range(int(min_port), int(max_port))]
    
    # fill the q with the list values
    fill_q(q, list_var)
    
    # create a list to store open ports in 
    open_ports = []
    # create a list to store threads
    threads = []
    # create a bunch of thread objects, and add to list
    for i in range(0,100):
        thread = threading.Thread(target=scan_from_q, args=[q, target, open_ports])
        threads.append(thread)

    # start their functions
    for t in threads:
        t.start()
    
    # end the thread's functions
    for t in threads:
        t.join()
    
    #notify about success
    print("finished")
    print(f"the open ports are: {open_ports}")

    if write_to_file_flag == 'y':
        print("writing to file...")
        write_to_file("output.txt", open_ports)



if __name__ == "__main__":
    main()
