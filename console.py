#!/usr/bin/python3
"""The Class HBNBCommand
This module contains the command console for HBnB.
"""


import cmd

class HBNBCommand(cmd.Cmd):
    """The HBnBCommand interpreter"""

    prompt = '(hbnb) '

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
