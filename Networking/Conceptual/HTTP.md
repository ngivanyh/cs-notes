---
tags: [networking, networking/layer4, networking/conceptual]
title: HTTP
date created: Thursday, December 25th 2025, 10:06:47 am
date modified: Saturday, April 11th 2026, 9:52:58 pm
parent: Conceptual
nav_order: 6
---
# HTTP
## HTTP Methods
They are really just names, and they do the same thing, open a TCP request and send it to the host at some address at some socket. They are named differently for humans to discern different requests from one another. 

You might say the data in a `POST` request is not seen in the address bar, that's by choice. Under the hood, the things they're doing is mostly the same.
## H3 (HTTP V3)
Old HTTP uses TCP (see more: [[TCP - IP, UDP, ICMP, Ports]]), this version uses a modified version of UDP, the idea behind it is that the modern web is quite stable enough to just ignore the check of whether the request has made it to the host. 

#networking #networking/layer4 #networking/conceptual 

 