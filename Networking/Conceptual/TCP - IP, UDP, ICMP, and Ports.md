## TCP/IP
IP, Internet Protocol, see [here](obsidian://open?vault=Computers%20-%20Infinity%20Stones&file=Networking%2FConceptual%2FIP). TCP/IP's TCP includes protocols **around** TCP too, **not just TCP**. Those protocols include TCP, UDP, ICMP, SCTP, ESP, AH, and others.

## ICMP
- Crucial to Internet infrastructure, they may contain some messages about your system status ([`ping`](obsidian://open?vault=Computers%20-%20Infinity%20Stones&file=Networking%2FCommands%2F%60ping%60) uses ICMP)
- Supports IPv4 & IPv6, they may seem similar on the surface, but internally they're different.
## UDP
- Minimal
- Doesn't do data flow management, it just sends packets. It doesn't treat the flow as one entity, and therefore it doesn't treat each packet as part of one thing, it just coincidentally sends packets to the same destination.
- It cannot tell if the packets ever reach its destination, as I've said, it just sends packets. So it's the application's responsibility to do such things.
- Provides freedom for the application to do their own work regarding the management of the packets it wants. Sometimes, the fact that the protocol doesn't care is a good thing for something like online meetings, streaming, and stuff. 
- VPNs use UDP (most of them).
- FASTTTT
- called "connectionless", because of its "carelessness"
## TCP
- Unlike UDP, handles the reliability stuff.
- To start a connection, the host (A) that's making the request first sends a `SYN` packet to the other side of the connection (B), if B receives the `SYN` packet (and doesn't ignore/reject, but rather accepts), then it'll send a `SYN-ACK` packet to `ACK`nowledge the connection that was made, then A will send a `ACK` packet back, and that's the TCP connection established. (*three-way handshake*)
- The opposite of UDP, therefore it's a "connected" protocol. (It treats the data flow as one entity)
- The order of packets sent **MUST** be received in the same order by the other side.
- A *four-way handshake* is done after the packets are received by the other side of your connection, to tear down the connection made by the *three-way handshake*. (`CLOSE_WAIT`, `TIME_WAIT`, `FIN_WAIT_2`, `LAST_ACK`)
- When the connection is getting choppy during a TCP connection, the host might send a TCP reset message, which tells the other host to "throw away the connection ASAP". Higher level protocols get cut off. And TCP doesn't to the four-way handshake. Mostly likely server-side error.
## Other Protocols
- See `/etc/protocols`, for more protocols
- Each protocol has a name and an ID, they use this ID in the header of a packet. (can be seen through packet capture and analyzation, or when you're writing packet filtering rules)
## Ports
- Separate for TCP and UDP
- They are defined by *software*
- `0 - 65535`
- So long as you have different source IPs, you can connect to the same server at the same port, with the same port.
- Clients normally make network requests on high numbered ports not used for many purposes. `root` can open TCP or UDP ports under around `1024`. Called *ephemeral* ports. Check your OS for the specific range.
- IPv4 representation: `255.255.255.255:PORT` IPv6: `[ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff]:PORT`
- See `/etc/services` to see what port does what
- **DO NOT RUN SOFTWARE THAT LISTENS TO THE NETWORK AS `root`!!!!!!! DANGER APPROACHES!!!!**
