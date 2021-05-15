# coding = utf-8
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

def usage():
    print "Netcat Replacement"
    print
    print "Usage: bhpnet.py -t target_host -p port"
    print "-l --listen        - listen on [host]:[port] for incoming connections"
    print "-e --execute=file_to_run   - execute the given file upon receiving a connection"
    print "-c --command           - initialize a command shell"
    print "-u --upload=destination    - upon receiving connection upload a file and write to [destination]"
    print
    print
    print "Examples: "
    print "bhpnet.py -t 192.168.0.1 -p 5555 -l -c"
    print "bhpnet.py -t 192.168.0.1 -p 5555 -l -u=c:\\target.exe"
    print "bhpnet.py -t 192.168.0.1 -p 5555 -l -e=\"cat /etc/passwd\""
    print "echo 'ABCDEFGHI' | ./bhpnet.py -t 192.168.11.12 -p 135"
    sys.exit(0)

def main():
    global listen
    global port
    global execute
    global command
    global upload_destination
    global target
     
    if not len(sys.argv[1:]):
         usage()
 
# read the commandline options

    try:
        opts, args = getopt.getopt(sys.argv[1:],"hle:t:p:cu:", ¬
        ["help","listen","execute","target","port","command","upload"])
except getopt.GetoptError as err:
        print str(err)
        usage()
     
     for o,a in opts:
        if o in ("-h","--help"):
             usage() 
        elif o in ("-l","--listen"):
            listen = True
        elif o in ("-e", "--execute"):
            execute = a
        elif o in ("-c", "--commandshell"):
            command = True
        elif o in ("-u", "--upload"):
            upload_destination = a