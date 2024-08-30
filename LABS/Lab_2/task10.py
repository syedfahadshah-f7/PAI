def build_message(**info):
    output = ""
    for i in info:
        output += f"{i} : {info[i]}\n"
    return output

print(build_message(Name = "Fahad", Age = 19, City = "Karachi"))