View established Ethernet connections. Used for checking datalink errors and to see what ports and what protocols are currently used. Use with `-nr` to see routing tables (also can be done with [`route`](obsidian://open?vault=Computers%20-%20Infinity%20Stones&file=Networking%2FCommands%2F%60route%60)), `-i` to see the **default configured** routes. (all live ports `-a`, show IPv4 `-4`, show IPv6 `-6`, TCP only `-t`, UDP only `-u`, established only `-t` (only TCP can be "established"), listening only `-l`, all `-a`)

```
$ netstat
Active Internet connections
Proto Recv-Q Send-Q  Local Address          Foreign Address        (state)
tcp4       0      0  192.168.10.117.56804   20.189.173.2.https     ESTABLISHED
tcp4       0      0  192.168.10.117.56803   13.89.179.14.https     ESTABLISHED
tcp4       0      0  192.168.10.117.56802   13.89.179.14.https     ESTABLISHED   
```
You'd want the `errs` portion to be `0` or a small number.  (one for IPv4, one for IPv6)

```
$ netstat -nr
Routing tables

Internet:
Destination        Gateway            Flags               Netif Expire
255.255.255.255    255.255.255.255    flags               Expiry

Internet:
Destination        Gateway            Flags               Netif Expire
HEX                HEX                 flags               Expiry
```

`netstat` tries to use hostnames, and human-friendly port names (override with `-n`).