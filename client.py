import socket
UDP_IP_ADDRESS = "127.0.0.1"
UDP_PORT_NO = 6789

input = input()
input_list = input.split(" ")
command = input_list[0]

if command == '/msg':
    message = ' '.join(input_list[2:]).encode()  # get index 2 till the end

# match command: # switch
#     case "/leave":
#         pass
#     case "/register":
#         pass
#     case "/all":
#         pass
#     case "/msg":
#         message = ' '.join(input_list[2:])  # get index 2 till the end
#     case "/?":
#         pass
#     case _:
#         "Error: Command not found."



clientSock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
clientSock.sendto(message, (UDP_IP_ADDRESS, UDP_PORT_NO))



