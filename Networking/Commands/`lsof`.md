Lets you see what processes open which files. Useful because Unix treats network connections much like files. You can see what ports are doing what on what ports (it's more general purpose, but to narrow it down to ONLY network ports, use `-i`)

```
$ lsof -i
COMMAND     PID  USER   FD   TYPE             DEVICE SIZE/OFF NODE NAME
rapportd    957 ivann    9u  IPv4 0xea8a0ee4f8175683      0t0  TCP *:60018 (LISTEN)
rapportd    957 ivann   10u  IPv6 0x20501da4e15c5744      0t0  TCP *:60018 (LISTEN)
rapportd    957 ivann   19u  IPv6 0xc2babdef264d2fea      0t0  TCP [fe80:b::1c18:b13a:3f78:eff5]:60024->ipad.local:49713 (ESTABLISHED)
rapportd    957 ivann   20u  IPv6 0x887b16228b5ffb33      0t0  TCP [fe80:b::1c18:b13a:3f78:eff5]:60039->living-room.local:49153 (ESTABLISHED)
identitys   975 ivann   18u  IPv4 0xf505b6de27954a20      0t0  UDP *:*
identitys   975 ivann   23u  IPv4 0x61450c0ca6c5f70c      0t0  UDP *:*
```

`-n` turns off hostname/DNS resolution.