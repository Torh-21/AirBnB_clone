#!/usr/bin/env python3
""" This contains the entry point to the command interpreter """

import cmd
#from models.base_model import BaseModel
#from models.storage import storage


def parse(input_string):
    """ This processes the input string and return it in a parsed format """

    curly_braces_match = re.search(r"\{(.*?)\}", input_string)
    square_brackets_match = re.search(r"\[(.*?)\]", input_string)

    if curly_braces_match is None:
        if square_brackets_match is None:
            # Handle cases where neither curly braces nor square brackets are present.
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
            "BaseModel"
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

    def do_create(self, arg):
        """ Ex: create <class>
        Creates a new instance of a class, saves it (to the JSON file)
        and prints the id
        """

        class_name = parse(arg)
        if len(class_name) == 0:
            print("** class name missing **")
        elif class_name[0] not in HBNBcommand.__classes:
            print("** class doesn't exist")
        else:
            print(eval(class_name[0]().id))
            storage.save()

    def do_show(self, arg):
        """ Ex: show <class> <id> or <class>.show(<id>)
        Prints the string representation of an instance based on the class name and id.
        """

        class_id = parse(arg)
        objdict = storage.all()

        if len(class_id) == 0:
            print("** class name missing **")
        elif class_id[0] not in HBNBcommand.__classes:
            print("** class doesn't exist**")
        elif len(class_id) == 1:
            print("** instance id missing **")
        elif "{}.{}".format(class_id[0], class_id[1]) not in objdict:
            print("** no instance found **")
        else:
            print(objdict["{}.{}".format(class_id[0], class_id[1])])

    def do_destroy(self, arg):
        """ Ex: destroy <class> <id> or <class>.destroy(<id>)
        Deletes an instance based on the class name and id (save the change into the JSON file)
        """

        class_id = parse(arg)
        objdict = storage.all()

        if len(class_id) == 0:
            print("** class name missing **")
        elif class_id[0] not in HBNBcommand.__classes:
            print("** class doesn't exist**")
        elif len(class_id) == 1:
            print("** instance id missing **")
        elif "{}.{}".format(class_id[0], class_id[1]) not in objdict.keys():
            print("** no instance found **")
        else:
            del objdict["{}.{}".format(class_id[0], class_id[1])]
            storage.save()

    def do_all(self, arg):
        """ Ex: all or all <class>
        Prints all string representation of all instances based or not on the class name
        """

        class_name = parse(arg)
        if len(class_name) > 0 and class_name[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        else:
            obj = []
            for obj in storage.all.values():
                if len(class_name) > 0 and class_name[0] == obj.__class__.__name__:
                    obj.append(obj.__str__())
                elif len(class_name) == 0:
                    obj.append(obj.__str())
            print(obj)


if __name__ == "__main__":
    HBNBCommand().cmdloop()
