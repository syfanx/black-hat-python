import sys              # provides functions and variables which are used to manipulate different parts of the Python Runtime Environment. Allow access to system-specific parameters and functions.
import socket
import getopt
import threading
import subprocess

# define some global variables
listen = False
command = False
upload = False
execute = ""
target = ""
upload_destination = ""
port = 0