Firewalls commonly use a default deny policy, and their configuration of permitted network traffic depends on the enterprise/organization. They usually use [[TCP - IP, UDP, ICMP, and Ports]] ports and [[IP]] to see and control the network. But most ethernet switches and routers have **A**cess **C**ontrol **L**ists (ACLs) and packet filtering mechanisms built in.

Proxy servers and inspect and sanitize certain packets when they cross over the network. So when your traffic is not going your desired way, maybe it's because the proxy server's editing your HTTP headers and whatnot.

Load balancers distribute network traffic amongst different hosts. They redirect [[TCP - IP, UDP, ICMP, and Ports]] connections as "load dictates", and they might change the content for better redirection.