**Domain name system**/**nameserver**
On *TCP AND UDP* port 53, it maps domain names, e.g: [xkcd.com](https://xkcd.com) to its [[IP]]: 151.101.64.67. It provides a manageable and easier way than to hard code these domain names to the [[IP]]s with the "[[Hosts File]]". 

So the nameserver, so it's also called, is a domain name to [[IP]] mapping, if the domain name is in the entries of the nameserver's **cache**, it will return the [[IP]] of that host. Specify DNS hosts with [[IP]], not hostnames, as it needs the DNS in order to resolve hostnames.

DNS have *zones*, so like a `.com`, `.net`, `.org` (these top level domains are encompassed in a root zone) are all zones within DNS. Say one day there is a [videos.xkcd.com](https://xkcd.com), then that subdomain is a part of the the `.com` zone (which is part of the root zone). Complete collections of zones are in zone files.

##### The two types of DNS nameservers:

|         | Authoritative                                                                                                 | Recursive                                                                        |
| ------- | ------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- |
| Purpose | Contains information of ***specific*** domains. Returns an *authoritative* answer from that domain's servers. | Performs lookups for clients, returns the [[IP]] for that **authoritative** DNS. |
*best practice is to separate authoritative nameservers and recursive ones*
##### DNS Hierarchy:
Say you are accessing a host that's not in your DNS's cache. Your DNS chooses from one of the zones in the root zone. Then the root zone will refer it to an authoritative DNS within it, repeat until you reach the final, true, authoritative DNS you're looking for. Then that *authoritative* [[IP]] of that host will be returned back to you.

##### Forward and Reverse:
Forward → hostnames to [[IP]]
Reverse → [[IP]] to hostnames

Forward DNS'es can return multiple [[IP]]s, reverse ones can only return **one**.

#### Different types of records:

| Record  | Contained Items                                             | Purpose                                                                                                                       | Full Name                      |
| ------- | ----------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------- | ------------------------------ |
| `A`     | [[IP]]v4                                                    | If you're finding a [[IP]]v4 address, it'll return an `A` record with that [[IP]].                                            | Address                        |
| `AAAA`  | [[IP]]v6                                                    | Same as above, just [[IP]]v6.                                                                                                 | Address (\* 4 for some reason) |
| `PTR`   | hostname                                                    | Used *almost* only for reverse DNS, as it returns a hostname. (but other protocols might use it)                              | ointer                         |
| `SOA`   | Timing and responsibility info of the zone you're searching | Includes things like: "how long should a recursive nameserver cache entries?", "who do I contact problems with this domain?". | Start of Authority             |
| `CNAME` | DNS alias                                                   | Used for DNS redirects                                                                                                        | Canonical Name                 |
| `MX`    | Mailserver hostname                                         | Identifies one of the mailservers for a zone                                                                                  | Mail Exchanger                 |

#### DNS Codes:
- `NOERROR`: success!
- `NXDOMAIN`: DNS doesn't contain any records you're looking for.
- `SERVFAIL`: something went wrong. Maybe authoritative servers stopped answering queries,  your DNSSEC blew up (DNS Security Extensions), or your recursive nameserver fell ill.