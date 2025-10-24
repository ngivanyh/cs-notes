## Common Principles
- Subnets: A block of IPs. (Your ISP allocates a subnet to your organization, and the network administrator can divide the subnets into subnets etc.) (Devices must be on the same subnet to communicate with each other, to communicate with other devices on different subnets, you need a router) (Each subnet contains 2^x addresses, so the number of addresses in a subnet must be a power of two)
- Some form of protocol that links MAC addresses to IPs (IPv4: ARP, IPv6: ND) [ref](obsidian://open?vault=Computers%20-%20Infinity%20Stones&file=Networking%2FConceptual%2FARP%20%26%20ND)
- **DO NOT CONFUSE SHARING AN ETHERNET WITH ANOTHER HOST AND ABLE TO DIRECTLY CONNECT TO THAT HOST VIA IP** (they might be on different subnets, but all in all, they might be in the same broadcast domain)
## IPv4
- Representation: `255.255.255.255`, a 32 bit number
-  Netmasks: Indicates the size of the subnet. (Common one is: `255.255.255.0`). `255.255.255.0` is a 24 fixed bit netmask represented as `/24` at the end of IPs, it means you can have `32 - 24 = 8` unique IPs, ie. 2 to the 8 IPs.
- Unusable IPs: The first and last IPs, like `192.168.10.0` and `192.168.10.255`
- localhost: Either http://127.0.0.1 (/8) or just http://localhost
## IPv6
- Representation: 128 bit number, printed as eight groups of hex numbers -> e.g. `ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff`. If one group is `0`, then you just print `0` instead of `0000`. And if there are multiple groups of zero together, you can omit the largest group of `0`s by typing `::`, **can only be done once**.
- Netmasks: Usually only subnetted at `:` boundaries, so the natural subnets are `/16`, `/32`, `/48`, `/64` (most of the time it's `/64`)
- Configuration: IPv6, unlike IPv4 has autoconfiguration **built-in**
- localhost: http://::1 (only has one available address, no /8 shenanigans like IPv4)
- Link-local Addresses: IPv6 addresses autoconfigure even if no router is present. When it connects to a network, it presents an IPv6 address to the network. Addresses beginning with `fe8` are *link-local addresses*. Valid **only** to that broadcast domain, and are **always** `/64`. The operating systems will include the interface name to the address to tell them apart (since they are not globally unique).