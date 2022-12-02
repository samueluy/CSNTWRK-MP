import socket
import json
UDP_IP_ADDRESS = "127.0.0.1"
UDP_PORT_NO = 6789

def convert_and_send(sock, data, ip_and_port): # convert and send json to server;
    json_data = json.dumps(data) #convert to json
    try: # error checking
        sock.sendto(json_data.encode(), ip_and_port) # send to server   
        return 1
    except:
        return 0

try:
    clientSock = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
except socket.error as err:
    print("Socket error because of %s", err)

input = input()
input_list = input.split(" ")
command = input_list[0]

match command: # still need to check for command parameters
    case "/join":
        command_dict = {"command": command} # convert to dict
        if not convert_and_send(clientSock, command_dict, (UDP_IP_ADDRESS, UDP_PORT_NO)): # run and check if successful
            print("Error: Connection to the Message Board Server has failed! Please check IP Address and Port Number.")
        
    case "/leave": #
        command_dict = {"command": command}
        if not convert_and_send(clientSock, command_dict, (UDP_IP_ADDRESS, UDP_PORT_NO)):
            print("Erorr: Disconnection failed. Please connect to the server first.")
    
    case "/all":
        message = ' '.join(input_list[1:]) # get index 1 till the end for message
        msg_data = {"command": command, "message": message} # convert to dict
        convert_and_send(clientSock, msg_data, (UDP_IP_ADDRESS, UDP_PORT_NO))

    case "/register":
        handle = input_list[1] # get handle
        reg_data = {"command": command, "handle": handle} #convert to dict
        if not convert_and_send(clientSock, reg_data, (UDP_IP_ADDRESS, UDP_PORT_NO)):
            print("Registration failed. Handle or alias already exists.")

    case "/msg":
        handle = input_list[1] # get handle
        message = ' '.join(input_list[2:])  # get index 2 till the end for message
        msg_data = {"command": command, "handle": handle, "message": message} # convert to dict
        if not convert_and_send(clientSock, msg_data, (UDP_IP_ADDRESS, UDP_PORT_NO)):
            print("Handle or alias not found")

    case "/?":
        command_dict = {"command": command}
        convert_and_send(clientSock, command_dict, (UDP_IP_ADDRESS, UDP_PORT_NO))
    
    case _:
        print("Error: Command not found") 