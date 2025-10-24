Shows the system's current network configuration. Can be used to check your IP configuration when you can't connect to a network (other remedies include checking the ARP tables [`arp`](obsidian://open?vault=Computers%20-%20Infinity%20Stones&file=Networking%2FCommands%2F%60arp%60), [`ping`](obsidian://open?vault=Computers%20-%20Infinity%20Stones&file=Networking%2FCommands%2F%60ping%60)ing the default gateway, checking w/ the DNS via `nslookup`). On some devices, consider `ip a`

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