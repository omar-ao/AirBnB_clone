#!/usr/bin/python3
"""The Class HBNBCommand
This module contains the command console for HBnB.
"""


import cmd
from models import storage
from models.base_model import BaseModel


class_mapping = {
        "BaseModel": BaseModel
        }

class HBNBCommand(cmd.Cmd):
    """The HBnBCommand interpreter"""

    prompt = '(hbnb) '

    def do_create(self, line):
        """
        Creates a new instance and saves it to 
        JSON file and prints the instance id
        """
        class_name = line
        if invalid_class_name(class_name):
            return

        obj = class_mapping[class_name]()
        print(obj.id)
        storage.save()

    def do_show(self, line):
        """
        Prints the string representation of an instance
        based on the class name and id
        """
        if invalid_input(line):
            return
        args = list(line.split(" "))
        class_name, instance_id = args[:2]
        key = class_name + "." + instance_id
        objects = storage.all()
        print(objects[key])

    def do_destroy(self, line):
        """
        Deletes an instances based on the class and id
        """

        if invalid_input(line):
            return
        args = list(line.split(" "))
        class_name, instance_id = args[:2]
        key = class_name + "." + instance_id
        objects = storage.all()
        del(objects[key])
        storage.save()

    def do_all(self, line):
        """
        Prints all string representation of all instances
        based or not on the class name
        """
        objects = storage.all()
        if line:
            class_name = list(line.split(" "))[0]
            if invalid_class_name(class_name):
                return
            for key in objects.keys():
                if class_name in key.split("."):
                    print(objects[key])
            return

        for key in objects.keys():
            print(objects[key])

    def do_update(self, line):
        """
        Updates an instance based on the class name and id
        by adding or updating attribute
        """

        if invalid_input(line):
            return
        args = list(line.split(" "))
        if len(args) == 2:
            print("** attribute name missing **")
            return
        if len(args) == 3:
            print("** value missing **")
            return

    def do_quit(self, line):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, line):
        """Ctrl+D: Exits the program"""
        return True

    def emptyline(self):
        """Does nothing for *empty line + ENTER* (overide)"""
        pass

def invalid_input(line):
    """Validates input line"""
    args = list(line.split(" "))
    num_args = len(args)
    if num_args == 1:
        if invalid_class_name(line):
            return True
        invalid_instance_id(line, "")
        return True

    elif num_args in [2, 3, 4]:
        class_name, instance_id = args[:2]
        if invalid_class_name(class_name):
            return True
        if invalid_instance_id(class_name, instance_id):
            return True

    return False

def invalid_class_name(class_name):
    """
    Handles missing and invalid class name
    """
    if not class_name:
        print("** class name missing **")
        return True
    elif class_name not in class_mapping:
        print("** class doesn't exist **")
        return True
    return False

def invalid_instance_id(class_name, instance_id):
    """
    Handles missing and invalid instance id
    """
    if not instance_id:
        print("** intance id missing **")
        return True
    key = class_name + "." + instance_id
    objects = storage.all()
    if not objects:
        return True
    if key not in objects.keys():
        print("** no instance id found **")
        return True
    return False

if __name__ == '__main__':
    HBNBCommand().cmdloop()
