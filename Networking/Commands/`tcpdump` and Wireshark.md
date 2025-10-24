Both are packet sniffers, `tcpdump` is in the CLI, and Wireshark is an app. I.E. they display traffic to and from a server, even when the server rejects that traffic. For more complicated analysis, you'll probably want to use Wireshark.

You should use these with admin perms and most OS'es run them in an sandbox (to prevent malicious actors from corrupting your system with a corrupted packet sniffer)

## `tcpdump`:
- Filtering used with the [Berkeley Packet Filter (BFP)](https://biot.com/capstats/bpf.html) syntax (add to the end of the `tcpdump` command)
- Comes with every networked OS

## Wireshark:
- Fancy
- More for traffic analysis really
- Larger than `tcpdump`
- **NEVER EVER SHOULD GO ON A PRODUCTION SERVER** (too big, security reasons)
- Should be captured, put into a file and sent to `tcpdump` for analysis (just a recommendation)

## Usage
#### `tcpdump`:

`-D`: shows a list of interfaces, each of them are assigned a number ID.
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

`-i` specifies the interface you want to capture upon, you may use the interface name (`en0`, `lo0`, etc), but you can also use the numbers (`1`, `2`, etc)

`-n` disables [[DNS]] lookup, improves performance, declutters interface

`-w filename.pcap` writes to a `.pcap` file (binary encoded yes, but don't send unencrypted auth info through it)

`-r` reads `.pcap` files
#### Reading UDP packets ([[TCP - IP, UDP, ICMP, and Ports]])
`07:50:58.649775 IP 192.168.10.117.51538 > one.one.one.one.domain: 52271+ A? xkcd.com. (26)`

is formatted as below (roughly, results may vary):

`TIME PACKET_TYPE(IP for IPv4, IP6 for IPv6, 802.1 for Ethernet management) IP_ADDR-SRC.SRC_PORT >(move direction) DESTINATION DESTINATION_PORT [PACKET CONTENTS] (SIZE)`

#### Reading TCP packets ([[TCP - IP, UDP, ICMP, and Ports]])
TCP packets are similar to UDP packets in the way they're reported by `tcpdump`. But they include additional information that's unique to TCP.

**TCP Flags:**
- `S` for `SYN` packets
- `.` for `ACK` packets (Could be `SYN-ACK` (`S.`), `R-ACK` (`R.`), etc)
- `R` for TCP reset (forceful termination of connection)
- `F` for `FIN` (the end of the TCP connection, graceful)

Below are some that are not as common (for in depth debugging)
- `U` for urgent
- `W` and `E` for congestion control
- `P` for push

**Additional information a TCP packet may contain:**
- `seq` for `sequence`
- `win` for window size
- additional options (with `options`)

#### Filtering (simple):
- `arp` for `ARP` traffic only
- `ether host MAC-ADDR` for a specific MAC address
- `ip` for IP (traffic) only
- `ip host` (technically two keywords) specifies a specific host at a specific IP
- `or`, `and`, `not` just plain logical `OR`, `AND`, `NOT`
- `()` just like programming, you can separate different stuff with them, you need to escape them with `\`
- `udp` for UDP only
- `tcp` for TCP only
- `port NUMBER` for a specific port (add `tcp`, `udp`, or your protocol name in front, it's a simplification of `protocol and port number`)
