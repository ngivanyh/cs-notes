A communication endpoint for a process. Virtual.

**Local sockets**: System entities on the filesystem or in memory that accept connections from other programs.
**IPC**: Another common socket protocol, only in memory.

Unprivileged users running programs attached to a socket **SHOULDN'T** have any write perms to the config file.
#### [[TCP - IP, UDP, ICMP, and Ports#TCP/IP]] Sockets
They listen for network connections. One process can open any number of sockets. *Network socket* is a phrase to describe "open a [[TCP - IP, UDP, ICMP, and Ports#TCP/IP]] port". They can accept any number of connections as long as all the clients have unique source IPs. (similar to ports)