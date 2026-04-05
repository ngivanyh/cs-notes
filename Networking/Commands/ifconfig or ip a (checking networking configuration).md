---
tags: [networking, networking/commands]
title: ifconfig or ip a (checking networking configuration)
date created: Friday, June 27th 2025, 10:20:09 am
date modified: Saturday, February 28th 2026, 9:31:24 pm
parent: Commands
grand_parent: Networking
---
# ifconfig or ip a (checking networking configuration)
Shows the system's current network configuration. Can be used to check your IP configuration when you can't connect to a network (other remedies include checking the ARP tables [[arp]], [[ping]]ing the default gateway, checking w/ the DNS via `nslookup`). On some devices, consider `ip a`

```
$ ifconfig
# loads of stuff
```

```
$ ip a
# stuff
```

The things to look out for are `en0`, `lo0/loopback`, and for wireless solutions (something that starts with like `w`, and has `0`, or something)

Another alternative is `tcpdump -D`, it can show you the available interfaces for packet capture, aka checking your interfaces.

```
$ tcpdump -D
1.en0 [Up, Running, Wireless, Associated]
2.awdl0 [Up, Running, Wireless, Associated]
3.llw0 [Up, Running, Connection status unknown]
4.utun0 [Up, Running]
5.utun1 [Up, Running]
6.utun2 [Up, Running]
7.utun3 [Up, Running]
8.utun4 [Up, Running]
9.utun5 [Up, Running]
10.lo0 [Up, Running, Loopback]
11.anpi1 [Up, Running, Disconnected]
12.anpi0 [Up, Running, Disconnected]
13.en3 [Up, Running, Disconnected]
14.en4 [Up, Running, Disconnected]
15.en1 [Up, Running, Disconnected]
16.en2 [Up, Running, Disconnected]
17.bridge0 [Up, Running, Disconnected]
18.gif0 [none]
19.stf0 [none]
20.ap1
```

#networking #networking/commands 