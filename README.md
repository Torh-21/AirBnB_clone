# AirBnB clone - The console

## About
This is a team project to build a clone of the [AirBnb](https://www.airbnb.com/).

The console is a command interpreter similar to the shell. It will help manage the initialization, serialization, deserialization and abstraction between objects and how they are stored.

The console would basically do the following:

* Create a new object (ex: a new User or a new Place)
* Retrieve an object from a file, a database etc…
* Do operations on objects (count, compute stats, etc…)
* Update attributes of an object
* Destroy an object

## Installation
First you git clone:
```bash
git clone https://github.com/MichaelOmoniyi/AirBnB_clone.git
```

Then you navigate to the AirBnB_clone directory:
```bash
cd AirBnB_clone
```

### Execution

In Interactive mode:
```bash
$ ./console.py
(hbnb) help

Documented commands (type help <topic>):
========================================
EOF  help  quit

(hbnb) 
(hbnb) 
(hbnb) quit
$
```

In Non-Interactive mode:
```bash
$ echo "help" | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb)
$
$ cat test_help
help
$
$ cat test_help | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb)
$
```

## Usage
* Start the console in interactive mode
```bash
$ ./console.py
(hbnb)
```

* To see available commands:
```bash
(hbnb) help

Documented commands (type help <topic>):
========================================
EOF  all count create destroy help quit show update

(hbnb)
```

* To Quit the console:
```bash
(hbnb) quit
$
```
