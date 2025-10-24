*`Traces`* the *`route`* to the destination. (would look something like this). Used for debugging IP that might not be within your **broadcast domain** ([[Broadcast domain vs subnets]]).

```
$ traceroute google.com
 1  192.168.101.1 (192.168.101.1)  5.767 ms  4.447 ms  5.331 ms
 2  60-248-97-254.hinet-ip.hinet.net (60.248.97.254)  143.015 ms  10.898 ms  9.817 ms
 3  168-95-82-210.tpe4-3332.hinet.net (168.95.82.210)  142.183 ms  8.317 ms  138.450 ms
 4  220-128-9-242.tylc-3032.hinet.net (220.128.9.242)  8.373 ms  7.049 ms
    220-128-9-126.tylc-3032.hinet.net (220.128.9.126)  6.228 ms
 5  220-128-9-189.tylc-3336.hinet.net (220.128.9.189)  11.146 ms  103.773 ms  95.365 ms
 6  72.14.213.90 (72.14.213.90)  7.503 ms
    142.250.169.122 (142.250.169.122)  7.264 ms  6.979 ms
 7  192.178.106.71 (192.178.106.71)  8.386 ms * *
 8  142.251.226.168 (142.251.226.168)  14.484 ms
    209.85.243.196 (209.85.243.196)  7.460 ms
    142.251.226.170 (142.251.226.170)  9.321 ms
 9  192.178.105.252 (192.178.105.252)  11.345 ms
    nctsaa-ab-in-f14.1e100.net (142.250.77.14)  10.808 ms  6.857 ms
```

The three times at the back indicates the three packets sent to hop. (the trip and the return)

`*` means unknown (for the times, it means lost/unknown (either for packets or for responses to hosts))

`!H` means your host is unreachable
`A`, `!A`, `!X`, `!Z` means further communication is administratively prohibited

`-n` disables DNS lookup, which might improve times (slow traces might be because of a problem, especially if the trace without DNS is slow and then one with it (reverse lookup) is fast)

You can use this tool to check for mostly catastrophic network failures, but you might need to consider [[`tcpdump` and Wireshark]] for the nitty gritty and advanced diagnosis.