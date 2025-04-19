
# Made entirely by David Turnley (u1283279)

# Setup Instructions:

Assuming that this tarball has been unzipped already, and that the current directory is the folder in
which this README is contained.

These steps are assuming that this program is being run on a fresh instance of the powder emulator
that we are given in this class. If docker is already installed, and the terminal that will run
the orchestrator has already been "sudo bash"'d, then you can start with step 4.

Step 1: type "python David_Turnley_u1283279.py"
Step 2: input "setup" for the program once prompted
Step 3: wait for setup sequence
Step 4: type "python David_Turnley_u1283279.py" again
Step 5: input "start" for the program once prompted
Step 6: wait for docker to finish starting up. This will take on the order of 5 minutes
        and when complete, will type "FINISHED" into the console

Step 7: frr sometimes needs some time to distribute the information, so repeat inputting
        "ping" into the program until there is a ping with 0% packet loss. This usually takes
        <5 times to finish

Step 8: After a successful ping, the network should be ready

# Details

Each container is named one of "Router1, Router2, Router3, Router4, HostA, HostB" in case you
need to docker attach to one of them, and the topology of them is the same as is described
within the assignment PDF. 

For the IP topology, HostA is 10.0.10.10 and HostB is 10.0.35.15

So assuming you are attatched to HostA, to ping HostB would be the command:
    ping 10.0.35.15

# Orchestrator

I found it useful for the orchestrator to be a while loop that keeps accepting input commands
while running, so that is what it does. To exit this loop, typing "q" or "quit" as input work,
and along with this, typinng "help" displays help info for the program, the same that is
produced when running the program with a -h flag. 

As for functionality, I took the approach of having the orchestrator perform commands within
the shell. This was explicitely asked about in class, and was approved by the proffessor as
a method for completing this assignment. 

To change paths, type "north" into the orchestrator to have it go along the path:
    HostA - Router1 - Router2 - Router3 - HostB

and then typnig "south" will have it go along the path:
    HostA - Router1 - Router4 - Router 3 - HostB