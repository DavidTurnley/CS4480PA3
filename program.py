
# import subprocess

import os

import sys

from typing import cast

routerNames = ["Router1", "Router2", "Router3", "Router4"]

routerConnections = {"Router1":[0,2,4], "Router2": [1, 3], "Router3": [2, 4, 5], "Router4": [1, 3]}
routerID = {"Router1":1, "Router2":2, "Router3":3, "Router4":4}

def daemonCmd(router:str, input:str):
    os.system("docker exec -it " + router + " vtysh -c \'" + input + "\'")

def configure(router:str, input:list[str]):
    out = "docker exec -it " + router + "vtysh -c \"configure terminal\" "
    for i in input:
        out += "-c \"" + i + "\" "
    os.system(out)

userInput = ""
userInput = cast(str, userInput)

while not userInput.startswith("q") :

    userInput = input("Input Command ['q' or \"quit\" to quit, 'h' for help]\n")

    parsed = userInput.lower()

    if(parsed == "h" or parsed == "help"):
        print("[q][quit] to quit the program")
        print("[h][help] to show this help page")
    
    if(parsed == "start"):
        os.system("git clone https://github.com/DavidTurnley/CS4480PA3")
        os.system("cd CS4480PA3")
        os.system("./dockersetup")
        os.system("sudo bash")
        os.system("make start")

    if(parsed == "setup"):
        for router in routerNames:
            id = routerID.get(router)
            connections = routerConnections.get(router)

            # daemonCmd(router, "configure terminal")

            #daemonCmd(router, "router ospf")

            cmds = ["Filler"]

            cmds.clear()

            cmds.append("ospf router-id 10.0.10" + str(id) + ".1" + str(id))

            #daemonCmd(router, "ospf router-id 10.0.10" + str(id) + ".1" + str(id))
            for connection in connections:
                subnet = str(min(id, connection)) + str(max(id,connection))
                if(subnet == "01"):
                    subnet = "10"
                #daemonCmd(router, "network 10.0." + subnet + ".0/24 area 0.0.0.0")
                cmds.append("network 10.0." + subnet + ".0/24 area 0.0.0.0")
            # daemonCmd(router, "exit")

            configure(router, cmds)

            for i in range(len(connections)) :
                cmds.clear()
                cmds.append("interface eth" + str(i))
                cmds.append("ip ospf cost 5")
                configure(router, cmds)

                

            


        



