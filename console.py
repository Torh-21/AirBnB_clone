#!/usr/bin/env python3
""" This contains the entry point to the command interpreter """

import cmd
import re
from shlex import split
from models.amenity import Amenity
from models.base_model import BaseModel
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models import storage
from models.user import User


def parse(input_string):
    """ This processes the input string and return it in a parsed format """

    curly_braces_match = re.search(r"\{(.*?)\}", input_string)
    square_brackets_match = re.search(r"\[(.*?)\]", input_string)

    if curly_braces_match is None:
        if square_brackets_match is None:
            # Handle cases where neither curly braces nor square brackets
            # are present.
            return [item.strip(",") for item in split(input_string)]
        else:
            # Handle cases where square brackets are present.
            tokens = split(input_string[:square_brackets_match.span()[0]])
            result_list = [item.strip(",") for item in tokens]
            result_list.append(square_brackets_match.group())
            return result_list
    else:
        # Handle cases where curly braces are present.
        tokens = split(input_string[:curly_braces_match.span()[0]])
        result_list = [item.strip(",") for item in tokens]
        result_list.append(curly_braces_match.group())
        return result_list


class HBNBCommand(cmd.Cmd):
    """ Implement the command interpreter

    Attributes:
        prompt (str): The command prompt
        __classes (dict): The available classes
    """

    prompt = "(hbnb) "
    __classes = {
            "Amenity",
            "BaseModel",
            "City",
            "Place",
            "Review",
            "State",
            "User"
            }

    def do_quit(self, arg):
        """ Quit command to exit the program """
        return True

    def do_EOF(self, arg):
        """ Sends EOF signal to exit the program """
        print("")
        return True

    def emptyline(self):
        """ Does nothing """
        pass

    def do_create(self, user_input):
        """ Usage: create <class>
        Creates a new instance of a class, saves it (to the JSON file)
        and prints the id
        """

        class_name = parse(user_input)
        if len(class_name) == 0:
            print("** class name missing **")
        elif class_name[0] not in HBNBCommand.__classes:
            print("** class doesn't exist**")
        else:
            print(eval(class_name[0])().id)
            storage.save()

    def do_show(self, user_input):
        """ Usage: show <class> <id> or <class>.show(<id>)
        Prints the string representation of an instance based on
        the class name and id.
        """

        class_id = parse(user_input)
        objdict = storage.all()

        if len(class_id) == 0:
            print("** class name missing **")
        elif class_id[0] not in HBNBCommand.__classes:
            print("** class doesn't exist**")
        elif len(class_id) == 1:
            print("** instance id missing **")
        elif "{}.{}".format(class_id[0], class_id[1]) not in objdict:
            print("** no instance found **")
        else:
            print(objdict["{}.{}".format(class_id[0], class_id[1])])

    def do_destroy(self, user_input):
        """ Usage: destroy <class> <id> or <class>.destroy(<id>)
        Deletes an instance based on the class name and id
        (save the change into the JSON file)
        """

        class_id = parse(user_input)
        objdict = storage.all()

        if len(class_id) == 0:
            print("** class name missing **")
        elif class_id[0] not in HBNBCommand.__classes:
            print("** class doesn't exist**")
        elif len(class_id) == 1:
            print("** instance id missing **")
        elif "{}.{}".format(class_id[0], class_id[1]) not in objdict.keys():
            print("** no instance found **")
        else:
            del objdict["{}.{}".format(class_id[0], class_id[1])]
            storage.save()

    def do_all(self, user_input):
        """ Usage: all or all <class>
        Prints all string representation of all instances
        based or not on the class name
        """

        class_name = parse(user_input)
        if len(class_name) > 0 and class_name[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        else:
            objl = []
            for obj in storage.all().values():
                if len(class_name) > 0 and class_name[0] == obj.__class__.__name__:
                    objl.append(obj.__str__())
                elif len(class_name) == 0:
                    objl.append(obj.__str__())
            print(objl)

    def do_update(self, user_input):
        """ Usage:
        update <class name> <id> <attribute name> "<attribute value>"

        Updates an instance based on the class name and id by adding or
        updating attribute (save the change into the JSON file).
        """

        parsed_input = parse(user_input)
        instance_dict = storage.all()

        if len(parsed_input) == 0:
            print("** class name missing **")
            return False
        if parsed_input[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
            return False
        if len(parsed_input) == 1:
            print("** instance id missing **")
            return False
        instance_key = "{}.{}".format(parsed_input[0], parsed_input[1])
        if instance_key not in instance_dict.keys():
            print("** no instance found **")
            return False
        if len(parsed_input) == 2:
            print("** attribute name missing **")
            return False
        if len(parsed_input) == 3:
            try:
                attr_value = eval(parsed_input[2])
                if not isinstance(attr_value, dict):
                    raise NameError
            except NameError:
                print("** value missing or not a dictionary **")
                return False

        if len(parsed_input) == 4:
            instance = instance_dict[instance_key]
            attr_name = parsed_input[2]
            if attr_name in instance.__class__.__dict__.keys():
                attr_type = type(instance.__class__.__dict__[attr_name])
                instance.__dict__[attr_name] = attr_type(parsed_input[3])
            else:
                instance.__dict__[attr_name] = parsed_input[3]
        elif isinstance(eval(parsed_input[2]), dict):
            instance = instance_dict[instance_key]
            for key, value in eval(parsed_input[2]).items():
                if (
                    key in instance.__class__.__dict__.keys() and
                    type(instance.__class__.__dict__[key]) in {str, int, float}
                ):
                    attr_type = type(instance.__class__.__dict__[key])
                    instance.__dict__[key] = attr_type(value)
                else:
                    instance.__dict__[key] = value
        storage.save()


if __name__ == "__main__":
    HBNBCommand().cmdloop()
