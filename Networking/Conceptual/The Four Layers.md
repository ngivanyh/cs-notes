---
tags: [networking, networking/layer1, networking/layer2, networking/layer3, networking/layer4, networking/conceptual]
title: The Four Layers
date created: Friday, June 27th 2025, 11:51:32 am
date modified: Sunday, April 5th 2026, 10:18:57 pm
parent: Conceptual
grand_parent: Networking
nav_order: 14
---
# The Four Layers
Each layer rests on the one before it, if the bottom one fails, then all the others will come crashing down. But most of the time, if you fix that problem, then it'll all magically right itself.

| Layer Number | Layer Name | Layer Protocols/Items Related                                                                            | Troubleshooting Tools                                        | What it Does                                                           | Common Errors Related to it                                                                                                                                            |
| ------------ | ---------- | -------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------ | ---------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 1            | Physical   | Cables                                                                                                   | Fixing/Checking the cable, [[ifconfig or ip a (checking networking configuration)]]              | Sends the traffic.                                                     | Broken equipment, shoddy equipment, incompatible equipment                                                                                                             |
| 2            | Datalink   | ND (Neighbor Discovery, for IPv6), ARP (Address Resolution Protocol, for IPv4), MAC addresses            | [[arp]], ND (varies between OS's), [[tcpdump and Wireshark]] | Transforms stuff into signals that could be chucked to the other side. | Frame errors (think packet errors), drops (think packet drops), overruns, collisions (these errors reduce performance, but might not necessarily bring down a network) |
| 3            | Network    | IP (IPv4, IPv6)                                                                                          | `ping`, [[traceroute]]                                       | Figures out where stuff goes.                                          | Misconfiguration, support (e.g. only supports IPv4, configured to only support IPv6, different subnets, etc)                                                           |
| 4            | Transport  | [[TCP - IP, UDP, ICMP, Ports]](everything that has IP must support ICMP, ping sends traffic w/ ICMP) | [[netstat]], [[netcat]], [[tcpdump and Wireshark]]           | As the name implies, transporting traffic.                             | No open ports, packet drops, misconfiguration, man-in-the-middle, etc                                                                                                  |

#networking #networking/layer1 #networking/layer2 #networking/layer3 #networking/layer4 #networking/conceptual 