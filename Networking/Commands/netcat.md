---
title: netcat
date created: Friday, June 27th 2025, 10:24:49 am
date modified: Saturday, April 11th 2026, 9:52:58 pm
---
# netcat
Lets you listen to the network on a specific port. And even send arbitrary network traffic through that port. Shortened as `nc`. Default connection type is TCP (for sending and listening).

Type what you want to send below

```
$ nc -v xkcd.com 80
Connection to xkcd.com port 80 [tcp/http] succeeded!
```

`-v` for verbose (almost needed every time as without it, it won't display errors)
`-u` for UDP
`-l` to listen

You can also create a `nc` listener, almost like a miniserver for you to ping. And you can string this up with a `nc` that sends traffic to that `nc` listener

You can also send files with `nc`. On the sender, you have to use `<` redirection to `nc`, and you must tell nc to close once the file is sent. On the receiver, you must setup a receiver and output the output using `>` to a file.

It's a good way to test whether you can connect to a system on a specific port, indicated by the message it first gives when you run the command.

#networking #networking/commands 