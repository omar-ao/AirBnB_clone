#!/usr/bin/python3
"""The Class HBNBCommand
This module contains the command console for HBnB.
"""


import cmd
from models import storage
from models.base_model import BaseModel

class HBNBCommand(cmd.Cmd):
    """The HBnBCommand interpreter"""

    prompt = '(hbnb) '

    class_mapping = {
            "BaseModel": BaseModel
            }

    def do_create(self, class_name):
        """Creates a new instance and saves it to JSON file
        and prints the instance id
        """
        if not class_name:
            print("** class name missing **")
            return
        elif class_name not in self.class_mapping:
            print("** class doesn't exist **")
            return
        obj = self.class_mapping[class_name]()
        print(obj.id)
        storage.save()

    def do_quit(self, line):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, line):
        """Ctrl+D: Exits the program"""
        return True

    def emptyline(self):
        """Does nothing for *empty line + ENTER* (overide)"""
        pass

if __name__ == '__main__':
    HBNBCommand().cmdloop()
