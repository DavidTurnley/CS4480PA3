
# import subprocess

import os

import sys

import time

from typing import cast

routerNames = ["Router1", "Router2", "Router3", "Router4"]

routerConnections = {"Router1":[0,2,4], "Router2": [1, 3], "Router3": [2, 4, 5], "Router4": [1, 3]}
routerID = {"Router1":1, "Router2":2, "Router3":3, "Router4":4}

def daemonCmd(router:str, input:str):
    os.system("docker exec -it " + router + " vtysh -c \'" + input + "\'")

def configure(router:str, input:list[str]):
    out = "docker exec -it " + router + " vtysh -c \"configure terminal\""
    for i in input:
        out += " -c \"" + i + "\""
    out += " -c \"end\""
    print(out)
    os.system(out)

    daemonCmd(router, "write memory")

def setLinkWeights(router:str, val:int):
    cmds = ["Filler"]
    connections = routerConnections.get(router)
    for i in range(len(connections)) :
        cmds.clear()
        cmds.append("interface eth" + str(i))
        cmds.append("ip ospf cost " + str(val))
        configure(router, cmds)


userInput = ""
userInput = cast(str, userInput)

while not userInput.startswith("q") :

    userInput = input("Input Command ['q' or \"quit\" to quit, 'h' for help]\n")

    parsed = userInput.lower()

    if(parsed == "h" or parsed == "help"):
        print("[q][quit]  to quit the program")
        print("[h][help]  to show this help page")
        print("[setup]    if docker needs to be installed/doing sudo bash")
        print("              Should be run BEFORE start, but only needs to run once")
        print("[start]    starts containers and initializes them")
        print("              Will take a while, \"FINISHED\" text will print when done")
        print("[stop]     stops/shuts down the containers")
        print("[north]    to swap traffic to the norh path")
        print("[south]    to swap traffic to the south path")
        print("[oneach X] to run a vtysh command \"X\" on each router")
        print("[ping]     perform a ping from HostA to HostB")
    
    if(parsed == "setup"):
        os.system("bash dockersetup")
        os.system("sudo bash")

    if(parsed == "start"):

        '''
        os.system("docker compose up -d")
        os.system("docker compose build")
        for r in routerNames:
            msg = "docker cp ./daemons "+ r +":etc/frr/"
            print(msg)
            os.system(msg)
        for r in routerNames:
            msg = "docker exec -it "+ r +" service frr restart"
            print(msg)
            os.system(msg)

        os.system("docker exec -it HostA route add -net 10.0.35.0/24 gw 10.0.10.11")
        os.system("docker exec -it HostB route add -net 10.0.10.0/24 gw 10.0.35.13")
        '''

        print("make start")
        os.system("make start")

        print("Finished Make...")
        time.sleep(1.5)

        for router in routerNames:
            id = routerID.get(router)
            connections = routerConnections.get(router)

            cmds = ["router ospf"]

            cmds.append("ospf router-id 10.0.10" + str(id) + ".1" + str(id))
            for connection in connections:
                subnet = str(min(id, connection)) + str(max(id,connection))
                if(subnet == "01"):
                    subnet = "10"
                cmds.append("network 10.0." + subnet + ".0/24 area 0.0.0.0")

            configure(router, cmds)

            for i in range(len(connections)) :
                cmds.clear()
                cmds.append("interface eth" + str(i))
                cmds.append("ip ospf cost 5")
                configure(router, cmds)

        os.system("docker exec -it HostA ping -c 5 10.0.10.11")

        cmd = "show ip ospf neighbor"
        for router in routerNames:
            daemonCmd(router, cmd)

        print("\n\n\n\n\nFINISHED!\n\n\n")

    if(parsed == "stop"):
        print("docker compose down")
        os.system("docker compose down")

    if(parsed == "south"):
        setLinkWeights("Router2", 100)
        setLinkWeights("Router4", 1)

    if(parsed == "north"):
        setLinkWeights("Router4", 100)
        setLinkWeights("Router2", 1)

    if(parsed == "ping"):
        os.system("docker exec -it HostA ping -c 5 10.0.35.15")
    
    if(parsed.startswith("oneach")):
        cmd = userInput.split(" ", 1)[1]
        for router in routerNames:
            print(router + ": ")
            daemonCmd(router, cmd)
        print("Finished!")


                

            


        



