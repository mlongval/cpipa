#!/usr/bin/python3
"""
CPIPA : Current  
        Public 
        IP  
        Address

This program will query a public IP address server.
The printed output from this program will be the PUBLIC IP address of the computer
(ie: if you are behind a router, it will be the ip-address of the router.)

This is usefull if you want to tunnel back into a computer that has a dynamically 
changing ip-address.

Have the computer you want to get into, let's call it the SERVER, check it's 
current public IP address every hour.
Then have it (the SERVER) write that value to a file on your Dropbox.
You will then have an updated record of the SERVER ip address and will be 
able to log back into it from anywhere (as long as you enabled port forwarding
on your router.... obviously...)

Public IP Servers used:
    ip.alt.io                   :   182.160.128.100
    bot.whatismyipaddress.com   :   24.114.23.103
    ifconfig.me                 :   49.212.202.172
    wget ipecho.net/plain -O - -q 

Usage is:

    -h or --help for explanation
    -a  get the ip from all servers and return it (will take longer)
    -t or --test to test all the id servers in this program.  Will return a list of the 
                public ip addresses returned and True if they are all the same.
    other wise with no argument will just return the public ip from the trusted server.
    
    Help is very badly written..... needs fixup.

    Version 0.1 BETA - 12-March-2013
    Author: Michael Longval
    Email:  mlongval _at_ gmail _dot_ com

    This software is liscensed under the GPL 

    This version of CPIPA has been tested only under Python3
    I don't use Python2.7 ... so if it breaks under 2.7 just try and fix it....

"""


#===================
# imports

import subprocess 
import argparse

#===================
# globals 

IP_Servers = (
                "/usr/bin/curl -s ip.alt.io",
                "/usr/bin/curl -s bot.whatismyipaddress.com",
                "/usr/bin/curl -s ifconfig.me",
                "/usr/bin/wget http://ipecho.net/plain -O - -q"
                )

preferred_IP_Server = 1


#===================
# Function Definitions

def decodeAndStrip(value):
    """ 
    Converts a string to utf-8 and strips off the spaces.
    """
    value = value.decode("utf-8")
    value = value.strip()
    return(value)
#end def decodeAndStrip

def askServer(serverID):
    """
    Get the current public ip address of THIS computer from server: serverID
    """
    myCPIPA = subprocess.check_output(IP_Servers[serverID], shell=True)
    myCPIPA = decodeAndStrip(myCPIPA)
    return(myCPIPA)
#end def askServer

def askPreferredServer():
    """
    Get the current public ip address of THIS computer from the server defined as perferred_IP_Server in globals
    """
    return(askServer(preferred_IP_Server))
#end def askPreferredServer

def askAllServers():
    """
    Go through all the servers in the list
    and check if they agree... return True if they do and False if they do not agree.
    
    It is used mostly to simply print the list of replies from the servers.
    """
    replies = []

    for i in range(len(IP_Servers)):
        replies.append(askServer(i))
    #end for
    
    print(replies)

    if replies.count(replies[0]) == len(replies):
        return(True)        # this implies a consensus among the different servers
    else:
        return(False)       # this implies there is no consesus 
    #end for
#end def askAllServers

def getConsensus():
    """
    This function will return the consensus ip address or Error
    """
    replies = []
    for i in range(len(IP_Servers)):
        replies.append(askServer(i))
    #end for

    if replies.count(replies[0]) == len(replies):
        return(replies[0])
    else:
        return("Error")
    #end if
#end getConsesus()

def getArguments():
    parser = argparse.ArgumentParser()

    parser.add_argument(
            "-t", "--test", 
            help="test all servers",
            action="store_true"
            )
    parser.add_argument(
            "-c", "--consensus",
            help="get values from all servers and return only if all servers report same address",
            action="store_true"
            )
    
    userInput = parser.parse_args()

    if userInput.test:
        return("testMode")
    elif userInput.consensus:
        return("consensusMode")    
    else:
        return("normalMode")
    #end if
#end def getArguments


#===================
# Main() Program

userChoice = getArguments()

if userChoice == "testMode":
    print(askAllServers())
elif userChoice == "allMode":
    reply = getConsensus()
    if reply == "Error":
        print("Error: There was no consensus among the servers.")
    else:
        print(reply)
else:
    print(askPreferredServer())
#end if

# END PROGRAM
#===================


