import os


class Menu:
    def __init__(self):
        print("Welcome to the console file manager!For start working write a 'help'")
        self.dir = os.getcwd()
        self.step = ["start", "help", "exit"]

    def (self):
        print(f"It is your current path :{self.dir}")

    def help(self):
        self.command = {"help":"print annotation for all commands",
                        "currentdir":"show your current directory",
                        "newdir":"create a new folder",
                        "deletedir":"delete a folder",
                        "createfile":"create a new file",
                        "deletefile":"delete a file",
                        "writefile":"write the text to the file",
                        "openfile":"viewing file contents",
                        "copyfile":"copies the file to another folder",
                        "movefile":"moves the file to another folder",
                        "renamefile": "changes the name of the file",
                        ""

                        }