import sys #This is for commandline stuff and console, /cmd shit.
import socket #This allows for port connection capabilities.
from datetime import datetime as dt

#Defining Our Target.
if len(sys.argv) == 2:
    target = socket.gethostbyname(sys.argv[1])
else:
    print("Invalid amount of arguments.")
    sys.exit()

#Banner/Display.
print("-" * 50)
print("Scanning: " + target)
print("Scan Started: " + str(dt.now()))
print("-" * 50)

#Scanning Functionality.
try:
    for port in range(50,85):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket.setdefaulttimeout(1)
        result = s.connect_ex((target, port))
        print("Checking port {}:".format(port))
        if result == 0:
            print("Port {}: open".format(port))
        s.close

except KeyboardInterrupt:
    print("\nExiting program.")
    sys.exit()

except socket.gaierror:
    print("Hostname could not be resolved.")
    sys.exit()

except socket.error:
    print("Couldn't connect to server.")
    sys.exit()