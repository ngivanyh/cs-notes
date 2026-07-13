---
title: Broadcast domain vs Subnets
date created: Wednesday, September 24th 2025, 10:12:30 pm
date modified: Wednesday, May 6th 2026, 2:40:22 pm
---
# Broadcast domain vs Subnets

|                                        | **Broadcast Domain**            | **Subnets** |
| -------------------------------------- | ------------------------------- | ----------- |
| Size                                   | Smaller                         | Larger      |
| Associated Layer ([[The Four Layers]]) | Datalink                        | Network     |
| Mechanisms                             | [[MAC Addresses, ARP, & ND]], and MAC addresses | [[IP]]      |
Sharing a "ethernet" is different from being in the same subnet. Sharing an ethernet implies that host you're trying to connect to is in your **broadcast domain** and you likely can connect as it's in your ARP/ND tables. But you can be in the same **subnet** and might not have previously connected to the host that you want to connect to now (ARP/ND tables to populated with that host's MAC address)

 #networking #networking/conceptual 