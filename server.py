import sys
from socket import socket, AF_INET, SOCK_DGRAM

def build_dictionary():
    d = {}
    # copy the file data
    with open(sys.argv[4], 'r') as fi:
        file_data = fi.readlines()
    # read every line from the file
    for line in file_data:
        if line not in ['\n', '\r\n'] :
            # split to key and value
            columns = line.split(',')
            # insert to the dictionary
            d[columns[0]] = columns[1].replace('\n', '')
    # return the dictionary
    return d


def ask_parent(key):
    parnet_ip = sys.argv[2]
    parnet_port = int(sys.argv[3])
    # build socket
    soc = socket(AF_INET, SOCK_DGRAM)
    # send question to parent
    soc.sendto(key, (parnet_ip, parnet_port))
    # get answer from parent
    ans, parent_info = soc.recvfrom(2048)
    # close socket
    soc.close()
    # return the new value
    return ans


def learn(key):
    # check if the server has a parent
    if sys.argv[2] == "-1" or sys.argv[3] == "-1":
        return "unknown"
    # ask parent for new value
    new_ip = ask_parent(key)
    # add the new key and value to the dictionary
    dic[key] = new_ip
    # add the new key and value to the file
    with open(sys.argv[4], 'a') as f:
        #f.write('\n' + key + ',' + new_ip + '\n')
        f.write(key + ',' + new_ip + '\n')
    return new_ip


# build a dictionary from file data
dic = build_dictionary()
# build socket
s = socket(AF_INET, SOCK_DGRAM)
source_ip = '0.0.0.0'
source_port = int(sys.argv[1])
s.bind((source_ip, source_port))
# get messages
while True:
    data, sender_info = s.recvfrom(2048)
    # check if key is in the dictionary
    if data in dic:
        ip = dic[data]
    else:
        # ask for value, and add the key to the dictionary
        ip = learn(data)
    # send answer
    s.sendto(ip, sender_info)
