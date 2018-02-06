#filename = "sample1.txt"

# def create_file():
#     with open(filename, "w") as file:
#         file.write("")

import datetime

filename = datetime.datetime.now()

def create_file():
    with open(filename.strftime("%Y-%m-%d-%H-%M")+".txt", "w") as file:
        file.write("")

create_file()