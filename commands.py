
# .split (ed) input = list data type
def commands(input):
    input_list = input.split(" ")
    match input_list[0]:
        case "/leave":
            pass
        case "/register":
            pass
        case "/all":
            pass
        case "/msg":
            message = ' '.join(input_list[2:]) # get index 2 till the end
        case "/?":
            pass
        case _:
            "Error: Command not found."