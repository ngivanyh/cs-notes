Lets you look at the [[DNS]]. `nslookup` also works, newer tools might include `dig`.

```
$ host xkcd.com
xkcd.com has address 151.101.128.67
xkcd.com has address 151.101.192.67
xkcd.com has address 151.101.64.67
xkcd.com has address 151.101.0.67
xkcd.com has IPv6 address 2a04:4e42:600::67
xkcd.com has IPv6 address 2a04:4e42:200::67
xkcd.com has IPv6 address 2a04:4e42:400::67
xkcd.com has IPv6 address 2a04:4e42::67
xkcd.com mail is handled by 30 aspmx5.googlemail.com.
xkcd.com mail is handled by 30 aspmx3.googlemail.com.
xkcd.com mail is handled by 20 alt1.aspmx.l.google.com.
xkcd.com mail is handled by 30 aspmx4.googlemail.com.
xkcd.com mail is handled by 30 aspmx2.googlemail.com.
xkcd.com mail is handled by 20 alt2.aspmx.l.google.com.
xkcd.com mail is handled by 10 aspmx.l.google.com.
```

`-v` for verbose answers

```
$ host -v xkcd.com
Trying "xkcd.com"
;; ->>HEADER<<- opcode: QUERY, status: NOERROR, id: 17355
;; flags: qr rd ra; QUERY: 1, ANSWER: 4, AUTHORITY: 0, ADDITIONAL: 0

;; QUESTION SECTION:
;xkcd.com.			IN	A

;; ANSWER SECTION:
xkcd.com.		278	IN	A	151.101.128.67
xkcd.com.		278	IN	A	151.101.192.67
xkcd.com.		278	IN	A	151.101.64.67
xkcd.com.		278	IN	A	151.101.0.67

Received 90 bytes from 192.168.10.142#53 in 6 ms
Trying "xkcd.com"
;; ->>HEADER<<- opcode: QUERY, status: NOERROR, id: 39987
;; flags: qr rd ra; QUERY: 1, ANSWER: 4, AUTHORITY: 0, ADDITIONAL: 0

;; QUESTION SECTION:
;xkcd.com.			IN	AAAA

;; ANSWER SECTION:
xkcd.com.		278	IN	AAAA	2a04:4e42:600::67
xkcd.com.		278	IN	AAAA	2a04:4e42:200::67
xkcd.com.		278	IN	AAAA	2a04:4e42:400::67
xkcd.com.		278	IN	AAAA	2a04:4e42::67

Received 138 bytes from 192.168.10.142#53 in 6 ms
Trying "xkcd.com"
;; ->>HEADER<<- opcode: QUERY, status: NOERROR, id: 62781
;; flags: qr rd ra; QUERY: 1, ANSWER: 7, AUTHORITY: 0, ADDITIONAL: 0

;; QUESTION SECTION:
;xkcd.com.			IN	MX

;; ANSWER SECTION:
xkcd.com.		278	IN	MX	30 aspmx5.googlemail.com.
xkcd.com.		278	IN	MX	30 aspmx3.googlemail.com.
xkcd.com.		278	IN	MX	20 alt1.aspmx.l.google.com.
xkcd.com.		278	IN	MX	30 aspmx4.googlemail.com.
xkcd.com.		278	IN	MX	30 aspmx2.googlemail.com.
xkcd.com.		278	IN	MX	20 alt2.aspmx.l.google.com.
xkcd.com.		278	IN	MX	10 aspmx.l.google.com.

Received 286 bytes from 192.168.10.142#53 in 8 ms
```

`HEADER` includes general information about the [[DNS]] query. The `status` includes the stuff like `NOERROR`, `SERVFAIL`, etc.

`QUESTION` can let you see what your machine wanted to see (the type of [[DNS]] record)

`ANSWER` is the answer from the [[DNS]]. There might be `AAAA`, `MX`, etc records.

Reverse [[DNS]] query: ([google.com](https://google.com))
```
$ host 142.250.196.206
206.196.250.142.in-addr.arpa domain name pointer nctsaa-ac-in-f14.1e100.net.
```

Add [[DNS]] server IP at the back to check if the [[DNS]] record exists.