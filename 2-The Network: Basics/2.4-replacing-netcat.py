import sys              # provides functions and variables which are used to manipulate different parts of the Python Runtime Environment. Allow access to system-specific parameters and functions.
import socket           # provides various objects, constants, functions and related exceptions for building full-fledged network applications including client and server programs.
import getopt           # a parser for command line options whose API is designed to be familiar to users of the C getopt() function.
import threading        # run multiple threads (tasks, function calls) at the same time. Allows python to execute other code while waiting; easily simulated with the 'sleep' function.
import subprocess       # spawn new processes, connect to their input/output/error pipes, and obtain their return codes.

# define global variables
listen = False
command = False
upload = False
execute = ""
target = ""
upload_destination = ""
port = 0