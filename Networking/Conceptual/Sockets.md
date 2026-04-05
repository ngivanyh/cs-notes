---
tags: [networking, networking/conceptual]
title: Sockets
date created: Friday, August 1st 2025, 11:06:45 am
date modified: Sunday, April 5th 2026, 10:18:57 pm
parent: Conceptual
grand_parent: Networking
nav_order: 12
---
# Sockets
A communication endpoint for a process. Virtual.

**Local sockets**: System entities on the filesystem or in memory that accept connections from other programs.
**IPC**: Another common socket protocol, only in memory.

Unprivileged users running programs attached to a socket **SHOULDN'T** have any write perms to the config file.
### TCP/IP Sockets
They listen for network connections. One process can open any number of sockets. *Network socket* is a phrase to describe "open a [[TCP - IP, UDP, ICMP, Ports#TCP/IP]](TCP/IP) port". They can accept any number of connections as long as all the clients have unique source IPs. (similar to ports)

 #networking #networking/conceptual 