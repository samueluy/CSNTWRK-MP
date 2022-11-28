import server
import commands

command = input()
command_values = command.split(" ")

if(command[0] == "/join"):
    # Need to add error checking
    ip_address = command_values[1]
    port_num = command_values[2]

    server.connect_to(ip_address, port_num)

