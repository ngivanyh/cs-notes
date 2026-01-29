|                                        | **Broadcast Domain**            | **Subnets** |
| -------------------------------------- | ------------------------------- | ----------- |
| Size                                   | Smaller                         | Larger      |
| Associated Layer ([[The Four Layers]]) | Datalink                        | Network     |
| Mechanisms                             | [[ARP & ND]], and MAC addresses | [[IP]]      |
Sharing a "ethernet" is different from being in the same subnet. Sharing an ethernet implies that host you're trying to connect to is in your **broadcast domain** and you likely can connect as it's in your ARP/ND tables. But you can be in the same **subnet** and might not have previously connected to the host that you want to connect to now (ARP/ND tables to populated with that host's MAC address)

 