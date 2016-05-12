#!/usr/bin/env python

import os
from subprocess import call

advertise_ip = os.environ['SERF_ADVERTISE_IP']
if os.environ['MULTINODE'] == "true":
    if os.environ['SERF_JOIN_ADDRESS'] != "":
        join_address = os.environ['SERF_JOIN_ADDRESS']
        '''
        It's multinode. We pass a join address to connect to another node,
        and a advertise IP of the network interface that has a route to 0.0.0.0
        binds to 0.0.0.0:7946
        '''
        command = ["serf", "agent", "-join", join_address,"-advertise", advertise_ip]
    else:
        '''
        It's multinode. We pass an advertise IP
        of the network interface that has a route to 0.0.0.0 binds to 0.0.0.0:7946
        '''
        command = ["serf", "agent", "-advertise", advertise_ip]
else:
    if os.environ['SERF_BIND_ADDRESS'] != "":
        bind_address = os.environ['SERF_BIND_ADDRESS']
        '''
        It's singlenode. We pass an binding IP of a custom docker network interface,
        binds and advertises to it.
        '''
        command = ["serf", "agent","-bind",bind_address+":7946"]
    else:
        '''
        It's singlenode. We use the IP of the default docker0 network interface,
        advertises to it but binds to 0.0.0:7946.
        '''
        command = ["serf", "agent", "-advertise", advertise_ip ]

call(command)