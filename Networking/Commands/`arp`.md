```
$ arp -a
```
Lists [ARP](obsidian://open?vault=Computers%20-%20Infinity%20Stones&file=Networking%2FConceptual%2FARP%20%26%20ND) table of current system.

`-n`: Show without hostname in the [ARP](obsidian://open?vault=Computers%20-%20Infinity%20Stones&file=Networking%2FConceptual%2FARP%20%26%20ND) table.

```
$ arp HOST_IP
```
See if the host you're looking for is on your [ARP](obsidian://open?vault=Computers%20-%20Infinity%20Stones&file=Networking%2FConceptual%2FARP%20%26%20ND) entries. So sometimes, when you can't `ping` to a host, it doesn't necessary mean the [network layer](obsidian://open?vault=Computers%20-%20Infinity%20Stones&file=Networking%2FConceptual%2FThe%20Four%20Layers) is broken, maybe you don't have a [ARP](obsidian://open?vault=Computers%20-%20Infinity%20Stones&file=Networking%2FConceptual%2FARP%20%26%20ND) entry for that machine. You can know if nothing comes out of the `arp HOST_IP`, the address is listed as `incomplete`, or `missing`. If such situation arise, then it's your datalink layer that's broken.

If you have a empty [ARP](obsidian://open?vault=Computers%20-%20Infinity%20Stones&file=Networking%2FConceptual%2FARP%20%26%20ND) table, try `ping`ing/connecting to other systems on the local network, that should populate the [ARP](obsidian://open?vault=Computers%20-%20Infinity%20Stones&file=Networking%2FConceptual%2FARP%20%26%20ND) table. If it doesn't work consult/check the physical layer/check your IP configuration.

For [IPv6](obsidian://open?vault=Computers%20-%20Infinity%20Stones&file=Networking%2FConceptual%2FIP), you may consider using something like `ndp -a` to list the ARP tables.