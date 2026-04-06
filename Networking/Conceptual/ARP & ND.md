---
title: ARP & ND
date created: Friday, June 27th 2025, 12:12:50 pm
date modified: Sunday, April 5th 2026, 10:18:47 pm
tags: [networking, networking/layer2, networking/conceptual]
parent: Conceptual
nav_order: 1
---
# ARP & ND
## ARP (Address Resolution Protocol)
Maps the MAC address to the IP address.  It is the glue that attaches the network and the datalink layer.

So if a host needs to transmit stuff to another host.

1. Makes an Ethernet request asking something along the lines of "Which MAC address is responsible for this IP address?"
2. (Hopefully) The host that'll receive the information we're trying to transfer "says" "It's me you're trying to send to. I have these addresses associated with me."
3. So the original host adds this information (IP, MAC address, etc) for the recipient host into an ARP table.

## ND (Neighbor Discovery)
Like ARP, but with a few changes.
- IPv4 addresses -> IPv6
- Works not just on [[Ethernet]], but other datalink protocols.
- ND tables have a few different states (list below are states that will likely be encountered)
    - Reachable: Live on the network
    - Stale: Was live, but expired on the ND cache
    - Permanent: Local or the machine itself
    - Failed: Looked for, not found

 #networking #networking/layer2 #networking/conceptual 