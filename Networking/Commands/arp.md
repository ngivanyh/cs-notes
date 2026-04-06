---
tags: [networking/commands, networking, networking/layer2]
title: arp
date created: Friday, June 27th 2025, 12:05:32 pm
date modified: Sunday, April 5th 2026, 10:18:57 pm
parent: Commands
nav_order: 2
---
# arp
**Highly related to: [[ARP & ND]]

```
$ arp -a
```

Lists the ARP table of current system.

`-n`: Show without hostname in the ARP table.

```
$ arp HOST_IP
```
See if the host you're looking for is on your ARP entries. So sometimes, when you can't `ping` to a host, it doesn't necessary mean the network layer is broken, maybe you don't have a ARP entry for that machine. You can know if nothing comes out of the `arp HOST_IP`, the address is listed as `incomplete`, or `missing`. If such situation arise, then it's your datalink layer that's broken.

If you have a empty ARP table, try `ping`ing/connecting to other systems on the local network, that should populate the ARP table. If it doesn't work consult/check the physical layer/check your IP configuration.

For IPv6, you may consider using something like `ndp -a` to list the ARP tables.

#networking/commands #networking #networking/layer2
